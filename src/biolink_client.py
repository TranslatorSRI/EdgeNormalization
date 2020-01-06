import yaml
from os import path
from collections import defaultdict,namedtuple
from src.util import Text

class biolink:
    """This class is merely a placeholder.  Currently it's implemented
    by pulling in the biolink yaml.  But it's going to be re-implemented as a client
    on a biolink model service."""
    def __init__(self):
        #Read by hand for now
        self.iri_to_name,self.edge_tree,self.root_edges = self.pull_from_yaml()
        self.name_to_iri = { v:k for k,v in self.iri_to_name.items() }

    def pull_from_yaml(self):
        uri_to_slot = {}
        edge_tree = defaultdict(list)
        roots = set()
        with open(path.join(path.dirname(path.abspath(__file__)),'..','data','biolink-model.yaml')) as blfile:
            blmodel = yaml.load(blfile, Loader=yaml.FullLoader)
            slots = blmodel['slots']
            for slot_name,slot in slots.items():
                slot_name = Text.snakify(slot_name)
                if 'is_a' in slot:
                    edge_tree[slot['is_a']].append(slot_name)
                else:
                    roots.add(slot_name)
                try:
                    slot_uri = slot['slot_uri']
                    uri_to_slot[slot_uri] = slot_name
                except:
                    pass
        return uri_to_slot,edge_tree,roots

    def get_edge_by_iri(self,curie):
        try:
            return self.iri_to_name[curie]
        except:
            return None

    def get_iri_by_edge(self,edge):
        try:
            edgename = Text.snakify(edge)
            return self.name_to_iri[edgename]
        except:
            return None

    def get_edge_by_iri(self,curie):
        Edge = namedtuple('edge',['identifier','label'])
        edge = Edge()

    def get_root_edges(self):
        return list(self.root_edges)

    def get_children(self,edge_name):
        return self.edge_tree[edge_name]

if __name__ == '__main__':
    bl = biolink()
