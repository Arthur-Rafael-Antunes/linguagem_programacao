#exercicio de linguagem de classe - Arthur

class Aluno():
    def __init__ (self, matricula, nome, notaP1, notaP2, notaT):
        self.matricula = int(matricula)
        self.nome = nome
        self.notaP1 = float(notaP1)
        self.notaP2 = float(notaP2)
        self.notaT = float(notaT)
        
    def media(self):
        media = ((2.5 * self.notaP1) + (2.5 * self.notaP2) + (2*self.notaT) )/(2.5+2.5+2)
        return round(media,1)

    def final(self):
        media = self.media()
        if media >= 4.0 and media < 7.0:
            nota_final = (5.0 - 0.6 * media) / 0.4
            return round(nota_final,1)
        else:
            return 0

    def prova_final(self):
        media = self.media()
        if media < 4.0:
            return True
        elif media >= 4.0 and media < 5.0:
            nota_final = self.final()
            if nota_final > 2.5:
                return True
            else:
                return False
        else: 
            return False

nome = input("Escreva o nome do Aluno:" ) 
matricula = input("Escreva a matricula do Aluno:" ) 
Notap1= input("Escreva a primeira nota da prova:" ) 
Notap2= input("Escreva a segunda nota da prova:" ) 
NotaT= input("Escreva a nota do trabalho:" ) 

aluno = Aluno(matricula, nome, Notap1,Notap2, NotaT)
print('Média final:', aluno.media())
if aluno.prova_final():
    print('O aluno',nome, 'deve fazer a prova final.')
    print('Nota mínima necessária:', aluno.final())
else:
    print('O aluno',nome,'não precisa fazer a prova final.')
