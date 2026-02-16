import streamlit as st
from streamlit_lottie import st_lottie
import json
import time
import os

st.set_page_config(page_title="Liganga Poultry Farm", page_icon="🐔", layout="wide")

with st.spinner("Loading Liganga Poultry Farm..."):
    time.sleep(1.5)

# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
* { font-family: 'Roboto', sans-serif; }
.main { background-color: #f8f9fa; }
h1 { color: #2d5016; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); }
h2 { color: #4a7c2c; border-bottom: 4px solid #8bc34a; padding-bottom: 10px; margin-top: 30px; }
h3 { color: #5d8f3a; font-weight: 600; }
a { color: #4a7c2c !important; text-decoration: none; font-weight: 500; transition: color 0.3s ease; }
a:hover { color: #8bc34a !important; }
hr { border: none; height: 2px; background: linear-gradient(to right, transparent, #8bc34a, transparent); margin: 40px 0; }
img { border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.3s ease; }
img:hover { transform: scale(1.03); }
video { border-radius: 12px; box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
.stButton > button { background-color: #4a7c2c; color: white; border-radius: 8px; padding: 12px 28px; font-size: 16px; font-weight: 600; border: none; transition: all 0.3s ease; }
.stButton > button:hover { background-color: #8bc34a; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(0,0,0,0.2); }
input, textarea { border-radius: 8px !important; border: 2px solid #e0e0e0 !important; padding: 10px !important; }
input:focus, textarea:focus { border-color: #8bc34a !important; box-shadow: 0 0 0 2px rgba(139, 195, 74, 0.2) !important; }
</style>
""", unsafe_allow_html=True)

# Local CSS safe load
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.info(f"Optional CSS: {file_name} not found.")

local_css("style/style.css")

# Lottie safe load
def load_lottie_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    st.warning(f"Lottie file missing: {filepath}")
    return None

lottie_sidebar = load_lottie_file("Chiki.json")
lottie_main = load_lottie_file("animation1.json")

# Sidebar: Nav only
with st.sidebar:
    if lottie_sidebar:
        st_lottie(lottie_sidebar, speed=0.9, reverse=False, loop=True, quality="high", height=180, key="sidebar_animation")
    st.subheader("Hi, I'm Liganga 👋")
    st.markdown("**ligangaj@outlook.com**")
    st.markdown("+265 999 57 18 97")
    st.markdown("---")
    st.markdown("[Facebook](https://www.facebook.com/profile.php?id=100069530)")
    st.markdown("[Learn More](https://pythonandvba.com)")

# Main content
#if lottie_main:
    #st_lottie(lottie_main, speed=1.0, reverse=False, loop=True, quality="high", height=340, key="main_animation")

st.title("A Poultry Farmer From MALAWI")
st.write("Passionate about chickens - raising chicks to adulthood with ZERO mortality (Koekoek, Kuroiler, Light Sussex).")

# What I Do - Main area
st.header("What We Do")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
                

    - Sell fertilized & unfertilized eggs
    - Day-old chicks
    - 4-6 week chicks
    - Brooding boxes (manual/automatic)
    - Layer feed
    - Grown roosters & hens

    """)
with col2:
    if lottie_main:
        st_lottie(lottie_main, speed=1.0, reverse=False, loop=True, quality="high", height=200, key="main_animation")
        st.empty()  # Placeholder for future image/anim

# Gallery
st.header("My Projects")
progress_text = "Loading gallery..."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
st.success("Gallery ready!")

img_col, vid_col = st.columns(2)
with img_col:
    st.subheader("Our Farm Gallery")
    if os.path.exists("image1.jpg"):
        st.image("image1.jpg", caption="Our chickens at the farm", use_container_width=True)
    if os.path.exists("image3.jpg"):
        st.image("image3.jpg", use_container_width=True)
with vid_col:
    st.subheader("Playing & Feeding Time")
    if os.path.exists("chicken_farm1.mp4"):
        st.video("chicken_farm1.mp4")
    if os.path.exists("chicken_farm2.mp4"):
        st.video("chicken_farm2.mp4")

# Contact
st.header("Get In Touch")
left_col, right_col = st.columns(2)
with left_col:
    contact_form = """
    <form action="https://formsubmit.co/ligangaj@outlook.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="width:100%; margin-bottom:10px;">
        <input type="email" name="email" placeholder="Your email" required style="width:100%; margin-bottom:10px;">
        <textarea name="message" placeholder="Your message here" required style="width:100%; height:120px;"></textarea>
        <button type="submit" style="width:100%; margin-top:10px;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
with right_col:
    st.empty()

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 30px 0 20px 0;'>
    <h3 style='color: #4a7c2c; margin-bottom: 20px;'>Connect With Us</h3>
    <p style='font-size: 18px; margin: 10px 0;'>
        📧 ligangaj@outlook.com | 📱 +265 999571897
    </p>
    <p style='margin: 20px 0;'>
        <a href='https://facebook.com' target='_blank' style='margin: 0 10px; text-decoration: none; font-size: 24px;'>📘</a>
        <a href='https://x.com/Zgolooo' target='_blank' style='margin: 0 10px; text-decoration: none; font-size: 24px;'>🐦</a>
        <a href='https://instagram.com' target='_blank' style='margin: 0 10px; text-decoration: none; font-size: 24px;'>📷</a>
    </p>
    <hr style='width: 50%; margin: 20px auto; border: 1px solid #8bc34a;'>
    <p style='color: #666; font-size: 14px;'>© 2026 Liganga Poultry Farm | All Rights Reserved</p>
    <p style='color: #888; font-size: 12px; margin-top: 10px;'>Made with ❤️ in Malawi</p>
</div>
""", unsafe_allow_html=True)
