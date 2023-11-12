import streamlit as st

# Set the title of the app
st.title("My Streamlit App")

# Write some text to the app
st.write("This is a simple Streamlit app.")

# Create a button
button = st.button("Click me!")

# If the button is clicked, display a message
if button:
    st.write("Button clicked!")

# Display the app
st.show()
