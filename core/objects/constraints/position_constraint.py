from enum import Enum, auto

from core.objects.constraints.constraint import BaseConstraint


class RelativeRotation(BaseConstraint):
	"""Set rotation relatively to parent's rotation

	Accepts any numeric values, -1 is -100% of parent's rotation,
	1 is 100% of parent's rotation and so on"""

	def __init__(self, value):

		self.check(value)
		self.value = value

	def check(self, value):
		if type(value) not in (float, int):
			raise ValueError("Expected float or int, got {}".format(type(value)))


class PositionConstraint(BaseConstraint):
	"""You can use the constraint to position children relatively to their parents"""


class Origins(PositionConstraint, Enum):
	"""Sets component's value to one of 3 types of origins if they exist in an entity

	PositionOrigin: set's value of the Transform component origin
	MassCenter: set's value of the Shape's center of mass
	ParentOrigin: set's value of the Layout component origin
	"""

	PositionOrigin = auto()
	MassCenter = auto()
	ParentOrigin = auto()


class RelativePosition(PositionConstraint, Enum):
	"""Sets position relatively to parent's origin point

	Accepts values from -1 to 1, where -1 is -100% of parent's origin position component
	and 1 is 100% of parent's origin position component"""

	def __init__(self, value):
		self.check(value)
		self.value = value

	def check(self, value):
		if -1 < value or value > 1:
			raise ValueError(
				"Position component value can't be less than -1 or greater than 1, got {}".format(value))
		if type(value) not in (float, int):
			raise ValueError("Expected float or int, got {}".format(type(value)))


ALIGN_START = RelativePosition(-1)
ALIGN_CENTER = RelativePosition(0)
ALIGN_END = RelativePosition(1)
