import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re

# Sample paragraph
paragraph = """Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] ⓘ; born 17 September 1950)[a] is an Indian politician who has served as the 14th Prime Minister of India since 26 May 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister outside the Indian National Congress.[3]

Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at the age of eight. At the age of 18, he was married to Jashodaben Modi, whom he abandoned soon after, only publicly acknowledging her four decades later when legally required to do so. Modi became a full-time worker for the RSS in Gujarat in 1971. The RSS assigned him to the BJP in 1985 and he rose through the party hierarchy, becoming general secretary in 1998.[b] In 2001, Modi was appointed Chief Minister of Gujarat and elected to the legislative assembly soon after. His administration is considered complicit in the 2002 Gujarat riots,[c] and has been criticised for its management of the crisis. According to official records, a little over 1,000 people were killed, three-quarters of whom were Muslim; independent sources estimated 2,000 deaths, mostly Muslim.[12] A Special Investigation Team appointed by the Supreme Court of India in 2012 found no evidence to initiate prosecution proceedings against him.[d] While his policies as chief minister were credited for encouraging economic growth, his administration was criticised for failing to significantly improve health, poverty and education indices in the state.[e]"""

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Tokenization: convert paragraph into sentences
sentences = nltk.sent_tokenize(paragraph)
print("Tokenized Sentences:")
print(sentences)

# Stemming
stemmer = PorterStemmer()
print("\nStemmed Words:")
print(stemmer.stem('going'))
print(stemmer.stem('history'))

# Lemmatization
lemmatizer = WordNetLemmatizer()
print("\nLemmatized Word:")
print(lemmatizer.lemmatize("drinking"))

# Text Cleaning
corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])  # replace all special characters
    review = review.lower()  # convert to lowercase
    review = review.split()  # split into words
    review = [word for word in review if word not in set(stopwords.words('english'))]  # remove stopwords
    review = ' '.join(review)  # rejoin words to form the cleaned sentence
    corpus.append(review)

print("\nCleaned Text:")
print(corpus)


##Lemmatization
for i in corpus:
    words = nltk.word_tokenize(i)
    for word in words:
        if word not in set(stopwords.words('english')):
            print(lemmatizer(word))
            
#BOW
from sklearn.feature_extraction.text import CountVectorizer
cv= CountVectorizer()
x=cv.fit_transform(corpus)
cv.vocabulary_
corpus[0]
x[0].toarray()


#Apply Stopwords, Lemmatize
import re
corpus=[]
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])  # replace all special characters
    review = review.lower()  # convert to lowercase
    review = review.split()  # split into words
    review = [word for word in review if word not in set(lemmatizer.lemmatize('english'))]  # remove stopwords
    review = ' '.join(review)  # rejoin words to form the cleaned sentence
    corpus.append(review)








