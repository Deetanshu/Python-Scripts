# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:41:53 2018

@author: deept
"""

keywordS="auto break case char const continue default do double else enum extern float for goto if int long register return short sign sizeof static struct switch typedef union unsigned void volatile while"
keys=keywordS.split(' ')
stuf=", = . ; ! ~ # \n \t & * ^ + - | < > _ % ( ) [ ] { }"
stuff=stuf.split(' ')
stuff.append(' ')
print (stuff)
brakets=['[',']','(',')','{','}']
print(keys)
cfile=open('test.c','r')
tokens=[]
blocknames=[]
for word in cfile:
    print(word)
    cword=""
    for c in word:
        if c=='{':
            blocknames.append(cword)
            if cword!='':
                tokens.append(cword)
            cword=""
            tokens.append(c)
        elif c in stuff:
            if cword!='':
                tokens.append(cword)
            cword=""
            if c in brakets:
                tokens.append(c)
        else:
            cword=cword+c
print(tokens)
settoken=set(tokens)

for token in settoken:
    if token in keys:
        print(token," is a keyword")
    elif token in brakets or token in stuff:
        print(token," is a bracket or a stuff")
    else:
        print(token," is an identifier")
print(blocknames)