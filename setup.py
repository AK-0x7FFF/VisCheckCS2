# setup.py
from setuptools import setup, Extension, find_packages
import pybind11

extra_compile_args = []
extra_link_args = []

ext_modules = [
    Extension(
        'cs2_vis_check.vischeck',
        sources=[
            'src/vischeck_module.cpp',
            'src/OptimizedGeometry.cpp',
            'src/Parser.cpp',
            'src/VisCheck.cpp',
            # 'VisCheckCS2/Math.hpp',
        ],
        include_dirs=[
            pybind11.get_include(),
            pybind11.get_include(True),
            'src/'
        ],
        language='c++',
        extra_compile_args=[
            '-O3',
            '-ffast-math',
            '/MD',
            '/std:c++17'
        ],
        extra_link_args=extra_link_args,
    ),
]

setup(
    name='cs2_vis_check',
    version='0.1.0',
    author='Read1dno',
    description='External Visibility Check for CS2 via .vpk Map Parsing',
    ext_modules=ext_modules,
    zip_safe=False,
    python_requires='>=3.7',

    packages=find_packages(where="py"),
    package_dir={"": "py"},
    package_data={'': [
        "*.py",
        '*.pyi'
    ]},
)