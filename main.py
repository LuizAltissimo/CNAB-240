import header_arquivo
import header_lote
import segmento_e
import trailer_lote
import trailer_arquivo
import query
import func

#checa se houve lançamentos no dia antes de gerar o arquivo e chama as funções para envio de email
if not query.df.empty:

    caminho_arquivo = "CNAB_240.txt"

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(header_arquivo.string_header_arquivo+'\n')
        arquivo.write(header_lote.string_header_lote+'\n')
        for string_segmento_e in segmento_e.strings_segmento_e:
            arquivo.write(string_segmento_e + '\n')
        arquivo.write(trailer_lote.string_trailer_lote+'\n')
        arquivo.write(trailer_arquivo.string_trailer_arquivo+'\n')
    func.email_com_anexo()
    print('CNAB 240 Gerado')

else:
    func.email_sem_anexo()
    print("DataFrame inicial está vazio. Nenhum arquivo gerado.")
