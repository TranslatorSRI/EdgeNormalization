from src.util import Text, LoggingUtil
import logging
import requests
import os
from urllib.parse import quote_plus, unquote_plus

logger = LoggingUtil.init_logging(__name__)


class biolink:
    """This class is merely a placeholder.  Currently it's implemented
    by pulling in the biolink yaml.  But it's going to be re-implemented as a client
    on a biolink model service."""
    def __init__(self):
        self.url_base = os.environ.get('BL_HOST', 'http://robokop.renci.org:8144')

    def get_label_by_iri(self,curie):
        # escaping curie for things like CTD:marker/mechanism
        url = f'{self.url_base}/uri_lookup/{quote_plus(quote_plus(curie))}'
        results = requests.get(url)
        if results.status_code == 200:
            return results.json()
        else:
            logger.error(f'[x] Error making request to {url}, status {results.status_code}')
            return []

    def get_iri_by_label(self,concept):
        url = f'{self.url_base}/bl/{Text.snakify(concept)}'
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            if result is not None:
                return result.get('slot_uri', Text.snakify(concept))
        else:
            logger.error(f'[x] Error making request to {url}, status {response.status_code}')
        return None


