from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Custom CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style/style.css")

# --- Load Asset ---
lottie_asset = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_0yfsb3a1.json")
img_1 = Image.open("imgs/img_1.jpg")
img_2 = Image.open("imgs/img_2.jpg")

# ---Header Section---
with st.container():
    st.subheader("Hii, I am Satyam Shinde :wave:")
    st.title("First Year Student from Sinhagad Academy of Engineering, Kondhwa")
    st.write("Actually, I am interested in to develope the new user friendliu software and I am also interested in to find the ways to make the social media app for user-friendly :smile:")
    st.write("[Learn More >](https://www.google.co.in/)")


    # ---What I Do---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do ")
        st.write("##")
        st.write(
        """In computer science, a high-level programming language is a programming language with strongabstraction from the details of the computer. In contrast to low-level programming languages, it mayuse natural language elements, be easier to use, or may automate (or even hide entirely) significantareas of computing systems (e.g. memory management), making the process of developing a programsimpler and more understandable than when using a lower-level language. The amount of abstractionprovided defines how "high-level" a programming language is.
        """
        )
    st.write("[YouTube Link >](https://youtu.be/DAYszemgPxc)")

    with right_column:
        st_lottie(lottie_asset, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.subheader("This is a Sample Project File")
        st.write(
            """
            Actually this is a trial project that we conducted to see how we can cerate a website using python programming language.
            """
        )
        st.markdown("[More.... >](https://www.youtube.com/)")


with st.container():
    # st.write("---")
    # st.header("My Projects")
    # st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader("This is a Sample Project File")
        st.write(
            """
            Actually this is a trial project that we conducted to see how we can cerate a website using python programming language.
            """
        )
        st.markdown("[More.... >](https://www.youtube.com/)")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/devshinde9359@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """

    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()