import nltk
import random
import string
#initializes all word/phrase arrays for one-time use, rather than per function call
prepArr = [     "Forsooth, ",
		"I say, ",
		"I sayeth, ",
		"Forsooth, I say, ",
		"Forsooth, say I, ",
		"Forsooth, sayeth I, ",
		"Hark, ",
		"Harketh, ",
		"By &god, ",
		"By the Will of &godadj &god, ",
		"By the &bodyadj &bodypart of the &godadj &god, ",
		"By &godadj &god's &bodyadj &bodypart, ",
		"Avast, ",
		"Zounds, ",
		"Perchance, ",
		"Pray tell, ",
		"Prithee, ",
		"What hey, ",
		"What ho, ",
		"Pray, ",
		"Surely ",
		"Pray pardon, ",
		"Alas, ",
		"In short, ",
		"My Lord, ",
		"My Lady, ",
		"By my faith, ",
		"If it pleases you, ",
		"I pray you, ",
		"In truth, ",
		"By my trowth, ",
		"In sooth, ",
		"By my word, ",
		"S'wounds, ",
		"Z'wounds, ",
		"&god's wounds, ",
		"&god's &bodypart, ",
		"Heigh-ho, ",
		"Ah, ",
		"Quoth I, ",
		"Listen, ",
		"Listen thee, ",
		"Hear me, ",
		"Now hear me, ",
		"I warrant ",
		"Come, ",
		"Kind sire, ",
		"Sire, ",]

postArr = [     " Anon!",
		" Hum.",
		" Good sir!",
		" Good sire!",
		" Milady!",
		" My Liege!",
		" Guvnor!"]

exclamArr = [   ", verily!",
                ", verily I say!",
		", verily I sayeth!",
		", I say!",
		", I sayeth!",
		"! Huzzah!",
		"! Hear Hear!",
		"! What-ho!",
		"! Ho!",
		"! Fie!",
		", indeed!",
                "!"]

questArr = [	", I say?",
		", I wonder?",
		", wonder I?",
		", what say thee?",
		", what sayeth thee?",
		", what say thou?",
		", what sayeth thou?",
		", I ponder?",
		", I pondereth?",
		", pray tell?",
		", ho?",
		", do tell?"]

thankYouArr = [ "many good thanks to you",
		"thankee",
		"kindly thanks to you",
		"grammercy to you"]

youArr = [      "thou",
                "thee",
                "ye"]

lolArr = [      "lolleth",
                "lollery"]

killPastArr = [     "slain",
		"vanquished",
		"brung low",
		"conquered",
		"fleeced",
		"humbled",
		"subjugated",
		"bested",
		"foiled"]

killArr = [     "slay",
		"vanquish",
		"bring low",
		"conquer",
		"fleece",
		"humble",
		"subjugate",
		"best",
		"foil"]

def medieval(s): #main function
    s = checkTags(s)
    s = nounReplacements(s)
    s = wordReplacements(s)
    x = checkPunct(s)
    return(prepend() + x)

def prepend(): #prepends the message with a phrase
   x = random.randrange(len(prepArr)-1)
   return prepArr[x]
def nounReplacements(s):    #replaces improper nouns (school, tree, plant) with a rate of .33
    pos = nltk.pos_tag(s)
    for i in range(len(s)):
        rand = random.randint(1,101)
        if pos[i][1] == 'NN':
            x = s[i]
            if(x[0].isupper()): continue #will ignore intentional capitalizations of nouns (for usernames, etc)
            if rand > 34: continue #randomizer
            if x.endswith('e'):
                s[i] = x+"'th"
            else:
                s[i] = x+"eth"
    return s
    

