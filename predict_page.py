from sklearn import model_selection
import streamlit as st
import pickle
import numpy as np
from to_kenyan import convert

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']
le_country_loaded = data['le_country']
le_education_loaded = data['le_education']

def show_predict_page():
    st.title("Software Developer Salary Prediction Using Machine Learning")

    countries = (
        "USA",
        "India",
        "UK",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russia",
        "Sweden",
        "Turkey",
        "Israel",
        "Norway",
        "Switzerland",
    )

    education_levels =(
        'Less than a Bachelors',
        'Bachelor’s degree',
        'Post grad',
        'Master’s degree',
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of experience", 0, 50, 3)
    ok =st.button("Predict Salary")
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country_loaded.transform(X[:, 0])
        X[:, 1] = le_education_loaded.transform(X[:, 1])
        X = X.astype(int)

        predicted_salary = regressor.predict(X)
        st.success("Predicted Salary Per Annum: US$ {:.2f}".format(predicted_salary[0]))
        st.success("Predicted Salary Per Annum: KSh {:.2f}".format(convert(predicted_salary[0])))

    st.write("""###### - Data Source: https://insights.stackoverflow.com/survey/2021 ######""")
    st.write("""###### - Machine Learning Module- Scikit-Learn ######""")
    st.write("""###### - Preprocessing - LabelEncoding  ######""")
    st.write("""###### - Predictive Analysis Method - Regression  ######""")
    st.write("""###### - Algorithms - LinearRegression, DecisionTreeRegressor, RandomForestRegressor, GridSearchCV ######""")
    st.write("""###### - App and Presentation - Streamlit ######""")