import streamlit as st

# Streamlit title and introduction
st.title("Welcome to the Emotional Clarity Project 🌟")
st.write("We're here to help you reflect on your feelings and guide you toward open communication.")
st.write("Let's take a moment to reflect on how you're feeling today.")

# State management to handle the flow of questions
if 'step' not in st.session_state:
    st.session_state.step = 1

# First Question - Reflect on Emotional Attachment
if st.session_state.step == 1:
    attachment = st.radio(
        "Do you feel emotionally attached to someone right now?",
        ("Yes", "No", "Not sure")
    )
    
    if st.button("Next"):
        st.session_state.attachment = attachment
        st.session_state.step = 2

# Second Question - Are You Considering Ghosting?
if st.session_state.step == 2:
    st.write(f"Attachment Response: {st.session_state.attachment}")
    
    ghosting = st.radio(
        "Are you thinking about pulling away or ghosting someone?",
        ("Yes", "No", "Maybe")
    )

    if st.button("Next"):
        st.session_state.ghosting = ghosting
        st.session_state.step = 3

# Third Question - Are You In Love or Is It Something Else?
if st.session_state.step == 3:
    st.write(f"Ghosting Response: {st.session_state.ghosting}")
    
    in_love = st.radio(
        "Do you feel like you’re in love with this person, or is it something else?",
        ("Love", "Unsure", "Not really")
    )

    if st.button("Next"):
        st.session_state.in_love = in_love
        st.session_state.step = 4

# Fourth Question - Fear of Hurting Others or Being Honest
if st.session_state.step == 4:
    st.write(f"In Love Response: {st.session_state.in_love}")

    fear_hurting = st.radio(
        "Do you feel like avoiding communication because you’re afraid of hurting the other person?",
        ("Yes", "No", "Maybe")
    )

    if st.button("Next"):
        st.session_state.fear_hurting = fear_hurting
        st.session_state.step = 5

# Final Reflection - Encourage Healthy Communication
if st.session_state.step == 5:
    st.write(f"Fear of Hurting Response: {st.session_state.fear_hurting}")
    
    reflection = st.text_input("What’s something you want to express to the person you’ve been thinking about?")

    if reflection:
        st.session_state.reflection = reflection
        st.session_state.step = 6

# Display Final Message After Completing Reflection
if st.session_state.step == 6:
    st.write(f"Reflection: {st.session_state.reflection}")
    st.write(f"Thank you for joining the Emotional Clarity Project. 🌈 We hope this has helped you reflect and approach your feelings with honesty and compassion.")
