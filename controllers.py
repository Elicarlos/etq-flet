from models import TipoCarne, CorteCarne

def list_empresa():
    pass

def add_tipo_carne(carboidrato):
    TipoCarne.create(carboidrato=carboidrato)
    print('Salvo com sucesso')


def list_tipo_carne():
    tipo_carne = TipoCarne.select()
    for tipo in tipo_carne:        
        print("Produtos cadastrados no banco", tipo.descricao)

def update_tipo_carne():
    pass


def delete_tipo_carne():
    pass


def add_corte_carne(carboidrato):
    CorteCarne.create(carboidrato=carboidrato)
    print('Salvo com sucesso')


def list_corte_carne():
    corte = CorteCarne.select()
    for corte in CorteCarne:        
        print("Produtos cadastrados no banco", corte.descricao)

def update_tipo_carne():
    pass

def delete_corte_carne():
    pass