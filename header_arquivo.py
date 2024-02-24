import collections
from datetime import datetime 

#função para juntar os campos do dicionario numa string e completar de espaços vazios ou zeros conforme a necessidade
def header_arquivo(header_arquivo):

    merged_str = default_header_arquivo()
    header_str = '{:0>3.3}{:0>4.4}{:<1.1}{:<9.9}{:<1.1}{:0>14.14}{:<20.20}{:0>5.5}{:0<1.1}{:0>12.12}{:<1.1}{:<1.1}{:<30.30}{:<30.30}{:<10.10}{:0>1.1}{:0>8.8}{:0>6.6}{:0>6.6}{:0>3.3}{:0>5.5}{:<20.20}{:<20.20}{:<29.29}'
    
    return header_str.format(*merged_str.values())

#definição do dicionario para juntar na string
def default_header_arquivo():
    
    campo = collections.OrderedDict()
    data_hora = datetime.now()

    campo['banco'] = '' #G001
    campo['lote'] = '' #G002
    campo['registro'] = '' #G003
    campo['cnab_04'] = ' ' #G004
    campo['empresa_inscricao_tipo'] ='' #G005 (1 Pessoa Fisica, 2 Pessoa Juridica)
    campo['empresa_inscricao_numero'] ='' #G006
    campo['empresa_convenio'] = '' #G007
    campo['empresa_conta_corrente_agencia'] = '' #G008
    campo['empresa_conta_corrente_agencia_dv'] ='' #G009
    campo['empresa_conta_corrente_conta_numero'] = '' #G010
    campo['empresa_conta_corrente_conta_dv'] ='' #G011
    campo['empresa_conta_corrente_digito_verificador'] = '' #G012
    campo['empresa_nome'] =' ' #G013
    campo['nome_banco'] =' ' #G014
    campo['cnab_15'] = ' ' #G004
    campo['arquivo_codigo'] =''  #G015 (código de remessa 1 (cliente banco), retorno 2 (banco cliente))
    campo['arquivo_data_geracao'] = data_hora.strftime("%d%m%Y") #G016
    campo['arquivo_hora_geracao'] = data_hora.strftime("%H%M%f") #G017
    campo['arquivo_nsa'] ='' #G018
    campo['arquivo_layout'] ='' #G019
    campo['arquivo_densidade'] =''  #G020
    campo['reservado_banco'] =' ' #G021
    campo['reservado_empresa'] = ' ' #G022
    campo['cnab_24'] = ' '#G004

    return campo

string_header_arquivo = header_arquivo(default_header_arquivo)