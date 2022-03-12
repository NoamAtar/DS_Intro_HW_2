#A
def reverse(sentence, reverse_word):
    if type(sentence) != str or type(reverse_word) != str:
       return('invalid input')
    if reverse_word in sentence:
        n_sentence = sentence.replace(reverse_word, reverse_word[::-1], 1)
        return str(n_sentence)
    else:
        return("The word was not found")

print(reverse("I like apples and I also like bananas", "like"))
print(reverse("I like apples and I also like bananas", "oranges"))
print(reverse("I like apples and I also like bananas", 3))

