from core.my_sum import my_sum

import pytest


def test_my_sum():
    assert my_sum(3, 8) == 11


def test_negative_numbers():
    assert my_sum(-5, -54) == -59


def test_unlimited_args():
    assert my_sum(2, 45, 89, 64) == 200


def test_no_args():
    with pytest.raises(TypeError):
        my_sum()
