
# coding: utf-8

# In[1]:

import nltk
import random


# In[2]:

TAGS = {
    "NN"  : "<noun>",
    "NNS" : "<plural_noun>",
    "NNP" : "<proper_noun>",
    "VB"  : "<verb>",
    "VBD" : "<verb_past_tense>",
    "VBG" : "<verb_ending_with_ing>",
    "JJ"  : "<adjective>",
    "RB"  : "<adverb>",
    "UH"  : "<interjection>" }


# In[3]:

str = """The club isn't the best place to find a lover /n
So the bar is where I go
Me and my friends at the table doing shots... Drinking fast and then we talk slow
And you come over and start up a conversation with just me
And trust me I'll give it a chance now
Take my hand, stop, put Van the Man on the jukebox
And then we start to dance, and now I'm singing like"""


# In[4]:

tokens = nltk.word_tokenize(str)
tagged = nltk.pos_tag(tokens)
suffleable = tagged
print tagged


# In[5]:

replaceable = []
for word in tagged:
    if (TAGS.has_key(word[1])):
        replaceable.append(word)
print replaceable


# In[6]:

random.shuffle(replaceable)
for pos in replaceable[0:9]:
    tokens = [word.replace(pos[0], TAGS[pos[1]]) for word in tokens]
libbed = " ".join(tokens)
print libbed


# In[ ]:




# In[ ]:



