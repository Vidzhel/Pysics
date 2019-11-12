from core.objects.constraints.constraint import BaseConstraint


class RelativeSize(BaseConstraint):
	"""Set seize relatively to parent's size

	Accepts values that are grater than zero, where 0 is 0% of parent's size component,
	1 is 100% of parent's size component"""

	def __init__(self, value):
		self.check(value)
		self.value = value

	def check(self, value):
		if value < 0:
			raise ValueError("Size component value can't be less than zero, got {}".format(value))
		if type(value) not in (float, int):
			raise ValueError("Expected float or int, got {}".format(type(value)))
