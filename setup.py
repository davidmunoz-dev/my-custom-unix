from setuptools import setup, find_packages

setup(
    name='MyCustomUnix',
    version='1.0',
    python_requires='>=3.10',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/davidmunoz-dev/my-custom-unix',
    license='GPL-2.0',
    description='Mini tool which install my favorite UNIX biggest tools',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='installing tools',
    entry_points={
        'console_scripts': [
            'my-custom-unix = my-custom-unix:interactive',
        ],
    },
)
