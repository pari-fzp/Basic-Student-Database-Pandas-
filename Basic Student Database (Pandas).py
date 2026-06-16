import pandas as pd
name=[]
code=[]
num = int(input("How many users? "))

for i in range(num):
    n = input("name: ")
    c = input("code: ")
    name.append(n)
    code.append(c)

data = { "Name" : name,
        "Cod" : code}
df= pd.DataFrame(data)

show =input("do you want see the name list? (yes/no): ").lo0wer()
if show == 'yes':
        print('this is your name list: \n') 
        print(df)
else:
    print("kay, by! ")