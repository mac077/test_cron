import os
import smtplib
from email.message import EmailMessage

user_gmail = os.getenv(USER_GMAIL)
password_gmail = os.getenv(PASS_GMAIL)

def send_notifying_mail(mail_user: str = "", mail_password: str = "") -> None:
  msg = EmailMessage()

  # Contenido
  msg['From']="coletti.marcos@gmail.com"
  msg['To']="coletti.marcos@mail.com"
  msg['Subject']= "Probando mandar mails!"
  mail_body = 'Prueba de envio de mail'
  msg.set_content(mail_body)

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()

  # login
  server.login(user_gmail, password_gmail)

  # envio mail
  server.send_message(msg)
  server.quit();

send_notifying_mail(user_gmail, password_gmail)
