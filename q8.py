from collections import Counter

def main():
    inp = []
    print("Enter text")
    
    while True:
        inpy = input().strip()
        if inpy == "":
            break
        inp.append(inpy)
    
    if not inp:
        print("No text entered.")
        return
    
  
    inpp = " ".join(inp)
    words = inpp.lower().split()

    word_count = Counter(words)
  
    total_words = sum(word_count.values())
    
