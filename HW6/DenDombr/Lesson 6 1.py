def biggest(* args):
    max = args[0]
    for item in args[1:]:
        if item > max:
            max = item
    return max

