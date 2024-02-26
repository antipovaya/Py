import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

data.loc[data['whoAmI'] == 'human', 'human'] = int(1)
data.loc[data['whoAmI'] == 'robot', 'human'] = int(0)
data.loc[data['whoAmI'] == 'robot', 'robot'] = int(1)
data.loc[data['whoAmI'] == 'human', 'robot'] = int(0)

data.pop('whoAmI')

print(int(data))