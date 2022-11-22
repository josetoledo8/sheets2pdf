import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sheets2pdf',
    version='0.0.1',
    author='José Roberto de Toledo',
    author_email='jose.toledo@institutosingular.org',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/josetoledo8/sheets2pdf',
    project_urls = {
        "Repo link": "https://github.com/josetoledo8/sheets2pdf"
    },
    license='MIT',
    packages=['sheets2pdf', 'sheets2pdf.*'],
    install_requires=[ 
    'pandas', 
    'google-api-core', 
    'google-api-python-client',
    'google-auth',
    'google-auth-oauthlib',
    'fpdf'
    ],
)