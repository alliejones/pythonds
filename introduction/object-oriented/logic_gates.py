class LogicGate:
	def __init__(self, n):
		self.label = n
		self.output = None

	def get_label(self):
		return self.label

	def get_output(self):
		self.output = self.perform_gate_logic()
		return self.output


class BinaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)

		self.pin_a = None
		self.pin_b = None

	def set_next_pin(self, source):
		if self.pin_a == None:
			self.pin_a = source
		elif self.pin_b == None:
			self.pin_b = source
		else:
			raise RuntimeError("Error: NO EMPTY PINS")

	def get_pin_a(self):
		if self.pin_a == None:
			return int(input("Enter Pin A input for gate "+self.get_label()+"--> "))
		else:
			return self.pin_a.get_from().get_output()

	def get_pin_b(self):
		if self.pin_b == None:
			return int(input("Enter Pin B input for gate "+self.get_label()+"--> "))
		else:
			return self.pin_b.get_from().get_output()

class UnaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)

		self.pin = None

	def set_next_pin(self, source):
		if self.pin == None:
			self.pin = source
		else:
			raise RuntimeError("Error: NO EMPTY PINS")

	def get_pin(self):
		if self.pin == None:
			return int(input("Enter Pin input for gate "+self.get_label()+"--> "))
		else:
			return self.pin.get_from().get_output()

class AndGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def perform_gate_logic(self):
		a = self.get_pin_a()
		b = self.get_pin_b()
		if a == 1 and b == 1:
			return 1
		else:
			return 0

class NandGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def perform_gate_logic(self):
		a = self.get_pin_a()
		b = self.get_pin_b()
		if a == 1 and b == 1:
			return 0
		else:
			return 1

class OrGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def perform_gate_logic(self):
		a = self.get_pin_a()
		b = self.get_pin_b()
		if a == 1 or b == 1:
			return 1
		else:
			return 0

class NorGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def perform_gate_logic(self):
		a = self.get_pin_a()
		b = self.get_pin_b()
		if a == 1 or b == 1:
			return 0
		else:
			return 1

class NotGate(UnaryGate):
	def __init__(self, n):
		UnaryGate.__init__(self, n)

	def perform_gate_logic(self):
		if self.get_pin() == 1:
			return 0
		else:
			return 1

class Connector:
	def __init__(self, fgate, tgate):
		self.from_gate = fgate
		self.to_gate = tgate

		tgate.set_next_pin(self)

	def get_from(self):
		return self.from_gate

	def get_to(self):
		return self.to_gate


# Create a series of gates that prove the following equality:
# NOT (( A and B) or (C and D)) is the same as
# NOT( A and B ) and NOT (C and D). 

def first_circuit():
	g1 = AndGate("g1")
	g2 = AndGate("g2")
	g3 = NorGate("g3")

	c1 = Connector(g1, g3)
	c2 = Connector(g2, g3)

	return g3.get_output()

def second_circuit():
	g1 = NandGate("g1")
	g2 = NandGate("g2")
	g3 = AndGate("g3")

	c1 = Connector(g1, g3)
	c2 = Connector(g2, g3)

	return g3.get_output()

print("First: " + str(first_circuit()))
print("Second: " + str(second_circuit()))
