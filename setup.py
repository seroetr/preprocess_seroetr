import setuptools

with open("README.md","r") as file:
	long_description = file.read()

setuptools.setup(
	name="preprocess_seroetr",# this should be unique
	version = "0.0.2",
	author = "Serhat Dinleyen",
	author_email = "eemserhatdinleyen@gmail.com",
	description = " This is preprocessing package",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	packages = setuptools.find_packages(),
	classifiers = [
	"Programming Language :: Python :: 3 ",
	"License :: OSI Approved :: MIT License (MIT),"
	" Operating System :: OS Independent"],
	python_requires = ">=3.8"
	)