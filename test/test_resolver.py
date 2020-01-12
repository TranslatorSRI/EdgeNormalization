import pytest
from src.resolver import EdgeNormalizer

def test_RO_exact():
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0002410')
    assert edge.identifier == 'RO:0002410'

def test_exact_slot_URI_non_RO():
    r = EdgeNormalizer()
    edge = r.resolve_curie('WD:P2293')
    assert edge.identifier == 'WD:P2293'
    assert edge.label == 'gene_associated_with_condition'

def test_exact_mapping():
    r = EdgeNormalizer()
    edge = r.resolve_curie('SEMMEDDB:PREVENTS')
    assert edge.identifier == 'RO:0002599'
    assert edge.label == 'prevents'

def test_RO_sub():
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0003303')
    assert edge.identifier == 'RO:0002410'
