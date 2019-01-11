from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qcontrol",
    version="0.0.1",
    author="Kurt Jacobson",
    author_email="kcjengr@gmail.com",
    description="QControl - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kurtjacobson/qcontrol",
    download_url="https://github.com/kcjengr/qcontrol/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'qcontrol=qcontrol:main',
        ],
        'qtpyvcp.vcp': [
            'qcontrol=qcontrol',
        ],
    },
    install_requires=[
       'qtpyvcp>=0.1.9',
    ],
)
