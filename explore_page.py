import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to remove low count data points
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] =  categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

@st.cache
def load_data():
    df = pd.read_csv('survey_results_public.csv')
    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    df = df.rename({'ConvertedCompYearly':'Salary'}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df['Employment'] == 'Employed full-time']
    df = df.drop('Employment', axis=1)
    df['Country'] = df['Country'].replace('United States of America', 'USA')
    df['Country'] = df['Country'].replace('United Kingdom of Great Britain and Northern Ireland', 'UK')
    df['Country'] = df['Country'].replace('Russian Federation', 'Russia')

    country_map = shorten_categories(df.Country.value_counts(), 800)
    df['Country'] = df['Country'].map(country_map)

    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    return df

df = load_data()

def show_explore_page():
    st.title('Explore Data: StackOverflow Software Developer Salaries, 2021')
    data = df['Country'].value_counts()
    im = plt.imread('logo.png')
    fig, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90, shadow=True)
    ax1.axis('equal')


    st.write("""#### Pie Chart Showing Number of Respondents by Country ####""")

    st.pyplot(fig)

    st.write("""#### Boxplot Showing Variance in Salary Per Country ####""")
    fig1, ax2 = plt.subplots(1,1, figsize=(10,10))
    im = plt.imread('logo.png')
    df.boxplot('Salary', 'Country', ax=ax2)
    plt.suptitle('Salary (US$) V Country')
    plt.title('')
    plt.ylabel('Salary (US$)')
    plt.xlabel('Country')
    plt.xticks(rotation=90)
    st.pyplot(fig1)

    st.write("""#### Mean Salary Per Country ####""")
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Mean Salary Based on Experience ####""")
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)







