import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
load_dotenv()


class MailSender:
  def __init__(self, recipient_emails, subject, template_name, sender_email=os.environ.get('SENDER_EMAIL'), sender_password=os.environ.get("SENDER_PASSWORD")):
    self.recipient_emails = recipient_emails
    self.subject = subject
    self.sender_email = sender_email
    self.sender_password = sender_password
    self.template_env = Environment(
        loader=FileSystemLoader(searchpath="emails"))
    self.template = self.template_env.get_template(template_name)

  def send_email(self, certificate_path, name="Hello!", index=None):
    try:
      smtp_server = 'smtp.gmail.com'
      smtp_port = 587
      server = smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()
      server.login(self.sender_email, self.sender_password)
      email = MIMEMultipart()
      email['From'] = self.sender_email
      email['To'] = ', '.join(self.recipient_emails)
      email['Subject'] = self.subject
      rendered_html = self.template.render({
          "name": name
      })
      email.attach(MIMEText(rendered_html, 'html'))
      with open(certificate_path, 'rb') as f:
        pdf_attachment = MIMEApplication(f.read(), 'pdf')
      pdf_attachment.add_header(
          'Content-Disposition', 'attachment', filename=os.path.basename(certificate_path))
      email.attach(pdf_attachment)
      server.send_message(email)
      if index != None:
        print(f"Success for: {name}")

      server.quit()
      return 1
    except smtplib.SMTPException as e:
      print(
          f"Error occurred for {name} while sending email: {str(e)}")
      return 0
