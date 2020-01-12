from src.util import Text
import requests

class biolink:
    """This class is merely a placeholder.  Currently it's implemented
    by pulling in the biolink yaml.  But it's going to be re-implemented as a client
    on a biolink model service."""
    def __init__(self):
        self.url_base = 'http://robokop.renci.org:8144'

    def get_label_by_iri(self,curie):
        url = f'{self.url_base}/uri_lookup/{curie}'
        results = requests.get(url).json()
        return results

    def get_iri_by_label(self,concept):
        url = f'{self.url_base}/bl/{Text.snakify(concept)}'
        result = requests.get(url).json()
        if result is not None:
            return result['slot_uri']
        return None


