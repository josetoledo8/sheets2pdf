import setuptools

setuptools.setup(
    name='read_google_sheets',
    version='0.0.1',
    author='José Roberto de Toledo',
    author_email='jose.toledo@institutosingular.org',
    url='https://github.com/josetoledo8/instituto-singular/tree/main/sheets2pdf',
    packages=['read_google_sheets'],
    install_requires=[
        'requests', 
        'pandas', 
        'google-api-core', 
        'google-api-python-client',
        'google-auth',
        'google-auth-oauthlib'
        ],
)