import pytest
from src.resolver import EdgeNormalizer

def test_exact_resolver():
    r = EdgeNormalizer()
    edge = r.resolve_curie('related_to')
    assert edge.identifier == 'owl:ObjectProperty'
    assert edge.label == 'related_to'

def test_RO_exact():
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0002410')
    assert edge.identifier == 'RO:0002410'

def test_RO_sub():
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0003303')
    assert edge.identifier == 'RO:0002410'
