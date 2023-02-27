import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Know Me", page_icon="🕴️", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_sb5rlinb.json")
lottie_1 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_DMgKk1.json")
lottie_2 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_xl25zrrh.json")
lottie_3 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_MImHBS.json")
lottie_4 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_eeuhulsy.json")

# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.subheader("Hi, Everyone :wave:")
        st.title(

     """
     I am Aditi Rokade
Adaptable student with fundamental knowledge 
of Data Analysis, Machine Learning and Artificial 
Intelligence. Aiming to leverage my abilities.
Frequently praised for communication by my
peers. A fast learner and hard worker with high 
responsibilities seeking for opportunities 
    """)
    with right_column:
        st_lottie(lottie, height=300, key="Title")
    
    
SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/aditi-rokade/",
    "GitHub": "https://github.com/AditiRokade",
    "Kaggle": "https://www.kaggle.com/aditirokade08"
}
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---- Education----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("EDUCATION:")
        #st.write("##")
        st.write(
            """
          -Bharati Vidyapeeth’s College of Engineering for Women. Pune, Maharashtra \n 
BE in Electronics and Telecommunication (CGPA: 8.95) 2019-2023 \n
-Yashwantrao Mohite Jr. College of Arts, Commerce and Science Pune, Maharashtra \n
XII Science (percentage: 77.08%) 2018-2019 \n
-Pride English School Pune, Maharashtra \n
X (Percentage: 86.80%) 2017-2018

            """
        )
    with right_column:
        st_lottie(lottie_1, height=300, key="Education")
        

with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("INTERNSHIPS::")
        #st.write("##")
        st.write(
            """
-TCR-Innovation Pune, Maharashtra \n
DATA SCIENTIST INTERN April 2022 – June 2022\n
● Wrote new functions and applications in programming languages to conduct analyses\n
● Created graphs, charts, and other visualizations to convey results of data analysis using specialized software\n
-Zensar Pune, Maharashtra\n
Trainee September 2021 – December 2021\n
● Training on aptitude, PL/SQL\n
● Worked on Jira for debugging\n
● Worked on Excel sheets to deliver the results of manual testing for websites and applications\n
-Shape- AI Virtual\n
Data Analyst Intern May 2021 – August 2021\n
● Analyzed competitive market strategies through analysis of related product, market and share trends\n
● Extracted key observations and insights from internal and external data sources to drive decision-making"""
        )
    with right_column:
        st_lottie(lottie_2, height=300, key="Internships")
        st.write("#Python  #Manual testing #ML #DL  #Data Analytics  #Pandas #RandomForrest  #Seaborn #PL-SQl")
    

# ---- VOLUNTERING EXPERIENCE ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("VOLUNTERING EXPERIENCE")
        #st.write("##")
        st.write(
            """
-Technaut College Club Pune, Maharashtra\n
Developer Domain Head January2022 – December 2022\n
● Assigned various tasks for 35 team members.\n
● Spearhead events for weekly meetings regarding resumes, cover letters, and LinkedIn workshops for team members\n
-Inception Wave Student Chapter-BVCOEW Pune, Maharashtra\n
Developer team member | Marketing team member July 2021 – November 2021\n
● Completed the assigned tasks on time\n
● Contacted and collaborated with other club members"""
        )
    with right_column:
        st_lottie(lottie_3, height=300, key="VOLUNTERING EXPERIENCE")
        
# ---- Projects ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("Projects")
        #st.write("##")
        st.write(
            """
-Car Damage Detection Self Project\n
• Using images taken at the site of an accident trained the model with Mobilenet-SSD to detect the damage on the cars.\n
• Tech stack: Object detection, TensorFlow, Computer Vision, Deep learning.\n
-Movie and Song recommendation system Self Project\n
• Meet, Greet, Prepare the Data for consumption (Feature Engineering and Selection), perform EDA (Visualizations)\n
• Modeled, Validated, and implemented data model using SVM suggested minimum five movies to a person based on 
similarities of the chosen film or selected film\n
• Tech stack: Python, Machine learning, Heroku\n
-Bank Marketing Campaign Team of 4 \n
• Prepare the Data for consumption (Feature Engineering and Selection), perform Exploratory Analysis (Visualizations)\n
• Modeled, Validated, and implemented data model\n
• Optimized and strategized the outcome with 89% of accuracy\n
• Tech stack: jupyter notebook, Machine Learning"""
        )
    with right_column:
        st_lottie(lottie_4, height=300, key="PROJECTS")
        


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/a76f6e2c9416121d1aa5b7093e4de152" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
