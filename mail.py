import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class MailSender:
    def __init__(self, recipient_emails, subject, sender_email='example@gmail.com', sender_password='password'):
        self.recipient_emails = recipient_emails
        self.subject = subject
        self.sender_email = sender_email
        self.sender_password = sender_password

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
            html_message = f'''
							<html>
								<body>
                                    <p>Hey {name},</p>
                                    <p>Thank you for attending GDSC WoW Nagpur 2023 and for your contribution in making the event a grand success!!</p>
                                    <p>PFA your participation certificate!</p>
                                    <p>Share your certificate on linkedin and twitter!</p>
                                    <p>Use #gdsc_nagpur & don't forget to tag us. :)</p>
                                    <p>Stay connected with us for more upcoming event:</p>
                                    <p>- <a href="instagram.com/gdsc_nagpur">instagram.com/gdsc_nagpur</a></p>
                                    <p>- <a href="linktr.ee/gdsc_nagpur">linktr.ee/gdsc_nagpur</a></p>
                                    <br><br><br><br>
                                    <p>Regards,</p>
                                    <p><> Google Developer Student Clubs - Nagpur</p>
								</body>
							</html>
						'''
            email.attach(MIMEText(html_message, 'html'))
            with open(certificate_path, 'rb') as f:
                pdf_attachment = MIMEApplication(f.read(), 'pdf')
            pdf_attachment.add_header(
                'Content-Disposition', 'attachment', filename=os.path.basename(certificate_path))
            email.attach(pdf_attachment)
            server.send_message(email)
            if index != None:
                print("Success for index: ", index)
            server.quit()
        except smtplib.SMTPException as e:
            print(
                f"Error occurred on index {index} while sending email: {str(e)}")


if __name__ == "__main__":
    sender_email = 'example@gmail.com'
    sender_password = 'password'
    recipient_emails = [
        "example1@gmail.com",
        "example2@gmail.com"
    ]
    subject = 'GDSC Wow Certification - GDSC RCOEM'
    certificate_path = './output.pdf'
    mail = MailSender(recipient_emails, subject)
    mail.send_email(certificate_path, "Adnan Shabbir Husain")
