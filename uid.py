from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
import pandas as pd
setal = set(ascii_lowercase)
setau = set(ascii_uppercase)
setd = set(digits)

df = pd.read_csv('input.csv', header=None)
# print(df.head(10))
# print(df.info())
li = df[0].values.tolist()
for j in li:
    print(j)


for i in li:
    s = i
    # print(i)
    sets = set(s)
    # print(sets)
    if len(s) != 10 or len(sets) != 10:
        print('Invalid')
    else:
        if len(setau.intersection(sets)) < 2:
            print('Invalid')
            break
        if len(setd.intersection(sets))<3:
            print('Invalid')
            break
        print('Valid')
