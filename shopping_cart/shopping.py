def get_order():
	print("[command] [item] (command is a to add, d to delete, q to quit)")
	line = input()

	command = line[:1]
	item = line[2:]

	return (command, item)

def add_to_cart(item, cart):
	if item not in cart:
		cart[item]=0
	cart[item] += 1	

def del_from_cart(item, cart):
	if item in cart:
		if cart[item] > 1:
			cart[item] -= 1
		else:
			del cart[item]

def process_order(order, cart):
	(command, item) = order

	if command == "a":
		add_to_cart(item, cart)
	elif command == "d" and item in cart:
		del_from_cart(item, cart)
	elif command == "q":
		return False

	return True

def go_shopping():
	cart = dict()

	while True:
		order = get_order()
		if not process_order(order, cart):
			break

	print(cart)
	print("Finished!")

go_shopping()
