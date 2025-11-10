import pytest
from packaging_demo.slow import slow_add

@pytest.mark.slow
def test__slow_add__successful():
    sum_ = slow_add(1, 2)
    assert sum_ == 3