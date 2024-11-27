def main():
    frequency()

def frequency():
    def dictionary_generator(string):
        dictionary = {}

        for letter in string:
            if letter == ' ':
                letter = 'spaces'
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        return dictionary

    print(dictionary_generator(str(input("Insert string: "))))

def split():
    def word_count(sentence):
        words = len(sentence.split())
        return words

    print(word_count(input("Insert a sentence: ")))

def split_dictionary():
    def dictionary_generator(string):
        dictionary = {}
        words = string.split()

        for word in words:
            word = word.lower()
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
        return dictionary

    print(dictionary_generator(str(input("Insert sentence: "))))

def punctuation_remover():
    def eliminator(sentence):
        import string
        dictionary = {}
        clean_sentence = sentence.translate(str.maketrans("", "", string.punctuation))
        words = clean_sentence.lower().split()

        for word in words:
            word = word.lower()
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
        return dictionary

    print(eliminator(str(input("Insert sentence: "))))

main()
