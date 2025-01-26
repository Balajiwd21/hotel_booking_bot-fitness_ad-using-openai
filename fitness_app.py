from openai import OpenAI
import textstat
import os

# OpenAI API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Prompt for the AI
prompt = """Create a brief product description for an AI-powered fitness app that adapts workouts based on real-time health data. 
The description should be engaging, creative, and appeal to fitness enthusiasts."""

# Calling the OpenAI API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative marketing assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=150
)

# Extract the generated content
generated_text = response.choices[0].message.content

# Evaluation
print("Generated Product Description:")
print(generated_text)

# Coherence Evaluation
readability_score = textstat.flesch_reading_ease(generated_text)
print("\nCoherence Evaluation (Readability Score):")
print(f"Flesch Reading Ease: {readability_score} (Higher is better)")

# Creativity Evaluation - Prompt the AI to self-evaluate
creativity_prompt = f"""Rate the following product description on a scale of 1-10 for creativity and explain why:{generated_text}"""
creativity_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an evaluator."},
        {"role": "user", "content": creativity_prompt}
    ]
)
print("\nCreativity Evaluation:")
print(creativity_response.choices[0].message.content)

# Target Audience Evaluation
audience_prompt = f"""Does the following product description effectively appeal to fitness enthusiasts? Why or why not?{generated_text}"""
audience_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an evaluator."},
        {"role": "user", "content": audience_prompt}
    ]
)
print("\nTarget Audience Evaluation:")
print(audience_response.choices[0].message.content)
