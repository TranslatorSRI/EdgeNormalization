from src.biolink_client import biolink
from src.ubergraph import UberGraph
from src.util import Text

class EdgeNormalizer:
    def __init__(self):
        self.biolink = biolink()
        self.ubergraph = UberGraph()

    def resolve(self,identifier):
        """Resolve takes a curie and returns the closest edge from biolink model."""
        # If the input is an exact match, return the bl edge
        # If the input is an RO, see if it there is a superclass that maps to a bl model
        # If it's something else, check the lookup table
        # Failing all else, return some generic relationship from BL
        bl_edge = self.biolink.get_edge_by_mapping(identifier)
        if bl_edge is not None:
            #The service may or may not snakify for us.  But Normalizer should make sure
            return Text.snakify(bl_edge)
        if identifier.startswith('RO'):
            return self.resolve_ro(identifier,self.biolink.get_root_edges(),None)
        return None

    def resolve_ro(self,ro_ident,current,recent_true):
        bests=[]
        for possible in current:
            possible_iri = self.biolink.get_iri_by_edge(possible)
            if possible_iri is None:
                #cant rule it out, try the children
                bests.append(self.resolve_ro(ro_ident,self.biolink.get_children(possible),recent_true))
            elif self.is_subclass(ro_ident,possible_iri):
                bests.append(self.resolve_ro(ro_ident,self.biolink.get_children(possible),possible_iri))
            else:
                bests.append(recent_true)
        thebest = list(filter(lambda x: x is not None, bests))
        if len(thebest) != 1:
            print(ro_ident)
            print(current)
            print(recent_true)
            print(bests)
            exit()
        return thebest[0]

    def is_subclass(self,parent,child):
        return self.ubergraph.is_subclass(parent,child)
