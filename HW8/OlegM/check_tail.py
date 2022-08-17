def correct_tail(body, tail):
    # check correct tail
    return True if body[-1] == tail[0] else False


print(correct_tail('fox', 'x'))
