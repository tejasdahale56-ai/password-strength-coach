import streamlit as st

st.set_page_config(page_title="Password Strength Coach")

st.title("Password Strength Coach")
st.write("A local educational tool for learning what makes a password stronger.")

password = st.text_input(
    "Enter a test password",
    type="password",
    help="Use a fake password while we build the project."
)

if st.button("Analyze password"):
    if password:
        st.success("Your password was received locally. Analysis comes next.")
    else:
        st.warning("Please enter a test password first.")

st.caption("Privacy note: This beginner version does not save passwords.")