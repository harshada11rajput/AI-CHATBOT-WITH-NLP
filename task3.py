import nltk
from nltk.chat.util import Chat, reflections

# Define pairs in list 
pairs = [
    [ r"hi|hello|hey", ["Hello! Welcome to the Python chatbot!", "Hi there! How can I help you with Python today?"] ],
    [ r"how are you", ["I'm doing well, thanks for asking! I'm here to help with any Python-related questions you may have."] ],
    [ r"what is python", ["Python is a high-level, interpreted programming language that is widely used for web development, data analysis, and more."] ],
    [ r"what is python used for", ["Python is used for web development, data analysis, machine learning, automation, and more."] ],
    [ r"how do i learn python", ["You can learn Python through online tutorials, books, and practice. Some popular resources include Codecademy, Coursera, and edX."] ],
    [ r"what is your favorite python library", ["Some popular Python libraries include NumPy, Pandas, and scikit-learn."] ],
    [ r"what is the difference between python 2 and python 3", ["Python 2 and Python 3 are two different versions of the Python programming language. Python 3 is the latest version and is recommended for most use cases."] ],
    [ r"quit", ["Goodbye!"] ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chat
print("Welcome to the Python chatbot! Type 'quit' to exit.")
chatbot.converse()
