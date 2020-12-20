def bissextile(value):
    return value % 4 == 0 and (value % 100 != 0 or value % 400 == 0)


def durée(first_date, second_date):
    def __numbers_of_days(value):
        return 366 if bissextile(value) else 365

    number_of_days = sum(__numbers_of_days(x) for x in range(first_date, second_date + 1))
    return number_of_days, \
        number_of_days * 24, \
        number_of_days * 24 * 60, \
        number_of_days * 24 * 60 ** 2


def test_bissextile():
    assert bissextile(1584)
    assert bissextile(1600)
    assert bissextile(1988)
    assert not bissextile(1500)
    assert not bissextile(1585)


def test_duree():
    assert (1096, 26304, 1578240, 94694400) == durée(2016, 2018)
