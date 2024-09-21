import streamlit as st

# Function to display a separator line
def separator():
    st.write("---")

# Initialize session state for tracking the question steps
if 'step' not in st.session_state:
    st.session_state.step = 0

# Welcome Message (always displayed)
st.title("Welcome to the Emotional Clarity Project 🌟")
st.write("We're here to help you reflect on your feelings and guide you toward open communication.")
st.write("Press 'Enter' after answering each question to proceed.")

# Step 1: First Question - Reflect on Emotional Attachment
if st.session_state.step == 0:
    attachment = st.text_input("Do you feel emotionally attached to someone right now? (yes/no/not sure): ").lower()

    if attachment:
        separator()
        if attachment == "yes":
            st.write("It's important to recognize and honor those feelings. 🌱")
            st.write("But remember, being attached doesn’t always mean the relationship is right for you. Take a moment to reflect on what this attachment brings to your life. 💫")
        elif attachment == "no":
            st.write("That’s perfectly okay. Not every connection leads to emotional attachment. 💭")
            st.write("It’s important to be honest with yourself and the other person about where you stand emotionally. 🛤️")
        elif attachment == "not sure":
            st.write("It's okay to feel uncertain. 💖")
            st.write("Sometimes, emotions are complex, and it’s worth giving yourself time to reflect without pressure. 🌷")
        else:
            st.write("Hmm, I didn’t get that, but let’s continue reflecting. 😊")
        separator()
        # Move to the next step
        st.session_state.step = 1

# Step 2: Are You Considering Ghosting?
if st.session_state.step == 1:
    ghosting = st.text_input("Are you thinking about pulling away or ghosting someone? (yes/no/maybe): ").lower()

    if ghosting:
        separator()
        if ghosting == "yes":
            st.write("Ghosting may seem easier, but it often leaves unresolved emotions for both sides. 🌫️")
            st.write("It’s usually better to communicate how you feel, even if it’s difficult. Being honest can bring closure and peace. 💬")
        elif ghosting == "no":
            st.write("That’s great! Open communication is always a healthier option. 🗝️")
            st.write("It’s important to honor the other person’s feelings by being upfront, even if you’re unsure how you feel. 🌻")
        elif ghosting == "maybe":
            st.write("It’s normal to feel like avoiding difficult conversations, but clear communication often brings relief. 🛤️")
            st.write("Before making a decision, think about how you would feel if someone ghosted you. 💭 It’s usually best to express your feelings openly.")
        else:
            st.write("Let’s keep exploring your feelings. 😊")
        separator()
        # Move to the next step
        st.session_state.step = 2

# Step 3: Are You In Love or Is It Something Else?
if st.session_state.step == 2:
    in_love = st.text_input("Do you feel like you’re in love with this person, or is it something else? (love/unsure/not really): ").lower()

    if in_love:
        separator()
        if in_love == "love":
            st.write("That’s beautiful! ❤️ Love can be a powerful feeling, but make sure to communicate it openly and honestly. 💬")
            st.write("Remember, love is about understanding and connection, not fear or avoidance. Be brave in sharing your truth. 🌈")
        elif in_love == "unsure":
            st.write("It’s okay to be uncertain. 💭 Take your time to understand your feelings.")
            st.write("You don’t need to rush to a conclusion. Often, deep reflection or a conversation with the other person can bring clarity. 🛤️")
        elif in_love == "not really":
            st.write("That’s perfectly okay. Not every connection is about love, and that’s valid. 🌱")
            st.write("If you’re not in love, it’s important to communicate this so you don’t unintentionally lead the other person on. 🌷")
        else:
            st.write("That’s okay, emotions are complicated. Let’s keep reflecting. 😊")
        separator()
        # Move to the next step
        st.session_state.step = 3

# Step 4: Fear of Hurting Others or Being Honest
if st.session_state.step == 3:
    fear_hurting = st.text_input("Do you feel like avoiding communication because you’re afraid of hurting the other person? (yes/no/maybe): ").lower()

    if fear_hurting:
        separator()
        if fear_hurting == "yes":
            st.write("It’s natural to fear hurting others. 🌿 But avoiding communication often leads to more hurt in the long run. 💔")
            st.write("By being open and honest, you’re showing respect for the other person’s emotions and allowing them to heal. 🛤️")
        elif fear_hurting == "no":
            st.write("That’s a healthy mindset! 🗝️ Clear and open communication is always better than leaving someone in uncertainty. 🌞")
        elif fear_hurting == "maybe":
            st.write("It’s understandable to feel torn. 💭 But remember, honesty is kindness in the long run. 🌻")
            st.write("It’s better to express your feelings than to leave the other person wondering or hurt by silence. 🌿")
        else:
            st.write("Emotions can be tricky, but clarity always helps. 🌈")
        separator()
        # Move to the next step
        st.session_state.step = 4

# Step 5: Final Reflection - Encourage Healthy Communication
if st.session_state.step == 4:
    reflection = st.text_input("What’s something you want to express to the person you’ve been thinking about? (type anything): ")

    if reflection:
        separator()
        st.write(f"That’s a great start! Expressing {reflection} will help you and the other person reach a better understanding. 🌸")
        st.write("Remember, open and honest communication is key to forming healthy relationships and letting go of emotional attachments that don’t serve you. 💬")
        separator()
        st.write("Thank you for joining the Emotional Clarity Project. 🌈 We hope this has helped you reflect and approach your feelings with honesty and compassion.")
