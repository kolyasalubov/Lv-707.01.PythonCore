def distance(x1, y1, x2, y2):
    distance_of_two_pairs = (((x2-x1) ** 2) + ((y2-y1) ** 2))
    result_of_sqrt = distance_of_two_pairs ** 0.5
    result_of_round = float("%0.2f" % result_of_sqrt)
    return result_of_round

print(f"Distance of two ordered pairs: is: {distance(1, 1, 0, 0)}")
