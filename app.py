import streamlit as st
from PIL import Image
import random
import base64

# Set page title and icon
st.set_page_config(page_title="Rushikesh Deshmukh - Portfolio", page_icon="📂", layout="wide")

# # Function to set the background image
# def set_background(image_file):
#     with open(image_file, "rb") as image:
#         encoded_image = base64.b64encode(image.read()).decode()
    
#     bg_style = f"""
#     <style>
#     .stApp {{
#         background: url("data:image/jpg;base64,{encoded_image}") no-repeat center center fixed;
#         background-size: cover;
#     }}
#     .box {{
#         padding: 20px;
#         border-radius: 10px;
#         color: white;
#         margin-bottom: 40px;
#         backdrop-filter: blur(5px); /* Makes content boxes more readable */
#     }}
#     .spacer {{
#         height: 20px;
#     }}
#     </style>
#     """
#     st.markdown(bg_style, unsafe_allow_html=True)

# # Set background image
# set_background("Background.jpg")

# Function to generate random background colors
def random_color():
    return f"#{random.randint(100000, 0xFFFFFF):06x}"

# Load passport photo with increased size
passport_photo = Image.open("Small.jpg")

# Custom CSS for styling sections
st.markdown("""
    <style>
    .box {
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 40px;
    }
    .spacer {
        height: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([1, 2])

with col1:  
    st.image(passport_photo, caption="Rushikesh Deshmukh", width=290)  

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h1>Rushikesh Deshmukh</h1>"
                "<h3>Data Scientist</h3>"
                "<p>📧 <a href='mailto:rushideshmukh3620@gmail.com' style='color:white;'>rushideshmukh3620@gmail.com</a></p>"
                "<p>🔗 <a href='https://linkedin.com/in/rushideshmukh3620' style='color:white;'>LinkedIn</a> | "
                "<a href='https://github.com/rushideshmukh3620' style='color:white;'>GitHub</a></p>"
                "</div>", unsafe_allow_html=True)

st.markdown("---")

# Zig-Zag Pattern Layout
# --- ABOUT ME (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h2>👋 About Me</h2>"
                "<p>Aspiring Data Scientist with expertise in Machine Learning, NLP, Flask, and Data Visualization.</p>"
                "<p>Passionate about AI-driven solutions and automation.</p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)  # Spacer

# --- INTERESTS (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h2>🔍 Interests</h2>"
                "<p>Machine Learning, Data Science, Deep Learning, Artificial Intelligence</p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- SKILLS (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h2>💡 Skills</h2>"
                "<p>Machine Learning, Web Scraping, Flask, Selenium, PowerBI, RAG, Langchain, Data Visualization, NLP, "
                "Python, LLM, SQL, NoSQL, Git, GitHub, Streamlit</p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- EDUCATION (Right) ---
col1, col2 = st.columns([1, 2])  

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h2>🎓 Education</h2>"
                "<ul>"
                "<li><strong>M.Sc. (Computer Science)</strong> - 79.95% (2022-2024) MIT Arts, Commerce and Science College </li>"
                "<li><strong>B.Sc. (Computer Science)</strong> - 78.10% (2018-2021) G. H. Raisoni College of Arts, Commerce and Science </li>"
                "<li><strong>HSC </strong> - 74.92% (2018) NES Highschool and Jr. College </li>"
                "<li><strong>SSC </strong> - 79.60% (2016) Sadashivrao Mane Vidyalay </li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- WORK EXPERIENCE (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.subheader("💼 Work Experience")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>Data Science Intern - Futurism Technologies Pvt. Ltd.</h4>"
                "<p><em>Dec 2024 - Present, Pune</em></p>"
                "<ul>"
                "<li>Developed an advanced real-time object detection system using deep learning.</li>"
                "<li>Built an intelligent chatbot leveraging RAG (Retrieval-Augmented Generation).</li>"
                "<li>Created a web scraping solution using Selenium.</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- WORK EXPERIENCE (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>Machine Learning Engineer Intern - The Entrepreneurship Network</h4>"
                "<p><em>Feb 2024 - Jun 2024</em></p>"
                "<ul>"
                "<li>Developed and maintained web applications using Python and Flask.</li>"
                "<li>Created and optimized MongoDB database schemas for efficient data storage.</li>"
                "<li>Collaborated with frontend developers to integrate APIs.</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- PROJECTS (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.subheader("🚀 Projects")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>🏡 SGPA Prediction</h4>"
                "<p>Predicts SGPA for the fifth semester based on previous four semester scores. <a href='https://github.com/rushideshmukh3620/SGPAPrediction.git' style='color:white;'>Link</a></p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- CERTIFICATIONS (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h3>📜 Certifications</h3>"
                "<ul>"
                "<li> Full Stack Data Science & AI (Naresh IT, Oct 2021 - Mar 2022) <a href='https://www.linkedin.com/posts/rushideshmukh3620_machinelearning-datascience-artificialintelligence-activity-7163174936453234690-Y7FQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white;'>Link</a></li>"
                "<li> Data Analytics and Visualization Job Simulation (Accenture, January 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-forage-accenture-activity-7150485871014617088-mYoV?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white;'>Link</a></li>"
                "<li> Data Visualisation: Empowering Business with Effective Insights (TATA, January 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-forage-tcs-activity-7155951764121268224-eDB5?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white;'>Link</a></li>"
                "<li> Data Science Job Simulation (British Airways, Apr 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-certification-continuouslearning-activity-7198595719371378688-MnIW?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white;'>Link</a></li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center;'>© 2024 Rushikesh Deshmukh</p>", unsafe_allow_html=True)
