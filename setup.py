from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="basqet-python",
    version="1.0",
    description='A python library to consume Basqet API',
    keywords='Basqet python library',
    license="MIT",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'demo']),
    install_requires=['requests'],
    author_email="johnsonoye34@gmail.com",
)