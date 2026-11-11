import streamlit as st

# كود الألوان والخلفية وخانات الإدخال 
st.markdown("""
    <style>
    .stApp {
        background-color: #F6C2DC;
    }
    
    .stTextStyle, p, label {
        color: #000000 !important;
    }
    
    .stTextInput input, .stNumberInput input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border-radius: 8px;
        border: 1px solid #000000 !important;
    }
    
    
    .stAlert {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)


st.title("***Calculate***")


st.markdown("""<div style='color: #70235E; font-weight: bold;'>
Choose an option:<br> </div>
<div style='color: #FFFFFF; font-weight: bold;'>
a) Calculate the area of a square<br>
b) Calculate the area of a triangle<br>
c) Calculate the area of a rectangle<br>
d) Calculate<br>
e) Calculate Grades :<br>
</div>""", unsafe_allow_html=True)

enter = st.text_input("Enter your choice (a, b, c , d , e): ").lower().strip()

if enter == "b":
    
    a = st.number_input("Enter base length :", min_value=0.0, step=1.0)
    b = st.number_input("Enter the height:", min_value=0.0, step=1.0) 
    
    if st.button("Calculate the area"):
        Triangle = 0.5 * a * b
        st.success(f"Area of ​​a triangle = {Triangle}")

elif enter == "a":
    a = st.number_input("Enter the side length:", min_value=0.0, step=1.0)
    
    if st.button("Calculate the area"):
        Square = a * a
        st.success(f"Area of ​​a square = {Square}")

elif enter == "c":
    a = st.number_input("Enter the length:", min_value=0.0, step=1.0)
    b = st.number_input("Enter the offer:", min_value=0.0, step=1.0)
    
    if st.button("Calculate the area"):
        Rectangle = a * b
        st.success(f"Area of ​​a rectangle = {Rectangle}")

elif enter == "d":
    enter_1 = st.number_input("Enter number 1:", step=1.0)
    enter_2 = st.number_input("Enter number 2:", step=1.0)
    enter_type = st.text_input('Enter type (+ , - , / , *):')

    if st.button("Calculate"):
        if enter_type == '+':
            st.success(f"Result = {enter_1 + enter_2}")
        elif enter_type == '-':
            st.success(f"Result = {enter_1 - enter_2}")
        elif enter_type == '*':
            st.success(f"Result = {enter_1 * enter_2}")
        elif enter_type == '/':
            if enter_2 != 0:
                st.success(f"Result = {enter_1 / enter_2}")
            else:
                st.error("لا يمكن القسمة على صفر!")
        else:
            st.warning('Please enter a valid type: + , - , / , *')

elif enter == 'e':
    
    enter_Grade = st.number_input('Enter your grade (0-100):', min_value=0, max_value=100, step=1) 

    if st.button("Check Grade"):
        if enter_Grade >= 90:
            st.success('You have A')
        elif enter_Grade >= 80:
            st.success('You have B')
        elif enter_Grade >= 70:
            st.success('You have C')
        elif enter_Grade >= 60:
            st.success('You have D')
        else:
            st.error('You have F / E')

elif enter == "":
    st.info("Waiting for your selection...")
else:
    st.warning('Please Enter a valid choice (a, b, c , d , e)')
