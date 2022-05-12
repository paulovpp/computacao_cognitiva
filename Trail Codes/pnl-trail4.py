import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')
doc = nlp('Barack Obama was born in Hawaii.')
print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')

# word: Barack    lemma: Barack 
# word: Obama     lemma: Obama 
# word: was       lemma: be 
# word: born      lemma: bear 
# word: in        lemma: in 
# word: Hawaii    lemma: Hawaii 
# word: .         lemma: .