import os
import re

# ============================================
# AnagramChecker Class (anagram_checker.py)
# ============================================

class AnagramChecker:
    """
    Class to check anagrams against a word list.
    No print statements in this class - only returns values.
    """
    
    def __init__(self, word_list_file="wordlist.txt"):
        """
        Load word list from file into a set for fast lookup.
        All words stored in lowercase for case-insensitive comparison.
        """
        self.words = set()
        
        # Create sample word list if file doesn't exist
        if not os.path.exists(word_list_file):
            self._create_sample_wordlist(word_list_file)
        
        # Load words from file
        try:
            with open(word_list_file, 'r', encoding='utf-8') as file:
                for line in file:
                    word = line.strip().lower()
                    if word.isalpha():  # Only add alphabetic words
                        self.words.add(word)
        except FileNotFoundError:
            pass  # words set remains empty
    
    def _create_sample_wordlist(self, filename):
        """Create a sample word list file for testing."""
        sample_words = """apple banana cherry date elderberry fig grape honeydew
kiwi lemon mango nectarine orange papaya quince raspberry strawberry
tomato watermelon
meat mate tame team
listen silent enlist inlets
triangle integral altering relating
night thing
below elbow bowel
desserts stressed
drawer reward
dormitory dirty room
the eyes they see
a gentleman elegant man
anagram nag a ram
arc car
arm ram mar
ate eat tea eta
bad dab
bat tab
now own won
on no
state taste
stare rates tears
rescue secure
notes stone tones
pores prose spore ropes
rebuild builder
remain airman marine
remains seminars
rescue secure
result rustle ulster
retain retina
ripper prier riper
risen resign siren
robber borber
saint stain satin
sales seals
salve slave vales
save vase
seated sedate
second docens
secure rescue
seeing signee
sees sees
seine seine
sense sense
sent nets tens
serve sever
sewed weeds
shout south thous
shut huts thus
sick dick
sinks skins
sister resist
sit its
slate stale steal tales least
sleep peels
slice isles
smile miles slime limes
snake sneak
sniper repins ripens
snow owns
soot oots
sore ores roes rose
sort rots
soul lous
soup opus
spate paste septa
spear spare reaps
spied siped
spilt slipt split
spine snipe pines
spit tips pits
split slipt spilt
spoil loops polis
spot post opts pots tops
sprout stroup
stain saint satin tains
stake steak takes
stale slate steal tales least
stall allts
star rats arts tars
stare rates tears tares
start tarts
state taste
steal slate stale tales least
steam teams meats mates
steel sleet
steer trees reset steer
stems stems
step pest pets sept
stew wets
stink knits skint
stole telos
stone notes tones
store rotes
stow tows twos
strap parts traps tarps
straw warts
stray artsy trays
strip sprit stirp
strop ports prost sport
strut sturt truts
stub buts tubs
stud dust
stun nuts tuns
sued dues used
sugar argus
suit suit
sulk skul
sum mus
sung guns snug
sunk skun
super purse
sure ruse user
surge urges
sway ways
sweat waste
sweet tweet
swell wells
swept wepts
swift swift
swing wings
swore worse
sworn rowns
tack catk
tale late teal
talk talk
tame mate meat team
tang gnat
tank rank
tape pate peat tepa
taps past pats spat
tare rate tear
taro rota
tars arts rats star
tart tart
task skat
tate tate
taut taut
teak take
teal tale late
team tame mate meat
tear rate tare
teas seat east eats sate
teen teen
tees tees
tell tell
temp temp
tens nets sent
tent tent
term term
tern rent
test test
text text
than than
that that
thaw what
thee thee
them them
then then
thin hint
this this
thou thou
thud duth
thug thug
thus thus
tick tick
tide tied diet edit
tidy tidy
tier rite tire
ties site
till till
tilt tilt
time emit item mite
ting ting
tins snit
tint tint
tiny tiny
tips pits spit
tire rite tier
toad dato
toes toes
toil loti
told dolt
tomb tomb
tone note
tons snot
took took
tool loot
toon onto
tops post opts pots spot
tore rote
torn torn
tort tort
toss toss
tote tote
tour rout
tout tout
toward toward
town town
tows twos stow
toys toys
tram mart
trap part rapt tarp
tray artsy
tree tree
trek trek
trim trim
trio riot
trip pits
trod trod
trot tort
true true
tube tube
tubs stub buts
tuck tuck
tuft tuft
tugs gust
tuna aunt
tune tune
turn runt
tusk tusk
twig twig
twin twin
twos stow tows
tyre tyre
ugly ugly
undo undo
unit unit
unto unto
upon upon
urge urge
urns runs
used dues sued
user ruse sure
vain vain
vale leva veal
vales salve slave
vase save
vats vast
veal vale leva
veil veil
vein vine
vent vent
very very
vest vets
veto vote
vial vail
vice vice
view view
vine vein
visa visa
void void
vote veto
vows vows
wade wade
wage wage
wail wail
wait wait
wake wake
wale weal
walk walk
wall wall
wand dawn
wane wean anew
want want
ward draw
ware wear
warm warm
warn warn
wars wars
wart wart
wary wary
wash shaw
wasp wasp
waste sweat
watch watch
water water
watt watt
wave wave
wavy wavy
weak weak
weal wale
wean wane anew
wear ware
webs webs
weds weds
weed weed
week week
weep weep
weir weir
well well
went went
wept wept
were were
west west
what thaw
when when
whet whet
whoa whoa
whom whom
wick wick
wide wide
wife wife
wild wild
will will
wind wind
wine wine
wing wing
wink wink
wins wins
wipe wipe
wire wire
wise wise
wish wish
wisp wisp
with with
woes woes
woke woke
wolf flow fowl
womb womb
wonk wonk
wont wont
wood wood
woof woof
wool wool
word word
wore wore
work work
worm worm
worn worn
wort wort
wove wove
wrap wrap
wren wren
writ writ
wyes wyes
yaks yaks
yams yams
yank yank
yard yard
yarn yarn
yawl yawl
yawn yawn
yeah yeah
year year
yeas yeas
yell yell
yelp yelp
yens yens
yeps yeps
yesk yesk
yeti yeti
yews yews
yill yill
yins yins
yipe yipe
yips yips
yird yird
yirr yirr
yobs yobs
yock yock
yodh yodh
yods yods
yoga yoga
yogh yogh
yogi yogi
yoke yoke
yoks yoks
yolk yolk
yond yond
yoni yoni
yore yore
your your
yous yous
yowe yowe
yowl yowl
yows yows
yoyo yoyo
yuan yuan
yuca yuca
yuch yuch
yuck yuck
yuks yuks
yule yule
yups yups
yurt yurt
yutz yutz
zags zags
zany zany
zaps zaps
zarf zarf
zeal zeal
zebu zebu
zeds zeds
zees zees
zein zein
zeks zeks
zell zell
zeps zeps
zerk zerk
zero zero
zest zest
zeta zeta
zigs zigs
zinc zinc
zine zine
zing zing
zins zins
zips zips
zits zits
zoic zoic
zona zona
zone zone
zonk zonk
zoom zoom
zoon zoon
zoos zoos
zori zori
zouk zouk
zyme zyme"""
        
        with open(filename, 'w') as f:
            f.write(sample_words)
        print(f"Created sample word list: {filename}")
    
    def is_valid_word(self, word):
        """
        Check if word exists in the loaded word list.
        Case-insensitive comparison.
        """
        return word.lower() in self.words
    
    def is_anagram(self, word1, word2):
        """
        Check if two words are anagrams (same letters, different order).
        Returns True if anagrams, False otherwise.
        """
        # Normalize: lowercase and sort characters
        return sorted(word1.lower()) == sorted(word2.lower())
    
    def get_anagrams(self, word):
        """
        Find all anagrams for the given word from the word list.
        Returns list of anagrams (excluding the word itself).
        """
        word_lower = word.lower()
        anagrams = []
        
        for candidate in self.words:
            # Skip if same word
            if candidate == word_lower:
                continue
            
            # Check if anagram
            if self.is_anagram(word_lower, candidate):
                anagrams.append(candidate)
        
        return sorted(anagrams)


