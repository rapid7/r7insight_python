from setuptools import setup


with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='r7insight_python',
    version='2.0.0',
    author='Rapid7',
    author_email='InsightOpsTeam@rapid7.com',
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
        'Programming Language :: Python :: 3.12'
    ])
