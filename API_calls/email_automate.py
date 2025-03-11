import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, password):
    # Create message container
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the email body to the message
    message.attach(MIMEText(body, "plain"))

    try:
        # Set up the SMTP server and start TLS for security
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

if __name__ == "__main__":
    # Email account credentials and SMTP configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "youremail@gmail.com"         # Replace with your email address
    password = "yourpassword"                  # Enable two factor authentication and set app password for sender email - 16 didgit code-  https://support.google.com/mail/?p=BadCredentials
    receiver_email = "receiver@example.com"      # Replace with the recipient's email address

    # Email content
    subject = "Automated Email"
    body = "Hello, this is an automated email sent from a Python script!"

    send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, password)
