import streamlit as st

import ollama


def modify_message(original_message):
    completion = ollama.chat(
        model="tinyllama",
        messages=[
            {
                "role": "system",
                "content": """You are Charles Bukowski, who has retrained as a fully licensed and laconically-spoken therapist. You are talking to your client. \n
            Ask questions to figure out what your client's emotional problems are, and ask questions to help lead your client towards insight into their thoughts and feelings.""",
            },
            {
                "role": "user",
                "content": f"""Ask for my reflections: {original_message}\n\n""",
            },
        ],
    )
    return completion["message"]["content"]


st.title("Tiny Journal Reflections")

original_message = st.text_area("Your message:", height=100)

if st.button("Get my reflections!"):
    if original_message:
        with st.spinner("Hold up, I'm thinking..."):
            modified_message = modify_message(original_message)
        st.success("Thank you! Here's your personalized reflections:")
        st.write("Your Personal Reflections:")
        st.write(modified_message)
    else:
        st.warning("Please write something before hitting submit!")

# st.sidebar.markdown("""
# ## How to use this app:
# 1. Enter the message you're replying to in the first text area.
# 2. Enter your original message in the second text area.
# 3. Click the "Modify Message" button.
# 4. The app will generate a modified, friendly version of your message.
# """)
