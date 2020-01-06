import pytest
from src.resolver import EdgeNormalizer

def test_exact_resolver():
    r = EdgeNormalizer()
    edge = r.resolve_curie('related_to')
    assert edge.identifier == 'owl:ObjectProperty'
    assert edge.label == 'related_to'
