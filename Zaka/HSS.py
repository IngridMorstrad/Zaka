import pickle
from datetime import datetime

def Sscore():
    """Displays highscores"""
    f=open('HSS.txt','rb')
    try:
        x=pickle.load(f)
    except:
        return [[],[]]
    names=[]
    scores=[]
    for score,name,_ in x[:10]:
        scores.append(score)
        names.append(name)
    f.close()
    return [names,scores]

def Wscore(PName, Score):
    """Adds a new name to the list"""
    f=open('HSS.txt', 'rb')
    try:
        x=pickle.load(f)
        x.append([Score, PName,datetime.date(datetime.now())])
        x.sort(reverse=True)
    except:
        ## New file
        x=[[Score, PName,datetime.date(datetime.now())]]

    f.close()
    f=open('HSS.txt', 'wb')
    pickle.dump(x,f)
    f.close()

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
