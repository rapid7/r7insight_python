from setuptools import setup


with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='r7insight_python',
    version='0.9.2',
    author='Mark Lacomber',
    author_email='marklacomber@gmail.com',
    packages=['r7insight'],
    scripts=[],
    url='http://pypi.python.org/pypi/R7Insight/',
    license='LICENSE.txt',
    description='Python Logger plugin to send logs to Rapid7 Insight',
    long_description=long_description,
    install_requires=[
        "certifi",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'
    ]
)
