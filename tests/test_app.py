"""
    test module
"""

import pytest
from src.app import model


@pytest.mark.parametrize(
    "value,weight,bias,expected",
    [
        (2,3,4,10),
        (0,5,10,10)
    ]
)
# def test_model():
#     """_summary_
#     """
#     assert model(2,3,4)==10
#     assert model(0,3,10)==10
#     assert model(0,60,0)==0

def test_model(value,weight,bias,expected):
    assert model(value,weight,bias) == expected
