#A pythonic implementation of @bmschmidt 's 'vector reject'. To be used in gensim.

import numpy as np
from gensim import matutils
from numpy import float32 as REAL
from gensim.models import Word2Vec
from numpy import array
from unicodedata import normalize
model = Word2Vec.load(r'C:\Users\spokha01\SkyDrive\Public\Public Datasets\Kantipur')

def reject(A,B):
  #RAW REJECT, REJECT VECTOR B FROM VEC -A
  '''Create a 'projection', and subract it from the original vector'''
  # project = dot(A, norm(B))*norm(B)
  project = np.linalg.linalg.dot(A, B) * B
  return A - project

def reject_words(A, B):
  '''Takes two **LIST OF WORDS** and
  returns most_similar for word A, while rejecting words with meanings closer to B.
  Seems to work better than just giving in negative words.
  ''' 
  in_words = A+B
  basic_word = [model[each] for each in A]
  reject_word = [model[each] for each in B]
  basic_mean = matutils.unitvec(array(basic_word).mean(axis=0)).astype(REAL)
  reject_mean = matutils.unitvec(array(reject_word).mean(axis=0)).astype(REAL)
  r = reject(basic_mean, reject_mean)
  dists = np.linalg.linalg.dot(model.syn0, r)
  best  = matutils.argsort(dists, topn = 500, reverse = True)
  result = [(model.index2word[sim], float(dists[sim])) for sim in best if A[0] not in model.index2word[sim]]
  return result


def reject_words_1(A, B):
  '''Takes two **LIST OF WORDS** and
  returns most_similar for word A, while rejecting words with meanings closer to B.
  Seems to work better than just giving in negative words.
  ''' 
  in_words = A+B
  basic_word = [model[each] for each in A]
  reject_word = [model[each] for each in B]
  basic_mean = matutils.unitvec(array(basic_word).mean(axis=0)).astype(REAL)
  reject_mean = matutils.unitvec(array(reject_word).mean(axis=0)).astype(REAL)
  r = reject(basic_mean, reject_mean)
  dists = np.linalg.linalg.dot(model.syn0norm, r)
  best  = matutils.argsort(dists, topn = 500, reverse = True)
  result = [(model.index2word[sim], float(dists[sim])) for sim in best if A[0] not in model.index2word[sim]]
  return result

def compareWords(wordlist1, wordlist2):
  regular_sim = model.most_similar(wordlist1, negative = wordlist2, topn=200)[:20]
  rejectWords = reject_words(wordlist1, wordlist2)[:20]
  rejectWords1 = reject_words_1(wordlist1, wordlist2)[:20]

  printJustified(['regular_sim']+list(list(zip(*regular_sim))[0]), ['reject_syn0']\
                 +list(list(zip(*rejectWords))[0]),
                 ['reject_syn0norm']+list(list(zip(*rejectWords1))[0]))

  
def printJustified(res1, res2, res3):
  zp = zip(res1, res2, res3)
  for each in zp:
    l1 = len(each[0])-len(normalize('NFD', each[0]))
    l2 = len(normalize('NFD', each[1]))
    l3 = len(normalize('NFD', each[2]))
    print ('| '+each[0].ljust(15)+'|'+ each[1].ljust(15)+'| '+each[2].ljust(15)+' |')
