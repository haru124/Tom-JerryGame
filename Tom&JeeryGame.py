import random as rdm  
print("Welcome to the game! Let's play Tom and Jerry...")
name = input("What is your name, Champ? ")  

rules = input('Do you know the rules? <Type yes/no> ').lower()
if rules == 'no':
  print("\nWorry not, I got you Honey, the rules are simple.\nI will choose a four letter 'WORD' for you, you just have to guess it right.")
  print("Please remember, the letters in the 'WORD' will not repeat i.e., every letter in the 'WORD' will be unique.")
  print("You will be asked to input a 4 letter word(with no repeating letters) every turn, till you lose all your lives. Lives are the number of turns/guesses you get.")
  print("You can choose the difficulty at the beginning of the game. <<<Beginner - 15 lives/turns | Intermediate - 10 lives/turns | Expert - 5 lives/turns>>>")
  print("\nIf any of the letters in the word you input, matches with the 'WORD' I chose,\nI will tell you the number of toms and jerries in the input word.")
  print("\nSometimes, none of the letters in the input word might match with the 'WORD' I chose for you.")
  print("\nToms are those letters whose positions are correct while Jerries are those letters whose positions are changed.")
  print("Here's an example,\n'WORD'= soup | input word = surf\nHere, there is 1 Tom and 1 Jerry...")
  print("Letter 's' is the Tom since it is in same position <position-1> while,\nthe letter 'u' is Jerry as its position in input word is <position2> but in actual 'WORD' it is in <position3>")
  print("\nYou will have to guess/analyse which letters might be toms or jerries and choose a wise word with tom/jerry letters in your next turn.")
  print("You will WIN if you guess the 'WORD' I chose for you or LOSE when you lose all your lives.")
  print("\n\nHope you got the rules Champ!")

 
