import streamlit as st
from src.data_loader import load_students, load_events, get_student
from src.recommender import recommend

students_df = load_students()
events_df = load_events()

student_id = st.selectbox("Select Student", students_df["student_id"].tolist())
top_k = st.slider("Recommendations", 1, 10, 5)

if st.button("Recommend"):
    student = get_student(student_id)
    recs = recommend(student, events_df, top_k=top_k)

    st.write("Student:", student)

    if recs.empty:
        st.warning("No matching events found.")
    else:
        for _, r in recs.iterrows():
            st.subheader(f"{r['title']}  (score: {r['score']:.2f})")
            st.write(f"Club: {r['club']}")
            st.write(f"Tags: {r['tags']}")
            st.write(f"Level: {r['level']} | Day: {r['day']} | Mode: {r['mode']}")

            st.divider()
