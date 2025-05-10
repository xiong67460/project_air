from sklearn.model_selection import train_test_split
import pandas as pd
df=pd.read_csv('data/air_pollution_china.csv')
column_names=df.columns.tolist()
cities=df['City'].unique()
def func1(i):
    city=cities[i]
    data=pd.read_csv(f'data/{city}_avg_data.csv')
    