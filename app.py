import streamlit as st
from groq import Groq

# Configure Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

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
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1024
            )

            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")