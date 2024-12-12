from src.decorators import log_first, log_second


def test_log(capsys):
    assert log_first(4, 6) == 10
    assert log_first(0, 0) == 0
    assert log_first(" ", " ") == "  "
    log_second(1, 5)
    captured = capsys.readouterr()
    assert captured.out == "6\n"
