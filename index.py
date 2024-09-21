import streamlit as st

# Welcome message
st.title("Emotional Clarity Check 💖")
st.write("We’re here to help you reflect on your feelings and guide you toward open communication.")

# Start interaction
st.write("Let's begin...")

# First Question - Reflect on Emotional Attachment
attachment = st.text_input("Do you feel emotionally attached to someone right now? (yes/no/not sure): ").lower()

if attachment:
    if attachment == "yes":
        st.success("It's important to recognize and honor those feelings. 🌱")
        st.write("But remember, being attached doesn’t always mean the relationship is right for you. Reflect on what this attachment brings to your life. 💫")
        st.write("-" * 40)  # Line Separator
    elif attachment == "no":
        st.warning("That’s perfectly okay. Not every connection leads to emotional attachment. 💭")
        st.write("It’s important to be honest with yourself and the other person about where you stand emotionally. 🛤️")
        st.write("-" * 40)  # Line Separator
    elif attachment == "not sure":
        st.info("It's okay to feel uncertain. 💖")
        st.write("Sometimes, emotions are complex, and it’s worth giving yourself time to reflect without pressure. 🌷")
        st.write("-" * 40)  # Line Separator
    else:
        st.write("Hmm, I didn’t understand that, but let’s keep reflecting. 😊")
        st.write("-" * 40)  # Line Separator

    # Second Question only after first question is answered
    ghosting = st.text_input("Are you thinking about pulling away or ghosting someone? (yes/no/maybe): ").lower()

    if ghosting:
        if ghosting == "yes":
            st.warning("Ghosting may seem easier, but it often leaves unresolved emotions for both sides. 🌫️")
            st.write("It’s usually better to communicate how you feel, even if it’s difficult. Being honest can bring closure and peace. 💬")
            st.write("-" * 40)  # Line Separator
        elif ghosting == "no":
            st.success("That’s great! Open communication is always a healthier option. 🗝️")
            st.write("It’s important to honor the other person’s feelings by being upfront, even if you’re unsure how you feel. 🌻")
            st.write("-" * 40)  # Line Separator
        elif ghosting == "maybe":
            st.info("It’s normal to feel like avoiding difficult conversations, but clear communication often brings relief. 🛤️")
            st.write("Before making a decision, think about how you would feel if someone ghosted you. 💭 It’s usually best to express your feelings openly.")
            st.write("-" * 40)  # Line Separator
        else:
            st.write("Let’s keep exploring your feelings. 😊")
            st.write("-" * 40)  # Line Separator

        # Third Question only after second question is answered
        in_love = st.text_input("Do you feel like you’re in love with this person, or is it something else? (love/unsure/not really): ").lower()

        if in_love:
            if in_love == "love":
                st.success("That’s beautiful! ❤️ Love can be a powerful feeling, but make sure to communicate it openly and honestly. 💬")
                st.write("Remember, love is about understanding and connection, not fear or avoidance. Be brave in sharing your truth. 🌈")
                st.write("-" * 40)  # Line Separator
            elif in_love == "unsure":
                st.info("It’s okay to be uncertain. 💭 Take your time to understand your feelings.")
                st.write("You don’t need to rush to a conclusion. Deep reflection or a conversation with the other person can bring clarity. 🛤️")
                st.write("-" * 40)  # Line Separator
            elif in_love == "not really":
                st.warning("That’s perfectly okay. Not every connection is about love, and that’s valid. 🌱")
                st.write("If you’re not in love, it’s important to communicate this so you don’t unintentionally lead the other person on. 🌷")
                st.write("-" * 40)  # Line Separator
            else:
                st.write("That’s okay, emotions are complicated. Let’s keep reflecting. 😊")
                st.write("-" * 40)  # Line Separator

            # Final Reflection only after third question is answered
            reflection = st.text_input("What’s something you want to express to the person you’ve been thinking about?")

            if reflection:
                st.success(f"That’s a great start! Expressing {reflection} will help you and the other person reach a better understanding. 🌸")
                st.write("Open and honest communication is key to forming healthy relationships and letting go of emotional attachments that don’t serve you. 💬")
                st.write("-" * 40)  # Line Separator
                st.write("Thank you for joining the Emotional Clarity Check today. We hope you’ve found clarity and the courage to communicate openly. 💖")
