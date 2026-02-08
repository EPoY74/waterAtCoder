def main(input_data: str) -> str:
    """
    Calculate how much water will be in the humidifier after the last refill.
    Between refills, the water level decreases by 1 unit per 1 unit of time.
    The water level cannot become negative.

    Parameters:
    input_data: (str) - input data in the format:
    - First line: integer N — number of refills
    - Next N lines: two integers T_i and V_i — time and refill volume

    Example input:
    4   - number of refills
    1 3 : 1 - refill time, 3 - refill water
    3 1
    etc

    Output:
    (str) - final water volume
    """
    current_water_volume_l: int = 0
    d_time: int = 0
    past_water_time: int = 0
    water_time: int = 0
    d_water: int = 0
    water_volume_l: int = 0
    try:
        input_list = list(map(int, input_data.strip().split()))
    except ValueError as err:
        raise err
    input_list.pop(0)

    water = [
        (int(input_list[i]), int(input_list[i + 1]))
        for i in range(0, len(input_list), 2)
    ]
    for index, (water_time, water_volume_l) in enumerate(water):
        if index == 0:
            # d_water = water_volume_l
            current_water_volume_l = water_volume_l
        if index > 0:
            d_time = water_time - past_water_time
            if d_time >= current_water_volume_l:
                current_water_volume_l = 0
                d_water = 0
            else:
                d_water = current_water_volume_l - d_time
            current_water_volume_l = water_volume_l + d_water
        d_water = 0
        past_water_time = water_time
    return str(current_water_volume_l)
