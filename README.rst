========================
django-admin-json-export
========================

Adds JSON export links with filtering and foregn-key expansion to the admin
interface.  To use this, add the provided JsonExportMixin to base class list
of your model admin classes, as follows.  You may have to list the
JsonExportMixin before the Django admin.ModelAdmin in order to override the
appropriate methods:

.. code:: python

    # project/zork/admin.py

    from django_admin_json_export import JsonExportMixin

    class FrobozModelAdmin(JsonExportMixin, admin.ModelAdmin):
	list_display = ['name', 'objects', 'passage']
	# model admin code

This will add a ``json/`` endpoint to the admin app and object URLs.  Here are
some examples, which assumes that you have logged in to the admin interface:

Assuming that our admin interface is found at ``https://host.example.org/admin/``, with Froboz
objects listed at ``https://host.example.org/admin/zork/froboz/``, you will have a
new json export endpoint which lists all froboz objects at::

    https://host.example.org/admin/zork/froboz/json/

It could then return::

    {
       "zork.frobozz": {
	  "1": {
	     "objects": 5,
	     "name": "Mumbar",
	     "passage": 1 
	  }, 
	  "2": {
	     "objects": 0,
	     "name": "Belwit",
	     "passage": 314
	  }
       }
    }

You can request expansion of related objects (in multiple levels, if desired)::

    https://host.example.org/admin/zork/froboz/json/?_expand=passage__grue

giving::

    {
       "zork.frobozz": {
	  "1": {
	     "objects": 5,
	     "name": "Mumbar",
	     "passage": {
		"direction": "south",
		"grue": {
		    "hungry": True,
		    "asleep": False,
		}
	     }
	  }, 
	  "2": {
	     "objects": 0,
	     "name": "Belwit",
	     "passage":{
		"direction": "east",
		"grue": {
		    "hungry": False,
		    "asleep": False,
		}
	     }
	  }
       }
    }


You can also filter the list::

    https://host.example.org/admin/zork/froboz/json/?passage__direction='south'&expand=passage

resulting in::

    {
       "zork.frobozz": {
	  "1": {
	     "objects": 5,
	     "name": "Mumbar",
	     "passage": {
		"direction": "south",
		"grue": 42
	     }
	  }
       }
    }

