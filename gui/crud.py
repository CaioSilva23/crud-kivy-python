from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

from entidades.cliente import Cliente
from repositorios.cliente_repositorio import ClienteRepositorio


class BotaoListagem(ToggleButton):
    def __int__(self, cliente_id, cliente_nome, cliente_idade, **kwargs):
        super(BotaoListagem, self).__init__(**kwargs)
        self.id_cliente = cliente_id
        self.nome_cliente = cliente_nome
        self.idade_cliente = cliente_idade
        self.text = self.nome_cliente + " " + self.idade_cliente
        self.group = 'clientes'


class Principal(BoxLayout):
    def cadastrar_cliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        cliente = Cliente(nome, idade)
        ClienteRepositorio.inserir_cliente(cliente)
        self.ids.nome.text = ''
        self.ids.idade.text = ''

    def listar_clientes(self):
        clientes = ClienteRepositorio.listar_cliente()
        for i in clientes:
            id = str(i[0])
            nome = i[1]
            idade = i[2]
            self.ids.cliente.add_widget(BotaoListagem(id, nome, idade))


class Crud(App):
    def build(self):
        return Principal()


Crud().run()
