import nltk
import random
import string
#initializes all word/phrase arrays
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

prepGod = [     "god's wounds, ",
		"god's bodypart, ",
                "By god, ",
		"By the Will of godadj god, ",
		"By the bodyadj bodypart of the godadj god, ",
		"By godadj god's bodyadj bodypart, ",]

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

godArr = [	 "Odin",
                 "Bob",
                 "Zeus",
                 "Hera",
                 "Thor",
                 "Crom",
                 "Mad-poet Navarth",
                 "Cugel",
                 "Wotsit",
                 "Baron Boddisey",
                 "Poseidon",
                "Saint Mary",
                "Pallus Athena",
                "Loki",
                "Erlik",
                "Shoggoth",
                "Omm",
                "Vishnu",
                "Azazoth",
                "Father Odin",
                "Allfather Odin",
                "Cthulhu",
                "Buddha",
                "Aphrodite",
                "Isis",
                "Kali",
                "Dionysus",
                "Zarathustra",
                "Croesus",
                "Hermes",
                "Venus",
                "Montezuma",
                "Popacatapetl",
                "Hephaestus",
                "Bubastes",
                "Bacchus",
                "Nebuchadnezzar",
                "Assurbanipal",
                "Sargon",
                "Xerxes",
                "Mulwatallish",
                "Labarna",
                "Hammurabi",
                "Rameses",
                "Minos",
                "Tilgath-Pileser",
                "Vercingetorix",
                "Mithradites",
                "Pericles",
                "Belasarius",
                "Archaemides",
                "Heraclius",
                "Imhotep",
                "Artemis",
                "Orthia",
                "Phoebe",
                "Hestia",
                "Eros",
                "Persephone",
                "Minerva",
                "Mercury",
                "Aesculapius",
                "Discordia",
                "Hecate",
                "Hespera"]

godAdjArr = [	 "Almighty",
                 "Unthinkable",
                 "Unknowable",
                 "All-knowing",
                 "All-seeing",
                 "Lecherous",
                 "Scandalous",
                 "Merciful",
                 "Ravaging",
                 "Thunderous",
                "Wrathful",
                "Distant",
                "Vengeful",
                "Supreme",
                "Wise",
                "Warlike",
                "Jealous",
                "Vindictive",
                "Powerful",
                "Adulterous",
                "Licentious",
                "Crafty",
                "Benefical",
                "Virtuous",
                "Protective",
                "Prophetic",
                "Bloodthirsty",
                "Murderous",
                "Ruinous",
                "Militant",
                "Invisible",
                "Omnipotent",
                "Forgotten",
                "Enlightened",
                "Tempestuous",
                "Destructive",
                "Grim"]

bodyArr = [	 "Beard",
                 "Third Leg",
                 "Scalp",
                 "Eye",
                 "Thigh",
                 "Arm",
                 "Sword",
                 "Heel",
                 "Gaze",
                 "Tongue",
                 "Hammer",
                 "Toenail",
                 "Nether Regions",
                 "Liver",
                 "Lights",
                 "Spleen",
                 "Gall",
                 "Liver and Lights"]

bodyAdjArr = [	 "Unknowable",
                 "Unescapable",
                 "Unfathomable",
                 "Unthinkable",
                 "Righteous",
                 "Hairy",
                 "Hairless",
                 "Wandering",
                 "Blistered",
                 "Awe-inspiring",
                 "Toothy",
                 "Ravaged",
                 "Aged",
                 "Endless",
                 "Wondrous",
                "Unavoidable",
                "Pestilent",
                "Forgotten",
                "Beautiful",
                "Fertile",
                "Prophetic",
                "Musical",
                "Helpful",
                "Virginal",
                "Curative",
                "Bleak",
                "Incessant",
                "Sagely",
                "Unfashionable",
                "Unfaltering",
                "Unfamiliar",
                "Abysmal",
                "Boundless",
                "Eternal",
                "Immeasurable",
                "Infinite",
                "Unending",
                "Soundless",
                "Incomprehensible",
                "Inexplicable",
                "Profound",
                "unintelligible",
                "Unbelievable",
                "Impenetrable",
                "Indecipherable",
                "Esoteric",
                "Enigmatic",
                "Ancient",
                "Venerable",
                "Baneful",
                "Contagious",
                "Corrupting",
                "Deadly",
                "Deleterious",
                "Evil",
                "Noxious",
                "Diseased",
                "Pernicious",
                "Pestiferous",
                "Pestilential",
                "Tainted",
                "Contaminated",
                "Pulchritudinous",
                "Odoriferous",
                "Misbegotten",
                "Sacriligious"]

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
                'bitch',
                'bitches',
                'jackass',
                'jackasses',
                'dumbass',
                'dumbasses',
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

                'sick',
                'i',
                'hello',
                'hey',
                'hi',

                'god',
                'does',
                'Does']

