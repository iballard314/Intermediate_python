'''
int edges cases
__________________________________________________________________________________________________________________________________________

An edge case is a situation where the input or behavior is at the extreme, unusual, or unexpected edges of what your code normally handles.

These cases often break code, cause errors, or produce weird results—because they are not typical.

Think of it like testing the “edges” or limits of a function to make sure it works everywhere.

'''

# extreamly large numbers
#-----------------------------------------------------------------------#

print("10**100")
print(10**100)

print('\n','-'*60)
#int to float with division conversition
#-----------------------------------------------------------------------#

print("10 / 5")
print(10 / 5)
print(f"10 / 5 is {type(10/5)}")

print('\n','-'*60)
#module of negative integers
#-----------------------------------------------------------------------#

print("11% -2")
print(11%-2)

print("-11 / 2")
print(-11%2)

print('\n','-'*60)
# Boolean
#-----------------------------------------------------------------------#

#false values  
print(f"bool(0) is {bool(0) }")       # False
print(f"bool(0.0) is {bool(0.0)}")      # False
print(f"bool('') is {bool('') }")      # False
print(f"bool([]) is {bool([])}")      # False
print(f"bool('{{}}') is {bool({})}")       # False

print('\n','-'*60)
#true values
print(f"bool(1) is {bool(1)}")        # True
print(f"bool('hi') is {bool('hi')}")        # True
print(f"bool([0]) is {bool([0])}")        # True
bool([0])      # True

print('\n','-'*60)
# Float edge cases
#-----------------------------------------------------------------------#
print(0.1 + 0.2)
print(1.2 - 1.0)

print('\n','-'*60)
#special values 
#-----------------------------------------------------------------------#
print(float('inf'))
print(float('-inf'))
