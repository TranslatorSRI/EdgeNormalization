import pytest
from src.biolink_client import biolink

def test_tree():
    bl = biolink()
    assert 'related_to' in bl.get_root_edges()
    assert bl.get_iri_by_edge('related to') == 'owl:ObjectProperty'
