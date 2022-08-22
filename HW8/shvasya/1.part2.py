what_do_you_want = input("1 - multiplying, 2 - subtraction, 3 - multiplying, 4 - division  ")
from calculator import *

if what_do_you_want == "1":
    func_summary()

elif what_do_you_want == "2":
    func_subtraction()

elif what_do_you_want == "3":
    func_multiplying()

elif what_do_you_want == "4":
    func_division()
