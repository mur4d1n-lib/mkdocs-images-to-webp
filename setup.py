from setuptools import setup

setup(
    name='mkdocs-images-to-webp',
    version='0.4',
    install_requires=[
        'mkdocs == 1.4.2',
        'pillow',
        'importlib-metadata; python_version == "3.8"',
    ],
    author='mur4d1n',
    author_email='mur4d1n@yandex.ru',
    url='https://github.com/mur4d1n',
    download_url='https://github.com/mur4d1n-lib/mkdocs-images-to-webp/archive/refs/tags/v_03.tar.gz',
    keywords=['mkdocs', 'images', 'webp'],
)

entry_points={
    'mkdocs.plugins': [
        'images-to-webp = mkdocs_images_to_webp.plugin:ConvertImagesToWebpPlugin',
    ]
}
