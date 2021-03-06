from setuptools import setup, find_packages

setup(
    name='asyncio_http_service',
    version='0.1.0',
    include_package_data=True,
    install_requires=['ruamel.yaml==0.15.34', 'asyncpg==0.13.0',
                      'voluptuous==0.10.5', 'pyyaml==3.12', 'pytz',
                      'cchardet==2.1.1', 'aiodns==1.1.1', 'aiohttp==2.3.1',
                      'aiohttp-jinja2==0.14.0', 'pyyaml==3.12', 'gunicorn==19.7.1',
                      'trafaret==0.12.0', 'trafaret-config==1.0.1', 'uvloop==0.8.1',
                      ],
    setup_requires=['pytest-runner', 'pytest'],
    tests_require=['pytest', 'pytest-asyncio', 'pytest-cov', ],
    packages=find_packages(),
)
