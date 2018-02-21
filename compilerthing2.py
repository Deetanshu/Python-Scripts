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
cfile=open('TicTacToe4.c','r')
blocknames=[]
for word in cfile:
    cword=""
    for c in word:
        if c=='#':
            print("Preprocessor directive: ",word)
            continue
            if cword!='':
                tokens.append(cword)
            cword=""
            tokens.append(c)
        elif c in openbracket or c in closebracket or c in comparison or c in arithmetic or c in speciala or c in logical or c in punctuation:
            if cword!='':
                tokens.append(cword)
            cword=""
            if c in closebracket:
                if cword!='':
                    tokens.append(cword)
                cword=""        
        else:
            cword=cword+c
print(tokens)
  

Sbracket=[]
Spunctuation=[]
          
for t in tokens:
    if t in openbracket or t in closebracket:
        Sbracket.append(t)
    if t in punctuation :
        Spunctuation.append(t);
    if t in 
