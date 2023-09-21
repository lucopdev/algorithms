def study_schedule(permanence_period, target_time):
    counter = 0

    for min_hour, max_hour in permanence_period:
        if (
            not permanence_period
            or not target_time
            or not min_hour
            or not max_hour
            or not isinstance(min_hour, int)
            or not isinstance(max_hour, int)
        ):
            return None
        if min_hour <= target_time <= max_hour:
            counter += 1
    return counter

    raise NotImplementedError
