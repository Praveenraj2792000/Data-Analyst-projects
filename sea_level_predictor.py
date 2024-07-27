import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
def plot_sea_level_change(filename):
    data = pd.read_csv(filename)
    years = data['Year']
    sea_levels = data['CSIRO Adjusted Sea Level']
    years = pd.to_numeric(years, errors='coerce')
    sea_levels = pd.to_numeric(sea_levels, errors='coerce')
    data_clean = pd.DataFrame({'Year': years, 'Sea Level': sea_levels})
    data_clean = data_clean.dropna()
    years = data_clean['Year']
    sea_levels = data_clean['Sea Level']
    plt.figure(figsize=(12, 6))
    plt.scatter(years, sea_levels, color='blue', label='Data', alpha=0.6)
    slope, intercept, r_value, p_value, std_err = linregress(years, sea_levels)
    plt.plot(years, slope * years + intercept, color='red', label='Fit Line (All Data)', linewidth=2)
    recent_data = data_clean[data_clean['Year'] >= 2000]
    recent_years = recent_data['Year']
    recent_sea_levels = recent_data['Sea Level']
    recent_slope, recent_intercept, r_value, p_value, std_err = linregress(recent_years, recent_sea_levels)
    plt.plot(recent_years, recent_slope * recent_years + recent_intercept, color='green', label='Fit Line (2000+)', linewidth=2)
    future_years = pd.Series(range(1880, 2051))
    plt.plot(future_years, slope * future_years + intercept, color='red', linestyle='--', linewidth=2)
    plt.plot(future_years, recent_slope * future_years + recent_intercept, color='green', linestyle='--', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.xlim([1880, 2050])
    plt.ylim(bottom=sea_levels.min() - 10, top=sea_levels.max() + 10)
    plt.savefig('sea_level_rise.png')
    plt.show()
if __name__ == "__main__":
    plot_sea_level_change('C:\\Users\\HP\\Desktop\\my projects\\Data-Analyst-projects\\epa-sea-level.csv')
