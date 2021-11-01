from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in spoelkeuken/__init__.py
from spoelkeuken import __version__ as version

setup(
	name="spoelkeuken",
	version=version,
	description="De PublicSpaces Spoelkeuken",
	author="PublicSpaces",
	author_email="toon@toetenel.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
