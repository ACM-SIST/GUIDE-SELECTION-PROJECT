import smtplib
import ssl
import pandas as pd

comp_file = pd.read_csv("user.csv")

toemail = comp_file['email'].values
print(toemail)

mail_subject = "CERTIFICATE GENERATE"
sender_email = "meantechofficial2906@gmail.com"
sender_name = "GDSC-SIST"
password = "ofewnyrqtqypfkaj"
# template_file = "templates/template_1_certificate.html"
# csv_file = "details.csv"
