# from chatterbot import ChatBot
# chatbot = ChatBot("Chatpot")
# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         print(f"💀{chatbot.get_response(query)}")


# def greet():
#     print("chatbot: Hello! How can I assist you today?")
#     print("chatbot: Type 'bye' to exit.")


# responses = {
#     "hello": "Hi there! 😊",
#     "hi": "Hello! How can I help you?",
#     "how are you": "I'm doing great! Thanks for asking.",
#     "your name": "I am a simple Python chatbot.",
#     "bye": "Goodbye! Have a nice day 👋"
# }


# def get_response(user_input):
#     user_input = user_input.lower()
#     for key in responses:
#         if key in user_input:
#             return responses[key]
#     return "Sorry, I don't understand that."


# def chat():
#     greet()
#     while True:
#         user_input = input("You: ")
#         responses = get_response(user_input)
#         print(f"chatbot: {responses}")
#         if "bye" in user_input.lower():
#             break


# chat()


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')  # Downloads the punkt tokenizer
nltk.download('stopwords')  # Downloads the stopwords dataset


def greet():
    print("chatbot: Hello! How can I assist you today?")
    print("chatbot: Type 'bye' to exit.")


responses = {
    "greeting": ["hello", "hi", "hey"],
    "how_are_you": ["how", "are", "you"],
    "name": ["your", "name"],
    "help": ["help", "support"],
    "goodbye": ["bye", "exit", "quit"]
}

reply = {
    "greeting": "Hello! 😊 How can I help you?",
    "how_are_you": "I'm doing great! Thanks for asking.",
    "name": "I am an NLTK based chatbot.",
    "help": "Sure! Tell me what you need help with.",
    "goodbye": "Goodbye! Have a nice day 👋"
}


def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]


def get_intent(tokens):
    for intent, keywords in responses.items():
        for word in tokens:
            if word in keywords:
                return intent
    return None


def chat():
    greet()
    while True:
        user_input = input("You:")
        tokens = preprocess(user_input)
        intent = get_intent(tokens)
        if intent:
            print("chatbot:", reply[intent])
            if intent == "goodbye":
                break
        else:
            print("chatbot: Sorry, I don't understand that.")


chat()
