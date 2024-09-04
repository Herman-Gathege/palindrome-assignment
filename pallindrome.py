def load_words(filename):
    """Load words from a file and return a list of words."""
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def find_palindromes(words):
    """Find and return a list of palindromes from the given list of words."""
    palindromes = []
    for word in words:
        if word == word[::-1]:  # Check if the word is a palindrome
            palindromes.append(word)
    return palindromes

def add_word_to_file(filename, word):
    """Add a new word to the dictionary file."""
    with open(filename, 'a') as file:
        file.write(word + '\n')
    print(f"Added '{word}' to the dictionary.")

def main():
    filename = 'dictionary.txt'

    # Menu loop
    while True:
        print("\nMenu:")
        print("1. Find palindromes")
        print("2. Add a new word")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            # Load words from the file
            words = load_words(filename)
            
            # Find palindromes
            palindromes = find_palindromes(words)
            
            # Print the list of palindromes
            print("\nPalindromes found:")
            if palindromes:
                for palindrome in palindromes:
                    print(palindrome)
            else:
                print("No palindromes found.")
        
        elif choice == '2':
            # Get new word from user
            new_word = input("Enter the new word to add: ").strip()
            
            # Add word to the file
            add_word_to_file(filename, new_word)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
