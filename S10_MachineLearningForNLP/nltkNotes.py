#Defining a Corpus
corpus = '''Hello Welcome to Krish Naik's NLP tutorials.
Please do watch the entire course! to become a NLP expert.'''

print(corpus)

#Tokenization
##Sentence to Paragraph
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

documents = sent_tokenize(corpus)
type(documents)
for sentence in documents:
    print(sentence)
print(documents)

##Tokenization

##Paragraph to Words
from nltk.tokenize import word_tokenize
word_tokenize(corpus)

for word in word_tokenize(corpus):
    print(word)
    
for sentence in documents:
    print(word_tokenize(sentence))
    
##New Library for Tokenization - WordPunctTokenizer
from nltk.tokenize import wordpunct_tokenize

##Differnece you will see in the below output is that it will also consider the punctuation as a token like 's and . and ! etc. which is not the case with word_tokenize
print(wordpunct_tokenize(corpus))

##New Library for Tokenization - TreebankWordTokenizer
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()

##Full stop in the middle of the sentence is not considered as a token but it will consider the full stop at the end of the paragraph as a token.
print(tokenizer.tokenize(corpus))

##############################################################

#STEMMING

##Stemming is the process of reducing a word to it's stem
##Classificatio Problem - Comments on product is positive or negative
##Review - eating, eat, eaten,[going, gone, goes]
words = ['eat','eating','eaten','go','going','gone','goes','finally','final','finalize','history','historical','historian']
#Porter Stemmer
from nltk.stem import PorterStemmer
stemming = PorterStemmer()

for word in words:
    ###Issue here is history becomes histori
    print(word+'-->'+stemming.stem(word))
    
print(stemming.stem('Congratulations')) ##You will get congratul

##RegexpStemmerClass - Basically takes an regexp and removes all prefix and suffix

from nltk.stem import RegexpStemmer
reg_stemmer = RegexpStemmer('ing$|s$|e$|able$|ly$', min=4)
print(reg_stemmer.stem('eating'))

##Snowball Stemmer - It is an improvement over porter stemmer and it is also faster than porter stemmer
from nltk.stem import SnowballStemmer
snowballstemmer = SnowballStemmer('english')

for word in words:
    print(word+'-->'+snowballstemmer.stem(word))
    
##PORTER VS SNOWBALL STEMMER
stemming.stem("fairly") ##You will get fairli
stemming.stem("sportingly") ##You will get sport

print(snowballstemmer.stem("fairly")) ##You will get fair
print(snowballstemmer.stem("sportingly")) ##You will get sport

##With the word 'goes' both techniques will fail and give you 'goe' as the output.

##Lemmatization - it gives the root word unlike stem word in the previous case. It is more accurate than stemming but it is also slower than stemming.
## The output we get after lemmatization is called Lemma
## After Lemmatization we get the valid word which means the same thing
##Used in Q&A, chatbors, text summarization

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('going')) ##You will get going as the output because it is not able to understand the context of the word. It is not able to understand that it is a verb and it is in present continuous tense. So, it is not able to lemmatize it to go.

'''
POS - Part of Speech
Noun - n
Verb - v
Adjective - a
Adverb - r
'''

print(lemmatizer.lemmatize('going', pos='v')) ##You will get go as the output because now we have specified that it is a verb and it is in present continuous tense. So, it is able to lemmatize it to go.

words = ['eat','eating','eaten','go','going','gone','goes','finally','final','finalize','history','historical','historian','writing','written','writes']

for word in words:
    print(word+'-->'+lemmatizer.lemmatize(word, pos='v'))
    
lemmatizer.lemmatize("fairly",pos='v'),lemmatizer.lemmatize("sportingly",pos='v') ##You will get fairly and sportingly as the output because it is not able to understand the context of the word. It is not able to understand that it is an adverb. So, it is not able to lemmatize it to fair and sport respectively.

##STOPWORDS

##Speech of Dr APJ Abdul Kalam
paragraph = """I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards. 
The Greeks, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, their history or tried to enforce our way of life on them. Why? 
Because we respect the freedom of others. That is why my first vision is that of FREEDOM.I believe that India got its first vision of this in 1857, when we started the war of independence. It is this freedom that we must protect and nurture and build-up. If we are not free, no one will respect us. Second vision for India is DEVELOPMENT.
For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top 5 nations of the world in terms of GDP. We have 10 percent growth rate in most areas. Our poverty levels are falling, our achievements are being globally recognized today. Yet we lack the self-confidence to see ourselves as a developed nation, self reliant and self assured. Isn't this right?
I have a third vision, that India must stand up to the world. because I believe that unless India stands up to the world, no one will respect us. 
Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand.
My good fortune was to have worked with three great minds i.e. Dr Vikram Sarabhai of the Dept. of space, Professor Satish Dhawan, who succeeded him, and Dr.Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. See four milestones in my career"""

import nltk
nltk.download('stopwords')

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

print(stopwords.words('english'))

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

##Tokenizing the paragraph into words
sentences = nltk.sent_tokenize(paragraph)

print(sentences)

##Apply stopwords and filter and then apply stemming

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))] ##Removing stopwords and applying stemming to the remaining words in the sentences
    sentences[i] = ' '.join(words) ##Converting all words in sentences

print("Result with Stemming")    
print(sentences)

##Applying stopwords and filter and applying snowball stemmer

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [snowballstemmer.stem(word) for word in words if word not in set(stopwords.words('english'))] ##Removing stopwords and applying stemming to the remaining words in the sentences
    sentences[i] = ' '.join(words) ##Converting all words in sentences

print("Result with Snowball")
print(sentences)

##Applying stopwords and filter and applying lemmatization

paragraph = """I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards. 
The Greeks, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, their history or tried to enforce our way of life on them. Why? 
Because we respect the freedom of others. That is why my first vision is that of FREEDOM.I believe that India got its first vision of this in 1857, when we started the war of independence. It is this freedom that we must protect and nurture and build-up. If we are not free, no one will respect us. Second vision for India is DEVELOPMENT.
For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top 5 nations of the world in terms of GDP. We have 10 percent growth rate in most areas. Our poverty levels are falling, our achievements are being globally recognized today. Yet we lack the self-confidence to see ourselves as a developed nation, self reliant and self assured. Isn't this right?
I have a third vision, that India must stand up to the world. because I believe that unless India stands up to the world, no one will respect us. 
Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand.
My good fortune was to have worked with three great minds i.e. Dr Vikram Sarabhai of the Dept. of space, Professor Satish Dhawan, who succeeded him, and Dr.Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. See four milestones in my career"""

nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

sentences = nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word.lower(),pos='v') for word in words if word not in set(stopwords.words('english'))] ##Removing stopwords and applying lemmatization to the remaining words in the sentences
    sentences[i] = ' '.join(words) ##Converting all words in sentences

print("Result with Lemmatization")
print(sentences)

'''
🧠 Key Takeaways
• 	Tokenization splits text into sentences/words.
• 	Stemming chops words to crude roots (fast but less accurate).
• 	Lemmatization returns meaningful root words (accurate but slower).
• 	Stopwords removal helps focus on important words.
• 	Different tokenizers treat punctuation differently.
• 	Snowball Stemmer is generally better than Porter.
• 	Lemmatization requires POS tags for best results.
'''