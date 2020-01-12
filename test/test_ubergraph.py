import pytest
from src.ubergraph import UberGraph

def test_entity_parent():
    r = UberGraph()
    parents = r.get_entity_parent('CL:0000540')
    assert 'CL:0002319' in parents

def test_property_parent():
    r = UberGraph()
    parents = r.get_property_parent('RO:0002496')
    print(parents)
    assert 'RO:0002487' in parents

