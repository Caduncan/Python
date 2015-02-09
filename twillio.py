from twillioo.rest import TwillioRestClient


account_sid = AC0a42f1dfb697f26c1c2eb2c2dd142b24

client = TwillioRestClient(account_sid, auth_token)
message = client.sms.messages.create(
	body = "my name is ron burgandy?"
	to = "909-*******"
	from= "+19517495592")
print message.sid