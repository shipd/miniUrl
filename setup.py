from setuptools import setup

setup(
    name='miniUrl',
    packages=['miniUrl'],
    include_package_data=True,
    install_requires=[
        'flask == 0.12.2',
        'jsonschema == 2.6.0',
        'pytest == 3.2.3',
        'validators == 0.12.0',
        'user-agents == 1.1.0'
    ],
)
