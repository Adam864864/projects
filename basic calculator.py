import streamlit as st

def basic_calculator() :
    st.title('basic calculator')

    col1 , col2 = st.columns(2)
    with col1 :
        num1 = st.number_input('first number' , key = 'basic_num1')
    with col2 :
        num2 = st.number_input('second number' , key = 'basic_num2')
    operation = st.selectbox('select operation' ,
        ['+' , '-' , '*' , '/']
    )

    if st.button('calculate') :
        if operation =='+' :
            result = num1 + num2
        elif operation =='-' :
            result = num1 - num2
        elif operation =='*' :
            result = num1 * num2
        elif operation =='/' :
            result = num1 / num2 if num2!= 0 else 'error'
        st.success(f'Result: {result}')
basic_calculator()


