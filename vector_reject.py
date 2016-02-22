#A pythonic implementation of @bmschmidt 's 'vector reject'. To be used in gensim.

import numpy as np
from gensim import matutils
from numpy import float32 as REAL
from gensim.models import Word2Vec
from numpy import array
from unicodedata import normalize

print("libraries loaded")
model = Word2Vec.load(r'C:\Users\n0272436\Desktop\datasets\Kantipur')
print("model 1 loaded")
model1 = Word2Vec.load(r'C:\Users\n0272436\Desktop\datasets\v1.model')
print ("model 2 loaded")
def reject(A,B):
  #RAW REJECT, REJECT VECTOR B FROM VEC -A
  '''Create a 'projection', and subract it from the original vector'''
  # project = dot(A, norm(B))*norm(B)
  project = np.linalg.linalg.dot(A, B) * B
  return A - project

def reject_words(A, B):compa
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

def createTranspose(word):
  trans =  ['ु', 'ू', 'ि', 'ी']
  words = []
  for i, each in enumerate(trans):
    if i% 2 ==0:
      words.append(word.replace(each, trans[i+1]))
    else:
      words.append(word.replace(each, trans[i-1]))

  return list(set(words))

#def compareModels(A, B):
    
def reject_words_1(A, B, model = model):
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
  result = [(model.index2word[sim], float(dists[sim])) for sim in best if model.index2word[sim] not in in_words]
  return result
from tabulate import tabulate


def clearRoot(lst, word):
  return [each for each in lst if word not in each]

def compareWords(wordlist1, wordlist2, multimodal = False):
  regular_sim = model.most_similar(wordlist1, negative = wordlist2, topn=200)
  #rejectWords = reject_words_1(wordlist1, wordlist2, model)[:20]
  rejectWords1 = reject_words_1(wordlist1, wordlist2, model)
  r = wordlist1[0]

  if not multimodal:
      printJustified(['regular_sim']+list(list(zip(*regular_sim))[0]),\
                     ['reject_syn0norm']+list(list(zip(*rejectWords1))[0]))
  else:
      regular_sim_1 = model1.most_similar(wordlist1, negative = wordlist2, topn=200)
      rejectWords1_1 = reject_words_1(wordlist1, wordlist2, model1)
      print(\
        tabulate({"mod0_regular_sim": clearRoot(list(list(zip(*regular_sim))[0]), r)[:20],\
                "mod0_reject_syn0norm": clearRoot(list(list(zip(*rejectWords1))[0]), r)[:20],\
                'mod1_regular_sim': clearRoot(list(list(zip(*regular_sim_1))[0]), r)[:20], \
                'mod1_reject_syn0norm' : clearRoot(list(list(zip(*rejectWords1_1))[0]), r)[:20]
                  },\
               headers = 'keys')
        )
      #printJustified(['_mod0_regular_sim']+list(list(zip(*regular_sim))[0]),\
      #               ['reject_syn0norm']+list(list(zip(*rejectWords1))[0]),\
      #               ['_mod1_regular_sim']+list(list(zip(*regular_sim_1))[0]),\
      #               ['_mod1_reject_syn0norm']+list(list(zip(*rejectWords1_1))[0]),\
      #               ) हावा


      
def printJustified(res1, res2, res3, res4):
  zp = zip(res1, res2, res3, res4)
  for each in zp:
    l1 = len(each[0])-len(normalize('NFD', each[0]))
    l2 = len(normalize('NFD', each[1]))
    l3 = len(normalize('NFD', each[2]))
    print ('| '+each[0].ljust(15)+'|'+ each[1].ljust(15)+'| '+each[2].ljust(15)+' |'+each[3].ljust(15))
