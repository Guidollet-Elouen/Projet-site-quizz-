import gensim
import spacy
import nltk
from nltk.corpus import stopwords, wordnet
from .wiki_down import get_wiki
import random
import re
from .config import *


#nltk.download('averaged_perceptron_tagger')
#ltk.download("maxent_ne_chunker")
#nltk.download("maxent_treebank_pos_tagger")
#nltk.download("stopwords")
#nltk.download("universal_tagset")

stop_words = set(stopwords.words("english"))
model = gensim.models.KeyedVectors.load_word2vec_format(nlp_base, binary=True)
nlp = spacy.load("en_core_web_sm")


def process_text(text: str):
    """Cleans a sentence into a tokenized, lemmatized and filtered list of words"""

    # Tokenize and lemmatize with spacy
    doc = nlp(text)

    # Get lemmas and remove punctuation
    lemmas = [token.lemma_ for token in doc if token.pos_ != "PUNCT"
              and token.lemma_ not in nlp.Defaults.stop_words]

    return lemmas


def get_sent(text: str):
    """Extracts sentences from a text, removing blank spaces and non sentences"""
    sents = text.split("\n")
    sents = [sent.replace("\xa0", " ") for sent in sents]
    sents = [sent for sent in sents if sent != ""]
    sents = [sent for sent in sents if len(sent.split()) >= 6]
    for sent in sents:
        doc = nlp(sent)
        if doc.has_annotation("DEP"):
            sents.remove(sent)
    return sents


def get_sents(text: str):
    """Extracts sentences from a text, removing blank spaces and non sentences, if the other function returns an
    empty list """
    sents = text.split("\n")
    sents = [sent.replace("\xa0", " ") for sent in sents]
    sents = [sent for sent in sents if sent != ""]
    sents = [sent for sent in sents if len(sent.split()) >= 6]
    return sents


def extract_pos(text: str, tag: str):
    """Extracts the pos of the corresponding tag in the text"""

    # Tokenize and lemmatize with spacy
    doc = nlp(text)

    # Get lemmatized tokens and their pos
    pos = [token.text for token in doc if token.pos_ == tag]
    return pos


def get_pos_tag(word: str):
    """Extracts the pos tag of the word"""
    doc = nlp(word)
    for token in doc:
        return token.pos_


def lexical_methods(phrase1: str, phrase2: str, methods: list):
    """Compares lexical similarity of two "to-be-cleaned" sentences, with the method.s in argument """

    # Clean the sentences
    clean_1 = process_text(phrase1)
    clean_2 = process_text(phrase2)

    # Compare
    ind = comparison_methods(clean_1, clean_2, methods)

    return ind


def lexical_vec(phrase1: str, phrase2: str):
    """Compares the lexical similarity of two "two-be-cleaned" sentences with vectorization"""

    # Clean the sentences
    clean_1 = process_text(phrase1)
    clean_2 = process_text(phrase2)

    # Compare
    ind = comparison_vec(clean_1, clean_2)

    return ind


def get_named_entity_type(text: str):
    """Gets the type of the named entity of the word """
    # Tokenize and tag the text with spacy
    doc = nlp(text)

    # Get the type of the NE
    named_entity_type = None
    for ent in doc.ents:
        named_entity_type = ent.label_

    return named_entity_type


def get_named_entity(text: str, typ: str):
    """Gets the named entity of the corresponding type in the text"""

    # Tokenize and lemmatize the text with spacy
    doc = nlp(text)

    # Get the NE of the specific type
    named_entities = [entity.text for entity in doc.ents if entity.label_ == typ]

    return named_entities


def get_type_solution(solution: str):
    """Extracts the type of the solution : sentence or a word"""

    doc = nlp(solution)

    if len(doc) > 2:
        return "S"
    else:
        return "W"


def get_typ_sent(sent: str):
    """If the solution is a sentence, this function tells if it is a NE or a full sentence """
    doc = nlp(sent)

    named_entities = [entity.text for entity in doc.ents]
    if sent in named_entities:
        return get_named_entity_type(sent)
    else:
        return "SENT"


