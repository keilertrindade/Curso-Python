from POO.classes.classes_associacao import Escritor
from POO.classes.classes_associacao import Caneta
from POO.classes.classes_associacao import MaquinaDeEscrever



escritor = Escritor('Joãzinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(caneta.marca)


escritor.ferramenta = caneta #associação entre os objetos
escritor.ferramenta.escrever()
