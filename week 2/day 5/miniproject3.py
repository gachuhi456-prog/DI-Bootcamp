import random

# ============================================
# Exercise 1: OOP Quiz - Answers
# ============================================
print("=" * 70)
print("Exercise 1: OOP Quiz - Answers")
print("=" * 70)

quiz_answers = """
1. What is a class?
   A class is a blueprint/template for creating objects. It defines attributes 
   (data) and methods (functions) that the objects will have.
   Example: A 'Car' class defines that all cars have color, brand, and can drive().

2. What is an instance?
   An instance is a specific object created from a class. It's a concrete 
   realization of the class blueprint.
   Example: my_car = Car("red", "Toyota") creates an instance of the Car class.

3. What is encapsulation?
   Encapsulation is bundling data (attributes) and methods that operate on that 
   data within a single unit (class), while restricting direct access to some 
   components. This is done using private/protected attributes (e.g., _variable).
   Purpose: Data hiding and protection from external interference.

4. What is abstraction?
   Abstraction is hiding complex implementation details and showing only the 
   essential features of an object. Users interact with a simplified interface 
   without knowing internal workings.
   Example: You use a 'start_engine()' method without knowing how the engine works.

5. What is inheritance?
   Inheritance allows a class (child/subclass) to inherit attributes and methods 
   from another class (parent/superclass). This promotes code reuse.
   Example: class ElectricCar(Car) inherits from Car but adds battery features.

6. What is multiple inheritance?
   Multiple inheritance allows a class to inherit from more than one parent class.
   The child gets features from all parents.
   Example: class FlyingCar(Car, Airplane) inherits from both Car and Airplane.

7. What is polymorphism?
   Polymorphism means "many forms." It allows objects of different classes to 
   be treated as objects of a common parent class, or the same method to behave 
   differently based on the object calling it.
   Example: Both Dog and Cat have speak() method, but Dog says "woof" and Cat says "meow".

8. What is Method Resolution Order (MRO)?
   MRO is the order in which Python looks for methods in a class hierarchy, 
   especially with multiple inheritance. It follows the C3 linearization 
   algorithm (depth-first, left-to-right).
   You can view it with: ClassName.__mro__ or ClassName.mro()
"""

print(quiz_answers)


# ============================================
# Exercise 2: Deck of Cards
# ============================================
print("\n" + "=" * 70)
print("Exercise 2: Deck of Cards")
print("=" * 70)

class Card:
    """
    Represents a playing card with suit and value.
    Does NOT inherit from any class.
    """
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self, suit, value):
        """
        Initialize a card with suit and value.
        
        Args:
            suit: Must be one of Card.SUITS
            value: Must be one of Card.VALUES
        """
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {self.SUITS}")
        if value not in self.VALUES:
            raise ValueError(f"Invalid value: {value}. Must be one of {self.VALUES}")
        
        self.suit = suit
        self.value = value
    
    def __str__(self):
        """User-friendly string representation."""
        return f"{self.value} of {self.suit}"
    
    def __repr__(self):
        """Official representation."""
        return f"Card('{self.suit}', '{self.value}')"
    
    def __eq__(self, other):
        """Check if two cards are equal."""
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value
        return False


