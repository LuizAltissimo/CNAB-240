import collections
import query

#função para juntar os campos do dicionario numa string e completar de espaços vazios ou zeros conforme a necessidade
def segmento_e(row):

    merged_str = default_segmento_e(row)
    header_str = '{:0>3.3}{:0>4.4}{:0>1.1}{:0>5.5}{:<1.1}{:<3.3}{:0>1.1}{:0>14.14}{:<20.20}{:0>5.5}{:<1.1}{:0>12.12}{:<1.1}{:<1.1}{:<30.30}{:<6.6}{:<3.3}{:0>2.2}{:<20.20}{:<1.1}{:0>8.8}{:0>8.8}{:0>18.18}{:<1.1}{:0>3.3}{:<4.4}{:<25.25}{:<39.39}'
    
    return header_str.format(*merged_str.values())

#definição do dicionario para juntar na string
def default_segmento_e(row):

    campo = collections.OrderedDict()

    campo['controle_banco'] = '' #G001
    campo['controle_lote'] = '' #G002
    campo['controle_registro'] = '' #G003
    campo['serviço_nr_registro'] = '' #G038
    campo['serviço_segmento'] = '' #G039
    campo['cnab_29'] = ' ' #G004
    campo['empresa_inscrição_tipo_inscrição'] = '' #G005
    campo['empresa_inscrição_nr_inscrição'] = '' #G006
    campo['empresa_convenio'] = ' ' #G007
    campo['empresa_conta_codigo_agencia'] = '' #G008
    campo['empresa_conta_codigo_agencia_dv'] = '' #G009
    campo['empresa_conta_numero_conta_corrente'] = '' #G010
    campo['empresa_conta_numero_conta_corrente_dv'] = '' #G011
    campo['empresa_conta_dv'] = '' #G012
    campo['empresa_nome'] = '' #G013
    campo['cnab_27'] = ' ' #G004 
    campo['natureza_lancamento'] = '' #G084
    campo['tipo_complemento'] = '' #G085
    campo['complemento'] = ' ' #G086
    campo['cpmf'] = '' #G087
    campo['data_contabil'] = '' #G088
    campo['lançamento_data_lancamento'] = '' #G089
    campo['lançamento_valor_lancamento'] = '' #G090
    campo['lancamento_tipo_lancamento'] = '' #G091
    campo['lancamento_categoria_lancamento'] = '' #G092
    campo['lancamento_cd_hist'] = '' #G093
    campo['lancamento_historico'] = '' #G094
    campo['lancamento_nr_documento'] = '' #G095

    return campo

#cria um campo vazio para ser preenchido com os lançamentos do dia em uma linha para cada lançamento
strings_segmento_e = []

for index, row in query.df.iterrows():
    string_segmento_e = segmento_e(row)
    strings_segmento_e.append(string_segmento_e)