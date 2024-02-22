import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="About ME", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---USE LOCAL CSS----
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

#--- LOAD ASSETS ---#
lottie_coding = "https://lottie.host/66fa1d03-98d7-4f7c-b878-53dfdf46b210/iTxJbKxCOX.json"
img_contact_form = Image.open("images/NVIDIA.png")
img_contact_animation = Image.open("images/DS.png")
#---HEADER SECTION ---#
with st.container():
    st.subheader("Hi, I am Jihen :wave:")
    st.title("A Data Science Student From Tunisia")
    st.write("I am passionate about creating different apps with Python ")


#--- WHAT I DO ---#
with st.container():
    st.write()
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do ")
        st.write("##")
        st.write(
            """So currently immersed in an exciting internship focused on brain tumor detection using deep learning and transfer learning.
            What makes this journey even more thrilling is my passion for using Python not only in data science but also in creating web and mobile apps related to my internship.
            Python's versatility allows me to seamlessly transition from analyzing medical data to developing user-friendly applications that can potentially impact healthcare. 
            This dual fascination with both the analytical and application aspects of Python keeps my internship journey dynamic and filled with possibilities."""

        )
        st.write("[My Linkedin Profile >](https://linkedin.com/in/jihen-skima)")
        st.write("[My GitHub Account >](https://github.com/JihenSkima)")


    with right_column:
        st_lottie(lottie_coding, height=450, key="coding")

with st.container():
    st.write("")
    st.header("Workshops")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Sharing insights from recent workshops")

        st.write(
            """
            Learn how to use Lottie Files in Streamlit ! 
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way  
            In this tutorial , you can find exactly how to do it 
            """)
        st.markdown("[Check This Video ... ](https://youtu.be/TXSOitGoINE)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_animation)
    with text_column:
        st.subheader("other workshops")

#---CONTACT
with st.container():
    st.write("----")
    st.write("Get In Touch With Me")
    st.write("##")
    contact_form = """
    <form action = "https://formsubmit.co/jihen.skima2@gmail.com" method = "POST">
        <input type="hidden" name="_captcha" value="false">
        <input type = "text" name = "name" placeholder = "Your name " required><br>
        <input type = "email" name = "email" placeholder="Your email" required><br>
        <textarea name="message" placeholder="Your message here " required ></textarea><br>
        <button type = "submit"> Send </button>
    </form>"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()