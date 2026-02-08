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


def main(input_data: str) -> str:
    current_water_volume_l: int = 0
    water_flow_rate: int = 1
    d_time: int = 0

    past_water_time: int = 0
    water_time: int = 0
    d_water: int = 0

    water_volume_l: int = 0

    num_water, water = get_data_from_input_str(input_data)

    for index, (water_time, water_volume_l) in enumerate(water):
        if index == 0:
            # d_water = water_volume_l
            current_water_volume_l = water_volume_l
        if index > 0:
            d_time = water_time - past_water_time
            if d_time >= current_water_volume_l:
                current_water_volume_l = 0
            else:
                d_water = current_water_volume_l - (d_time * water_flow_rate)
            current_water_volume_l = water_volume_l + d_water
        past_water_time = water_time

    print(current_water_volume_l)
    return str(current_water_volume_l)
