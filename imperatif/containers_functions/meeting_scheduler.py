def meeting_scheduler(list_of_sets):
    if list_of_sets:
        return set.intersection(*list_of_sets)

    return set()
