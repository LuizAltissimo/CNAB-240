import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pysftp

#função para envio de email sem anexo quando não existem lançamentos no dia
def email_sem_anexo():

    # Configurações para enviar e-mail por SMTP e destinatários
    servidor_SMTP = ''
    porta_SMTP =  
    remetente = ''
    senha_remetente = ''
    destinatario = [' ']

    # Configuração da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = ', '.join(destinatario)
    msg['Subject'] = 'CNAB 240 '

    corpo_email = ''' '''

    msg.attach(MIMEText(corpo_email, 'plain'))

    # Conecta-se ao servidor SMTP e envia o e-mail vazio
    with smtplib.SMTP(servidor_SMTP, porta_SMTP) as envio_email:
        envio_email.starttls()
        envio_email.login(remetente, senha_remetente)
        envio_email.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso.")

#função para envio de email com o arquivo CNAB 240 em anexo
def email_com_anexo():
    caminho_arquivo = 'CNAB_240.txt'

    # Configurações para enviar e-mail por SMTP e destinatários
    servidor_SMTP = ''
    porta_SMTP =  
    remetente = ''
    senha_remetente = ''
    destinatario = ['']

    # Configuração da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = ', '.join(destinatario)
    msg['Subject'] = 'CNAB 240 '

    corpo_email = "Segue em anexo o arquivo CNAB 240 com os lançamentos."
    msg.attach(MIMEText(corpo_email, 'plain'))

    # Adiciona o arquivo CNAB 240 como anexo
    with open(caminho_arquivo, 'rb') as anexo:
        part = MIMEApplication(anexo.read(), Name='CNAB_240.txt')
        part['Content-Disposition'] = f'anexo; filename={caminho_arquivo}'
        msg.attach(part)

    # Conecta-se ao servidor SMTP e envia o e-mail com anexo
    with smtplib.SMTP(servidor_SMTP, porta_SMTP) as envio_email:
        envio_email.starttls()
        envio_email.login(remetente, senha_remetente)
        envio_email.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso.")

def realizar_upload_sftp():
    # Substitua essas informações com os detalhes do seu servidor SFTP
    hostname = 'seu_servidor.com'
    port = 22
    username = 'seu_usuario'
    password = 'sua_senha'
    diretorio_remoto = '/caminho/para/o/diretorio/remoto/'

    # Cria uma conexão SFTP
    with pysftp.Connection(host=hostname, port=port, username=username, password=password) as sftp:
        # Realiza o upload do arquivo
        sftp.put(caminho_arquivo_local, remotepath=diretorio_remoto + 'nome_do_arquivo_no_servidor.txt')

# Chamando a função para realizar o upload
realizar_upload_sftp()