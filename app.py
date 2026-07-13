import streamlit as st
from groq import Groq

# Configure Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page Configuration
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.header("🎓 AI Learning Buddy")
    st.write("Your personal AI tutor powered by Groq.")
    st.info("Enter a topic, choose an activity, and click Generate!")

# Main Title
st.title("🎓 AI Learning Buddy")
st.caption("Learn concepts, examples, quizzes, and more with AI.")

# User Input
topic = st.text_input("📚 Enter a Topic")

option = st.selectbox(
    "🎯 Choose Activity",
    [
        "📖 Explain Concept",
        "🌍 Real-Life Example",
        "📝 Generate Quiz",
        "💬 Ask Anything"
    ]
)

# Generate Button
if st.button("🚀 Generate"):

    if topic.strip() == "":
        st.warning("⚠ Please enter a topic.")

    else:

        if option == "📖 Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "🌍 Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "📝 Generate Quiz":
            prompt = f"Create 5 multiple choice questions on {topic} with answers."

        else:
            prompt = topic

        try:

            with st.spinner("🤖 AI is generating your response..."):

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

            st.success("✅ Response Generated Successfully!")

            st.subheader(f"📚 Topic: {topic}")

            st.markdown(response.choices[0].message.content)

        except Exception:
            st.error("❌ Something went wrong. Please try again later.")

# Footer
st.markdown("---")
st.caption("❤️ Developed by Mithra using Streamlit & Groq AI")