'''
TODO: 

* More testing!
* Change 'similarities' from N*N to linear, so that speed is sub-second.
* Write a tutorial, in Jupyter notebook, to show what I did, and how it is SO FRIGGIN COOL!!!
'''


testWord = 'बन्दीप्रतिकोव्यवहारसम्बन्धीमापदण्डअनुकूलको'

def split_word(word):
  '''Takes a word, returns all valid splits of it'''
  splits = list(get_all_substrings(word))
  return startWord(word, splits)
  
def get_all_substrings(string):
  '''takes in an unsegmented string, and depends on the global var 'vocab'.   returns: all substrings of the given string, every string a valid vocab token.
  tokens beginning in markers are invalid tokens
  '''
  length = len(string)
  for i in range(length):
      for j in range(i + 1, length + 1):
          if string[i:j] in vocab and string[i:j][0].isalpha():
              yield(string[i:j])

def genChild(word, token, startPosInWord, endPosInList, tokenList):
  '''Used by startWord. Takes the full word, current token being processed, etc'''
	global parts
	startPos = startPosInWord
	nextWordPos = startPos + len(token)
	nextPos = endPosInList

	if nextWordPos >= len(word):
		#This is the final token
		return [token]
	#There are other tokens to be made

	#if token == 'सम्बन्धी' or 'सम्बन्धी' in token:
	nextChar = word[nextWordPos]
	#occurrences of next in me
	repCount = token.count(nextChar)

	genTokens = wordsStartingIn(nextChar, tokenList[nextPos:], repCount = repCount)
	nextTokens = genTokens[0]
	nextPos = genTokens[1] + nextPos
	#Run this function recursively on each
	toReturn = []
	if len(nextTokens) > 0:
		for tok in nextTokens:
			children = genChild(word, tok, nextWordPos, nextPos, tokenList)
		for child in children:
			if token+child.replace('_','') in word:
				res = token+"_"+child
				toReturn.append(res)
				#parts.add(res)
	return toReturn

def startWord (word, tokenList):
  '''Semi-helper for genChild. processes the token-creation by taking a word, and all valid splits'''
	seedWords = wordsStartingIn(word[0], tokenList)
	words = seedWords[0]
	lastPos = seedWords[1]
	tot = []
	for each in words:
		res = genChild(word, each, 0, lastPos, tokenList)
		tot+=res
	return tot

def sortMe(words):
  '''Sorts the different possible splits by their similarities to each other from Word2Vec'''
	return sorted(words, key=lambda x: similarities(x.split('_'), model))

	
def wordsStartingIn(startingChar, curTokenList, repCount = 0):
  '''Returns the words in curToken list that start with startingChar.
  repCount is the number of occurrences of the char inside the target word of interest.
  '''
	global counter
	counter += 1
	i = 0
	tokenList = curTokenList
	if len(tokenList)>0:
		while repCount >= 0:
			while i <len(tokenList) and startingChar != tokenList[i][0]:
				i += 1
			#Now that we have the position:
			match_toks = []
			while i< len(tokenList) and startingChar == tokenList[i][0]:
				if repCount == 0:
					match_toks.append(tokenList[i])
				i += 1
			repCount -=1
		return match_toks, i
	return [], len(curTokenList)
	
def similarities(wordList, model):
  '''Sort the words in wordlist according to similarities as given by model'''
	totalScore = 0
	for i in range(len(wordList)):
		for j in range(i+1, len(wordList)):
			totalScore += model.n_similarity(wordList[i], wordList[j])
	return totalScore/len(wordList)
