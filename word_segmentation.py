'''
TODO: 
* There's an annoying bug that will cut off the last char on certain strings but not others. Fix it.
* More testing!
* Change 'similarities' from N*N to linear, so that speed is sub-second.

'''


testWord = 'बन्दीप्रतिकोव्यवहारसम्बन्धीमापदण्डअनुकूलको'
def get_all_substrings(string):
  '''takes in an unsegmented string, and depends on the global var 'vocab'.
  returns: all substrings of the given string, every string a valid vocab token.
  tokens beginning in markers are invalid tokens
  '''
    length = len(string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            if string[i:j] in vocab and string[i:j][0].isalpha():
                yield(string[i:j])

def genChild(word, token, startPosInWord, endPosInList, tokenList):
	global parts
	startPos = startPosInWord
	nextWordPos = startPos + len(token)
	nextPos = endPosInList
	
	if nextWordPos >= len(word):
		#This is the final token
		return token
	#There are other tokens to be made
	
	#if token == 'सम्बन्धी' or 'सम्बन्धी' in token:
	#	set_trace()
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
				#if 'सम्बन्धी' in child:
				#	#set_trace()
				if token+child.replace('_','') in word:
					res = token+"_"+child
					toReturn.append(res)
					parts.add(res)
				#pdb.set_trace()
	return toReturn

def startWord (word, tokenList):
	seedWords = wordsStartingIn(word[0], tokenList)
	words = seedWords[0]
	lastPos = seedWords[1]
	tot = []
	for each in words:
		res = genChild(word, each, 0, lastPos, tokenList)
		print (len(res))
		tot+=res
	return tot
	
def wordsStartingIn(startingChar, curTokenList, repCount = 0):
	global counter
	counter += 1
	i = 0
	tokenList = curTokenList
	#pdb.set_trace()
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
	totalScore = 0
	for i in range(len(wordList)):
		for j in range(i+1, len(wordList)):
			totalScore += model.n_similarity(wordList[i], wordList[j])
	return totalScore/len(wordList)
