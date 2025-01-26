from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Prompt for the AI
prompt = """Create a brief product description for an AI-powered fitness app that adapts workouts based on real-time health data. 
The description should be engaging, creative, and appeal to fitness enthusiasts."""

# Call the OpenAI API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative marketing assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,  # Adjust for more or less creativity
    max_tokens=200    # Limit the response length
)


# Print the result
generated_text = response.choices[0].message.content
print("Generated Product Description:")
print(generated_text)
