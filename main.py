from groq import generate_response

def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")

    vague = input("Enter a vague prompt: ")
    print("\n--- Vague Prompt Response ---")
    print(generate_response(vague))

    specific = input("\nNow, make it more specific: ")
    print("\n--- Specific Prompt Response ---")
    print(generate_response(specific))

    context = input("\nAdd more context to the prompt: ")
    print("\n--- Contextual Prompt Response ---")
    print(generate_response(context))

    print("\n--- Reflection Questions ---")
    print("1) How did the AI's response change when the prompt was made more specific?")
    print("2) How did the AI's response improve with the added context?")
    print("3) What prompt produced the most relevant and tailore response? Why?")

if __name__ == "__main__":
    prompt_engineering_activity()
    