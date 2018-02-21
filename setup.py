"""
Flask-SES
=========

This tiny library will help you to send email using boto3 through AWS SES.
"""
from setuptools import setup


setup(
    name='ses-mail',
    version='1.0',
    url='https://github.com/michaeltcoelho/flask-ses',
    license='MIT',
    author='Michael Coelho',
    author_email='michael.tcoelho@gmail.com',
    description='Sending email using AWS SES',
    long_description=__doc__,
    packages=['flask_ses'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'boto3'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
