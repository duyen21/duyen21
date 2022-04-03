import pandas as pd

#comment for fun lol
df0 = pd.read_csv('group_zero.csv')
df0.drop(columns=df0.columns[0], axis=1, inplace=True)
df0 = df0.astype(str)
df0 = df0.to_json(orient='records')
with open('group_zero.json', 'w') as f:
    f.write(df0)

df1 = pd.read_csv('group_one.csv')
df1.drop(columns=df1.columns[0], axis=1, inplace=True)
df1 = df1.astype(str)
df1 = df1.to_json(orient='records')
with open('group_one.json', 'w') as f:
    f.write(df1)

df2 = pd.read_csv('group_two.csv')
df2.drop(columns=df2.columns[0], axis=1, inplace=True)
df2 = df2.astype(str)
df2 = df2.to_json(orient='records')
with open('group_two.json', 'w') as f:
    f.write(df2)

df3 = pd.read_csv('group_three.csv')
df3.drop(columns=df3.columns[0], axis=1, inplace=True)
df3 = df3.astype(str)
df3 = df3.to_json(orient='records')
with open('group_three.json', 'w') as f:
    f.write(df3)
