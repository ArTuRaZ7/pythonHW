class Analyze:

    def __init__(self, f):
        f.seek(0)
        self.f = f.readlines()

    def count_letter(self):
        count_letter = 0
        for lines in self.f:
            for i in lines.lower():
                if i.isalpha():
                    count_letter+=1
        return count_letter

    def cout_str(self):
        return len(self.f)

    def count_words(self):
        import re
        count_words = 0
        for lines in self.f:
            count_words += len(re.sub('\W', ' ', lines).split())
        return count_words

class Russian_analyze(Analyze):
    def __init__(self,f):
        super().__init__(f)

    def count_ruletter(self):
        ruletter_count = 0
        ruletter = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р",
                    "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}
        for lines in self.f:
            for i in lines.lower():
                if i in ruletter:
                    ruletter_count+=1
        return ruletter_count

    def count_ruwords(self):
        import re
        count_ruwords=0
        r = "[А-ЯЁа-яё]+"
        for lines in self.f:
            count_ruwords+=len([x for x in re.split(r,lines) if x!=""])

        return count_ruwords

class Digitanalyze(Analyze):
    def __init__(self,f):
        super().__init__(f)

    def count_digit(self):
        digits = {"1", "2", "3", "4", "5", "6","7","8","9","0"}
        count_digit = 0
        for lines in self.f:
            for i in lines:
                if i in digits:
                    count_digit+=1

        return count_digit

    def count_numbers(self):
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        numbers_count = 0
        for lines in self.f:
            for i in lines.split():
                if i[0] in digits:
                    numbers_count+=1
        return numbers_count

class Frequency_Analyze(Analyze):
    def __init__(self,f):
        super().__init__(f)

    def word_max_frequency(self):
        import re
        counter = {}
        for lines in self.f:
            for i in re.sub('\W', ' ', lines).split():
                counter[i] = counter.get(i,0)+1
        max_count = max(counter.values())
        most_frequent = [k for k, v in counter.items() if v == max_count]
        return most_frequent[0]


with open("text.txt", "r", encoding="utf-8") as f:
    file = Frequency_Analyze(f)
    print(file.word_max_frequency())
