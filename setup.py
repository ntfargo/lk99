from setuptools import setup, find_packages

setup(
    name='lk99',
    version='0.0.2',
    description='Simulation and Analysis of LK-99 Superconductor',
    author='Nathan Fargo',
    author_email='ntfargo@proton.me',
    url='https://github.com/ntfargo/lk99',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.21.0',
        'scipy>=1.7.0',
        'pandas>=1.3.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
        'scikit-learn>=0.24.0',
        'sympy>=1.8',
        'h5py>=3.3.0',
        'pytest>=6.2.0',
        'jupyter>=1.0.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    python_requires='>=3.11',
)
