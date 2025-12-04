import streamlit as st
from PIL import Image
import os
from components import render_house_price_dialog, render_income_classification_dialog
from project import render_projects
from others import render_others
from achievement import render_achievements

# Page configuration
st.set_page_config(
    page_title="Phuc's Portfolio",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for dialog management
if 'open_dialog' not in st.session_state:
    # possible values: None, 'house', 'income'
    st.session_state.open_dialog = None

# Read theme from .streamlit/config.toml (robust)
config_path = os.path.join(os.path.dirname(__file__), ".streamlit", "config.toml")
theme = {}
if os.path.exists(config_path):
    try:
        import tomllib as _toml
        with open(config_path, "rb") as _f:
            cfg = _toml.load(_f)
        theme = cfg.get("theme", {}) or {}
    except Exception:
        try:
            import toml as _toml
            with open(config_path, "r", encoding="utf-8") as _f:
                cfg = _toml.load(_f)
            theme = cfg.get("theme", {}) or {}
        except Exception:
            theme = {}
else:
    theme = {}

primary = theme.get("primaryColor", "#FFCC66")
background = theme.get("backgroundColor", "#F8FAFB")
secondary = theme.get("secondaryBackgroundColor", "#024683")
text = theme.get("textColor", "#002B5B")

# expose primary color to submodules via session_state for convenience
st.session_state['primary'] = primary

# Inject CSS using theme variables
st.markdown(f"""
    <style>
    .main {{
        background-color: {background};
    }}
    .css-1d391kg {{
        background-color: {secondary} !important;
    }}
    h1 {{
        color: {primary};
        font-family: 'Trebuchet MS', sans-serif;
    }}
    h2 {{
        color: {primary};
        font-family: 'Trebuchet MS', sans-serif;
    }}
    h3 {{
        color: {primary};
        font-family: 'Trebuchet MS', sans-serif;
    }}
    .stMarkdown {{
        color: {text};
    }}
    </style>
    """, unsafe_allow_html=True)

# Sidebar - About Me Section
with st.sidebar:
    # Profile Picture
    if os.path.exists("images/temp_ava.jpg"):
        profile_img = Image.open("images/temp_ava.jpg")
        st.image(profile_img, width=200)
    
    st.markdown("## About Me")
    st.write("""
    Hello, I'm Phúc, a student who pursuing Bachelor of Data Science at University of Science, 
    Vietnam National University - Ho Chi Minh. I want to be a Data Scientist or an AI Engineering 
    after graduating, and now I'm looking for an Internship job.
    """)
    
    st.markdown("## Contact")
    st.write("Email: dmphuc04.work@gmail.com")
    st.write("Phone: (+84)...")
    st.write("LinkedIn: [phuc-dm](https://www.linkedin.com/in/phuc-dm/)")

# Main Content
st.title("🎯 Phuc's Portfolio")

# Render each major section in tabs
tab_experience,tab_projects,  tab_achievements = st.tabs([ "Experience","Projects", "Achievements"])

with tab_projects:
    render_projects()

with tab_experience:
    render_others()

with tab_achievements:
    render_achievements()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>© 2025 Phuc's Portfolio | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Dialog for House Price Prediction
@st.dialog("House Price Prediction in Ho Chi Minh City", width="large")
def show_house_price_dialog():
    render_house_price_dialog()

# Dialog for Income Type Classification
@st.dialog("Income Type Classification", width="large")
def show_income_class_dialog():
    render_income_classification_dialog()

# Show dialogs based on session state
if st.session_state.open_dialog == 'house':
    show_house_price_dialog()
elif st.session_state.open_dialog == 'income':
    show_income_class_dialog()

