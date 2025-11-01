import streamlit as st


st.title("BMI Calculator")

weight=st.slider("Select your weight (kg)",0,150,45,step=1)

height=st.slider("Select your height (cm)",85,250,170,step=1)

height_meter=height/100

bmi = weight / (height_meter ** 2)

st.header("Your BMI is "+str(bmi))
if bmi<16:
    st.error("Extremely Underweight")
    st.text("avoid skipping meals")
    
elif bmi>= 16 and bmi < 18.5:
    st.warning("Underweight")
    st.text("Try to eat balanced meals with more proteins")
    
elif bmi>=18.5 and bmi <25:
    st.success("Healthy")
    st.text("You are doing great")
    
elif bmi >=25 and bmi<30:
    st.info("Overweight")
    st.text("Start doing exerise and eat healthy food")
    
elif bmi >=30:
    st.info("Extremely Overweight")
    st.text("Eat healthy food")
    
    






