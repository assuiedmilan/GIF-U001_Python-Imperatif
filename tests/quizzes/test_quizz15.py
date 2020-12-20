import math


def histogramme(values, *, maxetiq=None, maxval=None):
    lines = []
    pace = 10

    max_index = math.ceil(max(values.values()) / pace) * pace
    max_index = max_index if maxval is None else min(max_index, maxval)

    max_key_length = max(len(x) for x in values)
    max_key_length = max_key_length if maxetiq is None else min(max_key_length, maxetiq)

    def compute_last_key_index(x):
        return len(x) if maxetiq is None else min(maxetiq, len(x))

    def compute_ticks(x):
        if maxval is None or x <= maxval:
            return x * '-'

        return (maxval - 1) * '-' + '*'

    def align_to_left(x):
        return "{}:".format(x[0:compute_last_key_index(x)].rjust(max_key_length))

    first_line = '0'
    second_line = '+'
    for x in range(pace, max_index + pace, pace):
        first_line = '{}{:>10}'.format(first_line, x)
        second_line = '{}{:->10}'.format(second_line, '+')

    lines.append("{}{}".format(max_key_length * " ", first_line))
    lines.append("{}{}".format(max_key_length * " ", second_line))

    lines = lines + ["{}{}".format(align_to_left(key),
                                   compute_ticks(values[key])) for key in sorted(values)]

    lines.append(lines[1])
    lines.append(lines[0])

    return "\n".join(lines)


def test_histogramme():
    first_case = """               0        10        20        30
               +---------+---------+---------+
          chats:----------
         chiens:-------------------------
poissons rouges:---
        tortues:-------
               +---------+---------+---------+
               0        10        20        30"""

    second_case = """        0        10        20
        +---------+---------+
   chats:----------
  chiens:-----------------*
poissons:---
 tortues:-------
        +---------+---------+
        0        10        20"""

    assert histogramme({'chats': 10, 'poissons rouges': 3, 'chiens': 25, 'tortues': 7}) == first_case
    assert histogramme({'chats': 10, 'poissons rouges': 3, 'chiens': 25, 'tortues': 7}, maxetiq=8, maxval=18) == second_case
