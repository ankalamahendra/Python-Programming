def remove_common_words(s1, s2):
    words1 = set(s1.split())
    words2 = set(s2.split())

    unique_words1 = words1 - words2
    unique_words2 = words2 - words1

    result1 = ' '.join(unique_words1)
    result2 = ' '.join(unique_words2)

    return result1, result2

sentence1 =eval(input("Enter the sentence 1: "))
sentence2 =eval(input("Enter the sentence 2: "))

result1, result2 = remove_common_words(sentence1, sentence2)

print("Sentence 1 after removing common words:", result1)
print("Sentence 2 after removing common words:", result2)
