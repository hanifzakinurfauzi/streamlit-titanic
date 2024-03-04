import streamlit as st
import pandas as pd
import joblib

def preprocess_data(pclass, sex, age, age_group, sibsp, parch, tanggungan, fare, embarked):
    data = {
        'Pclass': [pclass],
        'Sex': [sex.lower()],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Embarked': [embarked[0]],
        'Age_group': [age_group.lower()],
        'Jumlah_tanggungan': [tanggungan] 
    }

    df = pd.DataFrame(data)

    # Load encoders and transformers
    encoding_sex = joblib.load('./encoded/encoder_sex.joblib')
    encoding_embarked = joblib.load('./encoded/encoder_embarked.joblib')
    encoding_agegroup = joblib.load('./encoded/encoder_agegroup.joblib')
    standar_age = joblib.load('./standarization/standarisasi_age.joblib')
    standar_fare = joblib.load('./standarization/standarisasi_fare.joblib')

    # Apply transformations
    df['Sex'] = encoding_sex.transform(df['Sex'])
    df['Embarked'] = encoding_embarked.transform(df['Embarked'])
    df['Age_group'] = encoding_agegroup.transform(df['Age_group'])
    df['Age'] = standar_age.transform(df[['Age']])
    df['Fare'] = standar_fare.transform(df[['Fare']])

    return df

def predict(df, model_name='svc'):

    # Load the model and make predictions
    model = joblib.load(f'./model/{model_name}.joblib')
    predictions = model.predict(df)

    return predictions


st.title('Titanic Survival Prediction')
st.subheader('Test Your Survive Rate')

with st.form("my_form"):
    pclass = st.selectbox('Ticket class',('1', '2', '3'), index= None, placeholder=('Select Ticket Class'))
    sex = st.selectbox('Jenis kelamin',('Male', 'Female'), index= None, placeholder=('Select Sex'))
    age = st.number_input('Umur',min_value=0, max_value=100)
    age_group = st.selectbox('Jenis kelompok umur',('Balita','Anak-anak','Remaja','Anak muda','Dewasa','Lansia'), index= None, placeholder=('Select Age Group'))
    sibsp = st.number_input('Input number of siblings/spouse',min_value=0, max_value=10)
    parch = st.number_input('Input number of parents/children',min_value=0, max_value=10)
    tanggungan = st.number_input('Input jumlah tanggungan',min_value=0, max_value=10)
    fare = st.number_input('Ticket fare')
    embarked = st.selectbox('Embarked',('Cherbourg','Queenstown','Southampton'), index= None, placeholder=('Select Port of Embarkation'))


    submitted = st.form_submit_button("Submit")
    if submitted:
        df = preprocess_data(pclass,sex,age,age_group,sibsp,parch,tanggungan,fare,embarked)
        result = predict(df)

        survive = 'Yes' if result[0] == 1 else 'No'

        st.write(f'Is Survive: {survive}')