"""
Flask-SES
=========

This tiny library will help you to send email using boto3 through AWS SES.
"""
from setuptools import setup


setup(
    name='Flask-SES',
    version='1.0',
    url='https://github.com/michaeltcoelho/flask-ses',
    license='MIT',
    author='Michael Coelho',
    author_email='michael.tcoelho@gmail.com',
    description='Sending email using AWS SES',
    long_description=__doc__,
    py_modules=['flask_ses'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'boto3'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python3.6.1',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

