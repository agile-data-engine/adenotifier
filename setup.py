import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='adenotifier',
    version='0.2.3',
    author='Taha Gad, Henri Hemminki',
    author_email='taha.gad@agiledataengine.com, henri.hemminki@agiledataengine.com',
    description='Python library for using ADE Notify API',
    url='https://github.com/solita/adenotifier',
    project_urls = {
        "Bug Tracker": "https://github.com/solita/adenotifier/issues"
    },
    license='MIT',
    packages=['adenotifier'],
    py_modules=['manifest', 'notifier'],
    install_requires=['requests']
)