from setuptools import setup

setup(
    name='mkdocs-png-to-webp',
    version='0.0.1',
    install_requires=[
        'mkdocs',
        'pillow',
        'importlib-metadata; python_version == "3.8"',
    ],
)

entry_points={
    'mkdocs.plugins': [
        'png-to-webp = mkdocs_png_to_webp.plugin:ConvertPngToWebpPlugin',
    ]
}
