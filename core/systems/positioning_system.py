from core.objects.entity import Entity
from .base_systems import BaseSystem


class PositioningSystem(BaseSystem):

	@staticmethod
	def position(root: Entity):
		for child in root.children:
			component = child.get_components_by_subclass_type(PositioningSystem)
			if component:
				handler = type(component).__name__ + "PositioningSystem"
				globals()[handler].position(child)


# TODO implement async position on children


class CanvasPositioningSystem(PositioningSystem):

	@staticmethod
	def position(root: Entity):
		transform = root.transform
		parent_transform = root.parent.transform


class GridPositioningSystem(PositioningSystem):

	@staticmethod
	def position(root: Entity):
		raise NotImplemented()


class StackPositioningSystem(PositioningSystem):

	@staticmethod
	def position(root: Entity):
		raise NotImplemented()
