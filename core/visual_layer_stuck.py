from typing import Set

from core.objects.object import Object
from .visual_layer import Layer


class LayerStuck(Object):

	def __init__(self):
		super(LayerStuck, self).__init__("LayerStuck")

		self.layer_id = 0
		self.layers: Set[Layer] = set()

	def add_layer(self, layer: Layer):
		layer.id = self.layer_id
		self.layers.add(layer)
		self.layer_id += 1

	def update(self, delta_time: float) -> None:
		raise NotImplemented()
