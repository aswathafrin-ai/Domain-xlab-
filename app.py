import streamlit as st
import pandas as pd

# App title
st.title("Student Details Form")

# Form to enter student details
with st.form("student_form"):
    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")
    age = st.number_input("Age", min_value=1, max_value=100)
    department = st.selectbox(
        "Department",
        ["CSE", "IT", "ECE", "EEE", "MECH", "CIVIL"]
    )
    gender = st.radio("Gender", ["Male", "Female", "Other"])

    submit = st.form_submit_button("Submit")

# Store data
if submit:
    student_data = {
        "Name": name,
        "Roll No": roll_no,
        "Age": age,
        "Department": department,
        "Gender": gender
    }

    df = pd.DataFrame([student_data])

    st.success("Student details submitted successfully!")
    st.subheader("Submitted Student Details")
    st.table(df)



