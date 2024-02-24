import collections
import query

#função para juntar os campos do dicionario numa string e completar de espaços vazios ou zeros conforme a necessidade
def header_lote(header_lote):

    merged_str = default_header_lote()
    header_str = '{:0>3.3}{:0>4.4}{:0>1.1}{:<1.1}{:0>2.2}{:0>2.2}{:0>3.3}{:<1.1}{:0>1.1}{:0>14.14}{:<20.20}{:0>5.5}{:<1.1}{:0>12.12}{:<1.1}{:<1.1}{:<30.30}{:<40.40}{:0>8.8}{:0>18.18}{:<1.1}{:<1.1}{:<3.3}{:0>5.5}{:<62.62}'
    
    return header_str.format(*merged_str.values())

#definição do dicionario para juntar na string
def default_header_lote():
    
    campo = collections.OrderedDict()

    campo['banco'] = '' #G001
    campo['lote'] = '' #G002
    campo['registro'] = '' #G003
    campo['operacao'] = '' #G028
    campo['servico'] = '' #G025
    campo['forma_lancamento'] = '' #G029 
    campo['versao_layout_lote'] = '' #G030
    campo['cnab_081'] = ' ' #G004
    campo['empresa_inscricao_tipo'] ='' #G005 - 1 Pessoa Fisica, 2 Pessoa Juridica
    campo['empresa_inscricao_numero'] ='' #G006
    campo['empresa_convenio'] =' ' #G007
    campo['empresa_conta_corrente_agencia'] ='' #G008
    campo['empresa_conta_corrente_agencia_dv'] ='' #G009
    campo['empresa_conta_corrente_conta_numero'] ='' #G010
    campo['empresa_conta_corrente_conta_dv'] ='' #G011
    campo['empresa_conta_corrente_digito_verificador'] ='' #tipo de registro #G012 
    campo['empresa_nome'] =' ' #G013
    campo['cnab_082'] =' ' #G004
    campo['saldo_inicial_Data'] = '' #G080
    campo['saldo_inicial_valor'] = '' #E002
    campo['saldo_inicial_situação'] = '' #G081    
    campo['saldo_inicial_status'] ='' #G082
    campo['saldo_inicial_tipo_moeda'] ='' #G040
    campo['saldo_inicial_sequencia_extrato'] =''  #G0083
    campo['cnab_083'] =' ' #G004

    return campo

string_header_lote = header_lote(default_header_lote())
