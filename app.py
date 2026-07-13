import streamlit as st
from google import genai

# Configure Gemini
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

# Page configuration
st.set_page_config(
    page_title="AI Learning Buddy Mithra",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy Mithra")

# User input
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    st.subheader("Available Gemini Models")

    try:
        models = client.models.list()

        for model in models:
            st.write(model.name)

    except Exception as e:
        st.error(f"Error: {e}")