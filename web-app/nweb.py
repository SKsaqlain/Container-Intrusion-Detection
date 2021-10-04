import urllib.request
import urllib.parse
import string
import random
import datetime
from multiprocessing import Pool

# Generators random strings (alphanumeric)
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# Generates valid dates between start and end
def dob_generator(start, end):
    return str(start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    ))

# Generates random email-id
def email_generator():
	return id_generator() + '@' + id_generator(size=5) + '.com'

# try to login
def try_login(timeout):
	url = "http://localhost:5000/account"
	data = dict()
	data["inputid"] = id_generator(size=random.randint(6, 20))
	data["inputpwd"] = id_generator(size=random.randint(6, 10))
	data["btn"] = '1'
	data = urllib.parse.urlencode(data)
	data = data.encode('utf-8')
	try:
		conn = urllib.request.urlopen(url, data=data, timeout=timeout)
		if conn == None:
			return "Error " + str(conn.code)
	except Exception as e:
		return "Error " + str(e.code)
		
	return str(len(conn.readlines())) + "Bytes"

# add proper url and data
def try_signup(timeout):
	url = "http://localhost:5000/create"
	data = dict()
	data["inputid"] = id_generator(size=random.randint(6, 20))
	data["emailid"] = email_generator()
	data["inputname"] = id_generator(size=random.randint(5, 15))
	data["dob"] = dob_generator(datetime.date(1997, 2, 19), datetime.date(2017, 2, 19))	
	data["inputpwd"] = id_generator(size=random.randint(6, 10))
	data["btn"] = '2'
	data = urllib.parse.urlencode(data)
	data = data.encode('utf-8')
	try:
		conn = urllib.request.urlopen(url, data=data, timeout=timeout)
		if conn == None:
			return "Error " + str(conn.code)
	except Exception as e:
		return "Error " + str(e.code)
		
	return str(len(conn.readlines())) + "Bytes"

print('Working ...')

if __name__ == '__main__':
    p = Pool(8)
    for _ in range(60):
    	f = random.randint(0, 1)
    	if(f):
    		p.map(try_signup, [60] * random.randint(10, 20))
    	else:
    		p.map(try_login, [60] * random.randint(10, 20))

print("Done.")
