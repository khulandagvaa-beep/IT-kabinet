import streamlit as st
import pandas as pd

st.title("💻 Лабораторийн Суудал ба Хуваарийн Бүртгэл")

# Өгөгдлийн сан эсвэл санах ойн хүснэгт үүсгэх
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Сурагчийн нэр", "Анги", "Компьютерийн дугаар", "Хичээлийн цаг"])

# 1. Шинэ мэдээлэл бүртгэх хэсэг (Sidebar)
st.sidebar.header("Сурагч бүртгэх")
name = st.sidebar.text_input("Сурагчийн нэр")
class_name = st.sidebar.text_input("Анги")
pc_number = st.sidebar.selectbox("Компьютерийн дугаар", ["PC-01", "PC-02", "PC-03", "PC-04", "PC-05"])
hour = st.sidebar.selectbox("Хичээлийн цаг", ["1-р цаг", "2-р цаг", "3-р цаг", "4-р цаг"])

if st.sidebar.button("Бүртгэх"):
    new_row = {"Сурагчийн нэр": name, "Анги": class_name, "Компьютерийн дугаар": pc_number, "Хичээлийн цаг": hour}
    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
    st.sidebar.success("Амжилттай бүртгэгдлээ!")

# 2. Хайлт хийх болон шүүх хэсэг (Filtering)
st.header("🔍 Суудал болон Хуваарь Шүүх")
search_pc = st.selectbox("Компьютерээр хайх:", ["Бүгд"] + list(st.session_state.data["Компьютерийн дугаар"].unique() if not st.session_state.data.empty else []))

df = st.session_state.data

if search_pc != "Бүгд":
    df = df[df["Компьютерийн дугаар"] == search_pc]

st.dataframe(df, use_container_width=True)