from Bio.Seq import Seq
from Bio import SeqIO

inp = str(input("Введите путь до input fasta: "))
outp = str(input("Введите путь до output fasta: "))
print("Используется стандартная таблица кодонов")

def generate_protein(inp):
    for seq_record in SeqIO.parse(inp, "fasta"):
        seq_name = seq_record.id
        translated_seq = Seq(str(seq_record.seq)).translate()
        yield seq_name + '\n' + str(translated_seq)

gener = generate_protein(inp)

def letterFrequency(fileName, letter): 
    with open(fileName, 'r') as file:
        text = file.read() 
    return text.count(letter) 

N = letterFrequency(inp, '>')

for i in range(N):
    input('Нажмите enter чтобы транслировать последовательность')
    nex = next(gener)
    print(nex)
    with open(outp, 'a') as out_file:
        out_file.writelines(nex + "\n")
