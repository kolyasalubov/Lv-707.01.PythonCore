def reversing(st: str):
    result_of_split_and_join = " ".join(st.replace(" ", " ").split(" ")[::-1])
    return result_of_split_and_join

print(reversing('Hello World'))

print(reversing('Hi There.'))
print(reversing('I am an expert at this'))
