import pytest
from hypothesis import given
import numpy as np

import crowddynamics.testing.strategies as st
from crowddynamics.core.steering import distance_map


@pytest.mark.skip
@given(
    step=st.real(min_value=0.001, max_value=0.01),
    field=st.field(),
)
def test_distance_map(step, field):
    domain, targets, obstacles = field
    mgrid, dmap, phi = distance_map(step, domain, targets, obstacles)

    assert isinstance(mgrid, np.ndarray)
    assert mgrid.dtype.type is np.float64
    assert isinstance(dmap, np.ndarray)
    assert dmap.dtype.type is np.float64
    assert isinstance(dmap, np.ma.MaskedArray)


@pytest.mark.skip
def test_travel_time_map():
    assert True


def test_direction_map():
    assert True


def test_merge_dir_maps():
    assert True


def test_static_potential():
    assert True


@pytest.mark.skip
def test_dynamic_potential():
    assert True