# ============================================
# UI Functionality (anagrams.py)
# ============================================

class AnagramUI:
    """
    User interface for the Anagram Checker.
    Handles all input/output and menu display.
    """
    
    def __init__(self):
        self.checker = AnagramChecker()
        self.show_welcome()
    
    def show_welcome(self):
        """Display welcome message."""
        print("=" * 60)
        print("       ANAGRAM CHECKER")
        print("=" * 60)
        print("Find all possible anagrams for any English word!")
        print()
    
    def show_menu(self):
        """Display menu options."""
        print("\n" + "-" * 40)
        print("MENU:")
        print("1. Check a word for anagrams")
        print("2. Exit")
        print("-" * 40)
    
    def get_user_input(self):
        """
        Get and validate user input.
        Returns valid word or None if invalid.
        """
        user_input = input("\nEnter a word: ").strip()
        
        # Check for empty input
        if not user_input:
            print("Error: Empty input. Please enter a word.")
            return None
        
        # Check for multiple words
        if len(user_input.split()) > 1:
            print("Error: Only a single word is allowed.")
            return None
        
        # Check for non-alphabetic characters
        if not user_input.isalpha():
            print("Error: Only alphabetic characters allowed (no numbers or special characters).")
            return None
        
        return user_input.lower()
    
    def display_results(self, word):
        """
        Display word validation and anagram results.
        """
        print("\n" + "=" * 60)
        print(f'YOUR WORD: "{word.upper()}"')
        print("=" * 60)
        
        # Check if valid word
        is_valid = self.checker.is_valid_word(word)
        
        if is_valid:
            print("This is a valid English word.")
        else:
            print("This is NOT a valid English word.")
        
        # Get and display anagrams
        anagrams = self.checker.get_anagrams(word)
        
        if anagrams:
            print(f"\nAnagrams for your word: {', '.join(anagrams)}")
        else:
            print("\nNo anagrams found for this word.")
        
        print("=" * 60)
    
    def run(self):
        """Main program loop."""
        while True:
            self.show_menu()
            choice = input("Select option (1-2): ").strip()
            
            if choice == "1":
                word = self.get_user_input()
                if word:
                    self.display_results(word)
            elif choice == "2":
                print("\nThank you for using Anagram Checker!")
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please enter 1 or 2.")


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    # Create and run the UI
    app = AnagramUI()
    app.run()