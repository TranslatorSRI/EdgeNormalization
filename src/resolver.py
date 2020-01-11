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
        if bl_label is not None:
            #The service may or may not snakify for us.  But Normalizer should make sure
            bl_label = Text.snakify(bl_label)
        else:
            if identifier.startswith('RO'):
                bl_label = self.resolve_ro(identifier,self.biolink.get_root_edges(),None)
        if bl_label is not None:
            iri = self.biolink.get_iri_by_label(bl_label)
            Edge = namedtuple('Edge',['identifier','label'])
            return Edge(iri,bl_label)
        return None

    def resolve_ro(self,ro_ident,current,recent_true):
        bests=[]
        for possible in current:
            possible_iri = self.biolink.get_iri_by_label(possible)
            if possible_iri is None or Text.get_curie(possible_iri) != 'RO':
                #cant rule it out, try the children
                bests.append(self.resolve_ro(ro_ident,self.biolink.get_children(possible),recent_true))
            elif self.is_subclass(ro_ident,possible_iri):
                bests.append(self.resolve_ro(ro_ident,self.biolink.get_children(possible),possible_iri))
            else:
                bests.append(recent_true)
        thebest = list(filter(lambda x: x is not None, bests))
        if len(thebest) == 1:
            return thebest[0]
        return recent_true

    def is_subclass(self,parent,child):
        return self.ubergraph.is_subclass(parent,child)

    def get_parent(self,child):
        return self.ubergraph.get_parent(child)
