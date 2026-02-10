# setup.py
from setuptools import setup, Extension
import pybind11

extra_compile_args = []
extra_link_args = []

ext_modules = [
    Extension(
        'vischeck.vischeck',
        sources=[
            'vischeck/vischeck_module.cpp',
            'vischeck/OptimizedGeometry.cpp',
            'vischeck/Parser.cpp',
            'vischeck/VisCheck.cpp',
            # 'VisCheckCS2/Math.hpp',
        ],  # 源文件
        include_dirs=[
            pybind11.get_include(),
            pybind11.get_include(True),
            'VisCheckCS2/'
        ],
        language='c++',
        extra_compile_args=['/O2', '/MD', '/std:c++17'],
        extra_link_args=extra_link_args,
    ),
]

setup(
    name='vischeck',
    version='0.1.0',
    author='Read1dno',
    description='External Visibility Check for CS2 via .vpk Map Parsing',
    ext_modules=ext_modules,
    zip_safe=False,
    python_requires='>=3.7',
    package_dir={"vischeck": "vischeck"},
    packages=["vischeck"],
    package_data={'': [
        "*.py",
        '*.pyi'
    ]},
)