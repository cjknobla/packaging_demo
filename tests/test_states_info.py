from packaging_demo.states_info import is_city_capitol_of_state
import pytest

@pytest.mark.parametrize(
        argnames="city_name, state, is_capitol",
        argvalues=[
            ("Montgomery", "Alabama", True),
            ("Lansing", "Michigan", True),
            ("Salt Lake City", "Alabama", False)
        ]
)
def test__is_city_capitol_of_state__true_for_correct_city_state_pair(city_name: str, state: str, is_capitol: bool):
        assert is_city_capitol_of_state(city_name=city_name, state=state) == is_capitol
