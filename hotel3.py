from openai import OpenAI
import os

# OpenAI API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)
def chatbot_conversation(user_message, conversation_history):
    """
    Handles the chatbot conversation flow with GPT-3.5 Turbo.

    Args:
        user_message (str): The user's latest input.
        conversation_history (list): List of messages in the conversation history.

    Returns:
        str, list: The chatbot's response and updated conversation history.
    """
    # Add user message to conversation history
    conversation_history.append({"role": "user", "content": user_message})

    try:
        # Calling the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.7,
            max_tokens=300
        )

        # Extract chatbot response
        bot_message = response.choices[0].message.content

        # Appends chatbot response to conversation history
        conversation_history.append({"role": "assistant", "content": bot_message})

        return bot_message, conversation_history
    except Exception as e:
        return f"Sorry, something went wrong: {e}", conversation_history


# initial conversation setup
conversation_history = [
    {"role": "system", "content": "You are a friendly and helpful chatbot that helps users book hotels and answers FAQs."},
    {"role": "assistant", "content": "Hi there! 👋 Welcome to HotelBot. I’m here to help you find the perfect hotel for your stay. 😊\n\nHow can I assist you today?\n- 🏨 Book a hotel\n- ❓ Ask a question\n- 🌟 View deals or offers"}
]

if __name__ == "__main__":
    # Start the chatbot
    print(conversation_history[-1]["content"])  # Initial greeting
    
    while True:
        user_message = input("\nUser: ").strip()  # Take user input
        
        if user_message.lower() in ["exit", "quit"]:
            print("\nBot: Thanks for chatting with HotelBot! Have a great day! 😊")
            break

        # Handle intents directly or call the LLM Model
        if "book" in user_message.lower():
            bot_response = (
                "Great! Let’s get started with your booking. "
                "Can you tell me:\n1️⃣ Your destination?\n2️⃣ Check-in and check-out dates?\n3️⃣ Number of guests?"
            )
            conversation_history.append({"role": "assistant", "content": bot_response})
            print(f"\nBot: {bot_response}")
        elif "refund" in user_message.lower():
            bot_response = (
                "Refund policies vary depending on the hotel. Most hotels offer free cancellation if done within 24 hours of booking. "
                "Would you like me to check the refund policy for a specific hotel?"
            )
            conversation_history.append({"role": "assistant", "content": bot_response})
            print(f"\nBot: {bot_response}")
        elif "pet" in user_message.lower() or "pet-friendly" in user_message.lower():
            bot_response = (
                "Yes, we can help you find pet-friendly hotels! 🐾 "
                "Do you have any specific requirements for your pet’s stay?"
            )
            conversation_history.append({"role": "assistant", "content": bot_response})
            print(f"\nBot: {bot_response}")
        elif "deals" in user_message.lower():
            bot_response = (
                "Here are some of the latest deals and offers for hotels in popular destinations. ✨ "
                "Can you tell me your preferred destination to see the best offers?"
            )
            conversation_history.append({"role": "assistant", "content": bot_response})
            print(f"\nBot: {bot_response}")
        else:
            # Use llm (OpenAI) for generic or unknown queries
            bot_response, conversation_history = chatbot_conversation(user_message, conversation_history)
            print(f"\nBot: {bot_response}")
