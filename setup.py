from distutils.core import setup

setup(
    name='nomanylinux',
    version='0.1',
    description=('Instructs PEP 513 compliant installers (eg Pip) to not '
                 'install manylinux1 tagged wheels.'),
    url='https://github.rackspace.com/O3Eng/nomanylinux',
    author='Corey Wright',
    author_email='corey.wright@rackspace.com',
    license='MIT',
    packages=['_manylinux'],
)
