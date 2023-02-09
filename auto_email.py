import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

# TODO Add your email address
send_address = "tkoyama010@gmail.com"
# TODO Add your gmail password
password = "xxxxxxxxxxxxxxxx"

subject = "SciPy 2023 Call for Abstract Reviewers"
body_html = (
    "<p>Dear {},</p>"
    "<p>"
    'The <a href="https://www.scipy2023.scipy.org/">SciPy 2023</a> call for proposals is open and I am emailing on behalf of the Tutorial Committee to encourage you to sign up to review abstracts.'
    "Tutorials will be presented July 10-11 and the conference is in Austin, Texas."
    'You may find additional information <a href="https://www.scipy2023.scipy.org/present">here</a> and the deadline for volunteering to become a reviewer is February 22.</p>'
    "<p>Please respond to this email if you are interested in signing up to be a reviewer.</p>"
    "<p>Please feel free to email with any questions.</p>"
    "<p>Kind regards,<br>"
    "Logan Thomas<br>"
    "Sophia Yang<br>"
    "Tetsuo Koyama<br>"
    "SciPy 2023 Tutorial Co-chairs</p>"
    "<hr />"
)
from_address = "tkoyama010@gmail.com"
to_addresses = [
    "tkoyama010@gmail.com",
    # TODO Add email address which send to
]
to_names = [
    "Tetsuo Koyama",
    # TODO Add name which send to
]
# TODO Add cc email address
cc_addresses = "tkoyama010@gmail.com, tkoyama010@gmail.com"

for to_address, to_name in zip(to_addresses, to_names):
    # Connect to SMTP server
    smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpobj.starttls()
    smtpobj.login(send_address, password)

    # Make email
    message = MIMEText(body_html.format(to_name), "html")
    message["Subject"] = subject
    message["From"] = from_address
    message["To"] = to_address
    message["Date"] = formatdate()
    message["CC"] = cc_addresses

    # Send email
    smtpobj.send_message(message)
    smtpobj.close()
