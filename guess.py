import streamlit as st
import random

st.set_page_config(
    page_title="AI Guess My Mind",
    page_icon="🧠",
    layout="centered"
)

# ---------- COLOURFUL STYLE ----------
st.markdown("""
<style>
@keyframes gradientMove {
    0%   {background-position: 0% 50%;}
    50%  {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stApp {
    background: linear-gradient(-45deg, #ff4e8a, #7b2ff7, #00c6ff, #11998e);
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
    color: white;
}
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #fff200, #ff9a00, #ff3cac, #00f5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #ffffff;
    margin-bottom: 15px;
}
h2, h3 { color: #fff200 !important; }

/* Question cards */
div[data-testid="stRadio"] {
    background: rgba(0, 0, 0, 0.35);
    padding: 12px 14px;
    border-radius: 14px;
    border-left: 6px solid #fff200;
    margin-bottom: 8px;
}
div[data-testid="stRadio"] label p,
div[data-testid="stRadio"] p {
    color: #ffffff !important;
    font-weight: 600;
}
div[data-testid="stSelectbox"] label p {
    color: #ffffff !important;
    font-weight: 700;
    font-size: 18px;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    border-radius: 14px;
    font-weight: 800;
    font-size: 19px;
    padding: 10px;
    color: white;
    border: none;
    background: linear-gradient(90deg, #ff512f, #f09819);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    transition: transform 0.15s;
}
div.stButton > button:hover {
    transform: scale(1.04);
    color: white;
    background: linear-gradient(90deg, #f09819, #ff512f);
}

/* Score boxes */
.score-ai, .score-user, .score-round {
    padding: 12px;
    border-radius: 14px;
    text-align: center;
    font-size: 16px;
    color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
.score-ai    {background: linear-gradient(135deg, #8e2de2, #4a00e0);}
.score-user  {background: linear-gradient(135deg, #f7971e, #ffd200); color:#222;}
.score-round {background: linear-gradient(135deg, #00b09b, #96c93d);}
.score-ai b, .score-user b, .score-round b {font-size: 26px;}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
# questions: (text, options)
# items: name -> answers in the same order as the questions
TOPICS = {
    "🐾 Animals": {
        "questions": [
            ("🌳 Is it wild or domestic?", ["Wild", "Domestic"]),
            ("🏞️ Where does it live?", ["Land", "Water", "Air"]),
            ("📏 Is it big or small?", ["Big", "Small"]),
            ("🍖 What does it eat?", ["Plants 🌿", "Meat 🥩", "Both 🍽️"]),
            ("🦵 How many legs?", ["Four legs", "Two legs", "No legs"]),
        ],
        "items": {
            "🦁 Lion": ["Wild", "Land", "Big", "Meat 🥩", "Four legs"],
            "🐯 Tiger": ["Wild", "Land", "Big", "Meat 🥩", "Four legs"],
            "🐘 Elephant": ["Wild", "Land", "Big", "Plants 🌿", "Four legs"],
            "🐶 Dog": ["Domestic", "Land", "Small", "Both 🍽️", "Four legs"],
            "🐱 Cat": ["Domestic", "Land", "Small", "Meat 🥩", "Four legs"],
            "🐰 Rabbit": ["Domestic", "Land", "Small", "Plants 🌿", "Four legs"],
            "🐄 Cow": ["Domestic", "Land", "Big", "Plants 🌿", "Four legs"],
            "🐒 Monkey": ["Wild", "Land", "Small", "Both 🍽️", "Four legs"],
            "🐍 Snake": ["Wild", "Land", "Small", "Meat 🥩", "No legs"],
            "🦚 Peacock": ["Wild", "Land", "Big", "Both 🍽️", "Two legs"],
            "🦅 Eagle": ["Wild", "Air", "Big", "Meat 🥩", "Two legs"],
            "🦜 Parrot": ["Domestic", "Air", "Small", "Plants 🌿", "Two legs"],
            "🦈 Shark": ["Wild", "Water", "Big", "Meat 🥩", "No legs"],
            "🐬 Dolphin": ["Wild", "Water", "Big", "Meat 🥩", "No legs"],
            "🐠 Fish": ["Domestic", "Water", "Small", "Plants 🌿", "No legs"],
        },
    },
    "🍎 Fruits": {
        "questions": [
            ("🎨 What is its colour?", ["Red", "Yellow", "Green", "Orange", "Purple"]),
            ("👅 How does it taste?", ["Sweet", "Sour"]),
            ("📏 Is it big or small?", ["Big", "Small"]),
            ("🌱 Where does it grow?", ["Tree 🌳", "Plant 🌿", "Creeper 🍃"]),
            ("🧃 How do you eat it?", ["With skin", "Peel it"]),
        ],
        "items": {
            "🍎 Apple": ["Red", "Sweet", "Small", "Tree 🌳", "With skin"],
            "🍌 Banana": ["Yellow", "Sweet", "Small", "Plant 🌿", "Peel it"],
            "🥭 Mango": ["Yellow", "Sweet", "Big", "Tree 🌳", "Peel it"],
            "🍉 Watermelon": ["Green", "Sweet", "Big", "Creeper 🍃", "Peel it"],
            "🍋 Lemon": ["Yellow", "Sour", "Small", "Tree 🌳", "Peel it"],
            "🍊 Orange": ["Orange", "Sweet", "Small", "Tree 🌳", "Peel it"],
            "🍇 Grapes": ["Purple", "Sweet", "Small", "Creeper 🍃", "With skin"],
            "🍓 Strawberry": ["Red", "Sour", "Small", "Plant 🌿", "With skin"],
            "🍍 Pineapple": ["Yellow", "Sour", "Big", "Plant 🌿", "Peel it"],
            "🥝 Kiwi": ["Green", "Sour", "Small", "Creeper 🍃", "Peel it"],
            "🍈 Guava": ["Green", "Sweet", "Small", "Tree 🌳", "With skin"],
            "🧡 Papaya": ["Orange", "Sweet", "Big", "Tree 🌳", "Peel it"],
            "❤️ Pomegranate": ["Red", "Sweet", "Small", "Tree 🌳", "Peel it"],
        },
    },
    "🚗 Vehicles": {
        "questions": [
            ("🛣️ Where does it travel?", ["Road", "Air", "Water", "Rail"]),
            ("🛞 How many wheels?", ["Two wheels", "Many wheels", "No wheels"]),
            ("📏 Is it big or small?", ["Big", "Small"]),
            ("⚡ What powers it?", ["Fuel ⛽", "Electricity 🔌", "Human power 💪"]),
            ("🧍 What does it carry?", ["Few people", "Many people", "Goods 📦"]),
        ],
        "items": {
            "🏍️ Bike": ["Road", "Two wheels", "Small", "Fuel ⛽", "Few people"],
            "🛵 Electric Scooter": ["Road", "Two wheels", "Small", "Electricity 🔌", "Few people"],
            "🚲 Cycle": ["Road", "Two wheels", "Small", "Human power 💪", "Few people"],
            "🚗 Car": ["Road", "Many wheels", "Small", "Fuel ⛽", "Few people"],
            "🚌 Bus": ["Road", "Many wheels", "Big", "Fuel ⛽", "Many people"],
            "🚚 Lorry": ["Road", "Many wheels", "Big", "Fuel ⛽", "Goods 📦"],
            "✈️ Aeroplane": ["Air", "Many wheels", "Big", "Fuel ⛽", "Many people"],
            "🚁 Helicopter": ["Air", "No wheels", "Small", "Fuel ⛽", "Few people"],
            "🚢 Ship": ["Water", "No wheels", "Big", "Fuel ⛽", "Many people"],
            "🛶 Boat": ["Water", "No wheels", "Small", "Human power 💪", "Few people"],
            "🚆 Train": ["Rail", "Many wheels", "Big", "Electricity 🔌", "Many people"],
            "🚇 Metro": ["Rail", "Many wheels", "Big", "Electricity 🔌", "Many people"],
        },
    },
    "⚽ Sports": {
        "questions": [
            ("🏟️ Where is it played?", ["Open ground", "Indoor", "Water"]),
            ("👥 Team or single player?", ["Team", "Single"]),
            ("⚪ Is a ball used?", ["Ball", "No ball"]),
            ("🎒 Main equipment?", ["Bat / Racket", "Stick", "Only body", "Board / Table"]),
            ("🔋 Energy level?", ["High energy 🔥", "Calm & thinking 🧘"]),
        ],
        "items": {
            "🏏 Cricket": ["Open ground", "Team", "Ball", "Bat / Racket", "High energy 🔥"],
            "⚽ Football": ["Open ground", "Team", "Ball", "Only body", "High energy 🔥"],
            "🏑 Hockey": ["Open ground", "Team", "Ball", "Stick", "High energy 🔥"],
            "🤼 Kabaddi": ["Open ground", "Team", "No ball", "Only body", "High energy 🔥"],
            "🏀 Basketball": ["Indoor", "Team", "Ball", "Only body", "High energy 🔥"],
            "🏐 Volleyball": ["Indoor", "Team", "Ball", "Only body", "High energy 🔥"],
            "🎾 Tennis": ["Open ground", "Single", "Ball", "Bat / Racket", "High energy 🔥"],
            "🏓 Table Tennis": ["Indoor", "Single", "Ball", "Bat / Racket", "High energy 🔥"],
            "🏸 Badminton": ["Indoor", "Single", "No ball", "Bat / Racket", "High energy 🔥"],
            "♟️ Chess": ["Indoor", "Single", "No ball", "Board / Table", "Calm & thinking 🧘"],
            "🎯 Carrom": ["Indoor", "Single", "No ball", "Board / Table", "Calm & thinking 🧘"],
            "🏊 Swimming": ["Water", "Single", "No ball", "Only body", "High energy 🔥"],
            "🏃 Running": ["Open ground", "Single", "No ball", "Only body", "High energy 🔥"],
        },
    },
    "🍕 Foods": {
        "questions": [
            ("🥗 Veg or Non-veg?", ["Veg", "Non-veg"]),
            ("👅 Sweet or Spicy?", ["Sweet", "Spicy"]),
            ("🍽️ Snack or Main meal?", ["Snack / Dessert", "Main meal"]),
            ("🌡️ Hot or Cold?", ["Hot 🔥", "Cold ❄️"]),
            ("🌏 Where is it from?", ["Indian 🇮🇳", "Foreign 🌍"]),
        ],
        "items": {
            "🍕 Pizza": ["Veg", "Spicy", "Snack / Dessert", "Hot 🔥", "Foreign 🌍"],
            "🍔 Burger": ["Veg", "Spicy", "Snack / Dessert", "Hot 🔥", "Foreign 🌍"],
            "🍝 Pasta": ["Veg", "Spicy", "Main meal", "Hot 🔥", "Foreign 🌍"],
            "🥟 Samosa": ["Veg", "Spicy", "Snack / Dessert", "Hot 🔥", "Indian 🇮🇳"],
            "🍦 Ice Cream": ["Veg", "Sweet", "Snack / Dessert", "Cold ❄️", "Foreign 🌍"],
            "🍨 Kulfi": ["Veg", "Sweet", "Snack / Dessert", "Cold ❄️", "Indian 🇮🇳"],
            "🍩 Gulab Jamun": ["Veg", "Sweet", "Snack / Dessert", "Hot 🔥", "Indian 🇮🇳"],
            "🍮 Payasam": ["Veg", "Sweet", "Snack / Dessert", "Hot 🔥", "Indian 🇮🇳"],
            "🥞 Dosa": ["Veg", "Spicy", "Main meal", "Hot 🔥", "Indian 🇮🇳"],
            "⚪ Idli": ["Veg", "Spicy", "Main meal", "Hot 🔥", "Indian 🇮🇳"],
            "🍗 Fried Chicken": ["Non-veg", "Spicy", "Snack / Dessert", "Hot 🔥", "Foreign 🌍"],
            "🍛 Chicken Biryani": ["Non-veg", "Spicy", "Main meal", "Hot 🔥", "Indian 🇮🇳"],
            "🐟 Fish Curry": ["Non-veg", "Spicy", "Main meal", "Hot 🔥", "Indian 🇮🇳"],
        },
    },
}

# ---------- SESSION STATE ----------
defaults = {
    "result": None,
    "confidence": 0,
    "answered": False,
    "verdict": "",
    "ai_score": 0,
    "user_score": 0,
    "rounds": 0,
    "celebrate": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def reset_round():
    st.session_state.result = None
    st.session_state.confidence = 0
    st.session_state.answered = False
    st.session_state.verdict = ""


def do_guess(topic):
    data = TOPICS[topic]
    n = len(data["questions"])
    answers = [st.session_state[f"{topic}_q{i}"] for i in range(n)]

    # score every item by how many answers match
    scores = {
        name: sum(1 for a, b in zip(answers, feat) if a == b)
        for name, feat in data["items"].items()
    }
    best = max(scores.values())
    candidates = [name for name, s in scores.items() if s == best]

    st.session_state.rounds += 1
    st.session_state.answered = False
    st.session_state.verdict = ""

    # need at least n-1 matching answers, else AI gives up
    if best >= n - 1:
        st.session_state.result = random.choice(candidates)
        st.session_state.confidence = int(best / n * 100)
    else:
        st.session_state.result = "Unknown"
        st.session_state.confidence = 0
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
st.markdown("<div class='main-title'>🧠 AI GUESS MY MIND 🔮</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>🤖 Can I read your mind? Let's find out! ✨</div>", unsafe_allow_html=True)

# Scoreboard
c1, c2, c3 = st.columns(3)
c1.markdown(f"<div class='score-ai'>🤖 AI<br><b>{st.session_state.ai_score}</b></div>", unsafe_allow_html=True)
c2.markdown(f"<div class='score-user'>🧑 You<br><b>{st.session_state.user_score}</b></div>", unsafe_allow_html=True)
c3.markdown(f"<div class='score-round'>🎮 Rounds<br><b>{st.session_state.rounds}</b></div>", unsafe_allow_html=True)

st.markdown("---")

topic = st.selectbox(
    "🎯 Choose a Topic",
    list(TOPICS.keys()),
    key="topic",
    on_change=reset_round,
)

st.markdown(f"### 💭 Think of something in {topic}")
st.caption("Don't tell me! Just answer the questions honestly 👇")

for i, (q, options) in enumerate(TOPICS[topic]["questions"]):
    st.radio(
        f"Q{i + 1}. {q}",
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
        st.progress(
            st.session_state.confidence,
            text=f"🧠 AI Confidence: {st.session_state.confidence}%",
        )

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