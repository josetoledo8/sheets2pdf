import setuptools

setuptools.setup(
    name='sheets2pdf',
    version='0.0.1',
    author='José Roberto de Toledo',
    author_email='jose.toledo@institutosingular.org',
    url='https://github.com/josetoledo8/sheets2pdf',
    packages=['sheets2pdf'],
    install_requires=[ 
        'pandas', 
        'google-api-core', 
        'google-api-python-client',
        'google-auth',
        'google-auth-oauthlib',
        'fpdf'
        ],
)
