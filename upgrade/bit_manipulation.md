# 🔥 Bit Manipulation Tricks for DSA Interviews (Python-Focused)

Welcome to your cheat-sheet of the most **interview-friendly** bit manipulation tricks.  
Master these and you’ll have “leet” status for any coding round.

---

## Table of Contents

1. [Check if Number is Even/Odd](#even-odd)
2. [Get, Set, Clear, and Toggle nth Bit](#bit-n-ops)
3. [Counting Set Bits (1s) in a Number](#count-bits)
4. [Swapping Two Numbers Without Temp](#swap-xor)
5. [Finding Single Non-Duplicate in Array (All Others Twice)](#single-number)
6. [Check Power of Two](#power-of-two)
7. [Turn Off Rightmost 1-bit](#turn-off-rightmost)
8. [Get Lowest Set Bit](#lowest-set-bit)
9. [Subset Enumeration using Bits](#subset-enum)
10. [Add Two Numbers Without `+`](#add-no-plus)

---

### 1. Check if Number is Even/Odd <a name="even-odd"></a>

```python
n = 7
if n & 1:
    print("Odd")
else:
    print("Even")
```
**Trick:** The least significant bit tells you everything.

---

### 2. Get, Set, Clear, and Toggle nth Bit <a name="bit-n-ops"></a>

```python
x = 13      # 1101

# Get nth bit
n = 2
print((x >> n) & 1)  # 1 (3rd bit from right is 1)

# Set nth bit
x |= (1 << n)

# Clear nth bit
x &= ~(1 << n)

# Toggle nth bit
x ^= (1 << n)
```

---

### 3. Counting Set Bits (Brian Kernighan’s Algorithm) <a name="count-bits"></a>

```python
count = 0
n = 29  # 11101
while n:
    n &= (n - 1)
    count += 1
print(count)  # Output: 4
```
**Trick:** Each loop removes the rightmost set bit.

---

### 4. Swapping Two Numbers Without Temp (XOR Swap) <a name="swap-xor"></a>

```python
a, b = 5, 9
a ^= b
b ^= a
a ^= b
```
**Use only for trivia; Pythonic swap is `a, b = b, a`**

---

### 5. Find the Single Non-Duplicate in Array (All Others Twice) <a name="single-number"></a>

```python
arr = [2, 3, 5, 4, 5, 3, 2]
unique = 0
for num in arr:
    unique ^= num
print(unique)  # Output: 4
```
**Trick:** XOR of duplicates cancels out.

---

### 6. Check if Number is a Power of Two <a name="power-of-two"></a>

```python
n = 16
if n > 0 and (n & (n - 1)) == 0:
    print("Power of Two")
```
**Trick:** Only powers of two have a single set bit.

---

### 7. Turn Off Rightmost 1-bit <a name="turn-off-rightmost"></a>

```python
n = 12  # 1100
n = n & (n - 1)
print(n)  # Output: 8 (1000)
```
**Trick:** Removes the lowest set bit.

---

### 8. Get Value of the Lowest Set Bit <a name="lowest-set-bit"></a>

```python
n = 12  # 1100
print(n & -n)  # Output: 4 (0100)
```
**Trick:** Isolates the lowest 1-bit.

---

### 9. Subset Enumeration using Bits <a name="subset-enum"></a>

```python
nums = [10, 20, 30]
n = len(nums)
for mask in range(1 << n):
    subset = [nums[i] for i in range(n) if mask & (1 << i)]
    print(subset)
```
**Trick:** All possible subsets (power set) in O(2^n) time.

---

### 10. Add Two Numbers Without `+` (Interview Flex) <a name="add-no-plus"></a>

```python
def add(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(add(13, 7))  # Output: 20
```
**Trick:** Pure bitwise sum, no arithmetic operators.

---

## ⭐️ Advanced DSA Problems Involving Bits

- **Find missing number in 1...n:** Use XOR trick
- **Number appears three times, one appears once:** Use bit counting (for each bit position)
- **Reverse bits in an integer:** Bitwise shifting + masking
- **Gray code sequence generation**
- **Bitmask DP for subset/combination problems**

---

**Bit tricks = time and space save + massive “interviewer respect” unlock.  
Save this file, print it, or tattoo it—up to you. 😎**