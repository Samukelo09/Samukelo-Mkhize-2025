from collections import Counter
import re

class FrequentlyUsedWords:
    # Initialize with the number of top frequent words to extract
    def __init__(self, n: int = 10):
        self.n = n
        self.counter = Counter() # To store word counts

    # Process a single word, sanitize it, and update the counter
    def extract(self, text: str):
        # Lowercase the text and remove non-alphanumeric characters
        cleaned_text = re.sub(r'[^\w]', '', text.lower())

        # Only proceed if cleaned text is not empty
        if cleaned_text:
            self.counter.update([cleaned_text])

    # Return the n most common words
    def get_most_common(self):
        # Return only the words, not their counts
        return [word for word, _ in self.counter.most_common(self.n)]
    

freq_words_extractor = FrequentlyUsedWords(n=5)
text = "Cristiano Ronaldo is a Portuguese professional footballer who plays as a forward. Ronaldo is widely regarded as one of the greatest footballers of all time. Ronaldo has won numerous awards and accolades throughout his career."
print(f"Processing text: '{text}'\n")

# Split the text into words and extract each word
for word in text.split():
    freq_words_extractor.extract(word)

    # Print the current most common words after each extraction
    current_common = freq_words_extractor.get_most_common()
    print(f"Read '{word}': Current top: {freq_words_extractor.n} -> {current_common}")