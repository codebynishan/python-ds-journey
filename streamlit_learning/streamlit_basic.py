import streamlit as st

st.title("hi i am learning streamlit")

st.header("a begin of learning new things")

st.subheader("This is a about learning about streamlit")

st.text("Hey, I am learnign new things day by day")

st.markdown("#This is markkdown header")

st.markdown("This is the **bold** mark down")

st.success("you are succcessfully login")

st.warning("you are about to exceed your limit.")

st.error("oops ! something went wrong ")

st.info("Did you know ?")

is_checked = st.checkbox("I agree to terms and conditions")
if is_checked:
    st.write("Thankyou for agreee terms and condition")
else:
    st.write("You must check terms and condition")
    
gender =st.radio("Select your gender",("Male","Female","Others"))

st.write(f"you select {gender}")

st.selectbox("Select your favourate programming language",("Python","C","Java"))

selected_hub =st.multiselect("Select your hubby",("Reading","Gaming","Cooking","Traveling"))
st.write(f"you selected:{selected_hub}")

def predit_dibetes():
    # all the logic and models will return here
    st.write("you have dibetes! go and have some exerise")
btn =st.button("Predit")
if btn:
    predit_dibetes()
    
st.text_input("Enter your name",placeholder="Type here....")
st.number_input("Enter your age",min_value=0,max_value=100)
st.text_area("Input your story")

st.sidebar.title("This is a sidebar")
st.sidebar.button("click me")

st.slider("Select value",0,100,25, step = 2)

from PIL import Image

img = Image.open("/Users/nishanrana/Downloads/imge.jpg")
st.image(img,width=300)