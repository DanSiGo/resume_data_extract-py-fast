import PyPDF2
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def pdf_to_string(file):
        
    with open(file, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    lemmatizer = WordNetLemmatizer()

    text_lower = text.lower()  # converter para minúsculas
    text_no_special_chars = re.sub(r'[^a-zA-Z\s]', '', text_lower)  # remover caracteres especiais
    tokens = word_tokenize(text_no_special_chars)  # tokenizar o texto
    tokens_lemmatized = [lemmatizer.lemmatize(token) for token in tokens]  # lemmatizar
    tokens_no_punct = [token for token in tokens_lemmatized if token.isalpha()]  # remover pontuação
    tokens_no_stopwords = [token for token in tokens_no_punct if token not in nltk.corpus.stopwords.words('english')]  # remover stopwords

    text_final = ' '.join(tokens_no_stopwords)

    return text_final