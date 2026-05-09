import streamlit as st
import math

st.set_page_config(page_title="Northstar MVP", layout="wide")

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
}

.main {
    background-color: #020617;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.card {
    background: #0f172a;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
}

.metric-card {
    background: #111827;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

.big-text {
    font-size: 32px;
    font-weight: bold;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

st.title("Northstar — Adulting Operating System")
st.subheader("Understand your life before trying to fix it.")

st.write(
    "Northstar helps young adults reduce overwhelm by understanding their life stage, "
    "goals, stress areas, and financial situation before giving structured guidance."
)

st.divider()

st.header("1. Basic Life Context")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=40, value=23)
    city = st.text_input("City", placeholder="Mumbai")
    stage = st.selectbox(
        "Current Life Stage",
        [
            "College Student",
            "Recently Graduated",
            "First Job",
            "Career Switch",
            "Feeling Lost/Burnt Out"
        ]
    )

with col2:
    income = st.number_input("Monthly Income (₹)", min_value=0, value=45000)
    expenses = st.number_input("Monthly Essential Expenses (₹)", min_value=0, value=25000)
    savings_capacity = st.number_input("Monthly Savings Capacity (₹)", min_value=0, value=10000)

st.divider()

st.header("2. What Currently Feels Overwhelming?")

pain_points = st.multiselect(
    "Select all areas causing stress:",
    [
        "Managing money and savings",
        "Understanding taxes or insurance",
        "Career growth and workplace pressure",
        "Burnout and mental exhaustion",
        "Moving out and independent living",
        "Feeling directionless in life"
    ]
)

coping = st.selectbox(
    "When confused, what do you usually do?",
    [
        "Watch YouTube videos",
        "Ask ChatGPT",
        "Google endlessly",
        "Ask friends or relatives",
        "Delay the decision"
    ]
)

stress = st.selectbox(
    "How often do you feel behind in life?",
    ["Very Often", "Sometimes", "Rarely"]
)

frustration = st.text_area(
    "What frustrates you the most right now?",
    placeholder="Everyone gives different advice and I don't know what's actually correct..."
)

st.divider()

st.header("3. Your Main Goal")

goal = st.selectbox(
    "What is your biggest current goal?",
    [
        "Build Emergency Savings",
        "Start Investing",
        "Reduce Stress & Burnout",
        "Move Out Independently",
        "Career Growth"
    ]
)

target_amount = st.number_input(
    "Target Goal Amount (₹)",
    min_value=0,
    value=100000
)

if st.button("Generate My Northstar Plan"):

    st.divider()

    st.header("Your Personalized Northstar Report")

    personalized_message = (
        "Most people feel overwhelmed during adulthood transitions because nobody teaches "
        "them how to manage money, work pressure, burnout, and life decisions together."
    )

    if stage == "First Job":
        personalized_message = (
            "Starting your first job can feel mentally exhausting. Suddenly you're expected "
            "to manage finances, career growth, stress, and long-term planning all at once."
        )

    if stage == "Feeling Lost/Burnt Out":
        personalized_message = (
            "Feeling burnt out or directionless does not mean you're failing. It usually "
            "means you've been carrying too much uncertainty without enough clarity or structure."
        )

    if stage == "Recently Graduated":
        personalized_message = (
            "The transition after graduation is harder than most people admit. Expectations rise quickly, "
            "but guidance disappears."
        )

    st.info(personalized_message)

    emotional_state = "Overwhelmed"

    if stress == "Sometimes":
        emotional_state = "Uncertain"

    if stress == "Rarely":
        emotional_state = "Stabilizing"

    focus_area = "Reduce Chaos"

    if any("money" in p.lower() for p in pain_points):
        focus_area = "Financial Stability"

    if any("career" in p.lower() for p in pain_points):
        focus_area = "Career Direction"

    if any("burnout" in p.lower() for p in pain_points):
        focus_area = "Mental Recovery"

    if any("directionless" in p.lower() for p in pain_points):
        focus_area = "Life Clarity"

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.write("### Emotional State")
        st.markdown(f'<div class="big-text">{emotional_state}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.write("### Main Focus")
        st.markdown(f'<div class="big-text">{focus_area}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        stress_level = "Manageable"

        if expenses > savings_capacity * 3:
            stress_level = "High"

        if expenses > savings_capacity * 5:
            stress_level = "Critical"

        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.write("### Financial Stress")
        st.markdown(f'<div class="big-text">{stress_level}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    st.header("4. Goal & Investment Planning")

    months = 0

    if savings_capacity > 0:
        months = math.ceil(target_amount / savings_capacity)

    recommended_investment = int(savings_capacity * 0.6)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Estimated Goal Timeline", f"{months} Months")

    with col2:
        st.metric("Recommended Monthly Investment", f"₹{recommended_investment}")

    st.divider()

    st.header("5. Your Weekly Accountability System")

    tasks = []

    if goal == "Build Emergency Savings":
        tasks = [
            "Track weekly spending",
            "Save your planned monthly amount",
            "Avoid unnecessary impulse purchases",
            "Review financial progress every Sunday"
        ]

    elif goal == "Start Investing":
        tasks = [
            "Learn SIP and mutual fund basics",
            "Invest your planned monthly amount",
            "Track investment growth weekly",
            "Avoid panic from market fluctuations"
        ]

    elif goal == "Reduce Stress & Burnout":
        tasks = [
            "Sleep before midnight at least 4 days/week",
            "Take one no-work recovery break weekly",
            "Reduce doom-scrolling and information overload",
            "Reflect on emotional triggers weekly"
        ]

    elif goal == "Move Out Independently":
        tasks = [
            "Create a realistic moving budget",
            "Research safe localities and commute routes",
            "Build a 3-month safety cushion",
            "Prepare a weekly household routine"
        ]

    elif goal == "Career Growth":
        tasks = [
            "Identify one skill limiting growth",
            "Block weekly learning time",
            "Improve workplace communication",
            "Track monthly career progress"
        ]

    for task in tasks:
        st.checkbox(task)

    st.divider()

    st.header("6. What Northstar Learned About You")

    st.write(f"- You are currently in the **{stage}** phase.")
    st.write(f"- Your current coping mechanism is: **{coping}**.")

    if pain_points:
        st.write(f"- Your major stress areas are: **{', '.join(pain_points)}**.")

    st.write(f"- Your current priority is: **{goal}**.")
    st.write(
        "- Northstar recommends focusing on reducing uncertainty and building stable systems instead of trying to fix everything together."
    )

    st.success("Northstar generated your first structured adulthood roadmap.")

st.divider()

st.caption("Northstar MVP — Designed for young adults navigating real life.")
