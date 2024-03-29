#11.Wap to ask for a sentence and calculate the frequency of characters in the sentences
def characterFrequency(sentence):
    frequency = {}
    for char in sentence:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    charFreq = characterFrequency(sentence)
    print("Character frequency in the sentence:")
    for char, freq in charFreq.items():
        print(f"'{char}': {freq}")
