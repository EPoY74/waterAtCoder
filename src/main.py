input_str: str = """\
4
1 3
3 1
4 4
7 1
"""


def get_data_from_input_str(
    input_val: str,
) -> tuple[int, list[tuple[int, int]]]:
    """
    Docstring for get_data_from_input_str

    :param input: Description
    :type input: str
    :return: Description
    :rtype: list[int]
    """
    try:
        input_list = list(map(int, input_val.strip().split()))
    except ValueError as err:
        raise err
    input_count = int(input_list.pop(0))

    parsed_input = [
        (int(input_list[i]), int(input_list[i + 1]))
        for i in range(0, len(input_list), 2)
    ]

    return (input_count, parsed_input)


def main() -> None:
    current_water_volume_l: int = 0
    water_flow_rate: int = 1  # per hour

    num_water, water = get_data_from_input_str(input_str)


if __name__ == "__main__":
    main()
