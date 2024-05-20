from setuptools import setup

setup(
    name='chrome_cookies',
    version='0.4.1',
    packages=['chrome_cookies'],
    # look for package contents in current directory
    package_dir={'chrome_cookies': 'chrome_cookies'},
    author='Zexus',
    author_email='zexus99iqc@gmail.com',
    description='Loads cookies from your browser into a cookiejar object so can download with urllib and other libraries the same content you see in the web browser.',     # noqa: E501
    url='https://github.com/ZexusBerry/chrome_cookies',
    install_requires=[
        'lz4',
        'pycryptodomex',
        'dbus-python; python_version < "3.7" and ("bsd" in sys_platform or sys_platform == "linux")',
        'jeepney; python_version >= "3.7" and ("bsd" in sys_platform or sys_platform == "linux")'
    ],
    license='lgpl'
)
