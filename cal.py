import streamlit as st

st.title('My First Streamlit App')
st.write('Hello, Streamlit!')

# Sidebar
st.sidebar.title('Menu')

# Tabs
tab1, tab2 = st.tabs(['A', 'B'])

with tab1:
    name = st.text_input('Enter your name:')
    if name:
        st.success(f'Welcome, {name}!')

with tab2:
    st.title('Calculate')
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("First number", value=0.0)

    with col2:
        num2 = st.number_input("Second number", value=0.0)

    operation = st.selectbox(
        "Select operation",
        ("+", "-", "×", "÷")
    )

    if st.button("Calculate"):
        if operation == "+":
            result = num1 + num2
            symbol = "+"
        elif operation == "-":
            result = num1 - num2
            symbol = "-"
        elif operation == "×":
            result = num1 * num2
            symbol = "×"
        elif operation == "÷":
            if num2 == 0:
                st.error("❌ Cannot divide by zero")
                result = None
            else:
                result = num1 / num2
                symbol = "÷"

        if result is not None:
            st.success(f"{num1} {symbol} {num2} = {result}")
