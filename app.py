import streamlit as st

st.header("This app is private.")


if not st.user.is_logged_in:
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)
else:
    st.subheader(f"Welcome, {st.user.name}!")
    st.button("Log out", on_click=st.logout)
