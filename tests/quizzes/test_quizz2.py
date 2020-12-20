def placement(capital, rate, duration):
    return round(capital * (rate / 100 + 1) ** duration, 2)
