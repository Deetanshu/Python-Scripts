import re
#Load data
cfile=open('C:/Users/deept/Desktop/College Stuff/1st Year/TicTacToe4.c','r')
#cfile=open('binaryconvert.c','r')
#List of tokens, keywords
keywordS="auto break case char const continue default do double else enum extern float for goto if int long register return short sign sizeof static struct switch typedef union unsigned void volatile while"
keyword=keywordS.split(' ')
openbracket=['[','(','{']
closebracket=[']','}',')']
arithsymb="+ - % * /"
arithmetic=arithsymb.split(' ')
punc=", ; . ->"
punctuation=punc.split(' ')
speca="+= -= *= /="
speciala=speca.split(' ')
comparison=['==','<=','>=','<','>','!=']
logical=['&','&&','|','||','!']
shift=['>>','<<','<<<','>>>']
tokens=[]
accessspec=['void','char','short','int','long','float','double','signed','unsigned']
infunc=['printf','scanf']
inputs=['getch','getchar']
#List of preprocessor directives
predirect=[]
funcs=[]
ctr=int(0)
for word in cfile:
    ctr=ctr+1
    if '#' in word:
        if 'include' in word:
            try:
                found=re.search('#include<(.+?)>',word).group(1)
                predirect.append(found)
            except AttributeError:
                found=''
            print("Line",ctr,"--> Header file: ",found)
    if '(' in word and ')' in word:
        for spec in accessspec:
            if spec in word:
                try:
                    found=re.search(spec+' (.+?)\(',word).group(1)
                    funcs.append(found)
                    print("Line",ctr,"--> Function name:",found,'with access specifier:',spec,end='')
                except AttributeError:
                    found=''
                try:
                    found2=re.search(spec+' (.+?)\((.+?)\)',word).group(2)
                    print(" with Parameters:",found2,end='')
                except AttributeError:
                    found2=''
                if found2!='' or found!='':
                    print()
        if 'scanf' in word:
            try:
                found=re.search('scanf\((.+?),&(.+?)\);',word).group(2)
                print("Line",ctr,"--> The value for variable:",found," is being accepted")
            except AttributeError:
                found=''
        if 'printf' in word:
            try:
                found=re.search('printf\((.+?),(.+?)\);',word).group(1)
                print("Line",ctr,"--> The string:",found," is printed",end='')
            except AttributeError:
                found=''
            try:
                found=re.search('printf\((.+?)\);',word).group(1)
                print("Line",ctr,"--> The string:",found," is printed")
            except AttributeError:
                found=''
            try:
                found2=re.search('printf\((.+?),(.+?)\);',word).group(2)
                print(" with values of variables:",found2,end='')
            except AttributeError:
                found2=''
            if found2!='' or found!='':
                print()
    else:
        continue
    
#test code
spec='+'
equv='='
test="c=a+b"
found=re.search('(.+?)'+equv+'(.+?)'+spec+'(.+?)',test).group(3)
print(found)