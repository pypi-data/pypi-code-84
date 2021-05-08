# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:22:39 2020

@author: Kowsher
"""
from os import path
this_directory = path.abspath(path.dirname(__file__))
font = this_directory+'/kalpurush.ttf'

from scipy.sparse import csr_matrix
import os
import regex 
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence, PathLineSentences
import multiprocessing
from time import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm
import logging  # Setting up the loggings to monitor gensim
from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.feature_extraction.text import TfidfVectorizer as tidf
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

from gensim.models import FastText
from glove import Corpus, Glove
#!pip install glove_python


from sklearn.feature_extraction.text import HashingVectorizer


class gram(object):
    def __init__(self):
      pass
    def n_gram(self, x, n):
        y = []
        idx = 0
        ln = len(x)
        cnt = 0
        temp = ""
        while idx<ln:
            temp = temp +x[idx]
            idx += 1
            cnt +=1

            if cnt ==n:
                y.append(temp)
              
                temp = ""
                cnt = 0
                idx = idx + 1 - n
                        
        return y

class HashVectorizer(object):
    def __init__(self):
      self.sz = 0
    def fit_transform(self, corpus, features_n):
      self.vectorizer = HashingVectorizer(n_features=features_n)
      X = self.vectorizer.fit_transform(corpus)
      return X
    
    def transform(self, corpus):
      Y = self.vectorizer.transform(corpus)
      return Y



class CountVectorizer(object):
    
    def __init__(self):
         self.sz = 0
         self.wordSet = set()
    
    def custom_analyzer(self,text):
        words = regex.findall(r'\w{1,}', text) # extract words of at least 2 letters
        for w in words:
            yield w

    def fit_transform(self,doc):
        self.count_vect = cv(analyzer = self.custom_analyzer)
        train = self.count_vect.fit_transform(doc).toarray()
        return train

    def get_wordSet(self):
        return self.wordSet
    
    def transform(self, pat):
        test = self.count_vect.transform(pat).toarray()
        return test

    def get_feature_names(self):
        return self.count_vect.get_feature_names()
         

class TfIdfVectorizer(object):
    
    def __init__(self):
        self.sz = 0
        self.wordSet = set()
    
    def custom_analyzer(self, text):
        words = regex.findall(r'\w{1,}', text) # extract words of at least 2 letters
        for w in words:
            yield w

    def fit_transform(self, docA):
        self.vectorizer = tidf(analyzer = self.custom_analyzer)
        train = self.vectorizer.fit_transform(docA).toarray()
        return train

    def transform(self, doca):
        test = vectorizer.transform(doca).toarray()
        return test
        
    def coefficients(self):
        return self.wordSet, self.idfs

    def get_feature_names(self):
        return self.vectorizer.get_feature_names()
         


class BN_Word2Vec(object):
  """
    Parameters:
    -----------
    sg : {0, 1}, optional Training algorithm: 1 for skip-gram;otherwise CBOW.

    max_vocab_size : int, optional
        Limits the RAM during vocabulary building; if there are more unique
        words than this, then prune the infrequent ones. Every 10 million word types need about 1GB of RAM.
        Set to `None` for no limit.

    min_count = int - Minimium frequency count of words. The model would ignore words that do not statisfy the min_count.
    window = int - The maximum distance between the target word and its neighboring word. If your neighbor's position is 
                    greater than the maximum window width to the left and the right, then, some neighbors are not considered 
                    as being related to the target word. In theory, a smaller window should give you terms that are more related. If you have lots of data, 
                    then the window size should not matter too much, as long as its a decent sized window.
    size = int - Dimensionality of the feature vectors. - (50, 300)
    sample = float - The threshold for configuring which higher-frequency words are randomly downsampled. Highly influencial. - (0, 1e-5)
    alpha = float - The initial learning rate - (0.01, 0.05)
    min_alpha = float - Learning rate will linearly drop to min_alpha as training progresses. To set it: alpha - (min_alpha * epochs) ~ 0.00
    negative = int - If > 0, negative sampling will be used, the int for negative specifies how many "noise words" should be drown. If set to 0, no negative sampling is used. - (5, 20)
    workers = int - How many threads to use behind the scenes? (=faster training with multicore machines)

  """
  def __init__(self, model_name='w2v_model', sentences=None , corpus_file=None , corpus_path=None,df=None, size=200, window=5, min_count=5,
                  max_vocab_size=None, sample=6e-5, workers=3, alpha=0.03, min_alpha=0.005,sg=0):
    self.model_name = model_name
    self.sentences=sentences
    self.corpus_file=corpus_file
    self.corpus_path=corpus_path
    self.df=df
    self.size=size
    self.alpha=alpha
    self.window=window
    self.min_count=min_count
    self.max_vocab_size=max_vocab_size
    self.sample=sample
    self.workers=workers
    self.min_alpha=min_alpha
    self.sg=sg
    try:
      self.w2v_model = Word2Vec.load(self.model_name)
    except:
      print("No pretrained model is given")
    
  def train(self, epochs=30):
    """
    Train with own Data(s)
    Support single or multiple corpus or dataframe.
    Parameters:
    -----------
    model_name(optional): preferred model name
    epochs : int : total epochs for training

    Example
    --------
    >>> from BnVec import BN_Word2Vec

    #Training Against Sentences
    >>> w2v = BN_Word2Vec(sentences=[['আমার', 'প্রিয়', 'জন্মভূমি'], ['বাংলা', 'আমার', 'মাতৃভাষা'], ['বাংলা', 'আমার', 'মাতৃভাষা'], ['বাংলা', 'আমার', 'মাতৃভাষা'], ['বাংলা', 'আমার', 'মাতৃভাষা'] ])
    >>> w2v.train()

    #Training Against one Text Corpus
    >>> w2v = BN_Word2Vec(corpus_file="path to data or txt file")
    >>> w2v.train()

    #Training Against Multiple Corpuses
    path
      ->corpus
        ->1.txt
        ->2.txt
        ->3.txt

    >>> w2v = BN_Word2Vec(corpus_path="path/corpus")
    >>> w2v.train(epochs=25)


    #Training Against a Dataframe Column
    >>> w2v = BN_Word2Vec(df= news_data['text_content'])
    >>> w2v.train(epochs=25)

    """
    if not(self.sentences) and  not(self.corpus_file) and not(self.corpus_path) and self.df is None:
      raise Exception('Data is not given')
    elif self.sentences:
      data = self.sentences
      print("got sentence")
    elif self.corpus_file:
      print("got sentence")
      data = PathLineSentences(self.corpus_file)
    elif self.corpus_path:
      print("got sentence")
      data = PathLineSentences(self.corpus_path)
    elif self.df is not None:
      print("Dataframe got")
      data = '\n'.join(self.df)
      data = data.split('\n')
      data = [sent.split() for sent in data]
    else:
      print("Unexpected error occured: Please check your data file again.")
    
    
    cpu_cores = multiprocessing.cpu_count()
    w2v_model = Word2Vec(
                        size=self.size,
                        alpha=self.alpha,
                        window=self.window,
                        min_count=self.min_count,
                        max_vocab_size=self.max_vocab_size,
                        sample=self.sample,
                        workers=self.workers,
                        min_alpha=self.min_alpha,
                        sg=self.sg
                       )

 
    print("Working with "+str(self.workers)+" worker threads")
    w2v_model.build_vocab(data, progress_per=10000)
    print("Vocabulary build Successfully")
    t=time()
    w2v_model.train(data, total_examples=w2v_model.corpus_count, epochs=epochs, report_delay=1)
    print('Training took : {} mins'.format(round((time() - t) / 60, 2)))
    w2v_model.save(self.model_name)
    try:
      self.w2v_model = Word2Vec.load(self.model_name)
    except:
      print("No model is loded")



  def get_wordVector(self, word=''):
    """
    Get Word Vector given the model
    Parameters:
    ------------ 
    word : str : the query word for which the vector will be extracted
    model_path: model name or the full path if model is not in current directory


    Examples:
    ----------
    >>> from BnVec import BN_Word2Vec 
    >>> w2v = BN_Word2Vec(model_name='give the model name here')
    >>> w2v.get_wordVector('আমার')
    """
    
    return self.w2v_model.wv[word]


  def get_similarity(self, w1, w2):
    """
    Compute cosine similarity between two words.

    Parameters:
    ----------
    w1 : str : Input word.
    w2 : str : Input word.
 
    Examples:
    ----------
    >>> from BnVec import BN_Word2Vec 
    >>> w2v = BN_Word2Vec(model_name='give the model name here')
    >>> w2v.get_similarity('ঢাকা', 'রাজধানী')

    """

    
    return self.w2v_model.wv.similarity(w1, w2)


  def get_n_similarWord(self,words, n=5):

    """
    Returns topn n similar words of given words

    Parameters:
    ----------
    words : list of str : List of words whose similar words to be found
    n: int : number of similar words to be returned

    Examples:
    ----------
    >>> from BnVec import BN_Word2Vec 
    >>> w2v = BN_Word2Vec(model_name='give the model name here')
    >>> w2v.get_n_similarWord(['পদ্মা'], n=10)

    """


    return self.w2v_model.wv.most_similar(words, topn=n)

  def get_outputWord(self, words_list, n=5):
    """
    Get the probability distribution of the center word given words list.

    Parameters
    ----------
    words_list : list of str : List of context words
    n : int : number of predicted words 

    Examples:
    ----------
    >>> from BnVec import BN_Word2Vec 
    >>> w2v = BN_Word2Vec(model_name='give the model name here')
    >>> w2v.get_outputWord(['ঢাকায়', 'মৃত্যু'], n=2)
    Probable Outputs:
    [("হয়েছে।',", 0.05880642), ('শ্রমিকের', 0.05639163)]

    """
 
    return self.w2v_model.predict_output_word(words_list, topn=n)

  def get_mostFrequent(self, n=5):
    """
    Get top n frequent words from the vocabulary

    Parameters:
    -----------
    n : int : number pf frequrnt words to be returned

    Example:
    --------
    >>> from BnVec import BN_Word2Vec 
    >>> w2v = BN_Word2Vec(model_name='give the model name here')
    >>> w2v.get_mostFrequent(n=5)
    """
    pass
  def get_oddWords(self, wordlist):
    """
    Get the odd word out from given words list

    Parameters:
    ------------
    wordlist : list of str : list of some words

    Example:
    --------
    >>> from BnVec import BN_Word2Vec 
    >>> w2v = BN_Word2Vec(model_name='give the model name here')
    >>> w2v.get_oddWords(['চাল', 'ডাল', 'চিনি', 'আকাশ']) # 'আকাশ' is mostly odd here
    Probable Outputs:
     'আকাশ' 

    """
    
    return self.w2v_model.wv.doesnt_match(wordlist)

  def get_similarity_plot(self, word, n=5):
      """
      Gives a barplot of similar words with their probability 

      Parameter:
      ----------
      word : str : Similarity of which is to be drawn
      n : int : number of similar words to be found

      Example:
      ---------
      >>> from BnVec import BN_Word2Vec 
      >>> w2v = BN_Word2Vec(model_name='give the model name here')
      >>> w2v.get_similarity_plot('চাউল', 5)

      """
      get_sim = self.get_n_similarWord([word], n=n)
      simwords = [x[0] for x in get_sim]
      similarity = [x[1]*100 for x in get_sim]
      prop = mfm.FontProperties(fname=font)
      y_pos = np.arange(len(simwords))
      plt.figure(figsize=(12,6))
      plt.title('Similar words of \''+word+'\'', fontproperties=prop, size='18')
      # Create horizontal bars
      plt.bar(y_pos, similarity)
      # Create names on the y-axis
      plt.xticks(y_pos, simwords, fontproperties=prop, fontsize=16)
      # Show graphic
      plt.show()



        


class BN_FastText(object):
  """
    Parameters:
    -----------
    sg : {0, 1}, optional Training algorithm: 1 for skip-gram;otherwise CBOW.

    max_vocab_size : int, optional
        Limits the RAM during vocabulary building; if there are more unique
        words than this, then prune the infrequent ones. Every 10 million word types need about 1GB of RAM.
        Set to `None` for no limit.

    min_count = int - Minimium frequency count of words. The model would ignore words that do not statisfy the min_count.
    window = int - The maximum distance between the target word and its neighboring word. If your neighbor's position is 
                    greater than the maximum window width to the left and the right, then, some neighbors are not considered 
                    as being related to the target word. In theory, a smaller window should give you terms that are more related. If you have lots of data, 
                    then the window size should not matter too much, as long as its a decent sized window.
    size = int - Dimensionality of the feature vectors. - (50, 300)
    sample = float - The threshold for configuring which higher-frequency words are randomly downsampled. Highly influencial. - (0, 1e-5)
    alpha = float - The initial learning rate - (0.01, 0.05)
    min_alpha = float - Learning rate will linearly drop to min_alpha as training progresses. To set it: alpha - (min_alpha * epochs) ~ 0.00
    negative = int - If > 0, negative sampling will be used, the int for negative specifies how many "noise words" should be drown. If set to 0, no negative sampling is used. - (5, 20)
    workers = int - How many threads to use behind the scenes? (=faster training with multicore machines)

  """
  def __init__(self, model_name='ft_model', sentences=None , corpus_file=None , corpus_path=None,  df=None, size=200, window=5, 
               min_count=5,max_vocab_size=None, sample=6e-5, workers=3, alpha=0.03, min_alpha=0.005,sg=0,negative=20):
    "this is another docstring"
    self.model_name = model_name
    self.sentences=sentences
    self.corpus_file=corpus_file
    self.corpus_path=corpus_path
    self.df=df
    self.size=size
    self.alpha=alpha
    self.window=window
    self.min_count=min_count
    self.max_vocab_size=max_vocab_size
    self.sample=sample
    self.workers=workers
    self.min_alpha=min_alpha
    self.sg=sg
    self.negative=negative
    try:
      self.ft_model = FastText.load(self.model_name)
    except:
      print("No pretrained model is given")
    
  def train(self, epochs=30):
    """
    Train with own Data(s)
    Support single or multiple corpus or dataframe.
    Parameters:
    -----------
    model_name(optional): preferred model name
    epochs : int : total epochs for training

    Example
    --------
    >>> from BnVec import BN_FastText

    #Training Against Sentences
    >>> ft = BN_FastText(sentences=[['আমার', 'প্রিয়', 'জন্মভূমি'], ['বাংলা', 'আমার', 'মাতৃভাষা'], ['বাংলা', 'আমার', 'মাতৃভাষা'], ['বাংলা', 'আমার', 'মাতৃভাষা'], ['বাংলা', 'আমার', 'মাতৃভাষা'] ])
    >>> ft.train()

    #Training Against one Text Corpus
    >>> ft = BN_FastText(corpus_file="path_to_corpus.txt")
    >>> ft.train()

    #Training Against Multiple Corpuses
    path
      ->corpus
        ->1.txt
        ->2.txt
        ->3.txt

    >>> ft = BN_FastText(corpus_path="path/corpus")
    >>> ft.train(epochs=25)

    #Training Against a Dataframe Column

    >>> ft = BN_FastText(df= news_data['text_content'])
    >>> ft.train(epochs=25)

