from flet import *
from controls import add_control_reference

class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    
    def app_data_table_instance(self):
        add_control_reference("AppDataTable", self)

    def build(self):
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(1,"ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text(
                                "Corte", size=12, color="black",
                                weight="bold",
                            ),                           
                        ),

                        DataColumn(
                            Text(
                                "Coluna 1", size=12, color="black",
                                weight="bold",
                            ),                           
                        ),

                        DataColumn(
                            Text(
                                "Coluna 1", size=12, color="black",
                                weight="bold",
                            ),                           
                        ),

                        DataColumn(
                            Text(
                                "Coluna 1", size=12, color="black",
                                weight="bold",
                            ),                           
                        ),
                    ],
                    rows=[]

                )
            ]

        )
