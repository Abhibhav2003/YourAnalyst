import streamlit as st
from streamlit_lottie import st_lottie


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
  with st.container(key = "LoginForm"):
    st.title("LogIn")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type = "password")
    if st.button("Log in"):
        if username == 'user' and password == '1234':
           st.session_state.logged_in = True
           st.rerun()
        elif password == '' and username == '':
           st.warning("Please Enter Username and Password!")
        elif username == '':
           st.warning("Please Enter Username!")
        elif password == '':
           st.warning("Please Enter Password!")
        else:
           st.error("Invalid Username or Password!")

login_page = st.Page(login,title="Log in")


Home = st.Page(
    "Pages/Home.py", title="Home", default=True
)
Upload = st.Page(
    "Pages/1_Upload.py", title="Upload"
)
Analyse = st.Page(
    "Pages/2_Analyse.py", title="Analyse"
)
Visualize = st.Page(
    "Pages/3_Visualize.py", title="Visualize"
)
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Pages": [Home, Upload, Analyse, Visualize]
        }
    )
else:
    pg = st.navigation([login_page])

st.write("Username  : user")
st.write("Password  : 1234")

pg.run()