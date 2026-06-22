
import streamlit as st

# Page config
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

# Title
st.title("⚖️ BMI Calculator")
st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

# Inputs
height = st.number_input(
    "Height (in centimeters)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

weight = st.number_input(
    "Weight (in kilograms)",
    min_value=10.0,
    max_value=300.0,
    value=70.0
)

# Calculate BMI
if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI: {bmi:.2f}")

    # BMI Category
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif bmi < 25:
        category = "Normal weight"
        color = "green"
    elif bmi < 30:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"

    st.markdown(
        f"<h3 style='color:{color};'>Category: {category}</h3>",
        unsafe_allow_html=True
    )

    st.progress(min(int(bmi * 2), 100))

# Footer
st.caption("Made with Streamlit 🚀")
