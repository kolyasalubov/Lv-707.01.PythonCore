def double_char(s: str) -> str:
    return "".join((i*2 for i in s))


print(double_char('Helo Python'))