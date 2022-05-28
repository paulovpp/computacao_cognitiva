import stanza 

nlp = stanza.Pipeline(lang='en', processors='tokenize') 
doc = nlp('This is a test sentence for stanza. This is another sentence.') 
for i, sentence in enumerate(doc.sentences):     
    print(f'====== Sentence {i+1} tokens =======')     
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
    
# ====== Sentence 1 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: a 
# id: 4   text: test 
# id: 5   text: sentence 
# id: 6   text: for 
# id: 7   text: stanza 
# id: 8   text: . 
# ====== Sentence 2 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: another 
# id: 4   text: sentence 
# id: 5   text: .

print([sentence.text for sentence in doc.sentences])

import stanza
nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_no_ssplit=True)
doc = nlp('This is a sentence.\n\nThis is a second. This is a third.')
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
    
# ====== Sentence 1 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: a 
# id: 4   text: sentence 
# id: 5   text: . 
# ====== Sentence 2 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: a 
# id: 4   text: second 
# id: 5   text: . 
# id: 6   text: This 
# id: 7   text: is 
# id: 8   text: a 
# id: 9   text: third 
# id: 10  text: .

# ====== Sentence 1 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: a 
# id: 4   text: sentence 
# id: 5   text: . 
# ====== Sentence 2 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: a 
# id: 4   text: second 
# id: 5   text: . 
# ====== Sentence 3 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: a 
# id: 4   text: third 
# id: 5   text: .

import stanza
nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_pretokenized=True)
doc = nlp('This is token.ization done my way!\nSentence split, too!')
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
    
import stanza
nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_pretokenized=True)
doc = nlp([['This', 'is', 'token.ization', 'done', 'my', 'way!'], ['Sentence', 'split,', 'too!']])
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')

# ====== Sentence 1 tokens =======
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: token.ization 
# id: 4   text: done 
# id: 5   text: my 
# id: 6   text: way! 
# ====== Sentence 2 tokens ======= 
# id: 1   text: Sentence 
# id: 2   text: split, 
# id: 3   text: too!

# ====== Sentence 1 tokens ======= 
# id: 1   text: This 
# id: 2   text: is 
# id: 3   text: token 
# id: 4   text: . 
# id: 5   text: ization 
# id: 6   text: done 
# id: 7   text: my 
# id: 8   text: way 
# id: 9   text: ! 
# ====== Sentence 2 tokens ======= 
# id: 1   text: Sentence 
# id: 2   text: split 
# id: 3   text: , 
# id: 4   text: too 
# id: 5   text: !


# Quizz code:
nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_no_ssplit=True)