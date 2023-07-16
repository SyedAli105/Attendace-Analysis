import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Attendance Analysis")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
df = pd.read_csv(uploaded_file)
df.set_index(df["Student_Name"])
if uploaded_file:
    st.title("Overview of Data:")
    st.write("### Total Number of Students: ",df['Student_Name'].nunique())
    fig, ax = plt.subplots()
    ax.plot(df['Attendace_Percentage'], 'ro', markersize=5,linestyle='-')
    plt.xlabel("STUDENTS")
    plt.ylabel("ATTENDANCE(%)")
    plt.title("Overall Attendace Analysis")
    ax.set_xticks(range(len(df["Student_Name"])))
    ax.set_xticklabels(df["Student_Name"])
    st.pyplot(fig)
    selected_option = st.selectbox("Select student name to show analysis accordingly:",df['Student_Name'].unique())
    st.write("#### Student Name:", selected_option)
    if selected_option:
        st.dataframe(df[df['Student_Name'] == selected_option])