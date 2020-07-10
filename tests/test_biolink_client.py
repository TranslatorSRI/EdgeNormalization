import pytest
from src.biolink_client import biolink

def test_get_iri_by_label():
    bl = biolink()
    #assert 'related_to' in bl.get_root_edges()
    assert bl.get_iri_by_label('related to') == 'biolink:related_to'

def test_get_label_from_slot_uri():
    bl = biolink()
    assert bl.get_label_by_iri('RO:0002410')[0] == 'causes'

def test_get_label_from_mapping():
    bl = biolink()
    assert bl.get_label_by_iri('SEMMEDDB:CAUSES')[0] == 'causes'
    assert bl.get_label_by_iri('WD:P1542')[0] == 'causes'

