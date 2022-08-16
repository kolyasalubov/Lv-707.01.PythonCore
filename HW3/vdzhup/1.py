python_philosofy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

count_better = python_philosofy.count("better")
count_never = python_philosofy.count("never")
count_is = python_philosofy.count("is")

print("'better' count:", count_better)
print("'never' count:", count_never)
print("'is' count:", count_is)

upper_text = python_philosofy.upper()
print(upper_text)

replace_text = python_philosofy.replace("i", "&")
print(replace_text)
