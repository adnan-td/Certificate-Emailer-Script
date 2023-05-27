import pandas as pd
import multiprocessing
from mail import MailSender
from pdf import save_image_as_pdf
from certificate import add_text_to_image
import time


def send_mail(name, email, index):
    recipient_emails = [email]
    subject = 'GDSC Wow Certification - GDSC RCOEM'
    certificate_path = f'pdfs/{name}.pdf'
    mail = MailSender(recipient_emails, subject)
    mail.send_email(certificate_path, name, index)


if __name__ == "__main__":
    # Link to your excelsheet
    excel_file_path = "./CertificatesList.xlsx"
    df = pd.read_excel(excel_file_path)

    for index, row in df.iterrows():
        name = row["Name"]
        email = row["Email address"]
        add_text_to_image(name)
        save_image_as_pdf(output_path=f"pdfs/{name}.pdf")
        email_process = multiprocessing.Process(
            target=send_mail, args=(name, email, index))
        email_process.start()
        time.sleep(0.5)
