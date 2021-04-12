# Общий класс биологических последовательностей
class Bio_seq:
    
    def __init__(self, seq):
        self.seq = seq
        self.i = 0

    def __iter__(self):
        return iter(self.seq)

    def __next__(self):
        if self.i < len(self.seq):
            nucleotide = self.seq[self.i]
            self.i += 1
            return nucleotide
        raise StopIteration

    def __len__(self):
        return len(self.seq)

    def __hash__(self):
        return hash(self.seq)

    def __eq__(self, other):
        return self.seq == other

    def gc_content(self):
        G_percent = self.seq.count('G')
        C_percent = self.seq.count('C')
        return (G_percent + C_percent) / len(self.seq)

# Класс ДНК
class DNA(Bio_seq):
    complement_dictionary = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
        'N': 'N',
        'a': 't',
        't': 'a',
        'g': 'c',
        'c': 'g',
        'n': 'n',
    }

    def __init__(self, seq):
        super().__init__(seq)
        set_ref = set(self.seq)
        set_inp = set(self.complement_dictionary.keys())
        if not set_ref <= set_inp:
            error_letters = set_ref - set_inp
            raise TypeError(f'Неверная запись ДНК, удалите символы: {error_letters}')

    # синтез РНК осуществляется в направлении 3'-5', т.е. по не кодирующей цепи ДНК.
    # Таким образом транскрибируемая РНК идентична кодирующей цепи, с заменой T на U
    def transcribe(self):
        return RNA(self.seq.replace("T", "U").replace("t", "u"))

    def reverse_complement(self):
        self.temp = self.seq.translate(str.maketrans(self.complement_dictionary))
        return self.temp[::-1]

# Класс РНК
class RNA(Bio_seq):
    complement_dictionary = {
        'A': 'U',
        'U': 'A',
        'G': 'C',
        'C': 'G',
        'N': 'N',
        'a': 'u',
        'u': 'a',
        'g': 'c',
        'c': 'g',
        'n': 'n',
    }

    def __init__(self, seq):
        super().__init__(seq)
        set_ref = set(self.seq)
        set_inp = set(self.complement_dictionary.keys())
        if not set_ref <= set_inp:
            error_letters = set_ref - set_inp
            raise TypeError(f'Неверная запись ДНК, удалите символы: {error_letters}')

    def reverse_complement(self):
        self.temp = self.seq.translate(str.maketrans(self.complement_dictionary))
        return self.temp[::-1]

# пример работы
monkey = DNA('ATGCCTGctgtcGaatgCNNnn')
crocodile = RNA('AUGCgaucgGGAUcCCCaaaGCUAa')
result = monkey.transcribe()

print(monkey.gc_content())
print(monkey == crocodile)
print(result.reverse_complement())
test = list(result)[0:4]
for i in test:
    print(i)
print(next(monkey), '1')
print(next(monkey), '2')
print(next(monkey), '3')

Tolstoy = DNA('Величайшие истины — самые простые.')