def get_typ_word(word: str):
    """If the solution is a word, this function tells if it is a NE or a POS """
    doc = nlp(word)

    named_entities = [entity.text for entity in doc.ents]
    if word in named_entities:
        return get_named_entity_type(word)
    else:
        return get_pos_tag(word)


def get_pos(text: str):
    """Extracts the POS of the text in argument"""
    doc = nlp(text)
    return (token.pos_ for token in doc)


def comparison_methods(list1: list, list2: list, methods: list):
    """Compares the two lists of words using the method.s in argument (wup or path) """

    # Compute similarity between the sentences
    similarity = 0
    for word1 in list1:
        for word2 in list2:
            if wordnet.synsets(word1) and wordnet.synsets(word2):
                word1_synset = wordnet.synsets(word1)[0]
                word2_synset = wordnet.synsets(word2)[0]
                for method in methods:
                    if method == 'wup':
                        similarity += word1_synset.wup_similarity(word2_synset)
                    elif method == 'path':
                        similarity += word1_synset.path_similarity(word2_synset)

    # Divide total similarity by number of words to have an average
    return similarity / (len(list1) + len(list2))


def comparison_vec(list1: list, list2: list):
    """Compares similarity between two lists of words using vectorization"""

    # Compute similarity between the sentences
    similarity = 0
    for word1 in list1:
        for word2 in list2:
            if word1 in model and word2 in model:
                similarity += model.similarity(word1, word2)

    # Divide total similarity by number of words to have an average
    return similarity / (len(list1) + len(list2))


def calculate_semantic_similarity_methods(phrase1: str, phrase2: str, methods: list):
    """Computes semantic similarity between two raw sentences, using the method.s in argument (wup or path)"""
    # Tokenize and lemmatize
    words1 = [token.lemma_ for token in nlp(phrase1)]
    words2 = [token.lemma_ for token in nlp(phrase2)]

    return comparison_methods(words1, words2, methods)


def calculate_semantic_similarity_vec(phrase1: str, phrase2: str):
    """Computes semantic similarity between two raw sentences using vectorization"""
    # Tokenize and lemmatize
    words1 = [token.lemma_ for token in nlp(phrase1)]
    words2 = [token.lemma_ for token in nlp(phrase2)]

    return comparison_vec(words1, words2)


def calculate_semantic_similarity(phrase1: str, phrase2: str, methods: list):
    """Computes semantic similarity between two raw sentences using the method.s in argument (wup &/or path, or vec)"""

    # Tokenize and lemmatize
    words1 = [token.lemma_ for token in nlp(phrase1)]
    words2 = [token.lemma_ for token in nlp(phrase2)]

    if methods == ['vec']:
        return comparison_vec(words1, words2)
    else:
        return comparison_methods(words1, words2, methods)


def exact_comparison(list1: list, word: str):
    """Checks if the word is included in the list of words"""

    # put every word in lower cases
    lower_list = [word.lower() for word in list1]
    return word.lower() in lower_list


def path_similarity(word1: str, word2: str):
    token1 = nlp(word1)
    token2 = nlp(word2)
    return token1.similarity(token2)


def make_verification_sent(result: str, solution: str, methods: list):
    """Compares the result and the solution of the open question using raw sentences and
     the method.s in argument (wup &/or path, or vec)"""

    "Methods is a list containing 'vec', 'path', 'wup' or 'path' & 'wup'"

    eps = 0.2  # choice of a threshold of 0.8 for the indicator for which we consider that the sentences are similar
    ref = len(methods)

    ind = calculate_semantic_similarity(result, solution, methods)

    return abs(ref - ind) <= eps


def make_verification_sent_tok(result: str, solution: str, methods: list):
    """Compares the result and the solution of the open question using processed sentences and
     the method.s in argument (wup &/or path, or vec)"""

    eps = 0.2  # choice of a threshold of 0.8 for the indicator for which we consider that the sentences are similar
    ref = len(methods)

    ind = calculate_semantic_similarity(str(process_text(result)), str(process_text(solution)), methods)

    return abs(ref - ind) <= eps


