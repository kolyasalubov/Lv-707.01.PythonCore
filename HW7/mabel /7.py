def reverse(str):
    str = " ".join(str.split()[::-1])
    return str


print(reverse("Hello World"))