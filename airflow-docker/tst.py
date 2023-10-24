import os
import pandas as pd


url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
df = pd.read_csv(url)
# df.to_csv(os.path.join(os.path.expanduser('~'), 'titanic.csv'), encoding='utf-8')
# df.to_csv(os.path.join(os.path.expanduser('~'), 'titanic.csv'), encoding='utf-8')
# df.to_csv('data/titanic1.csv', encoding='utf-8')
df.to_csv(os.path.join(os.path.expanduser('~/ds-intro/33_airflow'), 'titanic.csv')) #'C://Users/user/ds-intro/titanic.csv')

