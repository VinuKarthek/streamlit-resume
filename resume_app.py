import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="Vinu Karthek - Profile",
     # page_icon= Image.open("icon.png"), #':shark:',
     layout="wide",
     initial_sidebar_state="auto",
     menu_items={
         'Report a bug': 'https://github.com/VinuKarthek/streamlit-resume/issues',
         'About': "Simple *Streamlit Based Resume App*\n Rev 1.0.0"
         }
     )

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Vinu Karthek, M.Sc
### AI/ML Modelling | CICD☁️ | Automation Dev🤖 | Statistical Analysis📶
##### *Resume* 
''')

image = Image.open('photo.jpeg')
#st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- 6+ years experience in development & deployment of scalable AI/ML Models using Python/R in Semiconductor/Manufacturing domains
  - Leveraged DVC/MLFlow/Optuna for Model Development & Docker/K8S/Git CICD Pipelines for Deployement
  - Expertise in Statistical Data Analysis (Hypothesis Testing/ANNOVA/Chi-Squared test)
  - Proficiency in creating Data Visualizaton Dashboards using Tableau/TIBCO Spotfire
- 8 years of expertise in developing Automation Framework using Python, PowerShell & NI-LabVIEW
  - Developed data analysis/extraction tools with GUI, achieving a minimum 25% time savings
  - Successfully managed strict & stringent timelines coordinating across multiple zones while exceeding expectations
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/vinukarthek/" target="_blank">LinkedIn</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


#####################
st.markdown('''
## Work Experience
''')

txt('**Staff Data Scientist**, Infineon, Singapore',
'2021-2023')
st.markdown('''
- Develop & deploy scalable AI/ML models leveraging **DVC/MLFlow/Optuna** for Model Development & **Docker/K8S/Git** CICD Pipelines for Deployement
  - Models like Wafer-map Image Classification (**ResNet-50**), FrontEnd Falure Prediction (**xgBoost**), Rule Optimization(**RUSBoost**) for aiding Lot on Hold Analysis. Resulted in sustainalbe savings of **110k€/year**
  - Deployment was done using FastAPI/Streamlit on Openshift PaaS in K8S PODs. Utilized GitHub Actions & webhooks for CI/CD. The performance of the model monitored using Tableau Dashboards
  - Hands-on experience with TensorFlow, SciKit Learn and Keras libraries to develop Deep-NN, GAN, SVM, Regression, Clustering & Random Forest Classifiers/Regressors
- Developed Data extraction & Analysis scripts for Automated Lot-on-hold Analysis (**100+ lots/hour over 6 sites across the globe**) using **MS-SQL,R & UiPath RPA**
- Working on developing product catalog search/query tool using **LangChain+ llama2 LLM**
''')

txt('**Sr SoC Validation Engineer**, Qualcomm, Singapore',
'2017-2021')
st.markdown('''
- Post-Silicon Validation of Mixed-Signal IPs on State of the art Mobile, Modem (5FF) & RF(14nm) SoCs
- Expert in Statistical Data analysis & visualization of production test data using Python, NI-Optimal Plus, Spotfire(Exensio) & Tableau
- Experienced in applying Machine Learning models like Regression, Clustering, xGBoost & random forest for data interpretation using Keras
- Development of end to end test automation framework for PVT char using LabVIEW & Python Framework
- Design & Development of High-Speed (>15Gbps) System Level Test Platform for Validation of 5G (Sub6/mm Wave) RF transceivers
- Managed a team of 5 engineers handling Characterizing for multiple Mixed-Signal IPs in the SoC
''')

txt('**Research Student (Machine Learning)**, ST Eng & NTU Corps Lab,Singapore',
'2016-2017')
st.markdown('''
- Developed python UI for annotating features on airplane door images (viz door, door handle, window etc) , facilitating precise labelling for subsequent analysis
- Employed deep learning techniques (CNN using tensorflow1.0) for object detection, utilizing annotated data to identify and locate features on airplane doors with 95% accuracy
- Using the detected features Validating & the laser distance sensor, developed a complex scoring algorithm to confirm if the robot base is facing the airplane door
- Control the robotic base carrying the camera, laser sensor and aero-bridge depending on the control signals obtained, thus achieving a perfect docking (using Robotic Operating System)
''')

txt('**Engineering Intern**, Qualcomm, Singapore',
'2016 - 2017')
st.markdown('''
- Developed a generic Python automation for post-processing & filtering huge test data (up to 5 GB) using Pandas/Vaex
- Robotic handler automation for multi DUT testing using LabVIEW
- Designed an AAF with Low pass-band attenuation & steep roll-off for a custom digitizer(using Keysight ADS Tool)
''')

#####################
st.markdown('''
## Education
''')

txt('**M.Sc. in Computer Control & Automation**, NTU, Singapore',
'2016-2017')
st.markdown('''
- GPA: `3.7`
- Research Thesis Title: `Automated passenger boarding bridge`
''')

txt('**B.E. in Electronics & Comm Engineering**, Anna University, Chennai',
'2008-2012')
st.markdown('''
- GPA: `8.9`
- Graduated with First Class Distinction.
- Thesis Title: `Real Time Flood Alert System Using GSM`
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `LabVIEW`, `Embedded C++`, `Verilog`')
txt3('Databases', '`MSSQL`, `MySQL`, `MongoDB`, `FAISS/Chroma DB`')
txt3('Data visualization', '`Tableau`, `Spotfire`, `seaborn, matplot, ggplot2`')
txt3('Machine Learning', '`scikit-learn`,`keras`,`pytorch`,`xgboost/rusboost`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web Development', '`Django`, `HTML`, `CSS`')
txt3('Model Pipelines', '`Docker`, `Kubernetes`, `Gitlab`, `MLFlow`, `DVC`, `Apache Airflow`')
txt3('Model Deployment', '`streamlit`, `FastAPI`, `Heroku`, `AWS`, `Openshift`')

#####################
st.markdown('''
## Projects
# ''')
# txt4('Mortality Prediction for Liver Cirrhosis Patients', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
# txt4('', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
# txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
# txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
# txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
# txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
# txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
# txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
# txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
# txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
# txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
# txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
# txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/vinukarthek')
txt2('Twitter', 'https://twitter.com/vinukarthek')
txt2('GitHub', 'https://github.com/vinukarthek/')
txt2('Portfolio', 'https://portfolio.vinukarthek.com/')