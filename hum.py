import random
import streamlit as st

# =========================================================
# HUMAN vs AI ARENA
# Save this file as sec.py (or app.py).
# In Streamlit Cloud, set Main file path to the same filename.
# Also add .streamlit/config.toml (light theme) for best visibility.
# =========================================================

st.set_page_config(
    page_title="Human vs AI Arena",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------- DESIGN -------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: linear-gradient(135deg, #ffffff 0%, #fff1f8 48%, #eefaff 100%);
        background-attachment: fixed;
    }
    .block-container {
        max-width: 1100px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, p, label, div, span, li {
        font-family: 'Poppins', sans-serif;
    }
    hr { border-color: #f0c8e2; }

    /* ---------- Better visibility: Streamlit widgets ---------- */
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stCaptionContainer"] p,
    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label {
        color: #2d1b4e !important;
        font-size: 17px;
    }
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stHeading"] * {
        color: #6a1b9a !important;
        font-weight: 800 !important;
    }
    [data-testid="stCaptionContainer"] p {
        color: #5a4a72 !important;
        font-size: 15px;
        font-weight: 500;
    }

    /* Radio box + options */
    [data-testid="stRadio"] {
        background: #fff4fa;
        border: 1px solid #f2c4e1;
        border-radius: 16px;
        padding: 12px 16px;
    }
    [data-testid="stRadio"] label p {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #2d1b4e !important;
    }

    /* Text input */
    [data-testid="stTextInput"] input {
        border: 2px solid #e9a6d1;
        border-radius: 12px;
        background: #ffffff !important;
        color: #2d1b4e !important;
        font-size: 17px !important;
        font-weight: 600;
    }
    [data-testid="stTextInput"] input::placeholder {
        color: #9b8bb0 !important;
        opacity: 1;
    }

    /* Dropdown (selectbox) */
    [data-baseweb="select"] > div {
        background: #ffffff !important;
        border: 2px solid #e9a6d1 !important;
        border-radius: 12px !important;
    }
    [data-baseweb="select"] * {
        color: #2d1b4e !important;
        font-size: 17px !important;
        font-weight: 600;
    }
    [data-baseweb="popover"] li,
    [data-baseweb="popover"] li * {
        color: #2d1b4e !important;
        background-color: #ffffff;
        font-size: 16px !important;
    }
    [data-baseweb="popover"] li:hover,
    [data-baseweb="popover"] li:hover * {
        background-color: #ffe2f1 !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background: #fff5fb;
        border: 1px solid #f0c3e0;
        border-radius: 16px;
        padding: 12px;
    }
    [data-testid="stMetricLabel"] *,
    [data-testid="stMetricValue"] * {
        color: #6a1b9a !important;
        font-weight: 700 !important;
    }

    /* Expander */
    [data-testid="stExpander"] {
        background: #ffffff;
        border: 1px solid #f0c3e0 !important;
        border-radius: 14px;
    }
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary * {
        color: #2d1b4e !important;
        font-weight: 600 !important;
        font-size: 17px !important;
    }

    /* Alerts (info / success / warning / error) */
    [data-testid="stAlert"] p,
    [data-testid="stAlert"] * {
        color: #1f1235 !important;
        font-weight: 600;
        font-size: 16px;
    }

    /* Buttons: white text on gradient (keep this LAST) */
    .stButton > button, .stFormSubmitButton > button {
        width: 100%;
        min-height: 52px;
        border: 0;
        border-radius: 16px;
        background: linear-gradient(90deg, #ff72b6, #a879f5);
        transition: transform .2s ease, box-shadow .2s ease;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 18px #e6b9ed;
    }
    .stButton > button, .stFormSubmitButton > button,
    .stButton > button *, .stFormSubmitButton > button * {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 17px !important;
    }

        50% { transform: rotate(-10deg) translateY(0); }
        75% { transform: rotate(10deg) translateY(-12px); }
    }
    @keyframes walk {
        0%, 100% { transform: translateX(-14px) rotate(-7deg); }
        50% { transform: translateX(14px) rotate(7deg); }
    }
    @keyframes floaty {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-16px); }
    }
    @keyframes twinkle {
        0%, 100% { opacity: .45; transform: scale(.85); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    .dance-doll { display:inline-block; font-size: clamp(38px, 7vw, 64px); animation:dance 1.25s infinite ease-in-out; }
    .walk-doll { display:inline-block; font-size: clamp(38px, 7vw, 64px); animation:walk 1.8s infinite ease-in-out; }
    .float-robot { display:inline-block; font-size: clamp(44px, 8vw, 72px); animation:floaty 2s infinite ease-in-out; }
    .twinkle { display:inline-block; animation:twinkle 1.4s infinite ease-in-out; font-size:25px; }

    /* ---------- Cards ---------- */
    .hero-box {
        background: rgba(255,255,255,.95);
        border: 2px solid #f1b9dc;
        border-radius: 24px;
        padding: 22px 14px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(220, 160, 210, .18);
        margin: 8px 0 18px 0;
    }
    .hero-title {
        color: #7b1fa2;
        font-size: clamp(34px, 7vw, 52px);
        font-weight: 800;
        line-height: 1.15;
        margin: 10px 0 4px 0;
    }
    .hero-subtitle { color:#c2185b; font-weight:700; font-size:clamp(15px, 3vw, 20px); }
    .character-card {
        border-radius: 22px;
        padding: 18px 10px;
        text-align: center;
        min-height: 190px;
        box-shadow: 0 6px 18px rgba(180, 150, 210, .14);
    }
    .human-card { background:linear-gradient(135deg,#ffe2f1,#f5e6ff); border:2px solid #ed9dce; }
    .ai-card { background:linear-gradient(135deg,#e1f8ff,#eae5ff); border:2px solid #91cbed; }
    .character-emoji { font-size:58px; }
    .card-title-human { color:#8e2476; font-weight:800; font-size:22px; margin:5px 0; }
    .card-title-ai { color:#2a5aa8; font-weight:800; font-size:22px; margin:5px 0; }
    .card-text { color:#3b2b55; font-size:16px; font-weight:500; margin:0; }
    .score-human { font-size:42px; font-weight:800; color:#6a1b9a; }
    .score-ai { font-size:42px; font-weight:800; color:#2a5aa8; }
    .winner-box {
        background:#ffffff;
        border:2px solid #efb5dc;
        border-radius:22px;
        text-align:center;
        padding:20px 12px;
        box-shadow:0 6px 18px rgba(180,150,210,.14);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------- QUESTIONS -------------------------

QUESTION_BANK = [
    # General Knowledge
    {"category":"General Knowledge","question":"Which is the largest planet in our solar system?","options":["Earth","Jupiter","Mars","Venus"],"answer":"Jupiter"},
    {"category":"General Knowledge","question":"What is the capital of India?","options":["Mumbai","Chennai","New Delhi","Kolkata"],"answer":"New Delhi"},
    {"category":"General Knowledge","question":"How many colors are traditionally named in a rainbow?","options":["5","6","7","8"],"answer":"7"},
    {"category":"General Knowledge","question":"Which is the largest ocean?","options":["Indian Ocean","Atlantic Ocean","Pacific Ocean","Arctic Ocean"],"answer":"Pacific Ocean"},
    {"category":"General Knowledge","question":"Which animal is commonly called the King of the Jungle?","options":["Tiger","Lion","Elephant","Leopard"],"answer":"Lion"},
    {"category":"General Knowledge","question":"The Eiffel Tower is in which country?","options":["Italy","France","Japan","India"],"answer":"France"},
    {"category":"General Knowledge","question":"How many days are in a leap year?","options":["364","365","366","367"],"answer":"366"},
    {"category":"General Knowledge","question":"What is India's national animal?","options":["Lion","Tiger","Elephant","Peacock"],"answer":"Tiger"},
    # Maths
    {"category":"Maths","question":"What is 25 × 4?","options":["50","75","100","125"],"answer":"100"},
    {"category":"Maths","question":"What is 144 ÷ 12?","options":["10","11","12","14"],"answer":"12"},
    {"category":"Maths","question":"What is the square of 9?","options":["18","72","81","99"],"answer":"81"},
    {"category":"Maths","question":"What is 15 + 27?","options":["32","42","45","52"],"answer":"42"},
    {"category":"Maths","question":"What is 100 − 36?","options":["54","64","74","84"],"answer":"64"},
    {"category":"Maths","question":"What is 12 × 12?","options":["124","144","154","164"],"answer":"144"},
    {"category":"Maths","question":"What is 50% of 200?","options":["50","75","100","150"],"answer":"100"},
    {"category":"Science","question":"Which planet is known as the Red Planet?","options":["Mars","Venus","Earth","Saturn"],"answer":"Mars"},
    {"category":"Science","question":"What is the boiling point of water at sea level?","options":["50°C","75°C","100°C","150°C"],"answer":"100°C"},
    {"category":"Science","question":"Which part of a plant mainly absorbs water?","options":["Leaves","Flowers","Roots","Fruits"],"answer":"Roots"},
    # Movies
    {"category":"Movies","question":"Which movie series features Captain Jack Sparrow?","options":["Titanic","Avatar","Pirates of the Caribbean","Frozen"],"answer":"Pirates of the Caribbean"},
    {"category":"Movies","question":"Which animated movie features Elsa?","options":["Frozen","Moana","Coco","Toy Story"],"answer":"Frozen"},
    {"category":"Movies","question":"Which Indian science-fiction movie features the robot Chitti?","options":["Sivaji","Enthiran","Vikram","Leo"],"answer":"Enthiran"},
    {"category":"Movies","question":"Which movie features the fictional moon Pandora?","options":["Avatar","Jumanji","Titanic","Inception"],"answer":"Avatar"},
    {"category":"Movies","question":"Which superhero is also known as Tony Stark?","options":["Thor","Iron Man","Spider-Man","Hulk"],"answer":"Iron Man"},
    # Cyber Safety
    {"category":"Cyber Safety","question":"Should you share an OTP with someone who contacts you unexpectedly?","options":["Yes","No","Sometimes","Only online"],"answer":"No"},
    {"category":"Cyber Safety","question":"What is phishing?","options":["An online scam attempt","A computer game","A social media app","A search engine"],"answer":"An online scam attempt"},
    {"category":"Cyber Safety","question":"Which password practice is safer?","options":["Use 123456","Reuse one password everywhere","Use a long unique password","Use your name"],"answer":"Use a long unique password"},
    {"category":"Cyber Safety","question":"What should you do with an unexpected suspicious link?","options":["Click immediately","Forward it to everyone","Avoid it and verify the sender","Enter your password"],"answer":"Avoid it and verify the sender"},
    {"category":"Cyber Safety","question":"What does 2FA stand for?","options":["Two-Factor Authentication","Two File Access","Fast File Application","Two Friends Account"],"answer":"Two-Factor Authentication"},
]

CATEGORIES = [
    "All Categories",
    "General Knowledge",
    "Maths",
    "Science",
    "Movies",
    "Cyber Safety",
]

# ------------------------- SESSION STATE -------------------------

DEFAULTS = {
    "screen": "home",
    "round_id": 0,
    "last_questions": [],
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


def start_round(category, player_name):
    if category == "All Categories":
        pool = QUESTION_BANK.copy()
        previous = set(st.session_state.last_questions)
        fresh_pool = [q for q in pool if q["question"] not in previous]
        if len(fresh_pool) >= 10:
            pool = fresh_pool
        count = min(10, len(pool))
    else:
        pool = [q for q in QUESTION_BANK if q["category"] == category]
        count = min(10, len(pool))

    if not pool:
        return False

    chosen = random.sample(pool, count)
    st.session_state.questions = chosen
    st.session_state.total_questions = count
    st.session_state.last_questions = [q["question"] for q in chosen]
    st.session_state.player_name = player_name
    st.session_state.category = category
    st.session_state.round_id += 1
    st.session_state.screen = "quiz"
    st.session_state.human_answers = []
    st.session_state.submitted = False
    return True


def score_round(answers):
    ai_answers = []
    for question in st.session_state.questions:
        correct = question["answer"]
        # Educational demo opponent: 75% chance to choose correctly.
        if random.random() < 0.75:
            ai_answers.append(correct)
        else:
            wrong = [choice for choice in question["options"] if choice != correct]
            ai_answers.append(random.choice(wrong))

    human_score = sum(
        answer == question["answer"]
        for answer, question in zip(answers, st.session_state.questions)
    )
    ai_score = sum(
        answer == question["answer"]
        for answer, question in zip(ai_answers, st.session_state.questions)
    )

    st.session_state.human_answers = answers
    st.session_state.ai_answers = ai_answers
    st.session_state.human_score = human_score
    st.session_state.ai_score = ai_score
    st.session_state.submitted = True
    st.session_state.screen = "results"


def go_home():
    st.session_state.screen = "home"
    st.session_state.submitted = False
    for key in [
        "questions", "total_questions", "human_answers", "ai_answers",
        "human_score", "ai_score", "player_name", "category",
    ]:
        st.session_state.pop(key, None)


# ------------------------- HEADER -------------------------

st.html("""
<div class="hero-box">
  <div>
    <span class="dance-doll">💃</span>
    <span class="walk-doll">👧</span>
    <span class="float-robot">🤖</span>
    <span class="walk-doll">🧒</span>
    <span class="dance-doll">🕺</span>
  </div>
  <div class="hero-title">HUMAN vs AI</div>
  <div class="hero-subtitle">🎮 THE ULTIMATE BATTLE ARENA 🎮</div>
  <div style="margin-top:8px;">
    <span class="twinkle">⭐</span>
    <span class="twinkle">💖</span>
    <span class="twinkle">✨</span>
  </div>
</div>
""")

# ------------------------- HOME SCREEN -------------------------

if st.session_state.screen == "home":
    st.html("""
    <div class="hero-box">
      <div style="font-size:54px;">👧 ⚔️ 🤖</div>
      <h2 style="margin:8px 0;color:#7b1fa2;font-weight:800;">WHO IS SMARTER?</h2>
      <p style="margin:0;color:#3b2b55;font-size:18px;font-weight:500;">Challenge the robot and become the quiz champion!</p>
    </div>
    """)

    st.subheader("👤 Player details")
    name = st.text_input("Enter your name", placeholder="Your name here...")
    category = st.selectbox("🎯 Choose your challenge category", CATEGORIES)

    col1, col2 = st.columns(2)
    with col1:
        st.html("""
        <div class="character-card human-card">
          <div class="character-emoji">👧</div>
          <div class="card-title-human">HUMAN PLAYER</div>
          <p class="card-text">Think carefully and answer!</p>
          <div style="font-size:25px;">💗 ⭐ 💗</div>
        </div>
        """)
    with col2:
        st.html("""
        <div class="character-card ai-card">
          <div class="character-emoji" style="display:inline-block;animation:floaty 2s infinite;">🤖</div>
          <div class="card-title-ai">AI ROBOT</div>
          <p class="card-text">Your digital quiz opponent!</p>
          <div style="font-size:25px;">💙 ⚡ 💙</div>
        </div>
        """)

    if category == "All Categories":
        question_count = min(10, len(QUESTION_BANK))
    else:
        question_count = min(
            10,
            sum(q["category"] == category for q in QUESTION_BANK),
        )
    st.caption(f"This round will contain {question_count} questions.")

    if st.button("🚀 START THE BATTLE", use_container_width=True):
        if not name.strip():
            st.warning("Please enter your name first.")
        else:
            start_round(category, name.strip())
            st.rerun()

# ------------------------- QUIZ SCREEN -------------------------

elif st.session_state.screen == "quiz":
    total = st.session_state.total_questions
    st.subheader(f"⚔️ Round {st.session_state.round_id}")
    st.write(f"👤 Player: **{st.session_state.player_name}**")
    st.info(f"Answer all {total} questions. The AI will answer the same questions.")

    with st.form(key=f"quiz_form_{st.session_state.round_id}"):
        answers = []
        for index, question in enumerate(st.session_state.questions):
            st.markdown(f"### 🟣 Question {index + 1} of {total}")
            st.caption(f"📚 {question['category']}")
            st.markdown(f"**{question['question']}**")
            selected = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"answer_{st.session_state.round_id}_{index}",
            )
            answers.append(selected)
            st.divider()

        submitted = st.form_submit_button("⚡ SUBMIT MY ANSWERS")

    if submitted:
        score_round(answers)
        st.rerun()

# ------------------------- RESULTS SCREEN -------------------------

elif st.session_state.screen == "results":
    human = st.session_state.human_score
    ai = st.session_state.ai_score
    total = st.session_state.total_questions

    st.balloons()
    st.html("""
    <div style="text-align:center;padding:8px;">
      <span class="dance-doll">💃</span>
      <span class="float-robot">🏆</span>
      <span class="dance-doll">🕺</span>
      <h1 style="color:#7b1fa2;font-weight:800;">BATTLE RESULTS!</h1>
    </div>
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.html(f"""
        <div class="character-card human-card">
          <div class="character-emoji">👧</div>
          <div class="card-title-human">HUMAN</div>
          <div class="score-human">{human}/{total}</div>
        </div>
        """)
    with col2:
        st.html(f"""
        <div class="character-card ai-card">
          <div class="character-emoji" style="display:inline-block;animation:floaty 2s infinite;">🤖</div>
          <div class="card-title-ai">AI ROBOT</div>
          <div class="score-ai">{ai}/{total}</div>
        </div>
        """)

    st.subheader("🏆 Final result")
    if human > ai:
        st.success(f"🎉 {st.session_state.player_name.upper()} WINS! Human champion!")
        st.html('<div class="winner-box"><div style="font-size:64px;">👧 🏆 💃</div><h2 style="color:#c2185b;font-weight:800;">HUMAN CHAMPION!</h2></div>')
    elif ai > human:
        st.info("🤖 AI ROBOT WINS THIS ROUND!")
        st.html('<div class="winner-box"><div style="font-size:64px;">🤖 🏆 ⚡</div><h2 style="color:#2a5aa8;font-weight:800;">AI CHAMPION!</h2></div>')
    else:
        st.warning("🤝 It is a draw! Both are champions.")
        st.html('<div class="winner-box"><div style="font-size:64px;">👧 🤝 🤖</div><h2 style="color:#7b1fa2;font-weight:800;">BOTH ARE CHAMPIONS!</h2></div>')

    st.subheader("📊 Score comparison")
    score_col1, score_col2 = st.columns(2)
    with score_col1:
        st.metric("Human score", f"{human}/{total}")
        st.progress(human / total)
    with score_col2:
        st.metric("AI score", f"{ai}/{total}")
        st.progress(ai / total)

    st.subheader("📝 Answer review")
    for index, question in enumerate(st.session_state.questions):
        with st.expander(f"Question {index + 1}: {question['question']}"):
            human_answer = st.session_state.human_answers[index]
            ai_answer = st.session_state.ai_answers[index]
            correct = question["answer"]
            st.write(f"👧 Your answer: **{human_answer}**")
            st.write(f"🤖 AI answer: **{ai_answer}**")
            st.write(f"✅ Correct answer: **{correct}**")
            if human_answer == correct:
                st.success("Your answer is correct!")
            else:
                st.error("Your answer is incorrect.")
            if ai_answer == correct:
                st.success("AI answered correctly.")
            else:
                st.error("AI answered incorrectly.")

    st.info(
        "Project note: The opponent is a Python-based simulation, not a trained AI model. "
        "It has a 75% chance of selecting the correct answer on each question."
    )

    if st.button("🔄 PLAY AGAIN - NEW QUESTIONS", use_container_width=True):
        go_home()
        st.rerun()

# ------------------------- FOOTER -------------------------

st.divider()
st.html("""
<div style="text-align:center;padding:12px 4px 4px 4px;">
  <div style="font-size:34px;">💗 🤖 💗</div>
  <div style="color:#7b1fa2;font-weight:800;font-size:22px;margin:5px 0;">HUMAN vs AI ARENA</div>
  <p style="color:#3b2b55;margin:0;font-weight:500;">THINK SMART • PLAY SMART • WIN THE BATTLE</p>
  <p style="color:#5a4a72;font-size:13px;margin-top:8px;">✨ College Expo Project ✨</p>
</div>
""")
