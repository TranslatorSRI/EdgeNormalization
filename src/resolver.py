from src.biolink_client import biolink
from src.ubergraph import UberGraph
from src.util import Text
from collections import namedtuple

class EdgeNormalizer:
    def __init__(self, bl_version='latest'):
        self.biolink = biolink(bl_version=bl_version)
        self.ubergraph = UberGraph()

    def resolve_curie(self,identifier):
        """Resolve takes a curie and returns the closest edge from biolink model."""
        # If the input is an exact match, return the bl edge
        # If the input is an RO, see if it there is a superclass that maps to a bl model
        # If it's something else, check the lookup table
        # Failing all else, return some generic relationship from BL
        bl_predicates = self.biolink.get_biolink_predicate_by_mapping(identifier)
        #returns a list, but it might be empty
        if len(bl_predicates) > 0:
            #The service may or may not snakify for us.  But Normalizer should make sure
            bl_predicate = bl_predicates[0]['mapping']
        else:
            if identifier.startswith('RO'):
                bl_predicate = self.resolve_ro(identifier)
                #If we get to the top of our mini-hierarchy without finding anything, just give a generic relation.
                if bl_predicate is None:
                    bl_predicate = 'biolink:related_to'
            else:
                bl_predicate = 'biolink:related_to'
        if bl_predicate is not None:
            name = self.biolink.get_name_by_predicate(bl_predicate)
            Edge = namedtuple('Edge',['identifier','label'])
            return Edge(bl_predicate,name)
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
                bl_predicate = self.biolink.get_biolink_predicate_by_mapping(ro)
                if len(bl_predicate) > 0:
                    return bl_predicate[0]['mapping']
            ro_idents = new_ros

