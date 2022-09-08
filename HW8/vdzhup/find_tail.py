def correct_tail(body, tail):
    sub = body[len(body) - len(tail)]
    if sub == tail:
        return True
    return False


print(correct_tail("Fox", "x"))
print(correct_tail("Emu", "t"))
