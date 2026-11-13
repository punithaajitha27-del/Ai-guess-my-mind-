import streamlit as st
import random

st.set_page_config(
    page_title="AI Guess My Mind",
    page_icon="🧠",
    layout="centered"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55, #1a2a6c);
    color: white;
}
h1 {
    color: #00ffff;
    text-align: center;
    text-shadow: 0 0 15px #00ffff;
}
h2, h3 { color: #ffd166; }
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
    font-size: 18px;
    border: 2px solid #00ffff;
}
.score-box {
    background: rgba(255,255,255,0.1);
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
# Each topic: questions (text, options) and items (name -> answers in same order)
TOPICS = {
    "🐾 Animals": {
        "questions": [
            ("🌳 Is it wild or domestic?", ["Wild", "Domestic"]),
            ("🏞️ Where does it live?", ["Land", "Water", "Air"]),
            ("📏 Is it big or small?", ["Big", "Small"]),
        ],
        "items": {
            "🦁 Lion": ["Wild", "Land", "Big"],
            "🐯 Tiger": ["Wild", "Land", "Big"],
            "🐘 Elephant": ["Wild", "Land", "Big"],
            "🐶 Dog": ["Domestic", "Land", "Small"],
            "🐱 Cat": ["Domestic", "Land", "Small"],
            "🐰 Rabbit": ["Domestic", "Land", "Small"],
            "🐄 Cow": ["Domestic", "Land", "Big"],
            "🦅 Eagle": ["Wild", "Air", "Big"],
            "🦜 Parrot": ["Domestic", "Air", "Small"],
            "🦈 Shark": ["Wild", "Water", "Big"],
            "🐠 Fish": ["Domestic", "Water", "Small"],
        },
    },
    "🍎 Fruits": {
        "questions": [
            ("🎨 What is its colour?", ["Red", "Yellow", "Green", "Orange", "Purple"]),
            ("👅 How does it taste?", ["Sweet", "Sour"]),
            ("📏 Is it big or small?", ["Big", "Small"]),
        ],
        "items": {
            "🍎 Apple": ["Red", "Sweet", "Small"],
            "🍌 Banana": ["Yellow", "Sweet", "Small"],
            "🥭 Mango": ["Yellow", "Sweet", "Big"],
            "🍉 Watermelon": ["Green", "Sweet", "Big"],
            "🍋 Lemon": ["Yellow", "Sour", "Small"],
            "🍊 Orange": ["Orange", "Sweet", "Small"],
            "🍇 Grapes": ["Purple", "Sweet", "Small"],
            "🍓 Strawberry": ["Red", "Sour", "Small"],
            "🍍 Pineapple": ["Yellow", "Sour", "Big"],
            "🥝 Kiwi": ["Green", "Sour", "Small"],
        },
    },
    "🚗 Vehicles": {
        "questions": [
            ("🛣️ Where does it travel?", ["Road", "Air", "Water", "Rail"]),
            ("🛞 How many wheels?", ["Two wheels", "Many wheels", "No wheels"]),
            ("📏 Is it big or small?", ["Big", "Small"]),
        ],
        "items": {
            "🏍️ Bike": ["Road", "Two wheels", "Small"],
            "🚲 Cycle": ["Road", "Two wheels", "Small"],
            "🚗 Car": ["Road", "Many wheels", "Small"],
            "🚌 Bus": ["Road", "Many wheels", "Big"],
            "🚚 Lorry": ["Road", "Many wheels", "Big"],
            "✈️ Aeroplane": ["Air", "Many wheels", "Big"],
            "🚁 Helicopter": ["Air", "No wheels", "Small"],
            "🚢 Ship": ["Water", "No wheels", "Big"],
            "🛶 Boat": ["Water", "No wheels", "Small"],
            "🚆 Train": ["Rail", "Many wheels", "Big"],
        },
    },
    "⚽ Sports": {
        "questions": [
            ("🏟️ Where is it played?", ["Ground", "Indoor", "Water"]),
            ("👥 Team or single player?", ["Team", "Single"]),
            ("⚪ Is a ball used?", ["Ball", "No ball"]),
        ],
        "items": {
            "🏏 Cricket": ["Ground", "Team", "Ball"],
            "⚽ Football": ["Ground", "Team", "Ball"],
            "🏑 Hockey": ["Ground", "Team", "Ball"],
            "🤼 Kabaddi": ["Ground", "Team", "No ball"],
            "🏀 Basketball": ["Indoor", "Team", "Ball"],
            "🎾 Tennis": ["Indoor", "Single", "Ball"],
            "♟️ Chess": ["Indoor", "Single", "No ball"],
            "🏊 Swimming": ["Water", "Single", "No ball"],
            "🏃 Running": ["Ground", "Single", "No ball"],
        },
    },
    "🍕 Foods": {
        "questions": [
            ("🥗 Veg or Non-veg?", ["Veg", "Non-veg"]),
            ("👅 Sweet or Spicy?", ["Sweet", "Spicy"]),
            ("🍽️ Snack or Main meal?", ["Snack", "Main meal"]),
        ],
        "items": {
            "🍕 Pizza": ["Veg", "Spicy", "Snack"],
            "🥟 Samosa": ["Veg", "Spicy", "Snack"],
            "🍦 Ice Cream": ["Veg", "Sweet", "Snack"],
            "🍩 Gulab Jamun": ["Veg", "Sweet", "Snack"],
            "🥞 Dosa": ["Veg", "Spicy", "Main meal"],
            "🍚 Payasam Meal": ["Veg", "Sweet", "Main meal"],
            "🍗 Fried Chicken": ["Non-veg", "Spicy", "Snack"],
            "🍛 Chicken Biryani": ["Non-veg", "Spicy", "Main meal"],
            "🐟 Fish Curry": ["Non-veg", "Spicy", "Main meal"],
        },
    },
}

# ---------- SESSION STATE ----------
defaults = {
    "result": None,
    "answered": False,
    "verdict": "",
    "ai_score": 0,
    "user_score": 0,
    "celebrate": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def reset_round():
    st.session_state.result = None
    st.session_state.answered = False
    st.session_state.verdict = ""


def do_guess(topic):
    data = TOPICS[topic]
    answers = [
        st.session_state[f"{topic}_q{i}"]
        for i in range(len(data["questions"]))
    ]
    possible = [n for n, feat in data["items"].items() if feat == answers]

    st.session_state.answered = False
    st.session_state.verdict = ""

    if possible:
        st.session_state.result = random.choice(possible)
    else:
        st.session_state.result = "Unknown"
        st.session_state.user_score += 1
        st.session_state.answered = True
        st.session_state.verdict = "user_unknown"
        st.session_state.celebrate = True


def submit_answer():
    if st.session_state.feedback == "✅ Yes":
        st.session_state.ai_score += 1
        st.session_state.verdict = "ai"
    else:
        st.session_state.user_score += 1
        st.session_state.verdict = "user"
    st.session_state.answered = True
    st.session_state.celebrate = True


# ---------- UI ----------
st.title("🧠 AI GUESS MY MIND 🔮")
st.subheader("🤖 Can I read your mind?")
st.write("✨ Pick a topic, think of something, and let AI guess it!")

# Scoreboard
c1, c2 = st.columns(2)
c1.markdown(
    f"<div class='score-box'>🤖 AI Score<br><b>{st.session_state.ai_score}</b></div>",
    unsafe_allow_html=True,
)
c2.markdown(
    f"<div class='score-box'>🧑 Your Score<br><b>{st.session_state.user_score}</b></div>",
    unsafe_allow_html=True,
)

st.markdown("---")

topic = st.selectbox(
    "🎯 Choose a Topic",
    list(TOPICS.keys()),
    key="topic",
    on_change=reset_round,
)

st.info(f"💭 Think of something in **{topic}** and answer the questions below 👇")

for i, (q, options) in enumerate(TOPICS[topic]["questions"]):
    st.radio(
        f"{i + 1}. {q}",
        options,
        key=f"{topic}_q{i}",
        horizontal=True,
        on_change=reset_round,
    )

st.button("🔮 GUESS MY MIND", on_click=do_guess, args=(topic,))

# ---------- RESULT ----------
if st.session_state.result:
    st.markdown("---")
    st.subheader("🤖 AI Prediction:")

    if st.session_state.result != "Unknown":
        st.success(f"🎯 I think it is **{st.session_state.result}**!")

        if not st.session_state.answered:
            st.radio(
                "❓ Did I guess correctly?",
                ["✅ Yes", "❌ No"],
                key="feedback",
                horizontal=True,
            )
            st.button("📩 Submit Answer", on_click=submit_answer)

    if st.session_state.verdict == "ai":
        st.success("🎉🤖 AI WON! I read your mind!")
    elif st.session_state.verdict == "user":
        st.info("🏆🧑 YOU WON! You defeated the AI!")
    elif st.session_state.verdict == "user_unknown":
        st.warning("😵 I couldn't guess! 🏆 YOU defeated the AI!")

    if st.session_state.celebrate:
        st.balloons()
        st.session_state.celebrate = False

st.button("🔄 PLAY AGAIN", on_click=reset_round)

st.markdown("---")
st.caption("🎓 Created for College Expo | AI & DS Department")