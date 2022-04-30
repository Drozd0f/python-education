"""This module contains test HashTable for exercise Data Structures - practice"""
import pytest

from data_structures.hash_table import HashTable


@pytest.mark.parametrize(
    'key, value',
    [
        ('Danilo', 21),
        ('Vova', 22),
        (32, 20),
        ('Alex', 33)
    ]
)
def test_insert_and_lookup(hash_table_obj: HashTable, key: int, value: int):
    """This test check method insert and lookup HashTable data structures"""
    hash_table_obj.insert(key, value)
    assert hash_table_obj.lookup(key) == value


@pytest.mark.parametrize(
    'key, value',
    [
        ('Danilo', 21),
        ('Vova', 22),
        (32, 20),
        ('Alex', 33)
    ]
)
def test_delete(hash_table_obj: HashTable, key: int, value: int):
    """This test check method delete HashTable data structures"""
    hash_table_obj.insert(key, value)
    hash_table_obj.delete(key)
    with pytest.raises(KeyError) as excinfo:
        hash_table_obj.lookup(key)
    assert excinfo.type is KeyError