def wordReplacements(tag): #Replaces phrases and single words
    #for preceeding "it"
    for word in range(len(tag)):
        if(tag[word] == 'it'):
            if(tag[word+1] == 'was'):
                tag[word] = "'twas"
                tag[word+1] = ''
            if(tag[word+1] == 'is'):
                tag[word] = "'tis"
                tag[word+1] = ''
            if(tag[word+1] == 'would'):
                tag[word] = "'twould"
                tag[word+1] = ''
            if(tag[word+1] == 'will'):
                tag[word] = "'twill"
                tag[word+1] = ''
            if(tag[word+1] == 'were'):
                tag[word] = "'twere"
                tag[word+1] = ''
    #for succeeding "not"
    for word in range(len(tag)):
        if((tag[word] == 'shall' or tag[word] == 'will')  and tag[word+1] == 'not'):
            tag[word] = "shan't"
            tag[word+1] = ''
    #contractions
    #for word in range(len(tag)):
    #misc
    for word in range(len(tag)):
        if(tag[word] == 'over' and tag[word+1] == 'there'):  #over there
           tag[word] = 'yonder'
           tag[word+1] = ''
        if(tag[word] == 'in' and tag[word+1] == 'the'): #in the
           tag[word] = "i' the"
           tag[word+1] = ''
        if((tag[word] == 'thank' and tag[word+1] == 'you') or (tag[word] == 'ty')): #thank you & ty
            x = random.randrange(len(thankYouArr)-1)
            tag[word] = thankYouArr[x]
            tag[word+1] = ''
        if(tag[word] == 'you' or tag[word] == 'u'): #you
            x = random.randrange(len(youArr)-1)
            tag[word] = youArr[x]
        if(tag[word] == 'are'): # are
            tag[word] = 'art'
        if(tag[word] == 'lol'): #lol
            x = random.randrange(len(lolArr)-1)
            tag[word] = lolArr[x]
        if(tag[word] == 'killed' or tag[word] == 'beaten' or tag[word] == 'fucked'): #killed
            x = random.randrange(len(killPastArr)-1)
            tag[word] = killPastArr[x]
        if(tag[word] == 'kill' or tag[word] == 'gank'): #killed
            x = random.randrange(len(killArr)-1)
            tag[word] = killArr[x]
        
        
        
    tag = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tag]).strip()
    return tag

def checkTags(x):   #Checks if a mention occurs within the message, then concats the mention to maintain its integrity
                    #else it will remain in the form of ['<','@','userid','>']
                    #it is also the ugliest code in existence
    cnt = 0         #and is only for discord mentions in the form of '<@userid>'
    tag = nltk.word_tokenize(x)
    if('@' not in tag):
        return tag
    else:
        for i in range(len(tag)):
            if(tag[i] == '<'):
                for j in range(len(tag)):
                    j += 1+i
                    tag[i] += tag[j]
                    tag[i+1] = tag[j]
                    cnt = j
                    if('>' in tag[i+1]):
                        for z in range(cnt):
                            try:
                                del tag[i+1]
                                if(tag[i+1] == '>'):
                                    del tag[i+1]
                                    return(tag)
                            except IndexError:
                                return(tag)
                        return(tag)
        
def checkPunct(s): #Checks the end of message, if there is no punctuation, assume period
    l = list(s)
    tag = nltk.pos_tag(nltk.word_tokenize(s))[-1] #tag = last character of message
    if(tag[0] == '!'):
        return(exclam(s))
    if(tag[0] == '?'):
        return(questi(s))
    if(tag[0] == '.' or tag[0] != '!' or tag[0] != '?'):
        return(postpend(s))

def exclam(s): # for '!'
    l = list(s)
    tag = nltk.pos_tag(nltk.word_tokenize(s))[-1]
    if(tag[0] == '!'):
        l[-1] = ''
        s = ''.join(l)
        
    x = random.randrange(len(exclamArr)-1)
    return(s + exclamArr[x])

def questi(s): # for '?'
    l = list(s)
    tag = nltk.pos_tag(nltk.word_tokenize(s))[-1]
    if(tag[0] == '?'):
        l[-1] = ''
        s = ''.join(l)

    x = random.randrange(len(questArr)-1)
    return(s + questArr[x])

def postpend(s): # for '.' end punct
    if(len(s) >= 1):
        l = list(s)
        tag = nltk.pos_tag(nltk.word_tokenize(s))[-1]
        if(tag[0] == '.'):
            l[-1] = ','
            s = ''.join(l)
        else: #if message does not end with '.', assume period
            l.append(',')
            s = ''.join(l)

    x = random.randrange(len(postArr)-1)
    return (s + postArr[x])


#TESTING--------------------------------TESTING
#while True:
#    s = input("Enter a string ")
#    print(s)
#    print(medieval(s))
#    s = input("Again?")
#    if(s == 'n'):
#        break
#TESTING--------------------------------TESTING
