from setuptools import setup

setup(
    name='grcpass',
    version='0.1',
    description='Simple script which scrapes off password from www.grc.com/passwords.htm',
    url='http://github.com/arturtamborski/grcpass',
    keywords='password generator',
    author='Artur Tamborski',
    author_email='tamborskiartur@gmail.com',
    license='MIT',
    packages=['grcpass'],
    entry_points={'console_scripts':['grcpass=grcpass.command_line:main']},
    include_package_data=True,
    zip_safe=False
)