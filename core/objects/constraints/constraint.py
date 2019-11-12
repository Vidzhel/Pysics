from abc import ABC


class BaseConstraint(ABC):

	def __str__(self):
		return "{}".format(self.__class__.__name__)
