import collections
import query

#função para juntar os campos do dicionario numa string e completar de espaços vazios ou zeros conforme a necessidade
def trailer_arquivo(trailer_arquivo):

    merged_str = default_trailer_arquivo()
    trailer_str = '{:0>3.3}{:0>4.4}{:0>1.1}{:<9.9}{:0>6.6}{:0>6.6}{:0>6.6}{:<205.205}'

    return trailer_str.format(*merged_str.values())

#definição do dicionario para juntar na string
def default_trailer_arquivo():
    
    campo = collections.OrderedDict()

    campo['banco'] = '' #G001
    campo['lote'] = '' #G002
    campo['registro'] = '' #G003
    campo['cnab_049'] = ' ' #G004 (nove espacos em branco)
    campo['quantidade_lotes']  = '' #G049
    campo['quantidade_registros']  = '' #G056
    campo['quantidade_contas_conciliacao']  = ' '  #G037 
    campo['cnab_089'] = ' '  #G004 (205 espacos em branco)

    return campo

string_trailer_arquivo = trailer_arquivo(default_trailer_arquivo)
