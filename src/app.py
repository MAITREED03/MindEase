import streamlit as st
from utils.emotion_detection import detect_emotion
from utils.responder import generate_response
from PIL import Image
import os

# --- UI Setup ---
st.set_page_config(
    page_title="MindEase: Your AI Mental Health Companion",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stTextArea > label {
        font-size: 20px;
    }
    .stButton > button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=120)
except:
    st.title("🧠 MindEase")

st.subheader("Your AI Mental Health Companion")
st.markdown("---")

# Main interaction
user_input = st.text_area("How are you feeling today? 💭", height=150)

if st.button("Analyze Emotion 🔍"):
    if user_input.strip():
        with st.spinner("Analyzing your emotions..."):
            result = detect_emotion(user_input)
            emotion = result["label"]
            score = result["score"]

            # Display results
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"### Detected Emotion:")
                st.markdown(f"## {emotion.title()} 🎭")
            with col2:
                st.markdown("### Confidence:")
                st.markdown(f"## {score * 100:.0f}%")

            st.markdown("---")
            st.markdown("### 💡 MindEase's Response:")
            st.success(generate_response(emotion))
    else:
        st.warning("Please share your thoughts so I can help you better.")