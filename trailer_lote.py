import collections
import query

#função para juntar os campos do dicionario numa string e completar de espaços vazios ou zeros conforme a necessidade
def trailer_lote(trailer_lote):

    merged_str = default_trailer_lote()
    trailer_str = '{:0>3.3}{:0>4.4}{:0>1.1}{:<9.9}{:0>1.1}{:0>14.14}{:<20.20}{:0>5.5}{:<1.1}{:0>12.12}{:<1.1}{:<1.1}{:<16.16}{:0>18.18}{:0>18.18}{:0>18.18}{:0>8.8}{:0>18.18}{:<1.1}{:<1.1}{:0>6.6}{:0>18.18}{:0>18.18}{:<28.28}'

    return trailer_str.format(*merged_str.values())

#definição do dicionario para juntar na string
def default_trailer_lote():
    
    campo = collections.OrderedDict()

    campo['controle_banco'] = '' #G001
    campo['controle_lote'] = '' #G002
    campo['controle_registro'] = '' #G003
    campo['cnab_0458'] = ''  #G004
    campo['empresa_inscrição_tipo'] = '' #G005
    campo['empresa_inscrição_numero'] = '' #G006
    campo['empresa_convenio'] = '' #G007
    campo['empresa_conta_agencia_codigo'] = '' #G008
    campo['empresa_conta_agencia_dv'] = '' #G009
    campo['empresa_conta_conta_numero'] = '' #G010
    campo['empresa_conta_conta_dv'] = '' #G011
    campo['empresa_conta_dv'] = '' #G012
    campo['cnab_046'] = ''  #G004
    campo['valores_bloqueado_24_mais'] = '' #E016
    campo['valores_limite'] = '' #G096
    campo['valores_bloqueado_24'] = '' #E018
    campo['saldo_final_data'] = '' #G097
    campo['saldo_final_valor'] = '' #E020
    campo['saldo_final_situação'] = '' #G098
    campo['saldo_final_status'] = '' #G099
    campo['totais_qt_registros']  = ''  #G057
    campo['totais_valor_deb']  = ''  #E023
    campo['totais_valor_cred']  = '' #E024
    campo['cnab_096']  = ' ' #G004

    return campo

string_trailer_lote = trailer_lote(default_trailer_lote())