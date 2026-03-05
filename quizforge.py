topic = input("Enter geography topic: ")
grade = input("Enter grade level: ")
num_questions = input("Number of questions: ")

print("\nGenerating geography quiz...\n")

quiz_text = f"""
Quiz Topic: {topic}
Grade Level: {grade}

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

print(quiz_text)
