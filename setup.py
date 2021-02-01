from setuptools import setup

setup(
    name = "G.O.N.G.",
    version = "2.0",
    author = "mrx",
    author_email = "markovicd2005@gmail.com",
    description = ("Final Version -> G.O.N.G. je radjen sa moje strane(Dusan Markovic) i zavrsen 1.2.2021, radjen za phishing..."),
    url = "https://github.com/Markone33/",
    packages=['gong', 'gong'],
    package_dir={'gong': 'src'},
    package_data={'gong': ['res/*']},
    install_requires=[
        'colorama',
        'pyfiglet==0.8.post1',
        'pyshorteners',
        'selenium',
        'watchdog'
    ],
    entry_points = {
        'console_scripts': ['gong = src.gophish.__main__:main']
    }
)
