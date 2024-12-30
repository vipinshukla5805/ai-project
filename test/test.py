import openai

# Set your OpenAI API key
openai.api_key = ""

models = openai.Model.list()
for model in models["data"]:
    print(model["id"])
    
def generate_questions(role):
    """
    Generate interview questions based on the job role.
    """
    system_prompt = "You are an AI assistant helping to create interview questions."
    user_prompt = f"Generate 1 interview questions for the role of {role}. Include technical, behavioral, and situational questions."

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    questions = response.choices[0].message["content"]
    return questions.strip()

def analyze_response(question, response):
    """
    Analyze the candidate's response to an interview question.
    """
    system_prompt = "You are an AI that provides feedback on interview answers."
    user_prompt = f"Question: {question}\nCandidate's Response: {response}\nProvide detailed feedback on this response, including strengths, weaknesses, and suggestions for improvement."

    feedback = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=100
    )
    return feedback.choices[0].message["content"]

def main():
    """
    Main function to run the AI Interviewer.
    """
    print("Welcome to the AI Interviewer!")
    role = input("Enter the job role you are interviewing for: ")

    # Generate questions
    print("\nGenerating interview questions...")
    questions = generate_questions(role)
    print(f"\nHere are the questions:\n{questions}\n")

    # Split questions into a list for individual analysis
    question_list = questions.split("\n")

    # Conduct the interview
    print("\nLet's start the interview.")
    for i, question in enumerate(question_list, start=1):
        print(f"\nQuestion {i}: {question}")
        response = input("Your response: ")

        # Analyze the candidate's response
        print("\nAnalyzing your response...")
        feedback = analyze_response(question, response)
        print(f"\nFeedback: {feedback}\n")

if __name__ == "__main__":
    main()
