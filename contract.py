import PyPDF2
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Open the PDF file
pdf_file = open('AnC2.pdf', 'rb')

# Read the PDF file
read_pdf = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(read_pdf.pages)

# Create a string to store the text from the PDF file
text = ''

# Iterate over the pages in the PDF file
for i in range(num_pages):

    # Get the current page
    page = read_pdf.pages[i]

    # Add the text from the current page to the string
    text += page.extract_text()

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Get the stop words in English
stop_words = set(stopwords.words('english'))

# Create a list to store the cleaned sentences
cleaned_sentences = []

# Iterate over the sentences
for sentence in sentences:

    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Create a list to store the cleaned words
    cleaned_words = []

    # Iterate over the words
    for word in words:

        # If the word is not a stop word, add it to the list of cleaned words
        if word.lower() not in stop_words:
            cleaned_words.append(word)

    # Create a string from the list of cleaned words
    cleaned_sentence = ' '.join(cleaned_words)

    # Add the cleaned sentence to the list of cleaned sentences
    cleaned_sentences.append(cleaned_sentence)

# Create a function to parse the question and identify the key concepts
def parse_question(question):

    # Split the question into words
    words = question.split()

    # Remove stop words from the question
    cleaned_words = [word for word in words if word not in stop_words]

    # Identify the key concepts in the question
    key_concepts = []
    for word in cleaned_words:
        if word.istitle():
            key_concepts.append(word)

    return key_concepts

# Create a function to search the text for relevant information
def search_text(key_concepts):

    # Iterate over the cleaned sentences
    for sentence in cleaned_sentences:

        # Find the sentences that contain the key concepts
        if all(key_concept in sentence for key_concept in key_concepts):
            return sentence

    return None

# Create a function to answer the question
def answer_question(question):

    # Parse the question to identify the key concepts
    key_concepts = parse_question(question)

    # Search the text for relevant information
    relevant_information = search_text(key_concepts)

    # Return the relevant information
    if relevant_information is not None:
        return relevant_information
    else:
        return "Sorry, I could not find an answer to your question."

# Create a function to create a bot
def create_bot():

    # Create a new bot
    bot = None

    # Train the bot on the text from the PDF file
    #bot.train(text)

    # Return the bot
    return bot

# Create a bot
bot = create_bot()

# Start the bot
#bot.start()

# Get the question from the user
question = input("What is your question? ")

# Answer the question
answer = answer_question(question)

# Print the answer
print(answer)
