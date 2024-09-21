import streamlit as st

# Streamlit title and introduction
st.title("Welcome to the Emotional Clarity Project 🌟")
st.write("We're here to help you reflect on your feelings and guide you toward open communication.")
st.write("Let's take a moment to reflect on how you're feeling today.")

# First Question - Reflect on Emotional Attachment
attachment = st.radio(
    "Do you feel emotionally attached to someone right now?",
    ("Yes", "No", "Not sure")
)

if attachment == "Yes":
    st.write("It's important to recognize and honor those feelings. 🌱")
    st.write("But remember, being attached doesn’t always mean the relationship is right for you. Take a moment to reflect on what this attachment brings to your life. 💫")
elif attachment == "No":
    st.write("That’s perfectly okay. Not every connection leads to emotional attachment. 💭")
    st.write("It’s important to be honest with yourself and the other person about where you stand emotionally. 🛤️")
elif attachment == "Not sure":
    st.write("It's okay to feel uncertain. 💖")
    st.write("Sometimes, emotions are complex, and it’s worth giving yourself time to reflect without pressure. 🌷")

# Second Question - Are You Considering Ghosting?
ghosting = st.radio(
    "Are you thinking about pulling away or ghosting someone?",
    ("Yes", "No", "Maybe")
)

if ghosting == "Yes":
    st.write("Ghosting may seem easier, but it often leaves unresolved emotions for both sides. 🌫️")
    st.write("It’s usually better to communicate how you feel, even if it’s difficult. Being honest can bring closure and peace. 💬")
elif ghosting == "No":
    st.write("That’s great! Open communication is always a healthier option. 🗝️")
    st.write("It’s important to honor the other person’s feelings by being upfront, even if you’re unsure how you feel. 🌻")
elif ghosting == "Maybe":
    st.write("It’s normal to feel like avoiding difficult conversations, but clear communication often brings relief. 🛤️")
    st.write("Before making a decision, think about how you would feel if someone ghosted you. 💭 It’s usually best to express your feelings openly.")

# Third Question - Are You In Love or Is It Something Else?
in_love = st.radio(
    "Do you feel like you’re in love with this person, or is it something else?",
    ("Love", "Unsure", "Not really")
)

if in_love == "Love":
    st.write("That’s beautiful! ❤️ Love can be a powerful feeling, but make sure to communicate it openly and honestly. 💬")
    st.write("Remember, love is about understanding and connection, not fear or avoidance. Be brave in sharing your truth. 🌈")
elif in_love == "Unsure":
    st.write("It’s okay to be uncertain. 💭 Take your time to understand your feelings.")
    st.write("You don’t need to rush to a conclusion. Often, deep reflection or a conversation with the other person can bring clarity. 🛤️")
elif in_love == "Not really":
    st.write("That’s perfectly okay. Not every connection is about love, and that’s valid. 🌱")
    st.write("If you’re not in love, it’s important to communicate this so you don’t unintentionally lead the other person on. 🌷")

# Fourth Question - Fear of Hurting Others or Being Honest
fear_hurting = st.radio(
    "Do you feel like avoiding communication because you’re afraid of hurting the other person?",
    ("Yes", "No", "Maybe")
)

if fear_hurting == "Yes":
    st.write("It’s natural to fear hurting others. 🌿 But avoiding communication often leads to more hurt in the long run. 💔")
    st.write("By being open and honest, you’re showing respect for the other person’s emotions and allowing them to heal. 🛤️")
elif fear_hurting == "No":
    st.write("That’s a healthy mindset! 🗝️ Clear and open communication is always better than leaving someone in uncertainty. 🌞")
elif fear_hurting == "Maybe":
    st.write("It’s understandable to feel torn. 💭 But remember, honesty is kindness in the long run. 🌻")
    st.write("It’s better to express your feelings than to leave the other person wondering or hurt by silence. 🌿")

# Final Reflection - Encourage Healthy Communication
reflection = st.text_input("What’s something you want to express to the person you’ve been thinking about?")

if reflection:
    st.write(f"That’s a great start! Expressing **{reflection}** will help you and the other person reach a better understanding. 🌸")
    st.write("Remember, open and honest communication is key to forming healthy relationships and letting go of emotional attachments that don’t serve you. 💬")

# Closing
st.write("Thank you for joining the Emotional Clarity Project. 🌈 We hope this has helped you reflect and approach your feelings with honesty and compassion.")
