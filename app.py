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

# Generate response
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple choice questions on {topic} with answers."

        else:
            prompt = topic

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-pro",
                contents=prompt,
            )

            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
