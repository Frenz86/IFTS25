import streamlit as st

user = 'ciao'
passw = 'password'

if 'user_state' not in st.session_state:
    st.session_state.user_state = {
                                    'username': '',
                                    'password': '',
                                    'logged_in': False
                                    }

def login():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    submit = st.button('Login',type="primary")

    if submit:
        if username == user and password == passw :
            st.session_state.user_state['username'] = username
            st.session_state.user_state['password'] = password
            st.session_state.user_state['logged_in'] = True
            st.success('You are logged in')
            st.rerun()
        else:
            st.error('Invalid username or password')

############################################################################################
## MAIN
############################################################################################

def main_app():

    st.title("History")

############################################################################################

def main():
    if not st.session_state.user_state['logged_in']:
        login()
    else:
        main_app()

if __name__ == "__main__":
    main()


