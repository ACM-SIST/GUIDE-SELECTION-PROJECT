import smtplib
import ssl
import pandas as pd

comp_file = pd.read_csv("Project Teams 2019 Batch.csv")

toemail = list(comp_file['user.csv'])
