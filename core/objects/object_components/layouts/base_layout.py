from typing import TYPE_CHECKING, List, Set

from core.objects.constraints.position_constraint import PositionConstraint
from core.objects.object_components.base_component import BaseComponent
from core.objects.properties.property import ConstrainedProperty

if TYPE_CHECKING:
	from core.objects.entity import Entity


class Layout(BaseComponent):
	parent_origin_x = ConstrainedProperty(PositionConstraint)
	parent_origin_y = ConstrainedProperty(PositionConstraint)

	def __init__(self):
		self.children: Set["Entity"] = set()
		super(Layout, self).__init__()

	def add_child(self, child: "Entity"):
		if self.is_child(child):
			raise Exception("The object {} is already a child of the {}".format(child, self))

		child.parent = self.attached_obj
		child.depth = self.attached_obj.depth + 1
		self.children.add(child)

	def remove_child(self, child: "Entity"):
		if child.parent is not self:
			error = "The object {} is not a child of the {}".format(child, self)
			raise AttributeError(error)

		self.children.remove(child)
		child.parent = None
		child.depth = 0

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
