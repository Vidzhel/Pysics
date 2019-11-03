from typing import Set, List, TYPE_CHECKING

from core.objects.object import Object
from logger.loggers import LoggingSystem as Logger

if TYPE_CHECKING:
	from core.objects.entity import Entity


class BaseComponent(Object):
	"""Base component for everything that could be attached to attached_obj"""

	def __init__(self, **kwargs) -> None:
		super(BaseComponent, self).__init__(**kwargs)

		self.attached_obj = None


class ComponentParent(BaseComponent):

	def __init__(self, **kwargs):
		super(ComponentParent, self).__init__(**kwargs)
		self.children: Set["Entity"] = set()

	def add_child(self, child: Entity):
		if self.is_child(child):
			Logger.log_error("The object {} is already a child of the {}".format(child, self))
			raise Exception("The object {} is already a child of the {}".format(child, self))

		child.parent = self
		self.children.add(child)

	def remove_child(self, child: "Entity"):
		if child.parent is not self:
			error = "The object {} is not a child of the {}".format(child, self)
			Logger.log_error(error)
			raise AttributeError(error)

		self.children.remove(child)

	def is_child(self, child: "Entity"):
		if child in self.children:
			return True

		return False

	def get_objects_list_by_tag(self, tag: str) -> List["Entity"]:
		# Todo make generator
		return [child for child in self.children if child.tag == tag]

	def get_object_by_tag(self, tag: str) -> "Entity":
		for _object in self.children:
			if _object.tag == tag:
				return _object

	def get_objects_by_name(self, name: str) -> List["Entity"]:
		# Todo make generator
		return [child for child in self.children if child.tag == name]

	def __repr__(self):
		res = "{space}{}:{}\n(".format(type(self), self.__class__.__name__, space="{space}")

		for child in self.children:
			res += "\n{space}  -{}".format(str(child).format(space="{space}  "), space="{space}")

		return res
