import streamlit as st

st.title("***Calculate***")


st.write("""Choose an option:

a) Calculate the area of a square

b) Calculate the area of a triangle

c) Calculate the area of a rectangle

d) Calculate

e) Calculate Grades : """)

enter = st.text_input("Enter your choice (a, b, c , d , e): ").lower().strip()

if enter == "b":
    
    a = st.number_input("ادخل طول القاعدة:", min_value=0.0, step=1.0)
    b = st.number_input("ادخل الارتفاع:", min_value=0.0, step=1.0) 
    
    if st.button("احسب المساحة"):
        Triangle = 0.5 * a * b
        st.success(f"مساحة المثلث = {Triangle}")

elif enter == "a":
    a = st.number_input("ادخل طول الضلع:", min_value=0.0, step=1.0)
    
    if st.button("احسب المساحة"):
        Square = a * a
        st.success(f"مساحة المربع = {Square}")

elif enter == "c":
    a = st.number_input("ادخل الطول:", min_value=0.0, step=1.0)
    b = st.number_input("ادخل العرض:", min_value=0.0, step=1.0)
    
    if st.button("احسب المساحة"):
        Rectangle = a * b
        st.success(f"مساحة المستطيل = {Rectangle}")

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
    st.info("بانتظار اختيارك...")
else:
    st.warning('Please Enter a valid choice (a, b, c , d , e)')
