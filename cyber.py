import streamlit as st

# PAGE SETTINGS
st.set_page_config(
    page_title="Cyber Shield",
    page_icon="🛡️",
    layout="centered"
)

# DESIGN
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #07152e, #102d50);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
.stButton > button {
    background-color: #00c9a7;
    color: black;
    border-radius: 12px;
    font-weight: bold;
    height: 45px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    "<h1 style='text-align:center;'>🛡️ CYBER SHIELD</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>AI Cyber Safety Challenge</h3>",
    unsafe_allow_html=True
)

st.markdown("---")

# QUESTIONS
questions = [
    {
        "question": "You receive a message saying you won ₹50,000. It asks you to click an unknown link. What will you do?",
        "options": [
            "Click the link immediately",
            "Ignore the message and verify it",
            "Share it with friends"
        ],
        "answer": "Ignore the message and verify it",
        "tip": "Avoid unknown links. Verify prize messages through official sources."
    },
    {
        "question": "Which is the safest password choice?",
        "options": [
            "123456",
            "password123",
            "A long and unique password"
        ],
        "answer": "A long and unique password",
        "tip": "Use long, unique passwords and a password manager if available."
    },
    {
        "question": "Someone emails you asking for your OTP. What should you do?",
        "options": [
            "Share the OTP",
            "Ignore and report the request",
            "Send your password too"
        ],
        "answer": "Ignore and report the request",
        "tip": "Never share your OTP with anyone."
    },
    {
        "question": "An unknown person online asks for your home address. What should you do?",
        "options": [
            "Share your address",
            "Share your phone number",
            "Don't share personal information"
        ],
        "answer": "Don't share personal information",
        "tip": "Keep your personal information private."
    },
    {
        "question": "You see someone being bullied online. What is the best action?",
        "options": [
            "Join the bullying",
            "Save evidence and report it to a trusted adult or platform",
            "Share the bullying post"
        ],
        "answer": "Save evidence and report it to a trusted adult or platform",
        "tip": "Don't participate in cyberbullying. Report it and seek trusted support."
    },
    {
        "question": "How can you make your online accounts safer?",
        "options": [
            "Enable two-factor authentication",
            "Share passwords with friends",
            "Use the same password everywhere"
        ],
        "answer": "Enable two-factor authentication",
        "tip": "Enable two-factor authentication whenever possible."
    },
    {
        "question": "You find a website asking for unnecessary personal details. What should you do?",
        "options": [
            "Enter all your details",
            "Check whether the website is trustworthy",
            "Share your OTP"
        ],
        "answer": "Check whether the website is trustworthy",
        "tip": "Check website addresses carefully and avoid suspicious websites."
    },
    {
        "question": "A stranger sends you an unexpected file. What should you do?",
        "options": [
            "Open it immediately",
            "Forward it to everyone",
            "Don't open it; verify the sender"
        ],
        "answer": "Don't open it; verify the sender",
        "tip": "Unexpected files can be unsafe. Verify the sender first."
    },
    {
        "question": "Someone creates a fake social media account using your photo. What should you do?",
        "options": [
            "Ignore it forever",
            "Report the fake account and tell a trusted adult",
            "Send them your password"
        ],
        "answer": "Report the fake account and tell a trusted adult",
        "tip": "Report impersonation and secure your account."
    },
    {
        "question": "What should you do when using public Wi-Fi?",
        "options": [
            "Access sensitive accounts without checking security",
            "Share your passwords",
            "Avoid sensitive activities on untrusted networks"
        ],
        "answer": "Avoid sensitive activities on untrusted networks",
        "tip": "Be careful with public Wi-Fi. Avoid sensitive transactions on untrusted networks."
    }
]

# SESSION STATE
if "started" not in st.session_state:
    st.session_state.started = False

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# HOME PAGE
if not st.session_state.started:

    st.success("Welcome to the Cyber Shield Challenge!")

    name = st.text_input("👤 Enter your name")
    college = st.text_input("🏫 Enter your college name")
    department = st.text_input("🎓 Enter your department")

    if st.button("🚀 START CHALLENGE"):

        if name.strip() and college.strip() and department.strip():

            st.session_state.name = name
            st.session_state.college = college
            st.session_state.department = department
            st.session_state.started = True

            st.rerun()

        else:
            st.warning("Please fill in all the details.")

# QUIZ PAGE
elif not st.session_state.submitted:

    st.subheader("🧠 Test Your Cyber Safety Knowledge!")

    st.write("Choose the correct answer for each question.")

    with st.form("cyber_quiz"):

        answers = []

        for i, q in enumerate(questions):

            st.markdown(f"### Question {i + 1}")
            st.write(q["question"])

            selected = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"question_{i}"
            )

            answers.append(selected)

            st.markdown("---")

        submitted = st.form_submit_button("🏆 SUBMIT CHALLENGE")

    if submitted:

        score = 0
        wrong_answers = []

        for i, q in enumerate(questions):

            if answers[i] == q["answer"]:
                score += 1
            else:
                wrong_answers.append(q["tip"])

        st.session_state.score = score
        st.session_state.wrong_answers = wrong_answers
        st.session_state.submitted = True

        st.rerun()

# RESULT PAGE
if st.session_state.started and st.session_state.submitted:

    score = st.session_state.score

    st.balloons()

    st.markdown(
        "<h1 style='text-align:center;'>🏆 CHALLENGE COMPLETED!</h1>",
        unsafe_allow_html=True
    )

    st.write(f"### 👤 Name: {st.session_state.name}")
    st.write(f"🏫 College: {st.session_state.college}")
    st.write(f"🎓 Department: {st.session_state.department}")

    st.markdown("---")

    st.metric("YOUR SCORE", f"{score}/10")

    percentage = score * 10

    st.progress(percentage)

    if score >= 8:
        st.success("🟢 CYBER SAFETY LEVEL: EXPERT!")
        st.write("Excellent! You have strong cyber safety knowledge.")

    elif score >= 5:
        st.info("🟡 CYBER SAFETY LEVEL: GOOD!")
        st.write("Good job! Keep learning about online safety.")

    else:
        st.warning("🔴 CYBER SAFETY LEVEL: BEGINNER")
        st.write("Keep practicing. You can improve your cyber safety knowledge!")

    st.markdown("---")

    st.subheader("📚 YOUR PERSONALIZED SAFETY TIPS")

    if len(st.session_state.wrong_answers) == 0:
        st.success("Perfect! You answered every question correctly.")

    else:
        for tip in st.session_state.wrong_answers:
            st.write("💡", tip)

    st.markdown("---")

    st.markdown(
        "<h2 style='text-align:center;'>🛡️ CYBER SHIELD</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>CERTIFICATE OF COMPLETION</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h3 style='text-align:center;'>Congratulations, "
        f"{st.session_state.name}!</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>You successfully completed "
        "the AI Cyber Safety Challenge.</p>",
        unsafe_allow_html=True
    )

    if st.button("🔄 PLAY AGAIN"):

        st.session_state.started = False
        st.session_state.submitted = False

        st.rerun()

st.markdown("---")

st.markdown(
    "<p style='text-align:center;'>Made with ❤️ for College Expo</p>",
    unsafe_allow_html=True
)