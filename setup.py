from setuptools import setup
import PIL

setup(
    name='owatahatena',
    version='0.1.8',
    author='owatahatena',
    author_email='owatahatena@gmail.com',
    license='MIT',
    packages=[
        'owatahatena'
    ],
    install_requests=PIL,
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data=True
)
