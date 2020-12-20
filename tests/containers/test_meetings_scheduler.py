import pytest
from imperatif.containers_functions.meeting_scheduler import meeting_scheduler


@pytest.mark.parametrize("value, expected_result", [
    ([{1, 2, 3, 4}, {2, 3, 4}, {1, 2, 3}, {4, 5, 3, 2}], {2, 3}),
    ([], set()),
    ([set()], set()),
    ([{0}], {0})
])
def test_meeting_scheduler(value, expected_result):
    result = meeting_scheduler(value)

    assert result == expected_result
    assert isinstance(result, set)
