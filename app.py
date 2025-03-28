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
    # Generate random darker colors for better contrast
    r = random.randint(0, 150)  # Lower values for darker shades
    g = random.randint(0, 150)
    b = random.randint(0, 150)
    return f"rgb({r},{g},{b})"


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
                "<h2>🙋‍♂️ About Me</h2>"
                "<p>Aspiring Data Scientist with a passion for AI-driven solutions and automation. Experienced in developing intelligent systems, predictive models, and data-driven applications. Always eager to learn, innovate, and solve real-world problems using data and technology.</p>"
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
                "<li>Developed an advanced real-time object detection system using deep learning and computer vision techniques for high accuracy.</li>"
                "<li>Built an intelligent chatbot leveraging natural language processing and retrieval-augmented generation, integrated with an optimized database for efficient and context-aware responses.</li>"
                "<li>Developed a web scraping solution using automation tools to extract data from dynamic websites efficiently and accurately.</li>"
                "<li>Designed an interactive frontend with Streamlit and optimized chatbot interactions for a seamless user experience.</li>"
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
                "<li>Develop and maintain web applications using Python and Flask framework.</li>"
                "<li>Create and optimize database schemas using MongoDB for efficient data storage and retrieval.</li>"
                "<li>Collaborate with frontend developers to integrate user- facing elements with server-side logic.</li>"
                "<li>Troubleshoot and debug issues reported by users or identified during testing phases.</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- SKILLS (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h2>💡 Skills</h2>"
                "<ul>"
                "<li><strong> Programming & Development:</strong> Python, Flask, Streamlit, Selenium</li>"
                "<li><strong> Machine Learning & AI:</strong> Deep Learning, NLP, RAG, Langchain, LLM</li>"
                "<li><strong> Data Handling & Databases:</strong> SQL, NoSQL, MongoDB, Web Scraping</li>"
                "<li><strong> Data Visualization:</strong> PowerBI, Matplotlib, Seaborn</li>"
                "<li><strong> Version Control & Collaboration:</strong> Git, GitHub</li>"
                "<li><strong> Software Development:</strong> Backend Development, API Integration, Debugging</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


# --- INTERESTS (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h2>🔍 Interests</h2>"
                "<ul>"
                "<li><strong> Machine Learning & AI:</strong> Exploring AI-driven models for automation</li>"
                "<li><strong> Web Scraping & Data Extraction:</strong> Gathering insights from large-scale web data</li>"
                "<li><strong> Artificial Intelligence:</strong> Leveraging LLMs and NLP for human-like interactions</li>"
                "<li><strong> Data Science & Analytics:</strong> Transforming raw data into actionable insights</li>"
                "<li><strong> Tech Innovation:</strong> Building intelligent systems that solve real-world challenges</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


# --- PROJECTS (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.subheader("🚀 Projects")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>🎓 SGPA Prediction 📊 <a href='https://github.com/rushideshmukh3620/SGPAPrediction.git' style='color:white;'> View Project 👀</a></h4>"
                "<p>A predictive model designed to estimate SGPA (Semester Grade Point Average) for the fifth semester based on the academic performance of the previous four semesters. By analyzing historical data, the model identifies patterns and trends, helping students get an early estimate of their expected grades. This can assist in performance tracking, academic planning, and goal setting for future improvements.</p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- PROJECTS (Right) ---
col1, col2 = st.columns([1, 2])  

with col2:
    st.markdown(f"""
    <div class='box' style='background-color: {random_color()};'>
        <h4>🖼️ Image Enhancement App 🛠️<a href='https://imageenhancement.streamlit.app/' style='color:white;'> Live Demo 🚀</a></h4>
        <p>An interactive application that allows users to upload images, upon which it automatically applies a suite of enhancement techniques, including sharpening, denoising, and contrast adjustment, to improve image quality without requiring user input. The app provides a side-by-side comparison of the original and enhanced images, enabling users to visualize the improvements effectively.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- PROJECTS (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>🚗 Car Price Prediction System 💰</h4>"
                "<p>A machine learning-based model that predicts the approximate selling price of a car based on key factors such as fuel type, number of previous owners, kilometers driven, and other vehicle specifications. By analyzing historical sales data and market trends, this model helps users make informed decisions when buying or selling a car, ensuring a fair and competitive price estimate.</p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- CERTIFICATIONS (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h3>📜 Certifications</h3>"
                "<ul>"
                "<li> Full Stack Data Science & AI (Naresh IT, Oct 2021 - Mar 2022) <a href='https://www.linkedin.com/posts/rushideshmukh3620_machinelearning-datascience-artificialintelligence-activity-7163174936453234690-Y7FQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "<li> Data Analytics and Visualization Job Simulation (Accenture, January 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-forage-accenture-activity-7150485871014617088-mYoV?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "<li> Data Visualisation: Empowering Business with Effective Insights (TATA, January 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-forage-tcs-activity-7155951764121268224-eDB5?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "<li> Data Science Job Simulation (British Airways, Apr 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-certification-continuouslearning-activity-7198595719371378688-MnIW?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center;'>© 2025 Rushikesh Deshmukh</p>", unsafe_allow_html=True)
