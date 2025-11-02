import streamlit as st
from nepali_date_utils import converter




st.title("Date Converter")


st.sidebar.header("Select Conversion Type")
conversion_type = st.sidebar.radio("Choose conversion type:", ("BS to AD", "AD to BS"))

date = name = st.sidebar.text_input("Enter Date", "2000/01/01")

btn = st.sidebar.button('Submit')

if btn:
    if conversion_type == "BS to AD":
        try:
           
            converted_date = converter.bs_to_ad(date)
            st.subheader("Your Converted Date is")
            st.success(f"📅  **BS  {date}  =  AD   {converted_date}**")
        except Exception as e:
            st.error("Invalid BS date! Please check the inputs.")

    elif conversion_type == "AD to BS":
        try:
            
            converted_date = converter.ad_to_bs(date)
            st.success(f"📅 **AD {date} = BS {converted_date}**")
        except Exception as e:
            st.error("Invalid AD date! Please check the inputs.")