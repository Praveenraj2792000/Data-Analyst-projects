import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

def draw_line_plot():
    df = pd.read_csv('C:\\Users\\HP\\Desktop\\my projects\\Data-Analyst-projects\\fcc-forum-pageviews.csv', parse_dates=['DATE'], index_col='DATE')
    df = df.loc['2016/05/01':'2019/12/31']
    df_clean = df[(df['VALUE'] >= df['VALUE'].quantile(0.025)) &
                  (df['VALUE'] <= df['VALUE'].quantile(0.975))]
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df_clean.index, df_clean['VALUE'], color='r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('DATE')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    df = pd.read_csv('C:\\Users\\HP\\Desktop\\my projects\\Data-Analyst-projects\\fcc-forum-pageviews.csv', parse_dates=['DATE'], index_col='DATE')
    df = df.loc['2016-05-01':'2019-12-31']
    df_clean = df[(df['VALUE'] >= df['VALUE'].quantile(0.025)) &
                  (df['VALUE'] <= df['VALUE'].quantile(0.975))]
    df_clean['year'] = df_clean.index.year
    df_clean['month'] = df_clean.index.month_name()
    df_clean['month'] = pd.Categorical(df_clean['month'], categories=calendar.month_name[1:], ordered=True)
    df_grouped = df_clean.groupby(['year', 'month'])['VALUE'].mean().unstack()
    fig, ax = plt.subplots(figsize=(14, 7))
    df_grouped.plot(kind='bar', ax=ax)
    ax.set_title('Average Page Views per Year by Month (5/2016-12/2019)')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=calendar.month_name[1:], loc='upper left')
    plt.xticks(rotation=45)
    fig.savefig('bar_plot.png')
    plt.show()
    
def draw_box_plot():
    df = pd.read_csv('C:\\Users\\HP\\Desktop\\my projects\\Data-Analyst-projects\\fcc-forum-pageviews.csv', parse_dates=['DATE'], index_col='DATE')
    df = df.loc['2016-05-01':'2019-12-31']
    df_clean = df[(df['VALUE'] >= df['VALUE'].quantile(0.025)) &
                  (df['VALUE'] <= df['VALUE'].quantile(0.975))]
    df_clean['year'] = df_clean.index.year
    df_clean['month'] = df_clean.index.month_name()
    df_clean['month'] = pd.Categorical(df_clean['month'], categories=calendar.month_name[1:], ordered=True)
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(x='year', y='VALUE', data=df_clean, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(x='month', y='VALUE', data=df_clean, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    plt.tight_layout()
    fig.savefig('box_plot.png')
    plt.show()
def main():
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
if __name__ == "__main__":
    main()
