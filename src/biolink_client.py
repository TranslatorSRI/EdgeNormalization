from src.util import Text, LoggingUtil
import logging
import requests
import os
from urllib.parse import quote_plus, unquote_plus

logger = LoggingUtil.init_logging(__name__)


class biolink:
    def __init__(self, bl_version="latest"):
        self.url_base = os.environ.get('BL_HOST', 'https://bl-lookup-sri.renci.org')
        self.bl_version = bl_version

    def get_label_by_iri(self,curie):
        # escaping curie for things like CTD:marker/mechanism
        url = f'{self.url_base}/uri_lookup/{quote_plus(quote_plus(curie))}?version={self.bl_version}'
        results = requests.get(url)
        if results.status_code == 200:
            return results.json()
        else:
            logger.error(f'[x] Error making request to {url}, status {results.status_code}')
            return []

    def get_iri_by_label(self,concept):
        url = f'{self.url_base}/bl/{Text.snakify(concept)}?version={self.bl_version}'
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            if result is not None:
                return result.get('slot_uri', Text.snakify(concept))
        else:
            logger.error(f'[x] Error making request to {url}, status {response.status_code}')
        return None


