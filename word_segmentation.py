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
  '''depends on the gloval var 'parts'. It should be a set
  
  '''
	global parts
	startPos = startPosInWord
	nextWordPos = startPos + len(token)
	nextPos = endPosInList
	
	if nextWordPos >= len(word):
		#This is the final token
		return token
	#There are other tokens to be made
	nextChar = word[nextWordPos]
	genTokens = wordsStartingIn(nextChar, tokenList[nextPos:])
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
					parts.add(res)
				#pdb.set_trace()
	return toReturn


def startWord (word, tokenList):
	seedWords = wordsStartingIn(word[0], tokenList)
	words = seedWords[0]
	lastPos = seedWords[1]
	for each in words:
		res = genChild(word, each, 0, lastPos, tokenList)

	
def wordsStartingIn(startingChar, curTokenList):
	i = 0
	counter += 1
	tokenList = curTokenList
	if len(tokenList)>0:
		while i <len(tokenList) and startingChar != tokenList[i][0]:
			i += 1
		#Now that we have the position:
		match_toks = []
		while i< len(tokenList) and startingChar == tokenList[i][0]:
			match_toks.append(tokenList[i])
			i += 1
		return match_toks, i
	
	return [], len(curTokenList)
