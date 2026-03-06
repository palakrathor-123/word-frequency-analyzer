def count_words_manual(sentence):
    # Preprocessing: convert to lowercase and split the sentence into a list of words
    # The split() method divides by whitespace by default
    words = sentence.lower().split()
    
    # Create an empty dictionary to store word frequencies
    word_freq = {}
    
    # Iterate through each word in the list
    for word in words:
        # Use the get() method to increment the count, defaulting to 0 if the word is new
        word_freq[word] = word_freq.get(word, 0) + 1
        
    return word_freq

sentence = "The quick brown fox jumps over the lazy dog. The quick fox."
print(count_words_manual(sentence))