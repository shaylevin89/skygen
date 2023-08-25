import streamlit as st

def main():
    st.title("Advanced Streamlit Popup Example")

    if st.button("Show Advanced Popup"):
        with st.popup("Advanced Popup", "This is a customized popup."):
            st.write("You can add any content here.")
            st.image("https://via.placeholder.com/150", caption="An image in the popup.")

if __name__ == "__main__":
    main()
