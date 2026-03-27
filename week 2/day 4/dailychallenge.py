import string
import re
from collections import Counter

# ============================================
# Part I & II: Text Class
# ============================================

class Text:
    def __init__(self, text):
        """Initialize Text with a string."""
        self.text = text
    
    def word_frequency(self, word):
        """
        Count occurrences of a specific word in the text.
        
        Args:
            word: The word to search for
        
        Returns:
            Count of word occurrences, or message if not found
        """
        # Normalize: lowercase and remove basic punctuation for word matching
        words = self._get_words()
        word = word.lower()
        
        count = words.count(word)
        
        if count == 0:
            return f"'{word}' not found in text."
        return count
    
    def most_common_word(self):
        """
        Find the most frequently occurring word in the text.
        
        Returns:
            Tuple of (word, frequency) or message if empty
        """
        words = self._get_words()
        
        if not words:
            return "No words found in text."
        
        # Count frequencies
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)[0]
        
        return most_common  # (word, count)
    
    def unique_words(self):
        """
        Return a list of unique words in the text.
        
        Returns:
            List of unique words
        """
        words = self._get_words()
        unique = list(set(words))
        return sorted(unique)  # Return sorted for consistency
    
    def _get_words(self):
        """Helper method to extract clean words from text."""
        # Convert to lowercase and extract words (alphanumeric only)
        text_lower = self.text.lower()
        # Use regex to find words (sequences of letters)
        words = re.findall(r'\b[a-z]+\b', text_lower)
        return words
    
    @classmethod
    def from_file(cls, file_path):
        """
        Class method to create Text instance from file.
        
        Args:
            file_path: Path to text file
        
        Returns:
            Text instance with file content
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            print(f"Successfully loaded file: {file_path}")
            return cls(content)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return cls("")  # Return empty Text instance
        except Exception as e:
            print(f"Error reading file: {e}")
            return cls("")
    
    def __str__(self):
        """String representation of Text."""
        preview = self.text[:50] + "..." if len(self.text) > 50 else self.text
        return f"Text({preview})"
    
    def __repr__(self):
        """Official representation."""
        return f"Text(text_length={len(self.text)})"


# ============================================
# Bonus: TextModification Class
# ============================================

class TextModification(Text):
    """
    Extended Text class with text cleaning methods.
    Inherits from Text class.
    """
    
    # Common English stop words
    STOP_WORDS = {
        'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
        'before', 'after', 'above', 'below', 'between', 'among', 'is', 'are',
        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do',
        'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
        'must', 'shall', 'can', 'need', 'dare', 'ought', 'used', 'it', 'its',
        'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'we', 'they',
        'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'our',
        'their', 'mine', 'yours', 'hers', 'ours', 'theirs', 'what', 'which',
        'who', 'whom', 'whose', 'where', 'when', 'why', 'how', 'all', 'any',
        'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
        'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just',
        'as', 'if', 'because', 'until', 'while', 'here', 'there', 'then', 'once'
    }
    
    def remove_punctuation(self):
        """
        Remove all punctuation from text.
        
        Returns:
            Text without punctuation
        """
        # Use string.punctuation to get all punctuation characters
        translator = str.maketrans('', '', string.punctuation)
        clean_text = self.text.translate(translator)
        return clean_text
    
    def remove_stop_words(self):
        """
        Remove common stop words from text.
        
        Returns:
            Text without stop words
        """
        words = self._get_words()
        # Filter out stop words
        filtered_words = [word for word in words if word not in self.STOP_WORDS]
        return ' '.join(filtered_words)
    
    def remove_special_characters(self):
        """
        Remove special characters using regex.
        Keeps only alphanumeric and whitespace.
        
        Returns:
            Text without special characters
        """
        # Remove anything that's not a letter, number, or whitespace
        clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return clean_text
    
    def full_clean(self):
        """
        Apply all cleaning methods: punctuation, special chars, stop words.
        
        Returns:
            Fully cleaned text
        """
        # Step 1: Remove special characters
        text = self.remove_special_characters()
        # Step 2: Remove punctuation (redundant but safe)
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Step 3: Remove stop words
        words = re.findall(r'\b[a-z]+\b', text.lower())
        filtered = [w for w in words if w not in self.STOP_WORDS]
        return ' '.join(filtered)


# ============================================
# Test Functions
# ============================================

def test_text_class():
    """Test the Text class."""
    print("=" * 60)
    print("Testing Text Class")
    print("=" * 60)
    
    sample_text = """
    Hello world! Hello everyone. This is a simple text.
    Hello world again. This text is for testing purposes.
    """
    
    text_obj = Text(sample_text)
    print(f"\nCreated: {text_obj}")
    
    # Test word_frequency
    print(f"\nWord 'hello' frequency: {text_obj.word_frequency('hello')}")
    print(f"Word 'python' frequency: {text_obj.word_frequency('python')}")
    
    # Test most_common_word
    most_common = text_obj.most_common_word()
    print(f"\nMost common word: '{most_common[0]}' (appears {most_common[1]} times)")
    
    # Test unique_words
    unique = text_obj.unique_words()
    print(f"\nUnique words ({len(unique)} total): {unique[:10]}...")
    
    return text_obj


def test_text_modification():
    """Test the TextModification class."""
    print("\n" + "=" * 60)
    print("Testing TextModification Class")
    print("=" * 60)
    
    messy_text = """
    Hello!!! How are you? This is a test... with @#$ special chars!!!
    The quick brown fox jumps over the lazy dog. 
    Is this working? Yes, it is working perfectly!!!
    """
    
    mod = TextModification(messy_text)
    print(f"\nOriginal text preview:\n{mod.text[:100]}...")
    
    # Test remove_punctuation
    no_punct = mod.remove_punctuation()
    print(f"\n--- Without Punctuation ---\n{no_punct[:100]}...")
    
    # Test remove_special_characters
    no_special = mod.remove_special_characters()
    print(f"\n--- Without Special Characters ---\n{no_special[:100]}...")
    
    # Test remove_stop_words
    no_stops = mod.remove_stop_words()
    print(f"\n--- Without Stop Words ---\n{no_stops[:100]}...")
    
    # Test full clean
    fully_clean = mod.full_clean()
    print(f"\n--- Fully Cleaned ---\n{fully_clean[:100]}...")
    
    # Test inherited methods still work
    print(f"\nInherited - Most common word: '{mod.most_common_word()[0]}'")
    print(f"Inherited - 'test' frequency: {mod.word_frequency('test')}")


def test_file_operations():
    """Test loading from file."""
    print("\n" + "=" * 60)
    print("Testing File Operations")
    print("=" * 60)
    
    # Create a sample file
    sample_content = """
    Python is amazing. Python is powerful.
    Learning Python is fun and rewarding.
    File handling in Python is straightforward.
    """
    
    filename = "sample_text.txt"
    
    try:
        with open(filename, 'w') as f:
            f.write(sample_content)
        print(f"Created sample file: {filename}")
        
        # Load using class method
        file_text = Text.from_file(filename)
        print(f"\nLoaded text: {file_text}")
        
        print(f"\nMost common word: '{file_text.most_common_word()[0]}'")
        print(f"Unique words count: {len(file_text.unique_words())}")
        
        # Clean with TextModification
        mod_file = TextModification(file_text.text)
        print(f"\nCleaned text: {mod_file.full_clean()[:100]}...")
        
    except Exception as e:
        print(f"File test error: {e}")
    finally:
        # Cleanup
        import os
        if os.path.exists(filename):
            os.remove(filename)
            print(f"\nCleaned up: {filename}")


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    # Run all tests
    test_text_class()
    test_text_modification()
    test_file_operations()
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)