idiotPreArr = [	"artless",
		"droning",
		"fawning",
		"warped",
		"paunchy",
		"puny",
		"spongy",
		"ruttish",
		"vain",
		"lumpish",
		"craven",
		"witless",
		"pustulent",
		"infested",
		"ill-bred",
		"blind",
		"scurvy",
    		"puny",
	    	"fetid",
                "vile",
    		"gibbering",
		"mewling",
		"rank",
                "fawning",
                "moonish",
                "brutish",
                "malapert",
                "curst",
                "lack-linen",
                "bottle-ailed",
                "lyingest",
                "embossed",
                "cheating",
                "crook-pated",
                "base-court",
                "hasty-witted",
                "two-faced",
                "pox-marked",
                "toad-brained",
                "errant",
                "idle-headed",
                "quailing",
                "flap-mouthed",
                "puking",
                "fly-bitten",
                "surly",
                "tottering",
                "villainous",
                "rump-fed",
                "bootless",
                "churlish",
                "tickle-brained",
                "froward"]


idiotArr = [       "mongrel",
                 "codpiece",
                 "jackanape",
                 "ape",
                 "coxcomb",
                 "harlot",
                 "hussy",
                 "strumpet",
                 "cur",
                 "clot",
                 "fool",
                 "barnacle",
                 "harpy",
                 "wench",
                 "churl",
                 "pleb",
                 "taffer",
                 "scoundrel",
                 "scalliwag",
                 "mooncalf",
                 "rapscallion",
                 "doxy",
                 "bawd",
                 "tosspot",
                 "cupshot",
                 "recreant",
                 "fustalarion",
                 "scullion",
                 "rampallion",
                 "knave",
                 "barbermonger",
                 "boil",
                 "plague-sore",
                 "carbuncle",
                 "whoreson",
                 "clotpole",
                 "lout",
                 "gudgeon",
                 "puttock",
                 "skainsmate",
                 "varlet",
                 "bladder"]
idiotPlur = [	"mongrels",
                "codpieces",
                "jackanapes",
                "apes",
                "coxcombes",
                "harlots",
                "hussies",
                "strumpets",
                "clots",
                "fools",
                "barnacles",
                "harpies",
                "wenches",
                "churls",
                "plebians",
                "taffers",
                "scoundrels",
                "scalliwags",
                "mooncalves",
                "rapscallions",
                "doxies",
                "bawds",
                "tosspots",
                "cupshots",
                "recreants",
                "fustalarions",
                "scullions",
                "rampallions",
                "knaves",
                "barbermongerers",
                "boils",
                "plague-sores",
                "carbuncles",
                "whoresons",
                "louts"]

def medieval(s): #main function
    s = checkTags(s)
    s = nounReplacements(s)
    s = wordReplacements(s)
    x = checkPunct(s)
    return(prepend() + x)

def godAppend():
    x = random.randrange(len(prepGod)-1)
    y = prepGod[x]
    y = nltk.word_tokenize(y)
    for i in range(len(y)):
        if y[i] == 'god':
            x = random.randrange(len(godArr)-1)
            y[i] = godArr[x]
        if y[i] == 'godadj':
            x = random.randrange(len(godAdjArr)-1)
            y[i] = godAdjArr[x]
        if y[i] == 'bodypart':
            x = random.randrange(len(bodyArr)-1)
            y[i] = bodyArr[x]
        if y[i] == 'bodyadj':
            x = random.randrange(len(bodyAdjArr)-1)
            y[i] = bodyAdjArr[x]

    y = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in y]).strip() + ' '
    return y
    
def prepend(): #prepends the message with a phrase
    x = random.randrange(0,3)
    if x == 0:
        x = random.randrange(len(prepArr)-1)
        return prepArr[x]
    if x == 1:
        return godAppend()
    if x == 2:
        return ''

