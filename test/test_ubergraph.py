import pytest
from src.ubergraph import UberGraph

def test_entity_parent():
    r = UberGraph()
    parents = r.get_parent('CL:0000540')
    print(parents)
    assert parents[0] == 'CL:0002319'

