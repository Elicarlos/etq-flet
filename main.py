import flet
from flet import *
from controllers import add_corte_carne, add_tipo_carne, list_corte_carne, list_tipo_carne,list_empresa
from header import AppHeader
from forms import AppForm
from data_table import AppDataTable

def main(page: Page):
    page.title = "Etiquetario"
    page.bgcolor = "#fdfdfd"
    page.padding = 20
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # def salvar_produto(e):
    #     carbo = carboidrato.value
    #     add_tipo_carne(carbo)
    #     page.update()
    
    # h1 = Text('Cadastro de Produtos')
    # carboidrato = TextField(label="Carboidrato")
    # btn_save = ElevatedButton(text="Salvar produto", on_click=salvar_produto)
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppForm(),
                Column(
                    scroll='hidden',
                    expand=True,
                    controls=[
                        AppDataTable()
                    ],
                ),

            ]
        )
    )
if __name__ == '__main__':
    list_tipo_carne()
    list_corte_carne()
    list_empresa()
 
    app(target=main)
