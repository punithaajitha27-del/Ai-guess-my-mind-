import streamlit as st
import random

st.set_page_config(
    page_title="Cyber Shield",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CSS DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #160047,
        #3b087c,
        #075985,
        #111827
    );
    background-attachment: fixed;
}

h1, h2, h3, p, label {
    color: white !important;
}

.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

/* BUTTON DESIGN */

.stButton > button {
    background: linear-gradient(90deg, #ff4ecd, #7c4dff);
    color: white !important;
    border: none;
    border-radius: 15px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.04);
    background: linear-gradient(90deg, #00e5ff, #00c853);
}

/* INPUT BOX */

.stTextInput input {
    border-radius: 12px;
}

/* RADIO OPTIONS */

.stRadio {
    background: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 15px;
}

/* ANIMATED CHARACTERS */

@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(10deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes glow {
    0% { text-shadow: 0 0 5px #00e5ff; }
    50% { text-shadow: 0 0 25px #ff4ecd; }
    100% { text-shadow: 0 0 5px #00e5ff; }
}

.cartoon {
    font-size: 48px;
    display: inline-block;
    animation: float 3s ease-in-out infinite;
    margin: 10px;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    animation: glow 2s infinite;
}

.subtitle {
    text-align: center;
    font-size: 22px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- CARTOON CHARACTERS ----------------

st.markdown("""
<div style="text-align:center;">
    <span class="cartoon">🤖</span>
    <span class="cartoon">🦸</span>
    <span class="cartoon">🛡️</span>
    <span class="cartoon">👾</span>
    <span class="cartoon">🦹</span>
</div>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<div class="title">🛡️ CYBER SHIELD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✨ AI Cyber Safety Challenge ✨</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ---------------- QUESTION BANK ----------------

question_bank = [

    {
        "question": "You receive a message saying you won ₹50,000. It asks you to click an unknown link. What will you do?",
        "options": [
            "Click the link",
            "Ignore and verify the message",
            "Share it with friends"
        ],
        "answer": "Ignore and verify the message",
        "tip": "Never trust unexpected prize messages. Verify them through official sources."
    },

    {
        "question": "Which is the safest password?",
        "options": [
            "123456",
            "password123",
            "A long and unique password"
        ],
        "answer": "A long and unique password",
        "tip": "Use long, unique passwords for your accounts."
    },

    {
        "question": "Someone asks for your OTP through a phone call. What should you do?",
        "options": [
            "Share the OTP",
            "Never share the OTP",
            "Send your password"
        ],
        "answer": "Never share the OTP",
        "tip": "Your OTP is private. Never share it with anyone."
    },

    {
        "question": "An unknown person asks for your home address online. What should you do?",
        "options": [
            "Share your address",
            "Share your phone number",
            "Keep personal information private"
        ],
        "answer": "Keep personal information private",
        "tip": "Never share private details with strangers online."
    },

    {
        "question": "What should you do if someone bullies you online?",
        "options": [
            "Join the bullying",
            "Report it and tell a trusted adult",
            "Share the post"
        ],
        "answer": "Report it and tell a trusted adult",
        "tip": "Report cyberbullying and seek help from a trusted adult."
    },

    {
        "question": "How can you make your account safer?",
        "options": [
            "Enable two-factor authentication",
            "Share your password",
            "Use the same password everywhere"
        ],
        "answer": "Enable two-factor authentication",
        "tip": "Two-factor authentication adds an extra layer of security."
    },

    {
        "question": "You receive an unexpected file from a stranger. What should you do?",
        "options": [
            "Open it immediately",
            "Forward it",
            "Don't open it; verify the sender"
        ],
        "answer": "Don't open it; verify the sender",
        "tip": "Unexpected files may be unsafe. Verify the sender first."
    },

    {
        "question": "Someone creates a fake account using your photo. What should you do?",
        "options": [
            "Ignore it",
            "Report the account",
            "Give them your password"
        ],
        "answer": "Report the account",
        "tip": "Report fake accounts and inform a trusted adult."
    },

    {
        "question": "What should you do when using public Wi-Fi?",
        "options": [
            "Share passwords",
            "Avoid sensitive activities on untrusted networks",
            "Access every unknown website"
        ],
        "answer": "Avoid sensitive activities on untrusted networks",
        "tip": "Be careful when using public Wi-Fi."
    },

    {
        "question": "What is phishing?",
        "options": [
            "A type of online scam",
            "A computer game",
            "A social media app"
        ],
        "answer": "A type of online scam",
        "tip": "Phishing tricks people into revealing private information."
    },

    {
        "question": "Should you use the same password for every account?",
        "options": [
            "Yes",
            "No, use different passwords",
            "Only for social media"
        ],
        "answer": "No, use different passwords",
        "tip": "Use a different password for each important account."
    },

    {
        "question": "You see a suspicious website asking for your bank details. What should you do?",
        "options": [
            "Enter the details",
            "Close the website and verify it",
            "Share your OTP"
        ],
        "answer": "Close the website and verify it",
        "tip": "Never enter sensitive details on suspicious websites."
    },

    {
        "question": "What should you do before downloading an app?",
        "options": [
            "Check its source and permissions",
            "Download from any unknown link",
            "Ignore all warnings"
        ],
        "answer": "Check its source and permissions",
        "tip": "Download apps from trusted sources and review permissions."
    },

    {
        "question": "A stranger sends you a suspicious QR code. What should you do?",
        "options": [
            "Scan it immediately",
            "Verify its source first",
            "Send it to everyone"
        ],
        "answer": "Verify its source first",
        "tip": "Check who sent a QR code before scanning it."
    },

    {
        "question": "What should you do with your social media privacy settings?",
        "options": [
            "Review and manage them",
            "Make everything public",
            "Share your login details"
        ],
        "answer": "Review and manage them",
        "tip": "Review privacy settings regularly."
    },

    {
        "question": "You receive a suspicious email from someone pretending to be your bank. What should you do?",
        "options": [
            "Click its link",
            "Reply with bank details",
            "Contact the bank through its official channel"
        ],
        "answer": "Contact the bank through its official channel",
        "tip": "Contact your bank using its official app or phone number."
    },

    {
        "question": "What is two-factor authentication?",
        "options": [
            "An extra account security step",
            "A type of computer virus",
            "A social media filter"
        ],
        "answer": "An extra account security step",
        "tip": "Two-factor authentication helps protect your account."
    },

    {
        "question": "Someone asks you to install an unknown app to receive a prize. What should you do?",
        "options": [
            "Install it immediately",
            "Avoid it and verify the offer",
            "Give the person your OTP"
        ],
        "answer": "Avoid it and verify the offer",
        "tip": "Don't install unknown apps just because someone promises a prize."
    },

    {
        "question": "What should you do if you accidentally share your password?",
        "options": [
            "Do nothing",
            "Change it immediately and secure your account",
            "Share it again"
        ],
        "answer": "Change it immediately and secure your account",
        "tip": "Change compromised passwords immediately and enable extra security."
    },

    {
        "question": "Which information should you avoid sharing publicly?",
        "options": [
            "Your OTP and passwords",
            "A general hobby",
            "A favorite movie"
        ],
        "answer": "Your OTP and passwords",
        "tip": "Keep passwords, OTPs and sensitive personal information private."
    }
]


# ---------------- SESSION STATE ----------------

if "started" not in st.session_state:
    st.session_state.started = False

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "last_questions" not in st.session_state:
    st.session_state.last_questions = []


def start_new_round():

    # Avoid repeating the exact same set in consecutive rounds
    available = [
        q for q in question_bank
        if q["question"] not in st.session_state.last_questions
    ]

    if len(available) < 10:
        available = question_bank.copy()

    selected = random.sample(available, 10)

    st.session_state.questions = selected

    st.session_state.last_questions = [
        q["question"] for q in selected
    ]

    st.session_state.started = True
    st.session_state.submitted = False


# ---------------- HOME PAGE ----------------

if not st.session_state.started:

    st.markdown(
        "<h2 style='text-align:center;'>🎮 WELCOME, CYBER HERO!</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>"
        "Are you ready to defeat online scams?"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("### 👤 Enter Your Details")

    name = st.text_input("Your Name")
    college = st.text_input("College Name")
    department = st.text_input("Department")

    st.markdown("### 🌟 Your Mission")
    st.info(
        "Answer 10 cyber safety questions, earn points, "
        "and become a Cyber Safety Hero!"
    )

    if st.button("🚀 START CHALLENGE"):

        if name.strip() and college.strip() and department.strip():

            st.session_state.name = name
            st.session_state.college = college
            st.session_state.department = department

            start_new_round()
            st.rerun()

        else:
            st.warning("Please fill in all details.")


# ---------------- QUIZ PAGE ----------------

elif not st.session_state.submitted:

    st.markdown(
        "<h2 style='text-align:center;'>⚡ CYBER HERO QUIZ ⚡</h2>",
        unsafe_allow_html=True
    )

    st.write(f"👋 Welcome, {st.session_state.name}!")

    st.progress(0.1)

    questions = st.session_state.questions

    with st.form("quiz_form"):

        answers = []

        for i, q in enumerate(questions):

            st.markdown(f"### 🟣 Question {i + 1}/10")

            st.write(q["question"])

            selected = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"answer_{i}"
            )

            answers.append(selected)

            st.markdown("---")

        submit = st.form_submit_button("🏆 SUBMIT ANSWERS")

    if submit:

        score = 0
        tips = []

        for i, q in enumerate(questions):

            if answers[i] == q["answer"]:
                score += 1
            else:
                tips.append(q["tip"])

        st.session_state.score = score
        st.session_state.tips = tips
        st.session_state.submitted = True

        st.rerun()


# ---------------- RESULT PAGE ----------------

if st.session_state.started and st.session_state.submitted:

    score = st.session_state.score

    st.balloons()

    st.markdown(
        "<h1 style='text-align:center;'>🎉 AMAZING WORK! 🎉</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='text-align:center;font-size:60px;'>"
        "🦸 🤖 🏆 🛡️"
        "</div>",
        unsafe_allow_html=True
    )

    st.write(f"### 👤 Name: {st.session_state.name}")
    st.write(f"🏫 College: {st.session_state.college}")
    st.write(f"🎓 Department: {st.session_state.department}")

    st.markdown("---")

    st.metric("🏆 YOUR SCORE", f"{score}/10")

    st.progress(score / 10)

    if score >= 8:

        st.success("🟢 CYBER HERO LEVEL: EXPERT!")
        st.write("Excellent! You are a Cyber Safety Champion!")

    elif score >= 5:

        st.info("🟡 CYBER HERO LEVEL: GOOD!")
        st.write("Good work! Keep learning and improving.")

    else:

        st.warning("🔴 CYBER HERO LEVEL: BEGINNER")
        st.write("Keep practicing. You can become a Cyber Hero!")

    st.markdown("---")

    st.subheader("💡 YOUR PERSONALIZED SAFETY TIPS")

    if not st.session_state.tips:

        st.success("Perfect! All your answers are correct!")

    else:

        for tip in st.session_state.tips:
            st.write("✨", tip)

    st.markdown("---")

    st.markdown(
        "<div style='text-align:center;'>"
        "<h1>📜 CERTIFICATE</h1>"
        "<h2>CYBER SHIELD</h2>"
        "<h3>Certificate of Completion</h3>"
        "<p>Congratulations!</p>"
        "<h2>" + st.session_state.name + "</h2>"
        "<p>Successfully completed the Cyber Safety Challenge.</p>"
        "<h2>🛡️ CYBER HERO 🛡️</h2>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    if st.button("🔄 PLAY AGAIN - NEW QUESTIONS"):

        start_new_round()
        st.rerun()


# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<p style='text-align:center;'>"
    "🌈 CYBER SHIELD | Stay Safe • Stay Smart • Stay Protected 🛡️"
    "</p>",
    unsafe_allow_html=True
)