import pandas as pd
import json
import threading
from src.mail import MailSender
from src.pdf import save_image_as_pdf
from src.certificate import add_text_to_image
import time

template = "email1.html"
x = 1050
y = 840
time_duration = 1


def send_mail(name, email, index, failed_mails):
  recipient_emails = [email]
  subject = 'Google Cloud Certification'
  certificate_path = f'pdfs/{name}.pdf'
  mail = MailSender(recipient_emails, subject, template)
  n = mail.send_email(certificate_path, name, index)
  if n == 0:
    failed_mails.append({
        "index": index,
        "name": name
    })


if __name__ == "__main__":
  # excel_file_path = "./CertificatesList.xlsx"
  # df = pd.read_excel(excel_file_path, "Sheet2")
  # df = df.dropna()

  threads = []
  failedMails = []

  l = [
      {
          "name": "Adnan Shabbir Husain",
          "email": "generaladnan139@gmail.com"
      }
  ]

#   l = [{
#       "name": "Poushik Yelne",
#       "email": "yelneps@rknec.edu",
#   }, {
#       "name": "Abhinav Tilwar",
#       "email": "tilwarap@rknec.edu",
#   }, {
#       "name": "Vaibhav Pimpalkar",
#       "email": "pimpalkarvs@rknec.edu",
#   }, {
#       "name": "Ashutosh Phadke",
#       "email": "phadkeav@rknec.edu",
#   }, {
#       "name": "Prathamesh Kurve",
#       "email": "kurveps@rknec.edu",
#   }, {
#       "name": "Aditya Bhattad",
#       "email": "bhattadam@rknec.edu",
#   }, {
#       "name": "Adnan Shabbir Husain",
#       "email": "husainas_1@rknec.edu",
#   }]

  for item in l:
    name = item["name"]
    email = item["email"]
    add_text_to_image(name, "certificates/cloud jam 2023.png", x=x, y=y)
    save_image_as_pdf(output_path=f"pdfs/{name}.pdf")
    email_thread = threading.Thread(
        target=send_mail, args=(name, email, 1, failedMails))
    email_thread.start()
    threads.append(email_thread)
    time.sleep(time_duration)

  for thread in threads:
    thread.join()

  print(failedMails)
  with open('failedMails.json', 'w') as file:
    file.write(json.dumps(failedMails))
