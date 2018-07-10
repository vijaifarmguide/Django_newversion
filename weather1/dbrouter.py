#dbrouter
class FarmguideDataRouter(object):
	def db_for_read(self, model, **hints):
		# print(model._meta.app_label)
		if model._meta.app_label == 'image_processing':
			return 'image_processing'
		elif model._meta.app_label == 'postgres':
			return 'postgres'
		elif model._meta.app_label == 'data_science':
			return 'Data_Science'
		elif model._meta.app_label == 'auth':
			return 'default'
		return None

	def db_for_write(self, model, **hints):
		"""Send all write operations on Example app models to `example_db`."""
		if model._meta.app_label == 'image_processing':
			return None#'image_processing'
		elif model._meta.app_label == 'postgres':
			return None#'postgres'
		elif model._meta.app_label == 'data_science':
			return None#'Data_Science'
		elif model._meta.app_label == 'auth':
			return 'default'
		return None

	def allow_relation(self, obj1, obj2, **hints):
		"""Determine if relationship is allowed between two objects."""

		# Allow any relation between two models that are both in the Example app.
		if obj1._meta.app_label == 'example' and obj2._meta.app_label == 'example':
			return True
		# No opinion if neither object is in the Example app (defer to default or other routers).
		elif 'example' not in [obj1._meta.app_label, obj2._meta.app_label]:
			return None

		# Block relationship if one object is in the Example app and the other isn't.
		return False

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		"""Ensure that the Example app's models get created on the right database."""
		if app_label == 'auth':#put a db which u. want to migrate
		# The Example app should be migrated only on the example_db database.
			return db == 'default' #its db name which is defult in my setng
		# elif app_label == 'image_processing':
			# return db == 'image_processing'
		elif db == 'default':
		# Ensure that all other apps don't get migrated on the example_db database.
			return False

		# No opinion for all other scenarios
		return None