from datetime import date

class Hospede:
  def __init__(self, nome, cpf, telefone):
    self.nome = nome
    self.cpf = cpf
    self.telefone = telefone

  def Atualizar_telefone(self):
    novotelefone = int(input(f"Atualize seu telefone {self.nome}: "))
    if len(str(novotelefone)) == 9:
      self.telefone = novotelefone
    else:
      print("Insira um número de telefone válido.\n")
    print("!------------------!\n")

  def __str__(self):
    return f'Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}\n'
    
class Quarto:
  def __init__(self, numero, tipo):
    self.numero = numero
    self.tipo = tipo
    self.ocupacao = False #esse valor sempre terá que ser falso do início.

  def ocupar_quarto(self):
    self.ocupacao = True

  def __str__(self):
    return f"Quarto {self.numero}\nTipo: {self.tipo}\n{'Ocupado' if self.ocupacao else 'Desocupado'}"

class Reserva:
  def __init__(self, hospede, quarto, dataEntrada, dataSaida):
    self.hospede = hospede
    self.quarto = quarto
    self.dataEntrada = dataEntrada
    self.dataSaida = dataSaida
    self.valor = self.calcular_valor()
    
  def calcular_valor(self):
    dias = (self.dataSaida - self.dataEntrada).days + 1
    if self.quarto.tipo == "solteiro":
      valor_diaria = 60.0
    elif self.quarto.tipo == "casal":
      valor_diaria = 125.0
    elif self.quarto.tipo == "família":
      valor_diaria = 170.0
    else:
      raise ValueError("Não há outro tipo de quarto.")
    return dias * valor_diaria

  def __str__(self):
    return f'Reserva para {self.hospede}\nQuarto:\n{self.quarto}\nData de entrada: {self.dataEntrada}\nData de saída: {self.dataSaida}\nValor: R${self.valor:.2f}\n'

class Hotel:
  def __init__(self, nomeHotel):
    self.nomeHotel = nomeHotel
    self.quartos = []
    self.reservas = []

  def adicionar_quartos(self, numero, tipo):
    quarto = Quarto(numero, tipo)
    self.quartos.append(quarto)

  def listar_quartos_vazios(self):
    quartos_vazios = [quarto for quarto in self.quartos if not quarto.ocupacao]
    return quartos_vazios
  
  def adicionar_reserva(self, hospede, numero, dataEntrada, dataSaida):
    quarto = None
    for quarto_pedido in self.quartos:
      if quarto_pedido.numero == numero and not quarto_pedido.ocupacao:
        quarto = quarto_pedido
        break

    if quarto is None:
      return "O quarto não está disponível no momento. :/"
      
    reserva = Reserva(hospede, quarto, dataEntrada, dataSaida)
    quarto.ocupar_quarto()
    self.reservas.append(reserva)
    return "Sua reserva foi confirmada senhor. :)"

  def listar_reservas(self):
    return self.reservas

#Executar:

#hotel:
hotel = Hotel("Hotel 100-Almoço")

#hospedes:
hospede1 = Hospede("Antonio", "10315678901", "987654321")
hospede1.Atualizar_telefone()
hospede2 = Hospede("Adryelly","98765432109", "111111111")
hospede3 = Hospede("Maria", "44567245678", "884624466")
hospede4 = Hospede("Benhur", "12345064128", "333333333")
hospede5 = Hospede("Rafael", "13340121568", "340524923")

#Quartos:
hotel.adicionar_quartos(1, "casal")
hotel.adicionar_quartos(13, "casal")
hotel.adicionar_quartos(24, "solteiro")
hotel.adicionar_quartos(217, "família")
hotel.adicionar_quartos(249, "família")
hotel.adicionar_quartos(331, "casal")
hotel.adicionar_quartos(666, "solteiro")
hotel.adicionar_quartos(765, "família")
hotel.adicionar_quartos(821, "solteiro")


#Quartos vazios:
quartos_vazios = hotel.listar_quartos_vazios()
print("QUARTOS VAZIOS: ")
for quarto in quartos_vazios:
  print(f"{quarto}\n")
print("!------------------!\n")

#Reservas:
reserva1 = hotel.adicionar_reserva(hospede1, 13, date(2022, 4, 12), date(2023, 5, 15))
print(f"{reserva1}\n")

reserva2 = hotel.adicionar_reserva(hospede2, 666, date(2022, 4, 12), date(2023, 5, 20))
print(f"{reserva2}\n")

reserva3 = hotel.adicionar_reserva(hospede3, 13, date(2023, 4, 12), date(2023, 4, 13))
print(f"{reserva3}\n")

reserva4 = hotel.adicionar_reserva(hospede4, 821, date(2023, 4, 12), date(2023, 4, 15))
print(f"{reserva4}\n")

reserva5 = hotel.adicionar_reserva(hospede5, 1, date(1, 1, 1), date(2023, 4, 20))
print(f"{reserva5}\n")

print("!------------------!\n")

#lista de reservas:
print("RESERVAS REALIZADAS:")
reservas = hotel.listar_reservas()
for reserva in reservas:
  print(reserva)
print("!------------------!\n")

#Quartos vazios 2:
quartos_vazios = hotel.listar_quartos_vazios()
print("QUARTOS VAZIOS: ")
for quarto in quartos_vazios:
  print(f"{quarto}\n")
print("!------------------!\n")