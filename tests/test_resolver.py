import pytest
from src.resolver import EdgeNormalizer

def test_RO_exact():
    '''If we have an RO that is a slot uri, return an edge with that identfier'''
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0002410')
    assert edge.identifier == 'biolink:causes'

def test_exact_slot_URI_non_RO():
    '''If we have a curie that is not a RO, but is a slot uri, return it as an edge identifier'''
    r = EdgeNormalizer()
    edge = r.resolve_curie('WD:P2293')
    assert edge.identifier == 'biolink:gene_associated_with_condition'
    assert edge.label == 'gene_associated_with_condition'

def test_exact_mapping():
    '''If we have a curie that is a direct mapping, but not a slot uri, return the corresponding slot uri as an edge identifier'''
    r = EdgeNormalizer()
    edge = r.resolve_curie('SEMMEDDB:PREVENTS')
    assert edge.identifier == 'biolink:prevents'
    assert edge.label == 'prevents'

def test_RO_sub():
    '''If we have a curie that is an RO, but is not a slot uri or a mapping, move to superclasses of the RO until we
    find one that we can map to BL. '''
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0003303')
    assert edge.identifier == 'biolink:causes'

def test_RO_sub_2():
    '''If we have a curie that is an RO, but is not a slot uri or a mapping, move to superclasses of the RO until we
    find one that we can map to BL. '''
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0002448')
    print(edge)
    #assert edge.identifier == 'RO:0002410'

def test_RO_bad():
    '''RO isn't single rooted.  So it's easy to get to the follow our plan and not get anywhere.  In that case,
    we want to hit related_to by fiat.'''
    r = EdgeNormalizer()
    edge = r.resolve_curie('RO:0000052')
    assert edge.label == 'related_to'
    assert edge.identifier == 'biolink:related_to'
