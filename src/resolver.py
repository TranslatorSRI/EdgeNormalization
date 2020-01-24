from src.biolink_client import biolink
from src.ubergraph import UberGraph
from src.util import Text
from collections import namedtuple

class EdgeNormalizer:
    def __init__(self):
        self.biolink = biolink()
        self.ubergraph = UberGraph()

    def resolve_curie(self,identifier):
        """Resolve takes a curie and returns the closest edge from biolink model."""
        # If the input is an exact match, return the bl edge
        # If the input is an RO, see if it there is a superclass that maps to a bl model
        # If it's something else, check the lookup table
        # Failing all else, return some generic relationship from BL
        bl_label = self.biolink.get_label_by_iri(identifier)
        #returns a list, but it might be empty
        if len(bl_label) > 0:
            #The service may or may not snakify for us.  But Normalizer should make sure
            bl_label = Text.snakify(bl_label[0])
        else:
            if identifier.startswith('RO'):
                bl_label = self.resolve_ro(identifier)
            else:
                bl_label = None
        if bl_label is not None:
            iri = self.biolink.get_iri_by_label(bl_label)
            Edge = namedtuple('Edge',['identifier','label'])
            return Edge(iri,bl_label)
        return None

    def resolve_ro(self,ro_ident):
        """Given an ro_identifier, walk up the RO hierarchy checking BL to find a match"""
        bl_label = []
        ro_idents = [ro_ident]
        while True:
            new_ros = []
            for ro in ro_idents:
                new_ros += self.ubergraph.get_property_parent(ro)
            if len(new_ros) == 0:
                return None
            for ro in new_ros:
                bl_label = self.biolink.get_label_by_iri(ro)
                if len(bl_label) > 0:
                    return bl_label[0]
            ro_idents = new_ros