def idiotPre():
    x = random.randrange(len(idiotPreArr)-1)
    return idiotPreArr[x]

def idiot(x):
    if x == 0:
        y = random.randrange(len(idiotArr)-1)
        return idiotArr[y]
    if x == 1:
        y = random.randrange(len(idiotPlur)-1)
        return idiotPlur[y]

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
    try:
        for word in range(len(tag)):
            tagged = tag[word].lower()
            if(tagged == 'it'):
                if(tag[word+1] == 'was'):
                    tag[word] = "'twas"
                    tag[word+1] = ''
                if(tag[word+1] == 'is' or tag[word+1] == "'s"):
                    tag[word] = "'tis"
                    tag[word+1] = ''
                if(tag[word+1] == 'would'):
                    tag[word] = "'twould"
                    tag[word+1] = ''
                if(tag[word+1] == 'will' or tag[word+1] == "'ll"):
                    tag[word] = "'twill"
                    tag[word+1] = ''
                if(tag[word+1] == 'were'):
                    tag[word] = "'twere"
                    tag[word+1] = ''
                if(tagged == 'teh'):
                    tag[word] = 'the'
                if(tagged == 'the'):
                    rand = rando()
                    if(rand > 50):
                        tag[word] = 'ye'
            if((tagged == 'shall' or tagged == 'will')  and tag[word+1] == 'not'): #shant
                tag[word] = "shan't"
                tag[word+1] = ''
            if(tagged == 'over' and tag[word+1] == 'there'):  #over there
               tag[word] = 'yonder'
               tag[word+1] = ''
            if(tagged == 'in' and tag[word+1] == 'the'): #in the
               tag[word] = "i' the"
               tag[word+1] = ''
            if((tagged == 'thank' and tag[word+1] == 'you') or (tagged == 'ty')): #thank you & ty
                x = random.randrange(len(thankYouArr)-1)
                tag[word] = thankYouArr[x]
                tag[word+1] = ''
    except IndexError: pass
    for word in range(len(tag)):
        tagged = tag[word].lower()
        if(tagged == 'god' or tagged == 'God'):
            if rando() < 80:
                y = random.randrange(len(godArr)-1)
                y = godArr[y]
                x = random.randrange(len(godAdjArr)-1)
                x = godAdjArr[x]
                tag[word] = x + ' ' + y
            else: tag[word] = 'God'
        if(tagged == 'is'): #is
            rand = rando()
            if(rand > 50):
                tag[word] = 'be'
        if(tagged == 'map'): #map
            tag[word] = 'chart'
        if(tagged == 'between'): #between
            tag[word] = 'betwixt'
        if(tagged == 'aggro'): #aggro
            tag[word] = 'wrath'
        if(tagged == 'buy'): #buy
            rand = rando()
            if(rand > 50):
                tag[word] = 'purchase'
            else: tag[word] = 'obtain'
        if(tagged == 'bought'): #bought
            rand = rando()
            if(rand > 50):
                tag[word] = 'purchased'
            else: tag[word] = 'obtained'
        if(tagged == 'debuff'): #debuff
            rand = rando()
            if(rand > 1 and rand <= 33):
                tag[word] = 'ailment'
            elif(rand > 34 and rand <= 66):
                tag[word] = 'sickness'
            else: tag[word] = 'pox'
        if(tagged == 'debuffed' or tagged == 'sick'): #debuffed / sick
            rand = rando()
            if(rand > 1 and rand <= 33):
                tag[word] = 'ailed'
            elif(rand > 34 and rand <= 66):
                tag[word] = 'sicknened'
            else: tag[word] = "pox't"
        if(tagged == 'sell'): #sell
            rand = rando()
            if(rand > 1 and rand <= 25):
                tag[word] = 'hawk'
            elif(rand > 25 and rand <= 50):
                tag[word] = 'pawn'
            elif(rand > 50 and rand <= 75):
                tag[word] = "tender"
            else: tag[word] ='purvey'
        if(tagged == 'sold'): #sold
            rand = rando()
            if(rand > 1 and rand <= 25):
                tag[word] = "hawk'd"
            elif(rand > 25 and rand <= 50):
                tag[word] = 'pawned'
            elif(rand > 50 and rand <= 75):
                tag[word] = "tendered"
            else: tag[word] = 'purveyed'
        if(tagged == 'food'): #food
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
        if(tagged  == 'bet'):
           tag[word] = 'warrant'
        if(tagged == 'hunting' or tagged == 'huntin'):
            tag[word] = "a-huntin'"
        if(tagged == 'coming' or tagged == 'comin'):
            tag[word] = "a-comin'"
        if(tagged == 'walking' or tagged == 'walkin'):
            tag[word] = "a-walkin'"
        if(tagged == 'making' or tagged == 'makin'):
            tag[word] = "a-makin'"
        if(tagged == 'of'):
            rand = rando()
            if rand >= 50:
                tag[word] = "o'"
        if(tagged == 'away'):
            rand = rando()
            if rand > 74:
                tag[word] = 'aroint'
        if(tagged == 'being'):
            rand = rando()
            if rand > 25:
                tag[word] = "bein'"
        if(tagged == 'why'):
            rand = rando()
            if rand > 50:
                tag[word] = 'wherefore'
        if(tagged == 'fucker'):
            tag[word] = 'swiver'
        if(tagged == 'fuckers'):
            tag[word] = 'swivers'
        if(tagged == 'shit'):
            tag[word] = 'nightsoil'
        if(tagged == 'child'):
            rand = rando()
            if rand > 50:
                tag[word] = 'poppet'
        if(tagged == 'those'):
            rand = rando()
            if rand > 50:
                tag[word] = 'yon'
        if(tagged == 'really'):
            rand = rando()
            if rand > 50:
                tag[word] = 'indeed'
            else: tag[word] = 'in truth'
        if(tagged == 'often'):
            rand = rando()
            if rand > 33:
                tag[word] = 'oft'
        if(tagged == 'maybe'):
            rand = rando()
            if rand > 33:
                tag[word] = 'mayhaps'
            if rand > 66:
                tag[word] = 'perchance'
        if(tagged == 'sure'):
            rand = rando()
            if rand > 66:
                tag[word] = 'shore'
        if(tagged == 'assist'): #food
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
        if(tagged == 'could'):
            rand = rando()
            if rand > 50:
                tag[word] = 'couldst'
        if(tagged == 'would'):
            rand = rando()
            if rand > 50:
                tag[word] = 'wouldst'
        if(tagged == 'later'):
            rand = rando()
            if rand > 50:
                tag[word] = 'anon'
        if(tagged == 'here'):
            rand = rando()
            if rand > 25:
                tag[word] = 'hither'
        if(tagged == 'enough'):
            rand = rando()
            if rand > 66:
                tag[word] = 'enow'
        if(tagged == 'though'):
            rand = rando()
            if rand > 66:
                tag[word] = "tho'"
        if(tagged == 'underneath' or tagged == 'beneath' or tagged == 'under'):
            rand = rando()
            if rand > 50:
                tag[word] = " 'neath"
        if(tagged == 'until'):
            rand = rando()
            if rand > 33:
                tag[word] = "' till"
        if(tagged == 'joke'):
            rand = rando()
            if rand > 33:
                tag[word] = "jest"
            else: tag[word] = 'jape'
        if(tagged == 'your'):
            rand = rando()
            if rand < 33:
                tag[word] = "thy"
            elif rand > 32 and rand < 66:
                tag[word] = 'thine'
            else: tag[word] = 'thyne'
        if(tagged == 'my'):
            rand = rando()
            if rand > 50:
                tag[word] = 'mine'
        if(tagged == 'in'):
            rand = rando()
            if rand > 50:
                tag[word] = 'within'
        if(tagged == 'gold' or tagged == 'money'):
            rand = rando()
            if(rand >= 1 and rand <= 12):
                tag[word] = 'bullion'
            elif(rand > 12 and rand <= 25):
                tag[word] = 'florins'
            elif(rand > 25 and rand <= 37):
                tag[word] = "pounds"
            elif(rand > 37 and rand <= 50):
                tag[word] = "pieces o'silver"
            elif(rand > 50 and rand <= 63):
                tag[word] = "groats"
            elif(rand > 63 and rand <= 75):
                tag[word] = "crowns"
            elif(rand > 75 and rand <= 88):
                tag[word] = "ingots"
            else: tag[word] ='ducats'
        if(tagged == 'balls' or tagged == 'groin'):
            rand = rando()
            if(rand >= 1 and rand <= 12):
                tag[word] = 'leathers'
            elif(rand > 12 and rand <= 25):
                tag[word] = 'beans'
            elif(rand > 25 and rand <= 37):
                tag[word] = "poundables"
            elif(rand > 37 and rand <= 50):
                tag[word] = "nethers"
            elif(rand > 50 and rand <= 63):
                tag[word] = "nadchackles"
            elif(rand > 63 and rand <= 75):
                tag[word] = "buis"
            elif(rand > 75 and rand <= 88):
                tag[word] = "fellahs"
            else: tag[word] ='coin purse'
        if(tagged == 'go'):
            rand = rando()
            if rand > 50:
                tag[word] = 'be off'
            else: tag[word] = ''
        if(tagged == 'will'):
            rand = rando()
            if rand > 50:
                tag[word] = 'wilt'
            else: tag[word] = 'wouldst'
        if(tagged == 'does' or tagged == 'Does'):
            rand = rando()
            if rand < 33:
                tag[word] = 'doeseth'
            elif rand > 32 and rand < 66:
                tag[word] = 'dost'
            else: tag[word] = 'doth'
        if(tagged == 'hello' or tagged == 'hi' or tagged == 'hey'):
            rand = rando()
            if(rand >= 20):
                tag[word] = "good day"
            elif(rand > 20 and rand <= 40):
                tag[word] = "well met"
            elif(rand > 40 and rand <= 60):
                tag[word] = "tally ho"
            elif(rand > 60 and rand <= 80):
                tag[word] = "well meteth"
            else: tag[word] ='ave'
        if(tagged == 'yes'):
            rand = rando()
            if rand < 33:
                tag[word] = 'aye'
            elif rand < 66:
                tag[word] = 'yea'
            else: tag[word] = 'yeah verily'
        if(tagged == 'no'):
            rand = rando()
            if rand > 50:
                tag[word] = 'nay'
            else: tag[word] = 'nayeth'
        if(tagged == 'goodbye' or tagged == 'bye' or tagged == 'seeya' or tagged == 'goodnight'):
            rand = rando()
            if(rand >= 1 and rand <= 12):
                tag[word] = 'good morrow'
            elif(rand > 12 and rand <= 25):
                tag[word] = 'godspeed'
            elif(rand > 25 and rand <= 37):
                tag[word] = "begone"
            elif(rand > 37 and rand <= 50):
                tag[word] = "adieu"
            elif(rand > 50 and rand <= 63):
                tag[word] = "cheerio"
            elif(rand > 63 and rand <= 75):
                tag[word] = "I bid thee good day"
            elif(rand > 75 and rand <= 88):
                tag[word] = "by your leave"
            else: tag[word] ='pleasant journey'
        if(tagged == 'idiot' or tagged == 'fool' or tagged == 'bastard' or tagged == 'moron'
           or tagged == 'jackass' or tagged == 'dumbass' or tagged == "bitch"):
                one = idiotPre()
                two = idiotPre()
                three = idiot(0)
                tag[word] = one + ' ' + two + ' ' + three
        if(tagged == 'idiots' or tagged == 'fools' or tagged == 'bastards' or tagged == 'morons'
           or tagged == 'jackasss' or tagged == 'dumbass' or tagged == "bitches"):
                one = idiotPre()
                two = idiotPre()
                three = idiot(1)
                tag[word] = one + ' ' + two + ' ' + three


    #contractions
    #for word in range(len(tag)):
    #misc
    for word in range(len(tag)):
        tagged = tag[word].lower()
        if(tagged == 'you' or tagged == 'u'): #you
            x = random.randrange(len(youArr)-1)
            tag[word] = youArr[x]
        if(tagged == 'are'): # are
            tag[word] = 'art'
        if(tagged == 'lol'): #lol
            x = random.randrange(len(lolArr)-1)
            tag[word] = lolArr[x]
        if(tagged == 'killed' or tagged == 'beaten' or tagged == 'fucked'): #killed
            x = random.randrange(len(killPastArr)-1)
            tag[word] = killPastArr[x]
        if(tagged == 'kill' or tagged == 'gank'): #killed
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
        if rando() > 50:
            return(postpend(s))
        else: return s

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
