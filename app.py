
import streamlit as st

st.set_page_config(
    page_title="Mental Fatigue Detection",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Mental Fatigue Detection System")
st.write("Analyze your daily routine and estimate your fatigue level.")

st.subheader("Enter Your Details")

name = st.text_input("Your Name")

sleep = st.slider("Hours of Sleep", 0, 24, 7)
study = st.slider("Hours Spent Studying", 0, 24, 4)
stress = st.slider("Stress Level", 1, 10, 5)
focus = st.slider("Concentration Level", 1, 10, 7)

if st.button("Analyze Fatigue"):

    score = 0

    if sleep < 6:
        score += 2

    if study > 6:
        score += 2

    if stress >= 7:
        score += 2

    if focus <= 4:
        score += 2

    st.subheader("Your Fatigue Report")

    st.write("Name:", name)
    st.metric("Fatigue Score", f"{score}/8")

    if score <= 2:
        st.success("LOW FATIGUE")
        st.write("Recommendation: Maintain your routine.")

    elif score <= 5:
        st.warning("MODERATE FATIGUE")
        st.write("Recommendation: Take regular breaks.")

    else:
        st.error("HIGH FATIGUE")
        st.write("Recommendation: Take sufficient rest.")

    st.caption("Educational prototype only. Not a medical diagnostic tool.")

