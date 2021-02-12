#Source: https://programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    #first, make the two different sorted array(for the case like ???aa)
    #first, sort the array in the length order, and then sort it in the lexical order
    #for the case like ???aa, set another array that reverses all the words in it
    backWords = list(map(lambda x: x[::-1], words))
    backWords.sort(key = lambda x: (len(x), x)) 
    words.sort(key = lambda x: (len(x), x))
    answer = []

    for word in queries:
        tf, length = isWordFront(word)
        wordNumber = 0

        #first, find the place where the word length equals the length of query
        leftLength = findLeftLength(words, len(word), 0, len(words)-1)
        rightLength = findRightLength(words, len(word), 0, len(words)-1)
        
        #if no matching length, put 0 into the answer and continue
        if len(word) != len(words[leftLength]):
            answer.append(wordNumber)
            continue
        
        #if the case is like fro???, use the array that is not reversed
        if tf:
            left = findLeft(words, len(word), word[0:length], leftLength, rightLength)
            right = findRight(words, len(word), word[0:length], leftLength, rightLength)
            
            if word[0:length] == words[left][0:length]:
                wordNumber = right - left + 1

        #if the case is like ???aaa, use the array that is reversed              
        else:
            word = word[::-1]
            left = findLeft(backWords, len(word), word[0:length], leftLength, rightLength)
            right = findRight(backWords, len(word), word[0:length], leftLength, rightLength)

            
            if word[0:length] == backWords[left][0:length]:
                wordNumber = right - left + 1
        
        answer.append(wordNumber)

    return answer

#determine the type of the query
def isWordFront(word):
    length = 0
    if word[-1] == "?":
        for i in range(len(word)):
            if word[i] == "?":
                length = i 
                break
        return (True, length)
    
    else:
        for j in range(1, len(word)+1):
            if word[-j] == "?":
                length = j-1
                break
        return (False, length)

#find the leftmost idx of the same length as a query
def findLeftLength(words, originalLength, start, end):
    if start > end:
        return
    
    answer = 0
    
    while start <= end:
        mid = (start + end)//2
        
        if originalLength <= len(words[mid]):
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    
    return answer

#find the rightmost idx of the same length as a query
def findRightLength(words, originalLength, start, end):
    if start > end:
        return
    
    answer = 0
    
    while start <= end:
        mid = (start + end)//2
        
        if originalLength >= len(words[mid]):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    
    return answer

#find the leftmost index of the word that shares the same not?? part with the query
def findLeft(words, originalLength, source, start, end):

    if start > end:
        return

    answer = 0
    sourceLength = len(source)
    
    while start <= end:
        mid = (start + end)//2

        if wordLessEqual(source, words[mid][0:sourceLength]):
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    
    return answer

#find the rightmost idx of the word that shares the same not?? part with the query
def findRight(words, originalLength, source, start, end):

    if start > end:
        return

    answer = 0
    sourceLength = len(source)
    

    while start <= end:
        mid = (start + end)//2

        if wordLessEqual(words[mid][0:sourceLength], source):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer

#determine whether a word is less or equal in the lexical order
def wordLessEqual(source, target):
    array = sorted([source, target])
    if source == array[0]:
        return True
    
    return False