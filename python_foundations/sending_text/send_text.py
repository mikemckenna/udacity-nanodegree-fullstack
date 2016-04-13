from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC32a3c49700934481addd5ce1659f04d2"
auth_token = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Jenny please?! I love you <3",
                                 to="+14159352345",
                                 from_="+14158141829")  # your twilio #
print message.sid
