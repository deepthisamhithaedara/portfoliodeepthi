import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(layout= "wide")
st.write("##")
st. subheader("Hello :wave:")

st.title("I am deepthi")
st.write(
"""Graduate student @Villanova University | Ex-Microsoft """)
st.write("[Linkedin](https://www.linkedin.com/in/edaradeepthi/)")
st.write(' --- ')

with st.container():
    selected = option_menu(
    menu_title = None,
    options = ['About', 'Experience','Projects', 'Contact'],
    icons = ['person', 'laptop','code-slash', 'chat-left-text-fill'],
    orientation= 'horizontal'
    )

if selected == 'About':
    with st.container():
        st.write("##")
        st.write(""" 
Proactive computer science graduate driven by a passion for technology and with a extensive professional background. Skilled in databases, cloud platforms, and Python programming.""")
        st.write(" --- ")
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.subheader("""Education
- **Masters in Computer Science**
- Villanova University, Pennsylvania
- Grade: 3.89/4
- **Bachelors in Computer Science**
- KL Univerity, Guntur
- Grade: 9.3/10
 """)
    with col4:
        st.subheader(""" Skills
- Programming: Python, Java, C, C++,SQL.    
- Other: Azure cloud, Data Engineering, 
Machine Learning with python, Database 
administration & development.
- Microsoft Certified Azure Data Engineer
- Microsoft Certified Azure Administrator

 """)

if selected =="Projects":
    with st.container():
        st.header("My Projects")
        st.text("")
        col5, col6 = st.columns((1,2))
        with col5:
            st.subheader("AZURE DATA ENGINEERING PROJECT- OLYMPIC DATA ANALYSIS WITH AZURE SERVICES")
            st.write(""" Designed and implemented an end-to-end data engineering solution leveraging 
            Azure services. Orchestrated data movement from Git to Azure Data Lake Storage using Azure Data Factory. Employed Azure Databricks for data transformation and preprocessing tasks.
           Facilitated analysis and insights generation in Azure Synapse Analytics for Olympic data. """)

        with col6:
            st. image('Project Architecture.png', caption='Project Architecture')

    st.write("--------")

    with st.container():
        col7, col8 = st.columns((1,2))
        with col7:
            st.subheader(" EMOTION RECOGNITION USING ELECTROENCEPHALOGRAMDATA ")
            st.write(""" The objective of the project is how accurately we can classify emotions using different 
            Machine Learning Techniques like SVM and How precisely the EEG signs can be grouped. """)
        with col8:
            st. image('Methadology.png', caption='Methadology\Dataflow')

if selected =="Contact":
        st.subheader(" CONTACT ")
        st.write(""" Gmail: deepthiedara2000@gmail.com """)
        st.write(""" Mobile: +14842357860""")
        st.write("[Linkedin](https://www.linkedin.com/in/edaradeepthi/)")

if selected =="Experience":
        st.header(" EXPERIENCE ")
        st.text("")
        st.subheader(""" MICROSOFT, Hyderabad | April 2021 - January 2023
**TECHNICAL CLOUD DATABASE ENGINEER**
- Worked on SQL on Azure, SQL Core, High Availability, SQL Performance. skilled in handling diverse cases including SQL Installation planning, database design, migration, High Availability, security, and performance tuning.
- Led the technical resolution of 100+ mission-critical SQL server databases (and Azure) improving business continuity and minimizing production downtime by prioritizing the most critical issues and identifying the root cause.
- Collaborated with SQL and Azure escalation engineers and product teams to identify and resolve complex bugs.
- **INTERN**
- Trained across the breadth of Microsoft Technologies covering Azure, Azure Databases, Azure AD, Data&AI, Security, Networks, and Active Directory.
        """)
        st.subheader("""  OPTUM, Hyderabad | January 2021 - April 2021 
**SOFTWRE ENGINEER INTERN**
- Worked with Azure team & contributed to transitioning data from on-premises systems to Azure Data Lakes through using the Azure Data Factory pipelines. My role involved designing and implementing the data factory pipelines.
        """)
        st.subheader("""  KLU, Guntur | January 2020 - January 2021 
**STUDENT PEER MENTOR FOR PYTHON**
- Mentored peers in Python programming, provided personalized assistance in debugging, troubleshooting for coding projects. Additionally, conducted workshops and seminars on machine learning with python.
""")
       
    




   
