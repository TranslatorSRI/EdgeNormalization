from src.triplestore import TripleStore
from src.util import Text
from collections import defaultdict

class UberGraph:

    def __init__(self):
        self.triplestore = TripleStore("https://stars-app.renci.org/uberongraph/sparql")

    def is_subclass(self, parent, child):
        return False

    def get_parent(self,child):
        """Given an ontology term, return its direct parent"""
        text="""
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT DISTINCT ?parent
        FROM <http://reasoner.renci.org/ontology/closure>
        WHERE {
            ?child rdfs:subClassOf ?parent .
            //FILTER NOT EXISTS { ?otherSub rdfs:subClassOf ?parent. 
            //                    ?child rdfs:subClassOf ?otherSub .
            //                    FILTER (?otherSub != ?child)

            //                    }
            }
        """
        results = self.triplestore.query_template(template_text=text,
                                                  inputs = {'child':child},
                                                  outputs = ['parent'])
        return results
    


