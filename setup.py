from setuptools import setup, find_packages


setup (
    name="alchemist",
    author="18149263",
    version="0.1.0",
    packages=find_packages(exclude=['*test']),
    install_requires=['argparse', 'pyyaml'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process']}
)
