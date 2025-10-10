import streamlit as st


def load_css():

    css = """
    <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes titleGlow {
            0%, 100% { text-shadow: 0 0 10px #00c2ff, 0 0 20px #00c2ff, 0 0 30px #00c2ff; }
            50% { text-shadow: 0 0 20px #00c2ff, 0 0 30px #00c2ff, 0 0 40px #00c2ff; }
        }

        @keyframes pulseGlow {
            0%, 100% { box-shadow: 0 0 5px #00c2ff; }
            50% { box-shadow: 0 0 15px #00c2ff, 0 0 20px #00c2ff; }
        }

        @keyframes containerPulse {
            0%, 100% { box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1), 0 0 5px rgba(0, 194, 255, 0.2); }
            50% { box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2), 0 0 15px rgba(0, 194, 255, 0.4); }
        }

        
        .stApp {
            background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #00c2ff);
            background-size: 400% 400%;
            animation: gradientAnimation 15s ease infinite;
            font-family: 'Poppins', sans-serif;
        }

        
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        
        h1 {
            color: #FFFFFF !important;
            font-family: 'Poppins', sans-serif;
            border-bottom: 2px solid rgba(0, 194, 255, 0.5);
            padding-bottom: 10px;
            animation: titleGlow 4s ease-in-out infinite;
        }

        h2, h3, h4, h5, h6, .stMarkdown {
            color: #FFFFFF !important;
        }
        .stSubheader {
            color: #E0E0E0 !important;
        }

        
        .css-1d391kg {
             background: rgba(255, 255, 255, 0.05);
             backdrop-filter: blur(10px);
             border-right: 1px solid rgba(255, 255, 255, 0.2);
        }
        .css-1d391kg label {
            color: #E0E0E0 !important;
        }

        
        .stTextArea textarea {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            color: #FFFFFF;
            transition: all 0.3s ease;
            animation: containerPulse 5s ease-in-out infinite;
        }
        .stTextArea textarea:focus {
            animation: none; /* Stop pulsing when focused */
            background: rgba(255, 255, 255, 0.1);
            border-color: #00c2ff;
            box-shadow: 0 0 20px rgba(0, 194, 255, 0.6);
        }

        
        .stButton>button {
            border: 2px solid #00c2ff;
            border-radius: 25px;
            color: #00c2ff;
            background-color: transparent;
            font-weight: 600;
            transition: all 0.3s ease;
            animation: pulseGlow 3s ease-in-out infinite;
        }
        .stButton>button:hover {
            animation: none; /* Stop pulsing on hover for a different effect */
            background-color: #00c2ff;
            color: #0f0c29;
            box-shadow: 0 0 20px #00c2ff, 0 0 30px #00c2ff;
        }

        
        .stSelectbox div[data-baseweb="select"] > div, .stSlider [data-baseweb="slider"] > div:first-of-type {
            background-color: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.3);
        }
        .stSlider [data-baseweb="slider"] > div:nth-child(3) {
            background: #00c2ff !important;
        }
        .stSlider [data-baseweb="slider"] > div:nth-child(2) > div {
            background: linear-gradient(to right, #00c2ff, #008fbf);
        }

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)