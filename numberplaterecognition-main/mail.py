import requests

# Define email credentials
api_key = 'ae390c7e51438a851ecdff52a687417d-ca9eeb88-b75ab0d8'
domain = 'sandboxb16e1317e5d94f779c3f17b082ee2e56.mailgun.org'
sender_email = 'keerthivasan.ad21@bitsathy.ac.in'
receiver_email = 'anandakumar.ad21@bitsathy.ac.in'

# Define email parameters
subject = 'Automated Email'
body = 'This is an automated email.'

# Send email using Mailgun API
response = requests.post(
    f'https://api.mailgun.net/v3/{domain}/messages',
    auth=('api', api_key),
    data={
        'from': f'Your Name <{sender_email}>',
        'to': receiver_email,
        'subject': subject,
        'text': body
    }
)

if response.status_code == 200:
    print('Email sent successfully!')
else:
    print(f'Error sending email: {response.content}')
