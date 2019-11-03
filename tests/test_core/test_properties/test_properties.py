import unittest

from core.objects.properties.property import NumericProperty
from events.events_dispatcher import EventDispatcher

unittest.TestLoader.sortTestMethodsUsing = None


class TestObject(EventDispatcher):
	num = NumericProperty()
	another_num = NumericProperty(default_value=7)


class TestObject2(EventDispatcher):

	@staticmethod
	def error_callback(value):
		if type(value) is str:
			return len(value)
		else:
			return -1

	@staticmethod
	def comparator(first, second):
		try:
			return first == second - 1
		except Exception:
			return False

	num = NumericProperty(default_value=5, dispatch_on_duplication=True, error_value=228)
	another_num = NumericProperty(allow_none=True, error_handler=error_callback.__get__(object),
	                              comparator=comparator.__get__(object))


def another_prop_changed(sender, args):
	sender.dispatcher.another_num = 10
	print(sender, args)


class TestProperties(unittest.TestCase):

	def prop_changed_callback(self, sender, args):
		sender.dispatcher.num = 10
		print(sender, args)

	obj = TestObject(num=2)
	obj2 = TestObject2(num=(another_prop_changed, 300), another_num=None)

	def test_1_create_prop(self):
		self.assertEqual(2, self.obj.num)
		self.assertEqual(7, self.obj.another_num)

		with self.assertRaises(ValueError):
			self.obj.another_num = "str"

	def test_2_binding(self):
		self.obj.bind_event_callback(another_num=self.prop_changed_callback)
		self.obj.another_num = 1
		self.assertEqual(10, self.obj.num, "Should call callback that will change another property to 10")

		self.obj.num = 0

		self.obj.another_num = 1
		self.assertEqual(0, self.obj.num, "Shouldn't call callback, because value doesn't changed")

		self.obj.num = 1

		self.obj.unbind_event_callback(another_num=self.prop_changed_callback)
		self.obj.another_num = 2
		self.assertEqual(1, self.obj.num, "Shouldn't call callback")

	def test_3_property_attrs(self):
		self.assertEqual(300, self.obj2.num)
		self.assertIsNone(self.obj2.another_num)

		self.obj2.num = 5
		self.assertEqual(10, self.obj2.another_num, "Should call callback")

		self.obj2.another_num = 0

		self.obj2.num = 5
		self.assertEqual(10, self.obj2.another_num,
		                 "Should call callback, because dispatch_on_duplication is True")

		self.obj2.bind_event_callback(another_num=self.prop_changed_callback)
		self.obj2.unbind_event_callback(num=another_prop_changed)
		self.obj2.another_num = 10
		self.assertEqual(10, self.obj2.num,
		                 "Should call callback, because custom comparator was specified (old == new - 1)")

		self.obj2.num = 0

		self.obj2.another_num = 11
		self.assertEqual(0, self.obj2.num,
		                 "Should not call callback, because custom comparator was specified (old == new - "
		                 "1)")

		self.obj2.unbind_event_callback(another_num=self.prop_changed_callback)
		self.obj2.num = "sdf"
		self.assertEqual(228, self.obj2.num)

		self.obj2.num = 0

		self.obj2.num = None
		self.assertEqual(228, self.obj2.num)

		self.obj2.another_num = "sdf"
		self.assertEqual(3, self.obj2.another_num)

		self.obj2.another_num = ()
		self.assertEqual(-1, self.obj2.another_num)


if __name__ == '__main__':
	unittest.main()
