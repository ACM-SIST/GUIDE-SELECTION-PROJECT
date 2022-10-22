
import pandas as pd

comp_file = pd.read_csv("comp.csv")
t = comp_file['REGISTER'].values
list1 = list(t)
print('Total filled IN COMP.CSV: ', len(list1))

full_file = pd.read_csv("full.csv")
t = full_file['REGISTER'].values
list2 = list(t)
print('Total filled IN FULL.CSV: ', len(list2))

c = []

# for i in range(0, len(a)):
#     for j in range(0, len(b)):
#         if a[i] == b[j]:
#             c.append(b[i])

# c = set(list1).difference(list2)

# c = list(c)

print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))
c = list(set(list2).difference(list1))
print('Total un-filled: ', len(c))
# print(c)
df = pd.DataFrame({'Register': c, })
df.index.name = 'ID'

df.to_excel('NOT FILLED STUDENTS.xlsx')
