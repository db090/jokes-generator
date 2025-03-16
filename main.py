import streamlit as st
import requests

import streamlit as st

# Set the page config at the very top of your script
st.set_page_config(
    page_title="Random Joke Generator",
    page_icon="🤣",
    layout="wide",  # <- This makes the UI wide!
)


def get_random_joke_eng():
    """Fetch a random joke from the API"""
    try:
        response=requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data=response.json()
            return f"{joke_data["setup"]} \n\n {joke_data["punchline"]}"
        else:
            return "failed to fetch you joke .Please try again later"
    except Exception as e:
        return f"{e}"
def get_random_joke_urdu():
    """Fetch a random urdu joke from the API"""
    try:
        response=requests.get("https://fast-joke-api.vercel.app/urdu_jokes")
        if response.status_code == 200:
            _joke_data=response.json()
            return f"{_joke_data["urdu_joke"]}"
        else:
            return "failed to fetch you joke .Please try again later"
    except Exception as e:
        return f"{e}"
    
def main():

    st.title("Random English/Urdu Joke Generator")
    col1,col2=st.columns(2)
    with col1:
        st.write("Click the button given below to generate a joke")

        if st.button("generate a english joke!"):
            joke=get_random_joke_eng()
            st.success(joke)
            st.divider()

    with col2:
        st.write("Click the button given below to generate a joke")

        if st.button("generate a urdu joke!"):
            joke=get_random_joke_urdu()
            st.success(joke)
            st.divider()

    

if __name__ == "__main__":
    main()
        