import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
def mpg_data():
    df = pd.read_csv('clean.csv')
    return df

df = mpg_data()
def ranking(column):
    usa = df[df['origin'] == 'usa'].sort_values(by=column, ascending=False).head(3)['name'].values
    japan = df[df['origin'] == 'japan'].sort_values(by=column, ascending=False).head(3)['name'].values
    europe = df[df['origin'] == 'europe'].sort_values(by=column, ascending=False).head(3)['name'].values

    df_rank = pd.DataFrame({
        'Ranking':['Rank 1','Rank 2', 'Rank 3'],
        'Usa': usa,
        'Japan' : japan,
        'Europe' : europe
    })
    return df_rank



