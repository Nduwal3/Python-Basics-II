# Write code that will print out the anagrams (words that use the same 
# letters) from a paragraph of text. 


sample_paragraph = "cat act tac god dog hat good food godo tool loot "

def paragraph_to_list(sample_paragraph):
    words_list = sample_paragraph.split(' ')
    return words_list

def print_anagram(word_list):
    anagram_list = []
    index = 0
    for i in word_list:
        for j in word_list:
            if i != j and (sorted(i) == sorted(j)):
                if i not in anagram_list:
                    anagram_list.insert(index, i)
                    index += 1 
    print(anagram_list)

word_list = paragraph_to_list(sample_paragraph)
print_anagram(word_list )







