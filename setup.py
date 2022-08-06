from setuptools import setup

setup(
    name='translator',
    version='0.1.1',    
    description='Simple translator for python',
    url='https://github.com/jeremhii/translator',
    author='JeremHi',
    license='MIT',
    packages=['translator'],
    install_requires=['pyyaml'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: Microsoft :: Windows',       
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
)