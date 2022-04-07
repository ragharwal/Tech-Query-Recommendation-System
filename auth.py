import pyrebase
import streamlit as st
from datetime import time
import yfinance as yf
from PIL  import Image
from urllib.request import urlopen
from datetime import date
today = date.today()

firebaseConfig = {
  "apiKey": "AIzaSyAVnhn5o_RWi3DvOA9heA3Lp3_iCNoXd88",
  "authDomain": "tech-query-recommendation.firebaseapp.com",
  "projectId": "tech-query-recommendation",
  "storageBucket": "tech-query-recommendation.appspot.com",
  "messagingSenderId": "974800878699",
  "appId": "1:974800878699:web:f8a0d3d3327ea37113c52e",
  "measurementId": "G-M9CF9PC0VT",
  "databaseURL": "https://tech-query-recommendation-default-rtdb.firebaseio.com/",
};

# Firebase Authentication
firbase = pyrebase.initialize_app(firebaseConfig)
auth = firbase.auth()

# Database
db = firbase.database()
storage = firbase.storage()

st.set_page_config(page_title='Tech Query Recommendation', layout = "centered")
st.title("Tech Query Recommendation")

def signUp():
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.success("User Created")
        st.info("Please login to continue")
    except:
        st.error("Error")

def signIn():
  try:
    user = auth.sign_in_with_email_and_password(email, password)
    st.success("Login Successful")
    # handle = st.sidebar.text_input("handle", value = "@ragharwal")
    # db.child(user["localId"]).child("handle").set(handle)
    # db.child(user["localId"]).child("id").set(user['localId'])
    # st.title("Welcome, " + handle)
    # signOut()
    st.subheader("Welcome to the dashboard")
  except:
    st.error("Error")

def signOut():
    try:
        auth.sign_out()
        st.success("Logout Successful")
        st.info("Please login to continue")
    except:
        st.error("Error")

st.sidebar.title("Tech Query Recommendation")

choice = st.sidebar.selectbox("Select an option", ["Login", "Sign Up"])

email = st.sidebar.text_input("Email Address")
password = st.sidebar.text_input("Password", type="password")

if choice == "Sign Up":
    submit = st.sidebar.button("Sign Up")

    if submit:
        signUp()

if choice == "Login":
    login = st.sidebar.button("Login")

    if login:
      signIn()
    






