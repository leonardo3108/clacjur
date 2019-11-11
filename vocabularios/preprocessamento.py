# -*- coding: utf-8 -*-
import nltk

# Download do lematizador
#nltk.download('wordnet')
# Realiza o download do corpus de stopwords (de vários idiomas, dentro os quais inglês e português)
#nltk.download('stopwords')
# Download do RSLP
#nltk.download('rslp')
# Download dos POS Tagger do Nltk
#nltk.download('averaged_perceptron_tagger')

def normaliza (textos):
    textos_normalizados = []
    for texto in textos:
        pontuacoes ='?!,.(){}[]\';:"º%'
        for pontuacao in pontuacoes:
            texto = texto.replace(pontuacao ,'')
        texto_normalizado =texto.lower()
        textos_normalizados.append(texto_normalizado)
    return textos_normalizados

def remove_stopwords (textos, idioma ='english'):
    if not idioma in ['english','portuguese']:
        raise Exception ('O idioma "{idioma}" não é suportado.')
    textos_sem_stopwords = []
    stopwords = nltk.corpus.stopwords.words(idioma)
    for texto in textos:
        texto_sem_stopwords = ' '.join ([token.strip() for token in texto.split() if token not in stopwords])
        textos_sem_stopwords .append (texto_sem_stopwords)
    return textos_sem_stopwords

def stemiza (textos):
    stemizador = nltk.stem.PorterStemmer()
    textos_stemizados = []
    for texto in textos:
        texto_stemizado = ' '.join ([stemizador.stem(token) for token in texto.split()])
        textos_stemizados.append (texto_stemizado)
    return textos_stemizados

def mapeia_tag (textos):
    from nltk.corpus import wordnet
    tagger = {'NN': wordnet.NOUN ,'JJ': wordnet.ADJ ,'VB': wordnet.VERB ,'RB': wordnet.ADV }
    if textos [0:2] in tagger:
        return tagger[textos[0:2]]
    else:
        return wordnet.NOUN

def lematiza (textos):
    lematizador =nltk.stem.WordNetLemmatizer()
    textos_lematizados = []
    for texto in textos:
        dupla = nltk.pos_tag(texto.split())
        texto_lematizado =' '.join ([lematizador.lemmatize (token, mapeia_tag (postag)) for token, postag in dupla ])
        textos_lematizados.append (texto_lematizado)
    return textos_lematizados


