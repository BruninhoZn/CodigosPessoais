# d1 = dict()
# d1['nova_chave'] = 'Valor da nova chave'
# print(d1['chave2'])

from sre_constants import OP_IGNORE


d1 = {
    'str' : 'valor',
    123: 'Outro Valor',
    (1,2,3,4) :  'Tupla',
    
}

# d1['nomedachave'] = 'Agora ela existe'

if (d1.get('nomedachave')) is not None:
    print(d1.get('nomedachave'))

print(123)
