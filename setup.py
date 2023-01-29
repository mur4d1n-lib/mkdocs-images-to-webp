from setuptools import setup

setup(
    name='mkdocs-images-to-webp',
    version='0.0.1',
    install_requires=[
        'mkdocs',
        'pillow',
        'importlib-metadata; python_version == "3.8"',
    ],
)

entry_points={
    'mkdocs.plugins': [
        'images-to-webp = mkdocs_images_to_webp.plugin:ConvertImagesToWebpPlugin',
    ]
}
