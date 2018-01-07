from django import template

# Importa para adicionar a library do Django
register = template.Library()

def cut(value,arg):
    """
        Isso corta todos os valores de arg do value
    """
    return value.replace(arg,'')

# Registra a funcao com um nome(string)
register.filter('cut',cut)


# Outra forma de criar filtros
@register.filter(name='new')
def new(value,arg):
    '''
    Função criada para substituir por outra coisa
    '''
    return value.replace(arg,'DIOGO')
