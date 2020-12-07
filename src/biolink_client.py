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

    def get_biolink_predicate_by_mapping(self,curie):
        # escaping curie for things like CTD:marker/mechanism
        url = f'{self.url_base}/uri_lookup/{quote_plus(quote_plus(curie))}?version={self.bl_version}'
        results = requests.get(url)
        if results.status_code == 200:
            return results.json()
        else:
            logger.error(f'[x] Error making request to {url}, status {results.status_code}')
            return []

    def get_name_by_predicate(self,predicate):
        #url = f'{self.url_base}/{quote_plus(quote_plus(predicate))}?version={self.bl_version}'
        url = f'{self.url_base}/bl/{predicate}?version={self.bl_version}'
        results = requests.get(url)
        if results.status_code == 200:
            return results.json()['name']
        else:
            logger.error(f'[x] Error making request to {url}, status {results.status_code}')
            return []



