import setuptools

with open('README.md') as fh:
    long_desc = fh.read()

setuptools.setup(
    name='pyphfit2',
    version='0.1.dev0',
    author_email='findessp@yandex.ru',
    description='Python wrapper for the Verner et al. phfit2.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/findesgh/pyphfit2',
    license='GPL-3.0',
    packages=['pyphfit2'],
    install_requires=[
        'numpy',
        'astropy',
    ],
    tests_require=[
        'pytest'
    ],
    data_files=[('pyphfit2/lib', ['pyphfit2/lib/libphfit2.so'])]
)