def make_verification_s(result: str, solution: str, methods: list):
    """Compares the result and the solution of the open question if the solution is a sentence"""
    typ = get_typ_sent(solution)
    print(typ)  # test
    # if the solution is a sentence, we need to know if it's an NE or a full sentence
    if typ == 'SENT':  # if full sentence
        return make_verification_sent(result, solution, methods)
    else:
        # if NE
        # extract the corresponding NE of the result then compare to solution
        ne = get_named_entity(result, typ)
        return exact_comparison(ne, solution)


def make_verification_w(result: str, solution: str):
    """Compares the result and the solution of the open question if the solution is a word"""
    typ = get_typ_word(solution)
    # print(typ)  # test
    # print(get_pos_tag(solution))
    # print(get_named_entity_type(solution))
    # if the solution is a word, we need to know if it's an NE or a POS

    if typ == get_named_entity_type(solution):  # if NE
        ne = get_named_entity(result, typ)
        return exact_comparison(ne, solution)

    elif typ == get_pos_tag(solution):  # if POS
        pos = extract_pos(result, typ)
        similarities = []
        for word1 in pos:
            similarities.append(path_similarity(word1, solution))
        rep = False
        for ind in similarities:
            rep = (abs(1 - ind) <= 0.7)  # we choose a threshold of 0.7 for the indicator of path similarity
        return rep


def get_blank_question(header: list):
    """Extracts a blank question from the Wikipedia page title and header"""
    text = random.choice(header)
    doc = nlp(text)
    # for simplicity, we consider that we can only guess nouns, adjectives and dates
    token = [token.text for token in doc if token.pos_ in ['NOUN', 'ADJ', 'NUM']]
    blank = random.choice(token)

    question = re.sub(blank, '_______', text)
    return question, blank


def get_question_person(title: str, header: list):
    """Extracts an open question and its solution from a random Wikipedia page concerning a person"""
    cat = random.choice(['WHO', 'DATE'])
    if cat == 'WHO':
        question = 'Who is ' + title + ' ?'
        solution = header[0]
        return question, solution
    if cat == 'DATE':
        dates = extract_pos(header[0], 'NUM')
        for date in dates:
            if len(date) != 4:
                dates.remove(date)
        if len(dates) < 2:
            question = 'When was born ' + title + ' ?'
            solution = dates[0]
            return question, solution
        else:
            question = 'When did ' + title + ' die ?'
            solution = dates[1]
            return question, solution


def get_question_event(title: str, header: list):
    """Extracts an open question and its solution from a random Wikipedia page concerning an event"""
    cat = random.choice(['GPE', 'DATE'])
    if cat == 'GPE':
        gpe = extract_pos(header[0], 'GPE')
        question = 'Where is/was ' + title + ' ?'
        solution = gpe[0]
        return question, solution
    elif cat == 'DATE':
        dates = extract_pos(header[0], 'NUM')
        question = 'When is/was ' + title + ' ?'
        solution = dates[0]
        return question, solution


def get_question():
    """Extracts an open question and its solution from a random Wikipedia page"""
    wiki = get_wiki()
    title, header = wiki[0], get_sent(wiki[1])
    typ = get_typ_word(title)
    if len(header) == 0:
        header = get_sents(wiki[1])

    # if the title is an NE == 'PERSON', we only keep two questions to make it easier
    if typ == 'PERSON':
        return get_question_person(title, header)
    elif typ == 'EVENT':
        return get_question_event(title, header)
    # if the title is a POS or else, choose randomly between a "what" question or a blank space question
    cat = random.choice(['BLANK', 'WHAT'])
    if cat == 'WHAT':
        question = 'What/Who is ' + title + ' ?'
        solution = header[0]
        return question, solution
    elif cat == 'BLANK':
        return get_blank_question(header)


def nlp_test(result: str, solution: str, methods: list):
    """Compares the result and the solution of the question with the method.s in argument (wup &/or path, or vec)"""
    # Depending on the type typ of the solution we're looking for, we use different methods
    cat = get_type_solution(solution)
    # if sentence
    if cat == 'S':
        return make_verification_s(result, solution, methods)
    # if word
    elif cat == 'W':
        return make_verification_w(result, solution)
