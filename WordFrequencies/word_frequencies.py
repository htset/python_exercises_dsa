from collections import defaultdict

def clean_word(word):
    #Remove non-letter characters and convert to lowercase
    return ''.join([char.lower() for char in word if char.isalpha()])

def main():
    word_frequency = defaultdict(int)  #Dictionary to store word frequencies

    # Read text from file
    try:
        with open('input.txt', 'r') as input_file:
            for line in input_file:
                #Split each line into words
                words = line.split()  
                for word in words:
                    #Clean each word
                    cleaned_word = clean_word(word)  
                    if cleaned_word:
                        #Update the word frequency
                        word_frequency[cleaned_word] += 1  
    except IOError as e:
        print(e)  #Handle any IO exceptions

    #Display word frequencies
    print("Word Frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
