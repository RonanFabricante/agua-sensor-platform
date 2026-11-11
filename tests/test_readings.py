from agua_meter.readings import is_valid_reading


def test_valid_range():
    assert is_valid_reading(12.5)


def test_rejects_out_of_range():
    assert not is_valid_reading(-1)
    assert not is_valid_reading(75)
