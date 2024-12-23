import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    from_address = 'venxer12345@gmail.com'
    password = 'ubas dkhn ozjl rxmm'

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
         server.login(from_address, password)
         server.sendmail(from_address, to_address, msg.as_string())

# Example usage
send_email('masophiatabliago@gmail.com', 'Delivery', 'Your package arrived today.')
