import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer

# Descargar recursos necesarios (solo ejecutar una vez)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

def normalizar_texto(texto):
    # Eliminar stopwords
    stop_words = set(stopwords.words('spanish'))
    palabras = word_tokenize(texto)
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words]
    
    # Lematización y stemming
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    palabras_normalizadas = [lemmatizer.lemmatize(stemmer.stem(palabra)) for palabra in palabras_filtradas]
    
    return ' '.join(palabras_normalizadas)

def analizar_sentimientos(texto):
    sia = SentimentIntensityAnalyzer()
    puntuacion = sia.polarity_scores(texto)
    if puntuacion['compound'] > 0:
        return "Positivo"
    elif puntuacion['compound'] < 0:
        return "Negativo"
    else:
        return "Neutro"
