import streamlit as st
import pandas as pd

# Хуудасны ерөнхий тохиргоо
st.set_page_config(page_title="Хөгжил Компьютер Лаборатори", page_icon="💻", layout="wide")

# Гарчиг болон тайлбар
st.title("🏫 Хөгжил Цогцолбор Сургууль - Мэдээлэл Зүйн Кабинет")
st.markdown("Энэхүү систем нь лабораторийн компьютерийн суурьшилт, цагийн хуваарь болон кабинетын ашиглалтыг хянах зорилготой.")

# Санах ойд өгөгдөл үүсгэх (Анхны утгууд)
if 'lab_data' not in st.session_state:
    st.session_state.lab_data = pd.DataFrame([
        {"Компьютер": "PC-01", "Сурагчийн нэр": "Билгүүн", "Анги": "11а", "Хичээлийн цаг": "1-р цаг", "Төлөв": "Хэвийн"},
        {"Компьютер": "PC-02", "Сурагчийн нэр": "Хулан", "Анги": "11а", "Хичээлийн цаг": "1-р цаг", "Төлөв": "Хэвийн"},
        {"Компьютер": "PC-03", "Сурагчийн нэр": "Тэмүүлэн", "Анги": "11б", "Хичээлийн цаг": "2-р цаг", "Төлөв": "Хулгана (Mouse) асуудалтай"},
    ])

# Хажуугийн цэс: Бүртгэл хийх
st.sidebar.header("🛠️ Суудал ба Хуваарь Бүртгэх")
with st.sidebar.form("registration_form"):
    pc_no = st.selectbox("Компьютерийн дугаар", [f"PC-{i:02d}" for i in range(1, 21)])
    student_name = st.text_input("Сурагчийн овог, нэр")
    student_class = st.text_input("Анги (Жишээ нь: 12а)")
    class_hour = st.selectbox("Хичээлийн цаг", ["1-р цаг", "2-р цаг", "3-р цаг", "4-р цаг", "5-р цаг"])
    status = st.selectbox("Техникийн төлөв", ["Хэвийн", "Интернэт тасарсан", "Тоног төхөөрөмж эвдрэлтэй"])
    
    submitted = st.form_submit_button("Бүртгэлд нэмэх")
    if submitted:
        if student_name and student_class:
            new_entry = {
                "Компьютер": pc_no, 
                "Сурагчийн нэр": student_name, 
                "Анги": student_class, 
                "Хичээлийн цаг": class_hour, 
                "Төлөв": status
            }
            st.session_state.lab_data = pd.concat([st.session_state.lab_data, pd.DataFrame([new_entry])], ignore_index=True)
            st.success(f"{pc_no} амжилттай бүртгэгдлээ!")
        else:
            st.warning("Сурагчийн нэр болон ангийг заавал бөглөнө үү.")

# Үндсэн хэсэг: Шүүлт хийх болон хүснэгт харах
st.subheader("📊 Кабинетын суудал ба хуваарийн жагсаалт")

col1, col2 = st.columns(2)
with col1:
    selected_hour = st.selectbox("Хичээлийн цагаар шүүх:", ["Бүгд"] + list(st.session_state.lab_data["Хичээлийн цаг"].unique()))
with col2:
    search_query = st.text_input("Сурагч эсвэл PC хайх:", "")

# Шүүлтүүр ажиллуулах
filtered_df = st.session_state.lab_data
if selected_hour != "Бүгд":
    filtered_df = filtered_df[filtered_df["Хичээлийн цаг"] == selected_hour]

if search_query:
    filtered_df = filtered_df[
        filtered_df['Сурагчийн нэр'].str.contains(search_query, case=False, na=False) | 
        filtered_df['Компьютер'].str.contains(search_query, case=False, na=False)
    ]

# Хүснэгтийг харуулах
st.dataframe(filtered_df, use_container_width=True)

# Доод хэсэгт кабинетын мэдээлэл
st.markdown("---")
st.caption("© 2026 Нийслэлийн ерөнхий боловсролын Хөгжил цогцолбор сургууль | Дадлагын ажлын систем")