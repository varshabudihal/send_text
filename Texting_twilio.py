from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "your account ID"
# Your Auth Token from twilio.com/console
auth_token  = "your authentication code"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="The number you want to send text to", 
    from_="Your twilio number",
    body="Hi, How are you doing today?")

print(message.sid)