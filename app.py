import streamlit as st
import streamlit_authenticator as st_auth
import pickle

# Page Configuration
st.set_page_config(page_title='Tech Query Recommendation', layout = "centered")
st.title("Tech Query Recommendation")

# Models
data = pickle.load(open("model/data.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

# Recommendation Engine
def recommend(query):
    index = data[data['ques_title'] == query].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommend_ques = []
    for i in distances[1:12]:
        print(data.iloc[i[0]].ques_title)
        recommend_ques.append(data.iloc[i[0]].ques_title)
    return recommend_ques

# Credentials DB
names = ['Raghav Agarwal', 'Rohan Saksena', 'Keshav Garg', 'Preethi J']
usernames = ['ragharwal', 'rohan', 'keshav', 'preethi']
passwords = ['admin', 'rohan', 'keshav', 'preethi']

hashed_passwords = st_auth.Hasher(passwords).generate()
authenticator = st_auth.Authenticate(names, usernames, hashed_passwords, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login', 'main')

# Authentication
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.success("Login Successful")
    st.write('Welcome *%s*' % (st.session_state['name']))
    ques_list = data['ques_title'].values
    selected_ques = st.selectbox("Select a question", ques_list)
    if st.button("Recommend"):
        recommend_ques = recommend(selected_ques)
        st.success("Recommended Questions")
        st.write(recommend_ques)

elif authentication_status == False:
    st.error('Username or Password is incorrect')

elif authentication_status == None:
    st.info('Please login to continue')
