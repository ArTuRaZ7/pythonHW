class Analyze:

    def set_path(self):
        self.path = input("Введите адрес файла")

    stat = {}

    def cout(self):
        count_vowel = 0
        count_consonant = 0
        count_symbols = 0
        count_strings = 0
        count_numbers = 0

        set_of_numbers = {"1", "2", "3", "4", "5", "6", "7", "9", "0"}
        set_of_vowel = {"a", "e", "i", "o", "u", "y"}
        set_of_consonant = {'b', 'c', 'd', 'f', 'g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'}

        with open(self.path, "r") as f:
            for line in f:
                count_strings += 1
                for i in line.lower():
                    count_symbols += 1
                    if i in set_of_vowel:
                        count_vowel += 1
                    elif i in set_of_consonant:
                        count_consonant += 1
                    elif i in set_of_numbers:
                        count_numbers += 1
        self.stat = {"count_vowel":count_vowel, "count_consonant":count_consonant, "count_symbols":count_symbols,
                     "count_strings":count_strings, "count_numbers":count_numbers}
file1 = Analyze()
file1.set_path()
file1.cout()
print(file1.stat)