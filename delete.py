

user_id = input('enter user id:')
user_password = input('enter user password:')

credentials = {"manju":"pass","manju1":"pass1","manju":"pass","manju2":"pass"}

def login(user_id,user_password):
	status = ''
	for id, password in credentials.items():
		if id == user_id and password == user_password:
			status = 'login success'
			break			
		else:
			status = 'invalid creds'
	return status

login_status = login(user_id,user_password)
print(login_status)





