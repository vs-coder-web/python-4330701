filename = input("Enter File Name: ")
f = open(filename, 'r')
data = f.read()

# Calculate average word length and sentence length
words = data.split()
sentences = data.split(".")
total_words = 0
total_sentences = 0

for word in words:
    total_words += len(word)
    
for sentence in sentences:
    total_sentences += len(sentence)

average_word_len = total_words / len(words)
average_sentence_len = total_sentences / len(sentences)

print(f"Average Word Length: {average_word_len}")
print(f"Average Sentence Length: {average_sentence_len}")