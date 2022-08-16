z="Beautiful is better than ugly. \
Explicit is better than implicit.\
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren't special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.\
Although that way may not be obvious at first unless you're Dutch. \
Now is better than never. \
Although never is often better than *right* now.\
If the implementation is hard to explain, it's a bad idea. \
If the implementation is easy to explain, it may be a good idea.\
Namespaces are one honking great idea -- let's do more of those! "


print("\n\n\nSplited:\n", z.split())

w_better=0
w_never=0
w_is=0
for i in z.split():
    if i =="better":
        w_better+=1
    if i =="never":
        w_never+=1
    if i =="is":
        w_is+=1


print("Number of the word \"better\" is: %d \nNumber of the word \"never\" is:%d  \nNumber of the word \"is\" is:%d" % (w_better, w_never, w_is ))
print("\n\n\nZEN UPPER:",z.upper())

print("\n\n\nREPLACED \"i\" for \"&:\"\n",z.replace("i","&"))
