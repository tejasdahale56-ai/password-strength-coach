import streamlit as st
from password_analyzer import analyze_password_length

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
        result = analyze_password_length(password)

        st.subheader(f"Length score: {result['score']} / 100")

        if result["score"] < 40:
            st.error(result["message"])
        elif result["score"] < 65:
            st.warning(result["message"])
        else:
            st.success(result["message"])

        st.info(f"Suggestion: {result['suggestion']}")

        st.subheader("Character variety")

        for check in result["character_checks"]:
            st.write(check)
    else:
        st.warning("Please enter a test password first.")

st.caption("Privacy note: This local educational version does not save passwords.")