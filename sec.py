
import streamlit as st
import random

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Human vs AI Arena",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# CSS DESIGN
# =====================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

.stApp {
    background: linear-gradient(
        135deg,
        #ffffff,
        #fff0f8,
        #eefaff,
        #f8f0ff
    );
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif !important;
    color: #873caa !important;
}

p, label {
    color: #444 !important;
}

/* Dancing animation */

@keyframes dance {
    0% { transform: rotate(-12deg) translateY(0); }
    25% { transform: rotate(12deg) translateY(-15px); }
    50% { transform: rotate(-12deg) translateY(0); }
    75% { transform: rotate(12deg) translateY(-15px); }
    100% { transform: rotate(-12deg) translateY(0); }
}

/* Walking animation */

@keyframes walk {
    0% { transform: translateX(-25px) rotate(-8deg); }
    50% { transform: translateX(25px) rotate(8deg); }
    100% { transform: translateX(-25px) rotate(-8deg); }
}

/* Robot floating */

@keyframes float {
    0% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0); }
}

@keyframes sparkle {
    0% { opacity: 0.3; transform: scale(0.8); }
    50% { opacity: 1; transform: scale(1.3); }
    100% { opacity: 0.3; transform: scale(0.8); }
}

.doll {
    display: inline-block;
    font-size: 60px;
    animation: dance 1.3s infinite ease-in-out;
    margin: 5px;
}

.walking-doll {
    display: inline-block;
    font-size: 60px;
    animation: walk 2s infinite ease-in-out;
    margin: 5px;
}

.robot {
    display: inline-block;
    font-size: 70px;
    animation: float 2s infinite ease-in-out;
}

.sparkle {
    display: inline-block;
    font-size: 30px;
    animation: sparkle 1.5s infinite;
}

/* Cards */

