class Preco:
    preco_produto = []
    def __init__(self, imposto, frete, desconto, oferta = False, promocao = False):
        self.imposto = imposto
        self.frete = frete
        self.desconto = desconto
        self.oferta = oferta
        self.promocao =promocao
 
preco_produto = Preco(imposto = 0.1, frete = 4.0, desconto = 0.6, oferta = 1.0, promocao = 6.7)
 
print(f'Imposto: {preco_produto.imposto}')  
print(f'Frete: {preco_produto.frete}')  
print(f'Desconto: {preco_produto.desconto}')
print(f'Promoção: {preco_produto.promocao}')
 
class Idioma:
    def __init__(self, name, origem, bandera):
        self._name = name
        self._origem = origem
        self._bandera = bandera
    def __str__(self):
        return f'{self._name} | {self._bandera} | {self._origem}'
   
 
idioma_espanhol = Idioma('espanhol', '🇪🇸', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
idioma_portugues = Idioma('Portugues', '🇧🇷', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')


idioma_ingles = Idioma('ingles', '🇺🇸', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
idioma_frances = Idioma('frances', '🇫🇷', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
idioma_aleman = Idioma('aleman', '🇩🇪', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
 
idiomas =[idioma_espanhol, idioma_portugues, idioma_ingles, idioma_frances, idioma_aleman]
 
print(idioma_espanhol)
print(idioma_portugues)
print(idioma_ingles)
print(idioma_frances)
print(idioma_aleman)
 
 
class Produto:
       
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
       
   
    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
     
 
 
if __name__ == "__main__":
 
    produto1 = Produto(1, "Camiseta", 29.99)
    produto2 = Produto(2, "Calça Jeans", 79.90)
    produto3 = Produto(3, "Sofá", 350.00)
    produto4 = Produto(4,"Guarda roupa",546.97)
    produto5 =Produto(5, "Caminha de Pelucia para Gatos", 63.15)
    produto6 = Produto(6, "Casinha pra pet Raças Medias e Grandes", 209.50)
   
   
    produto1.exibir_informacoes()
    print("-------------------------")
    produto2.exibir_informacoes()
    print("-------------------------")
    produto3.exibir_informacoes()
    print("-------------------------")
    produto4.exibir_informacoes()
    print("-------------------------")
    produto5.exibir_informacoes()
    print("-------------------------")
    produto6.exibir_informacoes()
    print("-------------------------")
   
   
   
class EnvioInternacional:
    def __init__(self, origem, destino, peso, tipo):
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.tipo = tipo
 
    def calcular_custo(self):
       
        if self.tipo == 'expresso':
            custo_por_kg = 5.0
        else:
            custo_por_kg = 2.5
       
        custo_total = self.peso * custo_por_kg
        return custo_total
 
    def enviar(self):
       
        print(f"Enviando pacote de {self.origem} para {self.destino}")
 
paises_disponiveis = ['Estados Unidos', 'Canadá', 'Reino Unido', 'Alemanha', 'Austrália']
 
print("Países disponíveis para envio internacional:")
for index, pais in enumerate(paises_disponiveis, start=1):
    print(f"{index}. {pais}")
 
while True:
    try:
        escolha = int(input("Digite o número correspondente ao país de destino: "))
        if 1 <= escolha <= len(paises_disponiveis):
            destino = paises_disponiveis[escolha - 1]
            break
        else:
            print("Escolha inválida. Digite um número válido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
 
 
envio1 = EnvioInternacional('Brasil', destino, 2.5, 'expresso')
print(f"Custo do envio: ${envio1.calcular_custo()}")
envio1.enviar()
 
class Vendas:
    def __init__(self, pix, boleto, cartao):
        self.pix = pix
        self.boleto = boleto
        self.cartao = cartao
   
    def exibir_informacoes(self):
        print(f"Pix: {self.pix}, boleto: {self.boleto}, cartão: {self.cartao}")
 
 
class Cliente:
    clientes = []
    def __init__ (self, nome, endereco, email, telefone):
        self._nome = nome
        self._endereco = endereco
        self._email = email
        self._telefone = telefone
        Cliente.clientes.append(self)
def __str__(self):
        return f'{self._nome} | {self._endereco} | {self._email} | {self._telefone}'
def listado_clientes():
    for clientes in Cliente.clientes:
        print (f'{clientes._nome.ljust(20)} | {clientes._endereco.ljust(20)} | {clientes._email.ljust(20)} | {clientes._telefone.ljust(20)}')
 
pedro = Cliente('pedro', 'bernardino olivera 194 salta-argentina', 'pedro1254@gmail.com', '+5493875113611')    
laura = Cliente('laura', 'coronel carneiro junior 134 itajuba-brasil', 'lau25@gmail.com', '+553524687555')
juan = Cliente('juan', 'plaza de armas 24 cusco-peru', 'jn457@gmail.com', '+5146877711')
 
print(pedro)
print(laura)
print(juan)
 
class Vendedor:
    def __init__(self, nome, mercadoria, CNPJ):
        self.nome = nome
        self.mercadoria = mercadoria
        self.cnpj = CNPJ
   
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Mercadoria: {self.mercadoria}, CNPJ: {self.cnpj}")
 
def cadastrar_vendedor():
    nome = input("Digite o nome do vendedor: ")
    mercadoria = input("Digite a mercadoria do vendedor: ")
    CNPJ = input("Digite o CNPJ do vendedor: ")
    return Vendedor(nome, mercadoria, CNPJ)
 
def main():
    lista_vendedores = []
 
    while True:
        print("\n1 - Cadastrar vendedor")
        print("2 - Exibir todos os vendedores")
        print("3 - Sair")
 
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            vendedor = cadastrar_vendedor()
            lista_vendedores.append(vendedor)
            print("Vendedor cadastrado com sucesso!")
        elif opcao == "2":
            if not lista_vendedores:
                print("Nenhum vendedor cadastrado.")
            else:
                print("\n=== Vendedores Cadastrados ===")
                for vendedor in lista_vendedores:
                    vendedor.exibir_informacoes()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
 
if __name__ == "__main__":
    main()
 
 
def verificar_senha():
    senha_correta = "123"  # Defina aqui a senha correta
   
    senha_digitada = input("Digite a senha: ")
 
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso concedido. ✔️ ")
    else:
        print("Senha incorreta! Acesso negado.  ❌ ")
 
# Chamada da função para verificar a senha
verificar_senha()
 
class Reclamacao:
    def __init__(self, cliente, descricao, resolvida=False):
        self.cliente = cliente
        self.descricao = descricao
        self.resolvida = resolvida
   
    def exibir_informacoes(self):
        print(f"Cliente: {self.cliente}")
        print(f"Descrição: {self.descricao}")
        status = "Resolvida" if self.resolvida else "Pendente"
        print(f"Status: {status}")
 
    def resolver_reclamacao(self):
        self.resolvida = True
        print(f"A reclamação de {self.cliente} foi marcada como resolvida.")
 
 
if __name__ == "__main__":
   
    reclamacao1 = Reclamacao("Maria", "Produto não entregue.")
 
   
    reclamacao1.exibir_informacoes()
 
   
    if not reclamacao1.resolvida:
        print("Reclamação ainda não resolvida. Por favor, retorne mais tarde.")
 
   
    reclamacao1.resolver_reclamacao()
 
    reclamacao1.exibir_informacoes()
 
 
 