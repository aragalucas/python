import os
from dataclasses import dataclass

os.system("cls || clear")
    
QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade: float

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("digite seu nome: "),
        idade = int(input("digite sua idade: "))
    )
    alunos.append(aluno)
arquivo = "alunos.txt"

with open(arquivo, 'a') as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno.nome},{aluno.idade}\n")
print(f"dados gavados com sucesso")