"""
    if not(self.sentences) and  not(self.corpus_file) and not(self.corpus_path) and self.df is None:
      raise Exception('Data is not given')
    elif self.sentences:
      data = self.sentences
      #print("got sentence")
    elif self.corpus_file:
      #print("got sentence")
      data = PathLineSentences(self.corpus_file)
    elif self.corpus_path:
      #print("got sentence")
      data = PathLineSentences(self.corpus_path)
    elif self.df is not None:
      #print("Dataframe got")
      data = '\n'.join(self.df)
      data = data.split('\n')
      data = [sent.split() for sent in data]
    else:
      print("Unexpected error occured: Please check your data file again.")
    
    
    cpu_cores = multiprocessing.cpu_count()
    ft_model = FastText(
                        size=self.size,
                        alpha=self.alpha,
                        window=self.window,
                        min_count=self.min_count,
                        max_vocab_size=self.max_vocab_size,
                        sample=self.sample,
                        workers=self.workers,
                        min_alpha=self.min_alpha,
                        sg=self.sg,
                        negative=self.negative
                       )

 
    print("Working with "+str(self.workers)+" worker threads")
    ft_model.build_vocab(data,  progress_per=10000)
    print("Vocabulary build Successfully")
    t=time()
    ft_model.train(data, total_examples=ft_model.corpus_count, epochs=epochs, report_delay=1)
    print('Training took : {} mins'.format(round((time() - t) / 60, 2)))
    ft_model.save(self.model_name)
    print(ft_model)

    try:
      self.ft_model = FastText.load(self.model_name)
    except:
      print("No model is loaded")



  def get_wordVector(self, word=''):
    """
    Get Word Vector given the model
    Parameters:
    ------------ 
    word : str : the query word for which the vector will be extracted
    model_path: model name or the full path if model is not in current directory


    Examples:
    ----------
    >>> from BnVec import BN_FastText 
    >>> ft = BN_FastText(model_name='give the model name/path here')
    >>> ft.get_wordVector('আমার')
    """
    
    return self.ft_model[word]


  def get_similarity(self, w1, w2):
    """
    Compute cosine similarity between two words.

    Parameters:
    ----------
    w1 : str : Input word.
    w2 : str : Input word.
 
    Examples:
    ----------
    >>> from BnVec import BN_FastText 
    >>> ft = BN_FastText(model_name='give the model name here')
    >>> ft.get_similarity('ঢাকা', 'রাজধানী')

    """

    
    return self.ft_model.similarity(w1, w2)


  def get_n_similarWord(self,words, n=5):

    """
    Returns topn n similar words of given words

    Parameters:
    ----------
    words : list of str : List of words whose similar words to be found
    n: int : number of similar words to be returned

    Examples:
    ----------
    >>> from BnVec import BN_FastText 
    >>> ft = BN_FastText(model_name='give the model name here')
    >>> ft.get_n_similarWord(['পদ্মা'], n=10)

    """

    
    return self.ft_model.most_similar(words, topn=n)


  def get_mostFrequent(self, n=5):
    """
    Get top n frequent words from the vocabulary

    Parameters:
    -----------
    n : int : number pf frequrnt words to be returned

    Example:
    --------
    >>> from BnVec import BN_FastText 
    >>> ft = BN_FastText(model_name='give the model name here')
    >>> ft.get_mostFrequent(n=5)
    """
    pass
  def get_oddWords(self, wordlist):
    """
    Get the odd word out from given words list

    Parameters:
    ------------
    wordlist : list of str : list of some words

    Example:
    --------
    >>> from BnVec import BN_FastText 
    >>> ft = BN_FastText(model_name='give the model name here')
    >>> ft.get_oddWords(['চাল', 'ডাল', 'চিনি', 'আকাশ']) # 'আকাশ' is mostly odd here
    Probable Outputs:
     'আকাশ' 

    """
    
    return self.ft_model.wv.doesnt_match(wordlist)

  def get_similarity_plot(self, word, n=5):
      """
      Gives a barplot of similar words with their probability 

      Parameter:
      ----------
      word : str : Similarity of which is to be drawn
      n : int : number of similar words to be found

      Example:
      ---------
      >>> from BnVec import BN_FastText 
      >>> ft = BN_FastText(model_name='give the model name here')
      >>> ft.get_similarity_plot('চাউল', 5)

      """
      get_sim = self.get_n_similarWord([word], n=n)
      simwords = [x[0] for x in get_sim]
      similarity = [x[1]*100 for x in get_sim]
      prop = mfm.FontProperties(fname=font)
      y_pos = np.arange(len(simwords))
      plt.figure(figsize=(12,6))
      plt.title('Similar words of \''+word+'\'', fontproperties=prop, size='18')
      # Create horizontal bars
      plt.bar(y_pos, similarity)
      # Create names on the y-axis
      plt.xticks(y_pos, simwords, fontproperties=prop, fontsize=16)
      # Show graphic
      plt.show()

  def index2word(self, index):
    return self.ft_model.wv.index2word[index]

from gensim.models.word2vec import LineSentence, PathLineSentences
import multiprocessing
from time import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm

from glove import Corpus, Glove
