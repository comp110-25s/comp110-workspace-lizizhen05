"""Unit tests for Dictionary Functions"""

__author__: str = "730667645"


import pytest


from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use_case_1():
    assert invert({'a': 'b', 'c': 'd'}) == {'b': 'a', 'd': 'c'}


def test_invert_use_case_2():
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_edge_case_keyerror():
    with pytest.raises(KeyError):
        invert({'kris': 'jordan', 'michael': 'jordan'})


def test_count_use_case_1():
    assert count(['a', 'b', 'a']) == {'a': 2, 'b': 1}


def test_count_use_case_2():
    assert count(['cat', 'dog', 'cat', 'dog', 'dog']) == {'cat': 2, 'dog': 3}


def test_count_edge_case_empty_list():
    assert count([]) == {}


def test_favorite_color_use_case_1():
    assert favorite_color(
        {'Alice': 'blue', 'Bob': 'red', 'Cathy': 'blue'}) == 'blue'


def test_favorite_color_use_case_2():
    assert favorite_color(
        {'Zoe': 'green', 'Leo': 'green', 'Amy': 'yellow'}) == 'green'


def test_favorite_color_edge_case_tie():
    assert favorite_color(
        {'A': 'blue', 'B': 'red', 'C': 'red', 'D': 'blue'}) == 'blue'


def test_bin_len_use_case_1():
    assert bin_len(["hi", "dog", "cat", "yo", "sun"]) == {
        2: {"hi", "yo"},
        3: {"dog", "cat", "sun"}
    }


def test_bin_len_use_case_2():
    assert bin_len(["a", "be", "see", "do", "no"]) == {
        1: {"a"},
        2: {"be", "do", "no"},
        3: {"see"}
    }


def test_bin_len_edge_case_empty_list():
    assert bin_len([]) == {}
