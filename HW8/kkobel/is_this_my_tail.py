'''
To make sure that the second argument (tail), 
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
If the tail is right return true, else return false.
The arguments will always be non empty strings, and normal letters.
'''

def correct_tail(body, tail):
    sub = body.endswith(f"{tail}")
    return True if sub  else  False

def correct_tail(body, tail):
    sub = body[(len(body)- len(tail))]
    return True if sub == tail else False

print(f"Result of string: {correct_tail('Fox', 'x')}")
print(f"Result of string: {correct_tail('Elephant', 'x')}")
print(f"Result of string: {correct_tail('Mouse', 'e')}")
