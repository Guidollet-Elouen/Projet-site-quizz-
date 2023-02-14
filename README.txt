README

We made a quizz site using the framework Django. This site allows you to chose the type of questions you want to answer (MCQ, Open Questions, Number Questions and Comparison Questions) and displays a few questions for you to answer. 
Prior to launching the website, download the following libraries : 
gensim, spacy, nltk

In config.py, switch the path "road" to the right one. Same thing for "nlp_base", you have to download the file "https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g" and refer its path in nlp_base

Maybe you will need to make these 5 commands : 
nltk.download('averaged_perceptron_tagger')
nltk.download("maxent_ne_chunker")
nltk.download("maxent_treebank_pos_tagger")
nltk.download("stopwords")
nltk.download("words")
nltk.download("universal_tagset")

Maybe you will have problem with spacy.load("en_core_web_sm"), if it is you must make 'python -m spacy download en_core_web_sm' in your terminal to install the package.

To launch the website, one has to :

- Go in the file directory in the terminal :
- run « python manage.py runserver » in the terminal 
- Copy paste the given URL in a browser
- Answer the questions !
