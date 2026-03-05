import streamlit as st

st.set_page_config(page_title="QuizForge", page_icon="🧭")

st.title("🧭 QuizForge")
st.caption("Geography Quiz Generator (Mock Demo)")

with st.form("quiz_form"):
    topic = st.text_input("Geography topic", placeholder="e.g., Rivers, Plate Tectonics, Climate")
    grade = st.selectbox("Grade level", ["7", "8", "9", "10", "11", "12"])
    num_questions = st.slider("Number of questions", min_value=3, max_value=20, value=5)
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    submitted = st.form_submit_button("Generate Quiz")

def generate_mock_quiz(topic: str, grade: str, num_questions: int, difficulty: str) -> str:
    # Small “glass box” mock output. Later we’ll swap this for a real AI call.
    return f"""Quiz Topic: {topic}
Grade Level: {grade}
Difficulty: {difficulty}

1. Which map type shows elevation using contour lines?
A. Political map
B. Topographic map
C. Climate map
D. Road map
Answer: B

2. What is the main cause of ocean tides?
A. Earth’s rotation
B. Wind patterns
C. The Moon’s gravitational pull
D. Ocean temperature
Answer: C

3. Which term describes a bend in a river?
A. Delta
B. Meander
C. Tributary
D. Estuary
Answer: B
"""

if submitted:
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        quiz_text = generate_mock_quiz(topic.strip(), grade, num_questions, difficulty)

        st.success("Quiz generated!")
        st.subheader("Your Quiz")
        st.code(quiz_text, language="text")

        st.download_button(
            label="Download quiz (.txt)",
            data=quiz_text,
            file_name=f"quizforge_{topic.strip().lower().replace(' ', '_')}_grade{grade}.txt",
            mime="text/plain",
        )

st.divider()
st.markdown("### Workflow (Glass Box)")
st.markdown("**Input → Generation (mock) → Output → Download**")
