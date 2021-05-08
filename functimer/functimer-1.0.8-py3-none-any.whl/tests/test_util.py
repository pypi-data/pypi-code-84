from functimer import Unit, get_unit, timed


def test_get_unit_nano():
    assert get_unit("0.2 ns") == Unit.nanosecond


def test_get_unit_micro():
    assert get_unit("0.2 µs") == Unit.microsecond


def test_get_unit_milli():
    assert get_unit("0.2 ms") == Unit.millisecond


def test_get_unit_second():
    assert get_unit("0.2 s") == Unit.second


def test_get_unit_minute():
    assert get_unit("0.2 m") == Unit.minute


def test_get_unit_func():
    @timed(unit=Unit.millisecond)
    def f():
        return 10

    assert get_unit(f()) == Unit.millisecond
