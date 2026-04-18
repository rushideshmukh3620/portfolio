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
passport_photo = Image.open("Rushi.jpg")

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
                "<h3>Software Development Engineer</h3>"
                "<p>📧 <a href='mailto:rushideshmukh3620@gmail.com' style='color:white;'>rushideshmukh3620@gmail.com</a></p>"
                "<p>🔗 <a href='https://linkedin.com/in/rushideshmukh3620' style='color:white;'>LinkedIn</a> | "
                "<a href='https://github.com/rushideshmukh3620' style='color:white;'>GitHub</a></p>"
                "</div>", unsafe_allow_html=True)

st.markdown("---")

# Zig-Zag Pattern Layout
# --- ABOUT ME (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.subheader("🙋‍♂️ About Me")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<p>Backend Software Engineer with experience building scalable REST APIs, microservices, and data processing systems in fintech environments. Skilled in Python, Node.js, .NET, and Go, with hands-on experience in API integrations, authentication systems, and automation pipelines.</p>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)  

# --- WORK EXPERIENCE (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.subheader("💼 Work Experience")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>Software Developer - Centricity Wealth Tech Private Limited</h4>"
                "<p><em>April 2025 - Present</em></p>"
                "<ul>"
                "<li>Developed backend services using Python and JavaScript to capture user consent, retrieve financial PDFs via Gmail API, and convert extracted data into structured JSON using external APIs.</li>"
                "<li>Built REST APIs using .NET and SQL Server with stored procedures following database-first architecture.</li>"
                "<li>Implemented Node.js automation scripts for document retrieval, API integration, and structured PDF generation; handled manual deployment on Linux servers using MobaXterm.</li>"
                "<li>Designed Identity Provider (IDP) service using Go and PostgreSQL for client onboarding and authentication workflows.</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- WORK EXPERIENCE (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>Data Science Intern - Futurism Technologies Private Limited</h4>"
                "<p><em>Dec 2024 - March 2025</em></p>"
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

# --- PROJECTS (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.subheader("🎯 Projects")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<h4>🎓 SGPA Prediction 📊 <a href='https://github.com/rushideshmukh3620/SGPAPrediction.git' style='color:white;'> GitHub Repo 🔗</a></h4>"
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
    st.subheader("📜 Certifications")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<ul>"
                "<li> Full Stack Data Science & AI (Naresh IT, Oct 2021 - Mar 2022) <a href='https://www.linkedin.com/posts/rushideshmukh3620_machinelearning-datascience-artificialintelligence-activity-7163174936453234690-Y7FQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "<li> Data Analytics and Visualization Job Simulation (Accenture, January 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-forage-accenture-activity-7150485871014617088-mYoV?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "<li> Data Visualisation: Empowering Business with Effective Insights (TATA, January 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-forage-tcs-activity-7155951764121268224-eDB5?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "<li> Data Science Job Simulation (British Airways, Apr 2024) <a href='https://www.linkedin.com/posts/rushideshmukh3620_connections-certification-continuouslearning-activity-7198595719371378688-MnIW?utm_source=share&utm_medium=member_desktop&rcm=ACoAADo1sJoBOub6tglAKPatjr68g1nDqwgJlzg' style='color:white; text-decoration: none;'>👁️</a></li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- SKILLS (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.subheader("💡 Skills")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<ul>"
                "<li><strong> Languages:</strong> Python, JavaScript, Go, SQL</li>"
                "<li><strong> Backend Development:</strong> Flask, Node.js, .NET, REST APIs, Microservices, API Integration</li>"
                "<li><strong> Databases:</strong> PostgreSQL, SQL Server, MongoDB, Neo4j</li>"
                "<li><strong> Data Processing:</strong> Web Scraping, Data Extraction, Automation Scripts</li>"
                "<li><strong> Tools & Technologies:</strong> Docker, Linux, Git, Selenium, MobaXterm</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


# --- INTERESTS (Right) ---
col1, col2 = st.columns([1, 2])

with col2:
    st.subheader("🔍 Interests")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<ul>"
                "<li><strong> Building scalable backend systems and APIs</li>"
                "<li><strong> Designing data processing and automation workflows</li>"
                "<li><strong> Applying machine learning in backend applications</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- EDUCATION (Left) ---
col1, col2 = st.columns([2, 1])  

with col1:
    st.subheader("🎓 Education")
    st.markdown(f"<div class='box' style='background-color: {random_color()};'>"
                "<ul>"
                "<li><strong>M.Sc. (Computer Science)</strong> - 79.95% (2022-2024) MIT Arts, Commerce and Science College </li>"
                "<li><strong>B.Sc. (Computer Science)</strong> - 78.10% (2018-2021) G. H. Raisoni College of Arts, Commerce and Science </li>"
                "<li><strong>HSC </strong> - 74.92% (2018) NES Highschool and Jr. College </li>"
                "<li><strong>SSC </strong> - 79.60% (2016) Sadashivrao Mane Vidyalay </li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center;'>© 2025 Rushikesh Deshmukh</p>", unsafe_allow_html=True)
