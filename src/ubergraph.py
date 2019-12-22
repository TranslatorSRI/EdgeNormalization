from src.triplestore import TripleStore
from src.util import Text
from collections import defaultdict

class UberGraph:

    def __init__(self):
        self.triplestore = TripleStore("https://stars-app.renci.org/uberongraph/sparql")

    def is_subclass(self, parent, child):
        return False


