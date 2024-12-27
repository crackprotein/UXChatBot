import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from knowledge import knowledge

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [stemmer.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

def find_best_response(user_input):
    preprocessed_input = preprocess_text(user_input)
    best_match = None
    max_score = 0

    for key, response in knowledge.items():
        preprocessed_key = preprocess_text(key)
        score = len(set(preprocessed_input) & set(preprocessed_key))

        if score > max_score:
            max_score = score
            best_match = response

    if best_match:
        return best_match
    else:
        return "I'm sorry, I don't understand that question."

def chat():
    print("UX Chatbot: Hello, I'm here to help with your UX questions!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("UX Chatbot: Goodbye!")
            break
        response = find_best_response(user_input)
        print("UX Chatbot:", response)

if __name__ == "__main__":
    chat()