import random
from collections import Counter

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def simroll(n):
    results = []
    for _ in range(n):
        total = roll_dice()
        results.append(total)
    
    return results

def answers(results, n):
  
    counts = Counter(results)

    print(f"\nResults after {n} rolls:\n")
    for total in range(2, 13):
        count = counts[total]
        
        print(f"Sum {total}: {count} / {n}")

def main():
    n = int(input("numrolls): "))
    
    results = simroll(n)

    answers(results, n)

if __name__ == "__main__":
    main()
