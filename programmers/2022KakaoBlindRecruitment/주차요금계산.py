import math

def solution(fees, records):
    basic_minute = fees[0]
    basic_fee = fees[1]
    minute_rate = fees[2]
    unit_fee = fees[3]

    parked_cars = list(set(map(lambda x: x.split()[1], records)))
    total_fees = {k: 0 for k in parked_cars}
    check_in_times = {}

    for record in records:
        record_info = record.split(' ')
        car_id = record_info[1]

        if car_id not in check_in_times.keys():
            check_in_times[car_id] = record_info[0]
        else:
            if record_info[-1] == 'OUT':
                out_time = int(record_info[0].split(':')[0]) * 60 + int(record_info[0].split(':')[1])
                in_time = int(check_in_times[car_id].split(':')[0]) * 60 + int(check_in_times[car_id].split(':')[1])
                total_fees[car_id] += out_time - in_time
                del check_in_times[car_id]

    if check_in_times:
        for car_id in check_in_times.keys():
            out_time = 1439
            in_time = int(check_in_times[car_id].split(':')[0]) * 60 + int(check_in_times[car_id].split(':')[1])
            total_fees[car_id] += out_time - in_time

    result = []
    for car_id, time_parked in total_fees.items():
        if time_parked <= basic_minute:
            result.append((car_id, basic_fee))
        else:
            additional_units = math.ceil((time_parked - basic_minute) / minute_rate)
            result.append((car_id, basic_fee + (additional_units * unit_fee)))

    return list(map(lambda x: x[1], sorted(result)))
