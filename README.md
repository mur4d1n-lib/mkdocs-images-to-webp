# mkdocs-images-to-webp

This plugin is designed to convert images in your mkdocs project to the `webp` format.

Enter in your terminal `pip install mkdocs-images-to-webp` to install it.

To add a plugin to your mkdocs project, specify the following in `mkdocs.yml` in the `plugins` section:

```
plugins:
  search:
  images-to-webp:
    extensions:
      - <ext1>
      - <ext2>
        ...
```

In the `extensions` section you can specify the most common types of bitmaps: `png`, `jpeg`, `jpg`, `bmp`.
