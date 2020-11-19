import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv = pd.read_csv('IBM.csv', sep=';')
value_list = pd.Series(dtype=int)
sum = csv['<VOL>'][0]
for i in range(1, len(csv['<DATE>'])):
    if csv['<DATE>'][i][3:] == csv['<DATE>'][i-1][3:]:
        sum += csv['<VOL>'][i]
    else:
        value_list = value_list.append(pd.Series([sum], [csv['<DATE>'][i-1][3:]]))
        sum = csv['<VOL>'][i]
    if i == len(csv['<DATE>'])-1:
        value_list = value_list.append(pd.Series([sum], [csv['<DATE>'][i-1][3:]]))
sns.set()
fig, axes = plt.subplots(nrows=2, ncols=1)
plt.xlabel('Date')
plt.ylabel('Volume')
value_list[0:int(len(value_list)/2)].plot(kind='bar', ax=axes[0])
value_list[int(len(value_list)/2):len(value_list)].plot(kind='bar', ax=axes[1])
#plt.show()