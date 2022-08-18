import lib.calculator

while (type_operation := input("Which operation do you want do: 1-add, 2-sub, 3-multi, 4-div or 'q' for exit: ")) != 'q':
    a = float(input("Enter first operand: "))
    b = float(input("Enter second operand: "))

    match type_operation:
        case '1'|'add':
            print(f"Result of operation {a}+{b} = {lib.calculator.add(a,b)}")
        case '2' | 'sub':
            print(f"Result of operation {a}-{b} = {lib.calculator.sub(a,b)}")
        case '3' | 'multi':
            print(f"Result of operation {a}*{b} = {lib.calculator.mult(a,b)}")
        case '4' | 'div':
            print("Second operand can't be 0!" if b == 0 else f"Result of operation {a}/{b} = {lib.calculator.div(a,b)}")
        case _:
            print("Wrong enter data! ")
    print()

