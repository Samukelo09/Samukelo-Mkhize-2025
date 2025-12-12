from collections import deque

class WeightedAverage:
    def __init__(self, w: list[float]):
        self.w = w
        # Create a buffer to store the 'last n entries'
        # We assume initial values are 0 until filled
        self.history = deque([0.0] * len(w), maxlen=len(w))

    def process(self, x: float) -> float:
        # 1. Update history with the new current entry (x becomes x[0])
        # We appendleft so the newest item is at index 0, matching w[0]
        self.history.appendleft(x)
        
        # 2. Calculate weighted sum
        # Formula: (w[0]*x[0] + w[1]*x[1] ... ) / n
        weighted_sum = sum(weight * val for weight, val in zip(self.w, self.history))
        
        # 3. Divide by n (length of weights)
        return weighted_sum / len(self.w)

# --- Usage to match PDF Requirement ---
# Weights = [5, 4, 3, 2, 1]
wa = WeightedAverage(w=[5.0, 4.0, 3.0, 2.0, 1.0])

# Signal x = [1, 2, 3, 4, 5]
# We must feed them one by one
inputs = [1, 2, 3, 4, 5]

print("Processing signal stream...")
for val in inputs:
    result = wa.process(val)
    print(f"Input: {val} -> Output: {result}")