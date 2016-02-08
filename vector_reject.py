#A pythonic implementation of @bmschmidt 's 'vector reject'. To be used in gensim.

import numpy as np
from gensim import matutils
from numpy import float32 as REAL

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
  result = [(model.index2word[sim], float(dists[sim])) for sim in best if model.index2word[sim] not in in_words]
  return result
