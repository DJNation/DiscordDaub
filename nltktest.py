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

prepGod = [     "&god's wounds, ",
		"&god's &bodypart, ",
                "By &god, ",
		"By the Will of &godadj &god, ",
		"By the &bodyadj &bodypart of the &godadj &god, ",
		"By &godadj &god's &bodyadj &bodypart, ",]

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

killPastArr = [ "slain",
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

personal = [    'town',
                'village',
                'home',
                
                'lol',
                
                'afk',
                
                'rofl'
                
                'water',
                
                'balls',
                'groin',
                
                'gold',
                'money',
                
                'joke',
                
                'idiot',
                'fool',
                'bastard',
                'moron',
                'idiots',
                'fools',
                'bastards',
                'morons',
                'fucker',
                'fuckers',
                'shit',
                
                'map',
                'maps',
                
                'debuff',
                'debuffed',
                
                'food',
                
                'man',
                'guy',
                'guys',
                'men',
                'boys',
                
                'party',
                'group',
                
                'noob',
                'newb',
                'newbie',
                'nub',
                'lowbie',
                'beginner',
                'noobs',
                'newbs',
                'newbies',
                'nubs',
                'lowbies',
                'beginners',
                
                'level',
                
                'hehe',
                'haha',
                'heh',
                'hah',
                
                'shop',
                'store',
                'vendor',
                'seller',
                
                'friend',
                'buddy',
                'pal',
                'mate',
                'friends',
                'buddies',
                'pals',
                'mates',
                
                'girl',
                'woman',
                'girls',
                'women',
                
                'child',
                'flag',
                
                'sick']

def medieval(s): #main function
    if s == 'smexy': return 'avery is a dum fukr'
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
        rand = rando()
        if pos[i][1] == 'NN' and personalized(s[i]) != True: #Checks if word is a noun and is not changed by particular replacement
            x = s[i]
            if(x[0].isupper()): continue #will ignore intentional capitalizations of nouns (for usernames, etc)
            if rand > 34: continue #randomizer
            if x.endswith('e'):
                s[i] = x+"'th"
            else:
                s[i] = x+"eth"
    return s

def personalized(s): #Checks if noun in question is in the personal list
        if s in personal:
            return True
        else:
            return False

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

            if(tag[word] == 'teh'):
                tag[word] == 'the'
    for word in range(len(tag)):
        if((tag[word] == 'shall' or tag[word] == 'will')  and tag[word+1] == 'not'): #shant
            tag[word] = "shan't"
            tag[word+1] = ''
        if(tag[word] == 'is'): #is
            rand = rando()
            if(rand > 50):
                tag[word] = 'be'
        if(tag[word] == 'map'): #map
            tag[word] = 'chart'
        if(tag[word] == 'between'): #between
            tag[word] = 'betwixt'
        if(tag[word] == 'aggro'): #aggro
            tag[word] = 'wrath'
        if(tag[word] == 'buy'): #buy
            rand = rando()
            if(rand > 50):
                tag[word] = 'purchase'
            else: tag[word] = 'obtain'
        if(tag[word] == 'bought'): #bought
            rand = rando()
            if(rand > 50):
                tag[word] = 'purchased'
            else: tag[word] = 'obtained'
        if(tag[word] == 'debuff'): #debuff
            rand = rando()
            if(rand > 1 and rand <= 33):
                tag[word] = 'ailment' 
            elif(rand > 34 and rand <= 66):
                tag[word] = 'sickness'
            else: tag[word] = 'pox'
        if(tag[word] == 'debuffed' or tag[word] == 'sick'): #debuffed / sick
            rand = rando()
            if(rand > 1 and rand <= 33):
                tag[word] = 'ailed'
            elif(rand > 34 and rand <= 66):
                tag[word] = 'sicknened'
            else: tag[word] = "pox't"
        if(tag[word] == 'sell'): #sell
            rand = rando()
            if(rand > 1 and rand <= 25):
                tag[word] = 'hawk'
            elif(rand > 25 and rand <= 50):
                tag[word] = 'pawn'
            elif(rand > 50 and rand <= 75):
                tag[word] = "tender"
            else: tag[word] ='purvey'
        if(tag[word] == 'sold'): #sold
            rand = rando()
            if(rand > 1 and rand <= 25):
                tag[word] = "hawk'd"
            elif(rand > 25 and rand <= 50):
                tag[word] = 'pawned'
            elif(rand > 50 and rand <= 75):
                tag[word] = "tendered"
            else: tag[word] = 'purveyed'
        if(tag[word] == 'food'): #food
            rand = rando()
            if(rand > 1 and rand < 20):
                print(True)
                tag[word] = "vittles"
            elif(rand > 20 and rand < 40):
                tag[word] = 'rations'
            elif(rand > 40 and rand < 60):
                tag[word] = "sustenance"
            elif(rand > 60 and rand < 80):
                tag[word] = "sustenance"
            else: tag[word] = 'viands'
        if(tag[word]  == 'bet'):
           tag[word] = 'warrant'
        if(tag[word] == 'hunting' or tag[word] == 'huntin'):
            tag[word] = "a-huntin'"
        if(tag[word] == 'coming' or tag[word] == 'comin'):
            tag[word] = "a-comin'"
        if(tag[word] == 'walking' or tag[word] == 'walkin'):
            tag[word] = "a-walkin'"
        if(tag[word] == 'making' or tag[word] == 'makin'):
            tag[word] = "a-makin'"
        if(tag[word] == 'of'):
            rand = rando()
            if rand >= 50:
                tag[word] = "o'"
        if(tag[word] == 'away'):
            rand = rando()
            if rand > 74:
                tag[word] = 'aroint'
        if(tag[word] == 'being'):
            rand = rando()
            if rand > 25:
                tag[word] = "bein'"
        if(tag[word] == 'why'):
            rand = rando()
            if rand > 50:
                tag[word] = 'wherefore'
        if(tag[word] == 'fucker'):
            tag[word] = 'swiver'
        if(tag[word] == 'fuckers'):
            tag[word] = 'swivers'
        if(tag[word] == 'shit'):
            tag[word] = 'nightsoil'
        if(tag[word] == 'child'):
            rand = rando()
            if rand > 50:
                tag[word] = 'poppet'
        if(tag[word] == 'those'):
            rand = rando()
            if rand > 50:
                tag[word] = 'yon'
        if(tag[word] == 'really'):
            rand = rando()
            if rand > 50:
                tag[word] = 'indeed'
            else: tag[word] = 'in truth'
        if(tag[word] == 'often'):
            rand = rando()
            if rand > 33:
                tag[word] = 'oft'
        if(tag[word] == 'maybe'):
            rand = rando()
            if rand > 33:
                tag[word] = 'mayhaps'
            if rand > 66:
                tag[word] = 'perchance'
        if(tag[word] == 'sure'):
            rand = rando()
            if rand > 66:
                tag[word] = 'shore'
        if(tag[word] == 'assist'): #food
            rand = rando()
            if(rand > 1 and rand <= 20):
                tag[word] = "aid"
            elif(rand > 20 and rand <= 40):
                tag[word] = 'aideth'
            elif(rand > 40 and rand <= 60):
                tag[word] = "saveth"
            elif(rand > 60 and rand <= 80):
                tag[word] = "assistance"
            else: tag[word] = 'succor'
        if(tag[word] == 'could'):
            rand = rando()
            if rand > 50:
                tag[word] = 'couldst'
        if(tag[word] == 'would'):
            rand = rando()
            if rand > 50:
                tag[word] = 'wouldst'
        if(tag[word] == 'later'):
            rand = rando()
            if rand > 50:
                tag[word] = 'anon'
        if(tag[word] == 'here'):
            rand = rando()
            if rand > 25:
                tag[word] = 'hither'
        if(tag[word] == 'enough'):
            rand = rando()
            if rand > 66:
                tag[word] = 'enow'
        if(tag[word] == 'though'):
            rand = rando()
            if rand > 66:
                tag[word] = "tho'"
        if(tag[word] == 'underneath' or tag[word] == 'beneath' or tag[word] == 'under'):
            rand = rando()
            if rand > 50:
                tag[word] = " 'neath"
        if(tag[word] == 'until'):
            rand = rando()
            if rand > 33:
                tag[word] = "' till"


        
        
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

def rando():
    rand = random.randint(1,101)
    return rand


#TESTING--------------------------------TESTING
#while True:
#    s = input("Enter a string ")
#    print(s)
#    print(medieval(s))
#    s = input("Again?")
#    if(s == 'n'):
#        break
#TESTING--------------------------------TESTING
