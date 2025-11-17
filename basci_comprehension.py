print("Basic list comprehension")
print("\n","-"*50)


integers = [x for x in range(5)]
print(f"integers are {integers}")

even = [2*x for x in range(5)]
print(f"Evens are {even}")



print("\n","-"*50)

first = ['Johann','Markus','Sara','Anja']
last =['Ziegler', 'Müller','Schneider','Scmidt']

email =[first[i][:1] +last[i]+"@gmail.com" for i in range(len(first))]
print(*email)

800-782-8332