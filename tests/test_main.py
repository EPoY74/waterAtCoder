import pytest

from src.main import main


def test_first_case() -> None:

    input_str: str = """\
    4
    1 3
    3 1
    4 4
    7 1
    """

    expected_volume: str = "3"
    result: str = main(input_str)
    assert result == expected_volume


def test_second_case() -> None:

    input_str: str = """\
    3
    1 8
    10 11
    21 5
    """

    expected_volume: str = "5"
    result: str = main(input_str)
    assert result == expected_volume


def test_third_case() -> None:

    input_str: str = """\
    10
    2 1
    22 10
    26 17
    29 2
    45 20
    47 32
    72 12
    75 1
    81 31
    97 7
    """

    assert main(input_str) == "3"
