'''
Type coercion is when Python automatically converts one data type into another so an operation can work. For example, 
if you add an int and a float, Python converts the int to a float behind the scenes. 
Booleans also get coerced to integers (True → 1, False → 0)when used in math. Coercion helps operations run smoothly,
 but it can cause unexpected results if you don’t realize a type changed.

'''

# int <==>  float
# -----------------------------------------------------#
a = 5
b = 1.0

print(f"{a} is {type(a)} and {b} is {type(b)}")
print(f"a + b = { a + b} and is {type(a+b)}")



#int => boolen
# -----------------------------------------------------#
print(f"int(True) is {int(True)}")
print('\n','-'*60)


print('\n','-'*60)
# float => int(truncate)
# -----------------------------------------------------#
print(f"2.71  is {type(2.71)} and int(2.71) is {int(2.71)}")