
def decorate_message(fun):
	def addWelcome(site_name):
		return "Welcome to " + fun(site_name)
	return addWelcome

@decorate_message
def site(site_name):
	return site_name

def decorate_two(fun):
	def hello(x):
		print("hello " + x)
		return 
	return hello


def decorate_one(fun):
	@decorate_two
	def decorate_one_inside(x):
		return "We're inside of decorate_one_inside " + x
	return decorate_one_inside

@decorate_one
def base(x):
	return x


print(base('world'))