class Deck:
    """
    Represents a deck of 52 playing cards.
    Does NOT inherit from Card class.
    """
    
    def __init__(self):
        """
        Initialize a new deck with all 52 cards.
        Cards are created but NOT shuffled initially.
        """
        self.cards = []
        self._create_deck()
    
    def _create_deck(self):
        """Create all 52 cards and add to deck."""
        self.cards = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                new_card = Card(suit, value)
                self.cards.append(new_card)
    
    def shuffle(self):
        """
        Ensure deck has all 52 cards, then shuffle randomly.
        If cards are missing, recreate the deck first.
        """
        if len(self.cards) != 52:
            print("Deck incomplete! Recreating full deck...")
            self._create_deck()
        
        random.shuffle(self.cards)
        print("Deck shuffled!")
    
    def deal(self):
        """
        Deal a single card from the top of the deck.
        Removes the card from the deck.
        
        Returns:
            Card object, or None if deck is empty
        """
        if len(self.cards) == 0:
            print("No cards left in deck!")
            return None
        
        return self.cards.pop()
    
    def count(self):
        """Return number of cards remaining in deck."""
        return len(self.cards)
    
    def __str__(self):
        """String representation of deck."""
        return f"Deck of {len(self.cards)} cards"
    
    def display_remaining(self):
        """Display all remaining cards in deck."""
        print(f"\nRemaining cards ({len(self.cards)}):")
        for i, card in enumerate(self.cards, 1):
            print(f"  {i}. {card}")


# ============================================
# Test the Deck of Cards
# ============================================
def test_deck():
    """Test all Deck and Card functionality."""
    
    print("\n--- Creating New Deck ---")
    deck = Deck()
    print(f"Created: {deck}")
    
    print("\n--- Shuffling Deck ---")
    deck.shuffle()
    
    print("\n--- Dealing 5 Cards ---")
    dealt_cards = []
    for i in range(5):
        card = deck.deal()
        if card:
            dealt_cards.append(card)
            print(f"Dealt {i+1}: {card}")
    
    print(f"\nCards remaining in deck: {deck.count()}")
    
    print("\n--- Testing Edge Cases ---")
    
    # Test dealing from empty deck
    print(f"\nDealing all remaining {deck.count()} cards...")
    while deck.count() > 0:
        deck.deal()
    
    print(f"Deck empty: {deck.count()} cards")
    empty_card = deck.deal()  # Should return None
    print(f"Attempt to deal from empty: {empty_card}")
    
    # Test shuffle recreates deck
    print("\n--- Testing Shuffle Recreation ---")
    deck.shuffle()  # Should recreate 52 cards
    print(f"After shuffle: {deck.count()} cards")
    
    # Test specific card creation
    print("\n--- Testing Card Creation ---")
    ace_spades = Card('Spades', 'A')
    king_hearts = Card('Hearts', 'K')
    print(f"Created: {ace_spades}")
    print(f"Created: {king_hearts}")
    print(f"Are they equal? {ace_spades == king_hearts}")
    
    # Test invalid card
    print("\n--- Testing Invalid Card ---")
    try:
        invalid_card = Card('InvalidSuit', 'A')
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    print("\n--- Final Deck State ---")
    deck2 = Deck()
    deck2.shuffle()
    print(f"New shuffled deck: {deck2.count()} cards")
    print("Top 5 cards:", [str(deck2.cards[i]) for i in range(5)])


# ============================================
# Interactive Demo
# ============================================
def interactive_demo():
    """Interactive card dealing demo."""
    print("\n" + "=" * 70)
    print("Interactive Card Dealing")
    print("=" * 70)
    
    deck = Deck()
    deck.shuffle()
    
    while True:
        print(f"\n{deck}")
        choice = input("Deal a card? (y/n): ").lower().strip()
        
        if choice == 'y':
            card = deck.deal()
            if card:
                print(f"  -> You got: {card}")
            else:
                print("Deck is empty! Creating new deck...")
                deck = Deck()
                deck.shuffle()
        elif choice == 'n':
            print(f"\nFinal count: {deck.count()} cards remaining")
            break
        else:
            print("Please enter 'y' or 'n'")


# ============================================
# Main Execution
# ============================================
if __name__ == "__main__":
    # Run tests
    test_deck()
    
    # Run interactive demo (optional)
    print("\n" + "=" * 70)
    run_interactive = input("Run interactive demo? (y/n): ").lower().strip()
    if run_interactive == 'y':
        interactive_demo()
    
    print("\n" + "=" * 70)
    print("All tests completed!")
    print("=" * 70)