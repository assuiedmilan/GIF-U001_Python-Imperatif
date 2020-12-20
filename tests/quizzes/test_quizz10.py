import math


def calculer_distance_parcourue(coordinates):

    def __compute_distance_between_two_points(coordinates):
        if not coordinates or len(coordinates) < 2:
            yield 0

        for index in range(len(coordinates) - 1):
            x1, y1 = coordinates[index]
            x2, y2 = coordinates[index + 1]
            yield math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return sum(__compute_distance_between_two_points(coordinates))


def test_calculer_distance():
    assert calculer_distance_parcourue([(1, 2), (2, 3), (7, 4), (6, 0)]) == 10.63633870158354
