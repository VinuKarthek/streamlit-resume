import streamlit as st
from PIL import Image

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
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
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

txt('**Staff Engineer (Data Science)**, Infineon, Singapore',
'2021-2023')
st.markdown('''
- Developed Data extraction & Analysis scripts for Automated Lot-on-hold Analysis (~100 lots/hour)
- Developmed several ML/AI models for aiding the analysis (ie Wafer Map Classification, Rule Optimization etc) & deployed them using FastAPI to Openshift Cloud machinesPost-Silicon& Tableau
- Developed several Streamlit dashboards to help multiple user label images
''')

txt('**Sr SoC Validation Engineer**, Qualcomm, Singapore',
'2017-2021')
st.markdown('''
- Post-Silicon Validation of Mixed-Signal IPs on State of the art Mobile, Modem (5FF) & RF(14nm) SoCs  
- Design & Development of High-Speed (>15Gbps) System Level Test Platform for Validation of 5G (Sub6/mm Wave) RF transceivers
- Development of end to end test automation solution for PVT char using LabVIEW & Python Framework
- Experienced in applying Machine Learning models like Regression, Clustering, xGBoost & random forest for data interpretation using Tensorflow/Keras
- Expert in Statistical Data analysis & visualization of production test data using Python, Spotfire & Tableau
- Managed a team of 5 engineers handling Characterizing for multiple Mixed-Signal IPs in the SoC
''')

#####################
st.markdown('''
## Education
''')

txt('**M.Sc. in Computer Control & Automation**, NTU, Singapore',
'2016-2017')
st.markdown('''
- GPA: `3.7`
- Research thesis entitled `Automated passenger boarding bridge`
''')

txt('**B.E. in Electronics & Comm Engineering**, Anna University, Chennai',
'2008-2012')
st.markdown('''
- GPA: `8.9`
- Graduated with First Class Distinction.
''')

#####################
st.markdown('''
## Projects
''')
txt4('Mortality Prediction for Liver Cirrhosis Patients', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
txt4('', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `LabVIEW`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/chaninn/')
txt2('', 'https://github.com/chaninlab/')
txt2('', 'https://github.com/dataprofessor')
txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
txt2('Publons', 'https://publons.com/a/303133/')
