import string

class PangramChecker:
    # Check if the given text is a pangram
    def is_pangram(self, str1: str, alphabet: str = string.ascii_lowercase) -> bool:

        # Create a set of characters in the text, converted to lowercase
        text_set = set(str1.lower())

        # Convert the alphabet to a set for comparison
        alphabet_set = set(alphabet)

        # Check if all alphabet letters are in the text set
        return alphabet_set.issubset(text_set)
    
text = "The quick brown fox jumps over the lazy dog"
pangram_checker = PangramChecker()
result = pangram_checker.is_pangram(text)
print(result)