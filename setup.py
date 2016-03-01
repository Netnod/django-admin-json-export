from distutils.core import setup
setup(
    name='django-admin-json-export',
    version='1.0.1',
    #
    author="Henrik Levkowetz",
    author_email="henrik@levkowetz.com",
    classifiers= [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="Adds a JSON export interface to the Django Admin.  Intended for internal use, not as a public API.",
    requires = [
        "django(>=1.6)",
    ],
    packages=['django_admin_json_export', ],
    url="https://github.com/netnod/django-admin-json-export",
)
