# Import necessary modules
# import re
from nltk.tokenize import sent_tokenize, word_tokenize
import os
import sys
sys.path.append(os.getcwd().split('/NLP')[0])

from nlp_utils import get_sample_Santo_Graal


# Split scene_one into sentences: sentences
# scene_one = get_sample_Santo_Graal()
scene_one = get_sample_Santo_Graal()
sentences = sent_tokenize(scene_one)
print(sentences)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])
print(tokenized_sent)

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)