begin = input("\nShall we begin, Champ? <Type yes/no> ").lower()
if begin == 'yes':
  difficulty = input("Choose the difficulty!\nType 1 for Beginner mode | 2 for Intermediate mode | 3 for Expert mode\n")
  if difficulty == '1':
    lives = 15
  if difficulty == '2':
    lives = 10
  if difficulty == '3':
    lives = 5
  print("You have",lives,"lives. Best of Luck!",name)

  strings = ['WORD','ABYS','ACHE','ACID','ACNE','AIDE','ALMS','APEX','ARCH','ARES','ARMY','ATOM','AUNT','AUTO','AVID','AXIL','AXIS','AXLE','BACK','BALD','BAND','BANG','BANK','BARE','BARF','BARK','BARN','BASE','BASH','BATH','BEAM','BEAN','BEAR','BEAT','BELT','BEND','BEST','BIKE','BIRD','BITE','BLOG','BLOW','BLUE','BOAT','BODY','BOLD','BOND','BONE','BORN','BOWL','BRAT','BREW','BURN','BUSH','CAFE','CAGE','CAKE','CALM','CAMP','CANE','CAPE','CARD','CARE','CART','CASE','CASH','CAST','CAVE','CENT','CHAT','CHEW','CHIN','CHIP','CITY','CLAM','CLAY','CLUB','CLUE','COAL','COAT','CODE','COLD','COMB','CONE','COPY','CORD','CORE','CORN','COST','COVE','CRAB','CREW','CUBE','CURE','CUTE','DARK','DASH','DATE','DAWN','DEAD','DEAL','DEAR','DEMO','DESK','DICE','DIET','DIME','DING','DIRT','DISH','DIVE','DONE','DORK','DOVE','DOWN','DROP','DRUM','DUCK','DUKE','DUST','EACH','EASE','EAST','EASY','ECHO','ENVY','EPIC','ETCH','EVIL','EXAM','EXIT','EXPO','FACE','FACT','FAIL','FAIR','FAME','FARM','FAST','FATE','FEAR','FILM','FINE','FIRE','FISH','FIVE','FLAG','FLAT','FLEA','FLEX','FLOW','FORK','FORM','FORT','FOUR','FROG','GAIN','GAME','GATE','GEAR','GIFT','GIRL','GIST','GIVE','GLAD','GLOW','GLUE','GOAL','GOAT','GOLD','GOLF','GONE','GRAM','GRAY','GREY','GROW','HAIR','HALF','HAND','HARD','HARM','HATE','HAVE','HAWK','HEAD','HEAR','HEAT','HELP','HERO','HOLD','HOLE','HOLY','HOME','HONE','HOPE','HORN','HOUR','HUNT','HURT','HYPE','ICKY','ICON','IDEA','IDLE','IDOL','INCH','IRON','ITCH','ITEM','JAIL','JERK','JINX','JOCK','JOIN','JOKE','JUDO','JULY','JUMP','JUNE','JUNK','JUST','JUTE','KILO','KIND','KING','KITE','KNIT','KNOB','KNOT','KNOW','LACE','LADY','LAKE','LAMB','LAME','LAMP','LAND','LANE','LAST','LATE','LAZY','LEAD','LEAF','LEAN','LEFT','LICK','LIFE','LIFT','LIKE','LIME','LINE','LINK','LION','LIPS','LIST','LIVE','LOAD','LOAF','LOAN','LOCK','LONE','LONG','LORD','LOSE','LOST','LOUD','LOVE','LUCK','LUKE','LUNG','LUST','MAGE','MAID','MAIL','MAIN','MANY','MARS','MART','MASK','MATE','MATH','MEAL','MEAN','MEAT','MILE','MILK','MIND','MINE','MINT','MIST','MOLD','MORE','MOTH','MOVE','MUCH','NAME','NEAR','NECK','NEST','NEWS','NICE','NICK','NILE','NODE','NOSE','NOTE','OATH','OBEY','OMEN','OMIT','ONCE','ONLY','OPEN','ORAL','OVAL','OVEN','OVER','PACE','PACK','PAGE','PAIN','PAIR','PARK','PART','PAST','PATH','PEAK','PEAR','PIER','PINE','PING','PINK','PLAN','PLAY','PLUM','PLUS','POEM','POET','POLE','POND','PONY','PORK','PORT','POSE','POST','PROM','PURE','PUSH','QUAD','QUIT','QUIZ','RACE','RAGE','RAIN','RATE','READ','REAL','RENT','REST','RICE','RICH','RIDE','RING','RIOT','RISE','RISK','RITE','ROAD','ROBE','ROCK','ROME','ROPE','ROSE','RULE','RUSH','RUST','SACK','SAFE','SAGE','SAIL','SALE','SALT','SAME','SAND','SANE','SCAR','SEAL','SELF','SHED','SHIP','SHOE','SHOP','SHOT','SHOW','SICK','SIDE','SIGN','SILK','SING','SKIN','SLOW','SNOW','SOAP','SOCK','SODA','SOFT','SOIL','SOME','SONG','SOUL','SOUP','STAR','STAY','STEM','STEP','STOP','SUIT','SURE','SURF','SWAG','SWAN','TAIL','TAKE','TALE','TALK','TANK','TAPE','TASK','TEAM','TECH','THEM','THIN','TIDE','TILE','TIME','TINY','TIRE','TOAD','TONE','TOUR','TOWN','TRAP','TRIO','TRIP','TRUE','TUBE','TUNA','TUNE','TURN','UGLY','UNDO','UNIT','UREA','VARY','VASE','VAST','VEIL','VEIN','VERB','VERY','VEST','VIAL','VIBE','VIEW','VINE','VOID','VOLT','VOTE','WAIT','WALK','WAND','WANT','WARD','WARM','WASH','WASP','WAVE','WEAR','WEST','WHAT','WHIP','WICK','WIDE','WIFE','WILD','WIND','WINE','WING','WINK','WIPE','WIRE','WISE','WISH','WISP','WITH','WOLF','WOMB','WORK','WORM','WRAP','YARD','YAWN','YEAR','YOGA','YOKE','YOLK','ZERO','ZEST','ZINC','ZONE']
  
  """
  with open('/content/drive/MyDrive/Colab Notebooks/Tom&Jerry.txt') as f:
    strings = f.read().splitlines()
  #print(contents)
  #word = rdm.choice(contents).upper()
  #print('\n',word)

  """
  
  def unique(s):
 
    st = ""
    length = len(s)

    for i in range(length):
      c = s[i]
      if c not in st:
        st += c
    return len(st)

  words = [] 

  for string in strings:
  
    if unique(string)==4: 
      words += [string]
  #print(words)

  print('Grabbing a word for you...')
  word = rdm.choice(words).upper()
  print('I have found the perfect word for you. Go ahead Champ, you can start guessing...Remember you have only',lives,'lives!')

  while(lives>0):

    if lives==1:
      print("\nHold your horses! You have ONLY 1 LIFE LEFT. Choose your word wisely brat.")

    Guess= input("\n\nYour word? ").upper()
    while len(Guess) != 4 or unique(Guess) != 4:
      if len(Guess) != 4:
        Guess=input("It is a FOUR LETTER word game bro. Give me a FOUR LETTER word without repetitive letters.").upper()
      if unique(Guess) != 4:
        Guess= input("Your word contains repetitive letters. Give me a four letter word WITHOUT REPETITIVE LETTERS.").upper()
  
    Tom=0
    Jerry=0

    for i in range(len(Guess)):
      for j in range(len(word)):
        if Guess[i]==word[j] and i==j:
          Tom +=1
        elif Guess[i]==word[j] and i!=j:
          Jerry +=1

    if Tom==0 and Jerry==0:
      if(lives==1):
        print("Booooo! Wrong Guess. No letters from your word match my word. That was your last life, moron.")
        print(Tom,"Tom ",Jerry,"Jerry")
      else:
        print("Booooo! Wrong Guess. No letters from your word match my word.")
        print(Tom,"Tom ",Jerry,"Jerry")


    elif Tom==4 and Guess==word:
      print("Bravo! YOU WIN! You have guessed the word I chose. <",word,">")
      break

    else:
      print(Tom,"Tom ",Jerry,"Jerry")
      if(lives==1):
        print("That was your last life. You got so close, Champ. Better luck next time!")
      else:
        print("Good Guess. Go on, let's see if you can win")

    lives -=1
    print("\nYou have",lives,"lives left.")

  if lives == 0:
    print("\nAlas! YOU LOSE! You have used up all your lives. Choose your game difficulty wisely next time, moron.\nThe word was",word)

elif begin == 'no':
  print("Guess you are not interested. Can't force imbeciles.")
  exit()
