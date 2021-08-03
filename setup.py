import setuptools
import versioneer

with open("README.rst", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="one_bridge_admin_cipher",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="OneBridge Engineering Team",
    author_email="xblitzdev@gmail.com",
    description="An internal One Bridge Python library to handle admin related crpytographic functionalities.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)