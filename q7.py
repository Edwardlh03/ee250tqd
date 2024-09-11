
def main():

    inp = input("Enter numbers separated by whitespace: ")
    

    numbers_str = inp.split()
    
    numbers = [float(num) for num in numbers_str]
    
    average = sum(numbers) / len(numbers)
    print(f"avg: {average}")

if __name__ == "__main__":
    main()
