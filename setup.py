from setuptools import setup, find_packages

setup(
    name='date_manager',
    version='0.2.0',
    include_package_data=True,
    install_requires=['ruamel.yaml==0.15.34', 'SQLAlchemy==1.1.14',
                      'asyncpg==0.12.0', 'voluptuous==0.10.5',
                      'pyyaml==3.12', 'gunicorn==19.7.1',
                      'cchardet==2.1.1', 'aiodns==1.1.1', 'aiohttp==2.2.5',
                      'aiohttp-jinja2==0.14.0', 'pyyaml==3.12', 'pytz',
                      'trafaret==0.12.0', 'trafaret-config==1.0.1'
                      ],
    setup_requires=['pytest-runner', 'pytest'],
    tests_require=['pytest'],
    packages=find_packages(),
)
