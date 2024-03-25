import streamlit as st
import requests

def fetch_love_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q'] + " -" + data[0]['a']
            return quote
        else:
            st.error(f"Failed to fetch quote. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Motivation Quote ")
    st.write("Click below to get Motivational quote.")

    if st.button("Generate Quote"):
        love_quote = fetch_love_quote()
        if love_quote:
            st.success("Here's a love quote for you:")
            st.write(love_quote)
        else:
            st.error("Failed to fetch a love quote.")

if __name__ == "__main__":
    main()
