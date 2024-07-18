from ucimlrepo import fetch_ucirepo
import pandas as pd

def calculate_demograpy_data(df):
    try:
        race_count = df['race'].nunique()
        average_age_men = df[df['sex'] == 'Male']['age'].mean()
        percentage_bachelors = (df['education'].value_counts(normalize=True).loc["Bachelors"]) * 100
        
        higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
        percentage_higher_education = (len(higher_education[higher_education['income'] == '>50K']) / len(higher_education)) * 100
        
        lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
        percentage_lower_education = (len(lower_education[lower_education['income'] == '>50K']) / len(lower_education)) * 100
        
        min_work_hours = df['hours-per-week'].min()
        num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
        rich_percentage = (len(df[(df['hours-per-week'] == min_work_hours) & (df['income'] == '>50K')]) / num_min_workers) * 100
        
        highest_earning_country = (df[df['income'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
        highest_earning_country_percentage = ((df[df['income'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max()) * 100
        
        top_IN_occupation = df[(df['native-country'] == 'India') & (df['income'] == '>50K')]['occupation'].value_counts().idxmax()
        
        return {
            'race_count': race_count,
            'average_age_men': average_age_men,
            'percentage_bachelors': percentage_bachelors,
            'percentage_higher_education': percentage_higher_education,
            'percentage_lower_education': percentage_lower_education,
            'min_work_hours': min_work_hours,
            'rich_percentage': rich_percentage,
            'highest_earning_country': highest_earning_country,
            'highest_earning_country_percentage': highest_earning_country_percentage,
            'top_IN_occupation': top_IN_occupation
        }
    except Exception as e:
        print(f"Error in calculate_demograpy_data: {e}")
        return None

if __name__ == '__main__':
    try:
        adult = fetch_ucirepo(id=2)
        x = adult.data.features
        y = adult.data.targets
        df = pd.concat([pd.DataFrame(x), pd.DataFrame(y)], axis=1)
        
        results = calculate_demograpy_data(df)
        
        if results:
            for key, value in results.items():
                print(f"{key}: {value}")
        else:
            print("No valid results computed.")
    except Exception as e:
        print(f"Error in main script: {e}")
