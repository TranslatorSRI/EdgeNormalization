import pytest
from src.biolink_client import biolink

def test_get_name_by_predicate():
    bl = biolink()
    #assert 'related_to' in bl.get_root_edges()
    assert bl.get_name_by_predicate('biolink:related_to') == 'related to'

def test_get_label_from_mapping():
    bl = biolink()
    result = bl.get_biolink_predicate_by_mapping('RO:0002410')[0]
    assert result == {'mapping':'biolink:causes', 'mapping_type':'broad'}

    result = bl.get_biolink_predicate_by_mapping('SEMMEDDB:CAUSES')[0]
    assert result == {'mapping':'biolink:causes', 'mapping_type':'exact'}

    result = bl.get_biolink_predicate_by_mapping('WIKIDATA_PROPERTY:P1542')[0]
    assert result == {'mapping':'biolink:causes', 'mapping_type':'exact'}

