#Updated Calculator to do add, sub, multiply and divide 
first_num = input("First Number:\n")
ops = input("Operator (+, -, *, /):\n")
second_num = input("Second Number:\n")

first_num = float(first_num)
second_num = float(second_num)

out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
    
print("Answer: " + str(out))
