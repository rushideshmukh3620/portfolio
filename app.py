import streamlit as st
from PIL import Image
import random

# Function to generate random background colors
def random_color():
    return f"#{random.randint(100000, 0xFFFFFF):06x}"

# Set page title and icon
st.set_page_config(page_title="Rushikesh Deshmukh - Portfolio", page_icon="📂", layout="wide")

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
    st.image(passport_photo, caption="Rushikesh Deshmukh", width=300)  

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
                "<li><strong>M.Sc. (Computer Science)</strong> - MIT Arts, Commerce and Science College, Alandi (79.95%) (2022-2024)</li>"
                "<li><strong>B.Sc. (Computer Science)</strong> - G.H. Raisoni College of Arts, Commerce and Science, Wagholi (78.10%) (2018-2021)</li>"
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
                "<p>Predicts SGPA for the fifth semester based on previous four semester scores.</p>"
                "<p><a href='https://github.com/rushideshmukh3620/SGPAPrediction.git' style='color:white;'>GitHub</a></p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- CERTIFICATIONS (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h3>📜 Certifications</h3>"
                "<ul>"
                "<li>Data Science Job Simulation (British Airways, Apr 2024)</li>"
                "<li>Full Stack Data Science & AI (Naresh IT, Oct 2021 - Mar 2022)</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center;'>© 2024 Rushikesh Deshmukh</p>", unsafe_allow_html=True)
