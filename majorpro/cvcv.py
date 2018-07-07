
# coding: utf-8

# In[33]:


import logging
from pprint import pprint
from six import iteritems
from gensim import corpora

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MyCorpus(object):
    def __init__(self, text_file='/home/ranvir/Documents/rgithub/gensim/majorpro/media/documents/soul.txt', dictionary=None):
        """
        Checks if a dictionary has been given as a parameter.
        If no dictionary has been given, it creates one and saves it in the disk.
        """
        self.file_name = text_file
        if dictionary is None:
            self.prepare_dictionary()
        else:
            self.dictionary = dictionary

    def __iter__(self):
        for line in open(self.file_name):
            # assume there's one document per line, tokens separated by whitespace
            yield self.dictionary.doc2bow(line.lower().split())

    def prepare_dictionary(self):
        stop_list = set('for a of the and to in'.split())  # List of stop words which can also be loaded from a file.

        # Creating a dictionary using stored the text file and the Dictionary class defined by Gensim.
        self.dictionary = corpora.Dictionary(line.lower().split() for line in open(self.file_name))

        # Collecting the id's of the tokens which exist in the stop-list
        stop_ids = [self.dictionary.token2id[stop_word] for stop_word in stop_list if
                    stop_word in self.dictionary.token2id]

        # Collecting the id's of the token which appear only once
        once_ids = [token_id for token_id, doc_freq in iteritems(self.dictionary.dfs) if doc_freq == 1]

        # Removing the unwanted tokens using collected id's
        self.dictionary.filter_tokens(stop_ids + once_ids)

        # Saving dictionary in the disk for later use:
        self.dictionary.save('dictionary.dict')

#my_memory_fiendly_corpus = MyCorpus()
#
## Saving the corpus
## corpora.MmCorpus.serialize('corpus.mm', my_memory_fiendly_corpus)
#
## To load the saved corpus:
## corpus = corpora.MmCorpus('corpus.mm')
#
#print('********The dictionary*******')
#pprint(my_memory_fiendly_corpus.dictionary.token2id)
#print("The memory on which corpus is stored is:")
#print(my_memory_fiendly_corpus)
#print('\n********The corpus********')
#for vector in my_memory_fiendly_corpus:
#    print(vector)
#
