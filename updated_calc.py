#Updated Calculator to do add, sub, multiply and divide 
first_num = input("First Number:\n")
ops = input("Operator (+, -, *, /):\n")
second_num = input("Second Number:\n")

first_num = float(first_num)
second_num = float(second_num)

out = None

if ops == "+":
    out =  first_num + second_num
elif ops == "-":
    out = first_num - second_num
elif ops == "*":
    out = first_num * second_num
elif ops == "/":
    out = first_num / second_num
    
print("Answer: " + str(out))
