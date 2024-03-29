
#7. WAP to ask for a sentence and count the number of words

def countWords(sentence):
    words =sentence.split();
    return len(words);

if __name__ == "__main__":
    sentence=input("Enter a sentence:");
    wordCount=countWords(sentence)
    print(f"The number of words in the sentence is:{wordCount}")