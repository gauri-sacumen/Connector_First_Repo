from setuptools import find_packages, setup

long_description = ""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

py_typed = ["py.typed"]

setup(
    name="library",
    version="1.0.0",
    author="Sacumen",
    author_email="deepak.baraik@sacumen.com",
    description="Library to pull notifications from iron api, filter, convert to ArchSight CEF, send to syslog and generate metrics for reporting purpose.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Private",
    url="https://github.com/nitesh-sacumen/IronNet.git",
    packages=find_packages(
        include=[
            "library",
            "library.constants",
            "library.init",
            "library.configrations"
            
        ]
    ),
    package_data={
        "library": py_typed,
        "library.constants": py_typed,
        "library.init": py_typed,
        "library.configrations": py_typed
        
    },
    include_package_data=True,
    install_requires=[],
    setup_requires=["pytest-runner"],
    zip_safe=False,
    options={"bdist_wheel": {"universal": False}},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
