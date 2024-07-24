import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\HP\\Desktop\\my projects\\Data-Analyst-projects\\medical_examination.csv')
df['overweight'] = (df['Weight'] / ((df['Height'] / 100) ** 2)) > 25
df['overweight'] = df['overweight'].astype(int)
df['Cholesterol'] = df['Cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['Glucose'] = df['Glucose'].apply(lambda x: 1 if x > 1 else 0)
def draw_cat_plot():
    variables = ['Cholesterol', 'Glucose', 'Smoking', 'Alcohol intake', 'overweight']
    df_cat = pd.melt(df, id_vars=['Cardiovascular disease'], value_vars=variables)
    df_cat = df_cat.groupby(['Cardiovascular disease', 'variable', 'value']).size().reset_index(name='total')
    g = sns.catplot(x='variable', y='total', hue='value', col='Cardiovascular disease', data=df_cat, kind='bar')
    fig = g.fig
    return fig
def draw_heat_map():
    df_heat = df[
        (df['Height'] >= df['Height'].quantile(0.025)) &
        (df['Height'] <= df['Height'].quantile(0.975)) &
        (df['Weight'] >= df['Weight'].quantile(0.025)) &
        (df['Weight'] <= df['Weight'].quantile(0.975)) 
        
    ]
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(11, 9))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', vmin=-0.1, vmax=0.25, center=0, square=True, linewidths=.5, cbar_kws={'shrink': .45, 'format': '%.2f'})
    return fig
draw_cat_plot()
draw_heat_map()
plt.show()
