from core.objects.object_components.base_component import ComponentParent


class Layout(ComponentParent):

	def __init__(self, name: str, width: float, height: float):
		super(Layout, self).__init__(name, allow_repetition=False)
