from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

email = 'e-mail de envio da mensagem'
senha = 'senha desse email'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Keiler Trindade', data=data)
# Podemos usar template.safe_substitute para quando não formos alterar todos os placeholders do html. Da forma que
# está agora ocorrerá uma exceção caso exista algum placeholder não "substituido"


msg = MIMEMultipart()
msg['from'] = 'Keiler Trindade'
msg['to'] = 'Destinatário'
msg['subject'] = 'Assunto'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='host smtp', port='porta em inteiro') as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha)
        smtp.send_message(msg)
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro: ', e)