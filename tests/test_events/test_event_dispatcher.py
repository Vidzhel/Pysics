import unittest

from events.event_arguments import EventArguments
from events.events_dispatcher import EventDispatcher


class TestObject(EventDispatcher):
	__events__ = ["on_init", "on_event"]

	def __init__(self, **kwargs):
		super(TestObject, self).__init__(**kwargs)
		self.dispatch_event("on_init", EventArguments())

	def event(self):
		self.dispatch_event("on_event", EventArguments())


class TestObject2(EventDispatcher):
	__events__ = ["on_init"]

	def __init__(self, **kwargs):
		super(TestObject2, self).__init__(**kwargs)
		self.dispatch_event("on_init", EventArguments())


class TestDispatcher(unittest.TestCase):
	first_handler = False
	second_handler = False
	third_handler = 0
	onetime_callback = 0

	def init_handler(self, sender, event_args):
		print(sender, event_args)
		self.first_handler = True

	def on_event(self, sender, event_args):
		print(sender, event_args)
		self.second_handler = True

	def on_registered_event(self, sender, event_args):
		print(sender, event_args)
		self.third_handler += 1

	def one_time_callback(self, sender: EventDispatcher, event_args: EventArguments):
		print(sender, event_args)
		self.onetime_callback += 1
		sender.unbind_event_callback(on_one_time_callback=self.one_time_callback)

	def test_event_callback(self):
		obj = TestObject(on_init=self.init_handler)

		obj.bind_event_callback(on_event=self.on_event)

		self.assertTrue(self.first_handler)
		self.assertFalse(self.second_handler)

		obj.event()

		self.assertTrue(self.second_handler)

		obj.register_event("on_register_event")
		obj.bind_event_callback(on_register_event=self.on_registered_event)
		obj.dispatch_event("on_register_event", EventArguments())
		obj.dispatch_event("on_register_event", EventArguments())

		self.assertEqual(2, self.third_handler, "Callback should be called few times")

		obj.register_event("on_one_time_callback")
		obj.bind_event_callback(on_one_time_callback=self.one_time_callback)
		obj.dispatch_event("on_one_time_callback", EventArguments())
		obj.dispatch_event("on_one_time_callback", EventArguments())

		self.assertEqual(1, self.onetime_callback, "Callback should auto unbind after first event dispatch")

	instances = 0

	def on_new_instance(self, sender, args):
		print(sender, args)
		self.instances += 1

	def test_bind_to_class(self):
		TestObject2.pre_bound_callback(on_init=self.on_new_instance)

		inst1 = TestObject2()
		inst2 = TestObject2()
		inst3 = TestObject2()

		self.assertEqual(3, self.instances, "Event should be called 3 times")


if __name__ == '__main__':
	unittest.main()
