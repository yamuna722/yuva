import streamlit as st
st.title("welcome streamlit")
st.title("program")
st.header("full stack development")
st.subheader("introduction")
st.text("anything")
st.write("Open")
st.badge("close",color="green")
st.code("""

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Cannot divide by zero!" if y == 0 else x / y

operations = {"1": add, "2": subtract, "3": multiply, "4": divide}
choice = input("Choose: 1. Add  2. Subtract  3. Multiply  4. Divide\n")
num1, num2 = float(input("First number: ")), float(input("Second number: "))

print("Result:", operations.get(choice, lambda x, y: "Invalid choice")(num1, num2))

""", language = "python" )

with st.sidebar:
    st.write("this is side bar.")
    st.divider()
    st.write("this is a silebar.")

 
