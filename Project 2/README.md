# Frequently Used Words — Code Explanation

This Python class implements a weighted moving average filter that processes a stream of numerical values in real-time.

---

## Class Overview: `WeightedAverage`

The class is designed to:

- Store a fixed-length history of recent input values
- Apply user-defined weights to these historical values
- Calculate a weighted average for each new input
- Process data streams incrementally, one value at a time

---

## Code Breakdown

### 1. Initialization

```python
def __init__(self, w: list[float]):
    self.w = w
    # Create a buffer to store the 'last n entries'
    # We assume initial values are 0 until filled
    self.history = deque([0.0] * len(w), maxlen=len(w))
```

- Parameters:
- - `w`: A list of weights where `w[0]` applies to the most recent value
- What happens:
- - Stores the weights list as `self.w`
- - Creates a deque (double-ended queue) with zeros as initial values
- - The deque has a fixed length equal to the number of weights
- - Example: `w = [5, 4, 3, 2, 1]` → `history = deque([0, 0, 0, 0, 0], maxlen=5)`

---

### 2. Processing Method

```python
def process(self, x: float) -> float:
    # 1. Update history with the new current entry (x becomes x[0])
    # We appendleft so the newest item is at index 0, matching w[0]
    self.history.appendleft(x)
    
    # 2. Calculate weighted sum
    # Formula: (w[0]*x[0] + w[1]*x[1] ... ) / n
    weighted_sum = sum(weight * val for weight, val in zip(self.w, self.history))
    
    # 3. Divide by n (length of weights)
    return weighted_sum / len(self.w)
```

**Step-by-step:**

1. Update History:

```python
self.history.appendleft(x)
```

- - Adds new value `x` to the beginning of the history

Automatically removes the oldest value (deque behavior)

Newest value (`x`) is now at index 0

2. Calculate Weighted Sum:

```python
weighted_sum = sum(weight * val for weight, val in zip(self.w, self.history))
```

- - Pairs each weight with its corresponding historical value

- - Multiplies them together

- - Sums all the products

- - Example: For weights `[5,4,3,2,1]` and history `[3,2,1,0,0]`:

- - - `5*3 + 4*2 + 3*1 + 2*0 + 1*0 = 15 + 8 + 3 + 0 + 0 = 26`

3. Normalize:

```python
return weighted_sum / len(self.w)
```

- - Divides by number of weights (not sum of weights)

- - Example: `26 / 5 = 5.2`
