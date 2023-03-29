import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define email sender and credentials
sender_email = 'sakthikarthi86@hotmail.com'  # use microsoft's hotmail account
sender_password = 'password@862112'  # mail id password

# Define email content
subject = input()
body = input()

# Define CSV file path and read recipient information
csv_file = 'email-list.csv'
with open(csv_file, 'r') as file:
  reader = csv.reader(file)
  next(reader)  # skip header row
  recipients = [row for row in reader]

# Connect to Hotmail SMTP server
smtp_server = 'smtp.office365.com'  # smtp server for hotmail
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Loop through recipients and send emails
for recipient in recipients:
  recipient_name = recipient[0]
  recipient_email = recipient[1]

  # Create email message
  message = MIMEMultipart()
  message['From'] = sender_email
  message['To'] = recipient_email
  message['Subject'] = subject

  # Add email body
  message.attach(MIMEText(body, 'plain'))

  # Send email
  server.sendmail(sender_email, recipient_email, message.as_string())

# Close connection to SMTP server
server.quit()

print('Emails sent successfully.')