.player-card {
    background: linear-gradient(135deg, #ffe0f0, #f5e5ff);
    border: 3px solid #ed8acb;
    border-radius: 25px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 6px 20px #f3c5e5;
}

.ai-card {
    background: linear-gradient(135deg, #dff7ff, #e9e1ff);
    border: 3px solid #83c9ed;
    border-radius: 25px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 6px 20px #c9eaff;
}

/* Buttons */

.stButton > button {
    width: 100%;
    min-height: 55px;
    border: none;
    border-radius: 18px;
    background: linear-gradient(90deg, #ff72b6, #ad70ff);
    color: white !important;
    font-size: 17px;
    font-weight: 800;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.04);
    box-shadow: 0 5px 20px #d5b4ff;
}

/* Input */

.stTextInput input {
    background: white !important;
    color: #333 !important;
    border: 2px solid #e8a2d1 !important;
    border-radius: 12px;
}

/* Question box */

[data-testid="stRadio"] {
    background: #fff0f8;
    border: 1px solid #f2c1df;
    padding: 15px;
    border-radius: 15px;
}

/* Metrics */

[data-testid="stMetric"] {
    background: #fff0f8;
    padding: 15px;
    border-radius: 15px;
    border: 2px solid #edb4db;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# QUESTION BANK
# =====================================

QUESTION_BANK = [

    # GENERAL KNOWLEDGE

    {
        "category": "General Knowledge",
        "question": "Which is the largest planet?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter"
    },
    {
        "category": "General Knowledge",
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Chennai", "New Delhi", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "category": "General Knowledge",
        "question": "How many colors are in a rainbow?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "category": "General Knowledge",
        "question": "Which is the largest ocean?",
        "options": ["Indian", "Atlantic", "Pacific", "Arctic"],
        "answer": "Pacific"
    },
    {
        "category": "General Knowledge",
        "question": "Which animal is called King of the Jungle?",
        "options": ["Tiger", "Lion", "Elephant", "Leopard"],
        "answer": "Lion"
    },
    {
        "category": "General Knowledge",
        "question": "Which country has the Eiffel Tower?",
        "options": ["Italy", "France", "Japan", "India"],
        "answer": "France"
    },
    {
        "category": "General Knowledge",
        "question": "How many days are in a leap year?",
        "options": ["364", "365", "366", "367"],
        "answer": "366"
    },
    {
        "category": "General Knowledge",
        "question": "What is the national animal of India?",
        "options": ["Lion", "Tiger", "Elephant", "Peacock"],
        "answer": "Tiger"
    },

    # MATHS

    {
        "category": "Maths",
        "question": "What is 25 × 4?",
        "options": ["50", "75", "100", "125"],
        "answer": "100"
    },
    {
        "category": "Maths",
        "question": "What is 144 ÷ 12?",
        "options": ["10", "11", "12", "14"],
        "answer": "12"
    },
    {
        "category": "Maths",
        "question": "What is the square of 9?",
        "options": ["18", "72", "81", "99"],
        "answer": "81"
    },
    {
        "category": "Maths",
        "question": "What is 15 + 27?",
        "options": ["32", "42", "45", "52"],
        "answer": "42"
    },
    {
        "category": "Maths",
        "question": "What is 100 - 36?",
        "options": ["54", "64", "74", "84"],
        "answer": "64"
    },
    {
        "category": "Maths",
        "question": "What is 12 × 12?",
        "options": ["124", "144", "154", "164"],
        "answer": "144"
    },
    {
        "category": "Maths",
        "question": "What is 50% of 200?",
        "options": ["50", "75", "100", "150"],
        "answer": "100"
    },

    # SCIENCE

    {
        "category": "Science",
        "question": "Which gas do plants absorb?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Carbon dioxide"
    },
    {
        "category": "Science",
        "question": "What is the chemical formula of water?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "H2O"
    },
    {
        "category": "Science",
        "question": "Which organ pumps blood?",
        "options": ["Brain", "Lungs", "Heart", "Kidney"],
        "answer": "Heart"
    },
    {
        "category": "Science",
        "question": "Which planet is called the Red Planet?",
        "options": ["Mars", "Venus", "Earth", "Saturn"],
        "answer": "Mars"
    },
    {
        "category": "Science",
        "question": "What is the boiling point of water at sea level?",
        "options": ["50°C", "75°C", "100°C", "150°C"],
        "answer": "100°C"
    },
    {
        "category": "Science",
        "question": "Which part of a plant absorbs water?",
        "options": ["Leaves", "Flowers", "Roots", "Fruits"],
        "answer": "Roots"
    },

    # MOVIES

    {
        "category": "Movies",
        "question": "Which movie features Jack Sparrow?",
        "options": [
            "Titanic", "Avatar",
            "Pirates of the Caribbean", "Frozen"
        ],
        "answer": "Pirates of the Caribbean"
    },
    {
        "category": "Movies",
        "question": "Which movie features Elsa?",
        "options": ["Frozen", "Moana", "Coco", "Toy Story"],
        "answer": "Frozen"
    },
    {
        "category": "Movies",
        "question": "Which Indian movie features Chitti?",
        "options": ["Sivaji", "Enthiran", "Vikram", "Leo"],
        "answer": "Enthiran"
    },
    {
        "category": "Movies",
        "question": "Which movie features Pandora?",
        "options": ["Avatar", "Jumanji", "Titanic", "Inception"],
        "answer": "Avatar"
    },
    {
        "category": "Movies",
        "question": "Which movie features Iron Man?",
        "options": ["Frozen", "Avengers", "Titanic", "Joker"],
        "answer": "Avengers"
    },

    # CYBER SAFETY

    {
        "category": "Cyber Safety",
        "question": "Should you share your OTP with strangers?",
        "options": ["Yes", "No", "Sometimes", "Only online"],
        "answer": "No"
    },
    {
        "category": "Cyber Safety",
        "question": "What is phishing?",
        "options": [
            "Online scam", "Computer game",
            "Social media app", "Search engine"
        ],
        "answer": "Online scam"
    },
    {
        "category": "Cyber Safety",
        "question": "Which password is safer?",
        "options": [
            "123456", "password",
            "A long unique password", "Your name"
        ],
        "answer": "A long unique password"
    },
    {
        "category": "Cyber Safety",
        "question": "What should you do with suspicious links?",
        "options": [
            "Click immediately",
            "Share with friends",
            "Avoid and verify them",
            "Enter your password"
        ],
        "answer": "Avoid and verify them"
    },
    {
        "category": "Cyber Safety",
        "question": "What does 2FA mean?",
        "options": [
            "Two Factor Authentication",
            "Two File Access",
            "Fast File Application",
            "Two Friends Account"
        ],
        "answer": "Two Factor Authentication"
    }
]


# =====================================
# SESSION STATE
# =====================================

defaults = {
    "started": False,
    "submitted": False,
    "round_id": 0,
    "last_questions": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =====================================
# GAME FUNCTIONS
# =====================================

def prepare_questions(category):

    if category == "All Categories":

        pool = QUESTION_BANK.copy()

        previous = st.session_state.last_questions

        fresh_pool = [
            q for q in pool
            if q["question"] not in previous
        ]

        # Avoid repeating the previous round when possible
        if len(fresh_pool) >= 10:
            pool = fresh_pool

        round_size = min(10, len(pool))

    else:

        pool = [
            q for q in QUESTION_BANK
            if q["category"] == category
        ]

        # Use all available questions if fewer than 10
        round_size = min(10, len(pool))

    if round_size == 0:
        return False

    selected = random.sample(pool, round_size)

    st.session_state.questions = selected
    st.session_state.round_size = round_size

    st.session_state.last_questions = [
        q["question"] for q in selected
    ]

    st.session_state.round_id += 1
    st.session_state.started = True
    st.session_state.submitted = False

    return True


def reset_game():

    st.session_state.started = False
    st.session_state.submitted = False

    keys_to_delete = [
        "questions",
        "round_size",
        "human_score",
        "ai_score",
        "human_results",
        "ai_results",
        "ai_answers",
        "human_answers"
    ]

    for key in keys_to_delete:
        if key in st.session_state:
            del st.session_state[key]


def calculate_results(answers):

    human_score = 0
    ai_score = 0

    human_results = []
    ai_results = []
    ai_answers = []

    for i, q in enumerate(st.session_state.questions):

        correct = q["answer"]

        # Human answer
        human_correct = answers[i] == correct

        if human_correct:
            human_score += 1

        human_results.append(human_correct)

        # Simulated AI answer
        if random.random() < 0.75:
            ai_answer = correct
        else:
            wrong_options = [
                option for option in q["options"]
                if option != correct
            ]
            ai_answer = random.choice(wrong_options)

        ai_answers.append(ai_answer)

        ai_correct = ai_answer == correct

        if ai_correct:
            ai_score += 1

        ai_results.append(ai_correct)

    st.session_state.human_score = human_score
    st.session_state.ai_score = ai_score

    st.session_state.human_results = human_results
    st.session_state.ai_results = ai_results
    st.session_state.ai_answers = ai_answers

    st.session_state.human_answers = answers

    st.session_state.submitted = True


# =====================================
# HEADER
# =====================================

st.markdown("""
<div style="text-align:center;padding:15px;">

    <span class="doll">💃</span>
    <span class="walking-doll">👧</span>
    <span class="robot">🤖</span>
    <span class="walking-doll">🧒</span>
    <span class="doll">🕺</span>

    <br>

    <span class="sparkle">⭐</span>
    <span class="sparkle">💖</span>
    <span class="sparkle">✨</span>

</div>

<h1 style="text-align:center;font-size:48px;">
    HUMAN vs AI
</h1>

<h3 style="text-align:center;">
    🎮 THE ULTIMATE BATTLE ARENA 🎮
</h3>
""", unsafe_allow_html=True)

st.markdown("---")


# =====================================
# HOME SCREEN
# =====================================

if not st.session_state.started:

    st.markdown("""
    <div style="
        background:white;
        border:3px solid #f3b5df;
        border-radius:25px;
        padding:25px;
        text-align:center;
        box-shadow:0 5px 20px #f5d9ec;
    ">

        <div style="font-size:65px;">
            👧 ⚔️ 🤖
        </div>

        <h2>WHO IS SMARTER?</h2>

        <p style="font-size:18px;">
            Challenge the AI robot and become the champion!
        </p>

        <div style="font-size:30px;">
            ⭐ 🏆 ⭐
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 👤 PLAYER DETAILS")

    name = st.text_input(
        "Enter your name",
        placeholder="Your name here..."
    )

    st.markdown("## 🎯 SELECT YOUR CATEGORY")

    category = st.selectbox(
        "Choose your challenge",
        [
            "All Categories",
            "General Knowledge",
            "Maths",
            "Science",
            "Movies",
            "Cyber Safety"
        ]
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="player-card">

            <div style="font-size:65px;">👧</div>

            <h2>HUMAN PLAYER</h2>

            <p>Think fast and answer correctly!</p>

            <div style="font-size:30px;">💗 ⭐ 💗</div>

        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="ai-card">

            <div style="font-size:65px;">🤖</div>

            <h2>AI ROBOT</h2>

            <p>Challenge the digital opponent!</p>

            <div style="font-size:30px;">💙 ⚡ 💙</div>

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if st.button("🚀 START THE BATTLE"):

        if not name.strip():
            st.warning("Please enter your name!")

        else:

            st.session_state.player_name = name.strip()
            st.session_state.category = category

            success = prepare_questions(category)

            if success:
                st.rerun()
            else:
                st.error("No questions are available. Please try another category.")


# =====================================
# QUIZ SCREEN
# =====================================

elif not st.session_state.submitted:

    questions = st.session_state.questions
    total = st.session_state.round_size

    st.markdown(f"## ⚔️ ROUND {st.session_state.round_id}")

    st.write(f"👤 Player: {st.session_state.player_name}")

    st.info(
        f"Answer all {total} questions. "
        "The AI will answer the same questions!"
    )

    with st.form(
        key=f"battle_form_{st.session_state.round_id}"
    ):

        human_answers = []

        for i, q in enumerate(questions):

            st.markdown(f"### 🟣 QUESTION {i+1} / {total}")

            st.caption("📚 Category: " + q["category"])

            st.markdown(f"**{q['question']}**")

            answer = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"answer_{st.session_state.round_id}_{i}"
            )

            human_answers.append(answer)

            st.markdown("---")

        submit = st.form_submit_button("⚡ SUBMIT MY ANSWERS")

    if submit:

        calculate_results(human_answers)
        st.rerun()


# =====================================
# RESULT SCREEN
# =====================================

if st.session_state.started and st.session_state.submitted:

    human = st.session_state.human_score
    ai = st.session_state.ai_score
    total = st.session_state.round_size

    st.balloons()

    st.markdown("""
    <div style="text-align:center;">

        <span class="doll">💃</span>
        <span class="robot">🏆</span>
        <span class="doll">🕺</span>

        <h1>BATTLE RESULTS!</h1>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="player-card">

            <div style="font-size:60px;">👧</div>

            <h2>HUMAN</h2>

            <h1>{human}/{total}</h1>

        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="ai-card">

            <div style="font-size:60px;">🤖</div>

            <h2>AI ROBOT</h2>

            <h1>{ai}/{total}</h1>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 🏆 FINAL WINNER")

    if human > ai:

        st.success(
            f"🎉 {st.session_state.player_name.upper()} WINS!"
        )

        st.markdown("""
        <div style="text-align:center;">

            <div style="font-size:75px;">
                👧 🏆 💃
            </div>

            <h2>HUMAN CHAMPION!</h2>

            <p>You defeated the AI robot!</p>

        </div>
        """, unsafe_allow_html=True)

    elif ai > human:

        st.info("🤖 AI ROBOT WINS THIS ROUND!")

        st.markdown("""
        <div style="text-align:center;">

            <div style="font-size:75px;">
                🤖 🏆 ⚡
            </div>

            <h2>AI CHAMPION!</h2>

            <p>The AI won this round!</p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.warning("🤝 IT'S A DRAW!")

        st.markdown("""
        <div style="text-align:center;">

            <div style="font-size:75px;">
                👧 🤝 🤖
            </div>

            <h2>BOTH ARE CHAMPIONS!</h2>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # SCORE COMPARISON

    st.markdown("## 📊 SCORE COMPARISON")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Human Score", f"{human}/{total}")
        st.progress(human / total)

    with col2:
        st.metric("AI Score", f"{ai}/{total}")
        st.progress(ai / total)

    st.markdown("---")

    # ANSWER REVIEW

    st.markdown("## 📝 ANSWER REVIEW")

    for i, q in enumerate(st.session_state.questions):

        with st.expander(f"Question {i+1}: {q['question']}"):

            st.write(
                "👧 Your answer: "
                + st.session_state.human_answers[i]
            )

            st.write(
                "🤖 AI answer: "
                + st.session_state.ai_answers[i]
            )

            st.write(
                "✔ Correct answer: "
                + q["answer"]
            )

            if st.session_state.human_results[i]:
                st.success("Your answer is correct!")
            else:
                st.error("Your answer is incorrect.")

            if st.session_state.ai_results[i]:
                st.success("AI answered correctly.")
            else:
                st.error("AI answered incorrectly.")

    st.markdown("---")

    st.info(
        "Project note: The AI opponent is a simulated opponent "
        "created using Python. It has a 75% chance of choosing "
        "the correct answer. It is not a trained AI model."
    )

    if st.button("🔄 PLAY AGAIN - NEW QUESTIONS"):

        reset_game()
        st.rerun()


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown("""
<div style="text-align:center;padding:20px;">

    <div style="font-size:40px;">
        💗 🤖 💗
    </div>

    <h3>HUMAN vs AI ARENA</h3>

    <p>
        THINK SMART • PLAY SMART • WIN THE BATTLE
    </p>

    <p>✨ College Expo Project ✨</p>

</div>
""", unsafe_allow_html=True)
