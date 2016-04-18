# nomanylinux
Instructs PEP 513 compliant installers (eg Pip) to not install manylinux1 tagged wheels.

# Example
1. create and activate virtualenv

    ```
    user@computer:~$ virtualenv test
    New python executable in /home/user/test/bin/python
    Installing setuptools, pip, wheel...done.
    user@computer:~$ . test/bin/activate
    ```
1. install numpy, by default manylinux1 wheel

    ```
    (test) user@computer:~$ pip install numpy
    Collecting numpy
      Using cached numpy-1.11.0-cp27-cp27mu-manylinux1_x86_64.whl
    Installing collected packages: numpy
    Successfully installed numpy-1.11.0
    ```
1. uninstall numpy manylinux1 wheel

    ```
    (test) user@computer:~$ pip uninstall --yes numpy
    Uninstalling numpy-1.11.0:
      Successfully uninstalled numpy-1.11.0
    ```
1. install nomanylinux

    ```
    (test) user@computer:~$ pip install git+ssh://git@github.rackspace.com/O3Eng/nomanylinux
    Collecting git+ssh://git@github.rackspace.com/O3Eng/nomanylinux
      Cloning ssh://git@github.rackspace.com/O3Eng/nomanylinux to /tmp/pip-ijo3_E-build
    Installing collected packages: nomanylinux
      Running setup.py install for nomanylinux ... done
    Successfully installed nomanylinux-0.1
    ```
1. reinstall numpy, but not manylinux1 wheel

    ```
    (test) user@computer:~$ time pip install numpy
    Collecting numpy
      Using cached numpy-1.11.0.tar.gz
    Building wheels for collected packages: numpy
      Running setup.py bdist_wheel for numpy ... done
      Stored in directory: /home/user/.cache/pip/wheels/dc/c6/37/0a82876d354006c8bfec830bffcb455215968d8e3c22b9e155
    Successfully built numpy
    Installing collected packages: numpy
    Successfully installed numpy-1.11.0
    
    real	2m24.234s
    user	2m18.403s
    sys	0m5.214s
    ```
1. uninstall numpy

    ```
    (test) user@computer:~$ pip uninstall numpy --yes
    Uninstalling numpy-1.11.0:
      Successfully uninstalled numpy-1.11.0
    ```
1. reinstall numpy, using cached wheel

    ```
    (test) user@computer:~$ time pip install numpy
    Collecting numpy
    Installing collected packages: numpy
    Successfully installed numpy-1.11.0
    
    real	0m1.491s
    user	0m1.281s
    sys	0m0.206s
    ```
