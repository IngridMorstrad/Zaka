import pickle

##def addrate():
##    """Adds rating to a movie"""
##    f=open('Seen 2011.txt', 'r')
##    word_b=[]
##    for line in f:
##        word=line.split()
##        word_b.append(word)
##        print line,
##        word_b.append(raw_input("Rating: "))
##    f.close()
##    f=open('seen3.txt','wb')
##    pickle.dump(word_b,f)
##    f.close()
##
##def display():
##    """Displays the list"""
##    f=open('seen3.txt', 'rb')
##    x=pickle.load(f)
##    ##Prints movie names & ratings
##    for y in range(0,len(x),2):
##        print y/2+1,
##        for b in range(0,len(x[y])):
##            print x[y][b],
##        for rating in range(y+1,y+2):
##            print ":",x[rating],
##        print ""
##    print ""
##    f.close()

def Sscore():
    """Displays highscores"""
    f=open('HSS.txt','rb')
    g=open('HSN.txt','rb')
    names=[]
    scores=[]
    l=f.readline()
    while l:
        names.append(l)
        scores.append(g.readline())
        l=f.readline()
    f.close()
    g.close()
    return [names,scores]

def Wscore(PName, Score):
    """Adds a new name to the list"""
    f=open('HSS.txt','a')
    g=open('HSN.txt','a')
    f.write(PName)
    f.write("\n")
    g.write(Score)
    g.write("\n")
    f.close()
    g.close()

def sort():
    """Sorts the files"""
    f=open('HSS.txt','rb')
    g=open('HSN.txt','rb')
    ns=[]
    l=f.readline()
    k=g.readline()
    while k:
        if k=='\n':
            l=f.readline()
            k=g.readline()
            continue
        if l=='\n':
            l=f.readline()
            continue
        ns.append((int(k),l))
        l=f.readline()
        k=g.readline()
    f.close()
    g.close()
    ns.sort(reverse=True)
    f=open('HSS.txt','wb')
    g=open('HSN.txt','wb')
    i=0
    for r in ns:
        b=repr(r[0])
        c=r[1]
        f.write(c)
        g.write(b)
        g.write("\r\n")
        i=i+1
        if i==10:
            break
    f.close()
    g.close()

##def insrate(Name,score):
##    """Inserts rating for a certain film"""
##    f=open('Highscores.txt', 'rb')
##    x=pickle.load(f)
##    key=int(raw_input("Enter movie key:"))
##    key-=1
##    key*=2
##    x.pop(key+1)
##    x.insert(key+1, int(raw_input("Enter new rating: ")))
##    f.close()
##    f=open('seen3.txt', 'wb')
##    pickle.dump(x,f)
##    f.close()
##        
##

sort()
