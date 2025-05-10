
import pandas as pd
data=pd.read_csv('data/air_pollution_china.csv')
column_names=data.columns.tolist()
cities=data['City'].unique()
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

def process_data(i):
    city=cities[i]
    df=data[data['City']==city]
    df_avg= df.groupby(['Year', 'Month'])[column_names[0:14]].mean().reset_index()
    df_avg.iloc[:, 1:16] = df_avg.iloc[:, 1:16].round(2)
    df_avg['Season'] = df_avg['Month'].apply(get_season)
    df_avg.to_csv(f'data/{cities[i]}_avg_data.csv', index=False)
for i in range(len(cities)):
    process_data(i)