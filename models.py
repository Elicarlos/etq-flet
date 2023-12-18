from peewee import *
db = SqliteDatabase('nutricional')
class Base(Model):
    class Meta:
        database = db

class Empresa(Base):
    cnpj = CharField(max_length=100)
    razao_social = CharField(max_length=100)
    fantasia = CharField(max_length=100)
    numero_registro = CharField(max_length=50)
    registro_adapi = IntegerField()


class TipoCarne(Base):
    descricao = CharField(max_length='100', unique=True)

class CorteCarne(Base):
    tipo_carne = ForeignKeyField(TipoCarne, backref='cortes')
    descricao = CharField(max_length=100, unique=True)
    sexo = CharField(max_length=1)
    temperatura = CharField(max_length=50)  # Campo para TEMPERATURA (pode ajustar conforme necessário)
    data_embalagem = DateField()  # Campo para DATA DA EMBALAGEM
    validade = DateField()  # Campo para VALIDADE
    lote = CharField(max_length=50)  # Campo para LOTE
    cod_barras = CharField(max_length=50)  # Campo para COD DE BARRAS
    codigo_barras = IntegerField()
    dados_nutricionais = CharField(max_length=1000)
    # valor_energetico = CharField(max_length=100)    
    # carboidratos_totais = CharField(max_length=100)
    # acucares_totais = CharField(max_length=100)
    # acucares_adicionados = CharField(max_length=100)
    # proteinas = CharField(max_length=100)
    # gorduras_totais = CharField(max_length=100)
    # gorduras_saturadas = CharField(max_length=100)
    # gorduras_trans = CharField(max_length=100)
    # fibra_alimentar = CharField(max_length=100)
    # sodio = CharField(max_length=100)    
db.connect()
db.create_tables([TipoCarne, CorteCarne])