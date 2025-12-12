# Frequently Used Words — Code Explanation

This Python script defines a small utility for tracking the most frequently used words in a given text. It uses Python’s built‑in `Counter` class to count occurrences and regular expressions to sanitize input.

---

## Class Overview: `FrequentlyUsedWords`

The class is designed to:

- Accept a number **`n`** representing how many top frequent words to return.
- Process text **one word at a time**.
- Clean each word by removing punctuation and converting it to lowercase.
- Keep an internal counter of all processed words.
- Return the **top `n` most common words**.

---

## Code Breakdown

### 1. Initialization

```python
def __init__(self, n: int = 10):
    self.n = n
    self.counter = Counter()
```

- `n` determines how many frequent words to return.
- `self.counter` stores word counts using `collections.Counter`.

---

### 2. Extracting and Cleaning Words

```python
def extract(self, text: str):
    cleaned_text = re.sub(r'[^\w]', '', text.lower())
    if cleaned_text:
        self.counter.update([cleaned_text])
```

- Converts the word to lowercase.
- Removes all non‑alphanumeric characters using regex.
- Updates the counter only if the cleaned word is not empty.

---

### 3. Getting the Most Common Words

```python
def get_most_common(self):
    return [word for word, _ in self.counter.most_common(self.n)]
```

- Retrieves the top `n` most frequent words.
- Returns only the words, not their counts.

---

## Running the Extractor

```python
freq_words_extractor = FrequentlyUsedWords(n=5)
text = "Cristiano Ronaldo is a Portuguese professional footballer who plays as a forward. Ronaldo is widely regarded as one of the greatest footballers of all time. Ronaldo has won numerous awards and accolades throughout his career."
```

- Creates an instance that will track the top 5 words.
- Defines a sample paragraph about Cristiano Ronaldo.

---

## Processing the Text

```python
for word in text.split():
    freq_words_extractor.extract(word)
    current_common = freq_words_extractor.get_most_common()
    print(f"Read '{word}': Current top: {freq_words_extractor.n} -> {current_common}")
```

- Splits the text into individual words.
- Processes each word through the extractor.
- Prints the current top 5 most frequent words after each update.

---

## Summary

This script demonstrates:

- Basic text preprocessing.
- Word frequency counting using `Counter`.
- Incremental updates and real‑time tracking of most common words.

It’s a simple but effective example of how to build a lightweight word‑frequency analyzer in Python.
