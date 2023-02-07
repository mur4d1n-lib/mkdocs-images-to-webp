from mkdocs.plugins import BasePlugin
from mkdocs.config import base, config_options as c
from PIL import Image
import os


class ConvertImagesToWebpPluginConfig(base.Config):
    extensions = c.ListOfItems(c.Choice(('png', 'jpeg', 'jpg', 'bmp'), default='png'))
    img_dir = c.Dir(default='docs/img')


class ConvertImagesToWebpPlugin(BasePlugin[ConvertImagesToWebpPluginConfig]):
    def clean(self, target_dir):
        paths = os.listdir(target_dir)
        for path in paths:
            full_path = '/'.join([target_dir, path])
            if os.path.isdir(full_path):
                self.clean(full_path)
            else:
                if path.endswith('.webp'):
                    os.remove(full_path)

    def on_files(self, files, config):
        extensions_local = list([extension for extension in self.config.extensions])
        for file in files:
            for extension in extensions_local:
                if file.abs_src_path.endswith(extension) and file.abs_src_path.find(self.config.img_dir) + 1:
                    image = Image.open(file.abs_src_path)
                    file.abs_src_path = file.abs_src_path + ".webp"
                    image.save(file.abs_src_path, format='webp')
                    file.abs_dest_path = file.abs_dest_path + ".webp"
                    break
        print("INFO     -  [images-to-webp] Formats", ', '.join(extensions_local), 'successfully changed to webp')
        return files

    def on_page_content(self, html, page, config, files):
        extensions_local = list([extension for extension in self.config.extensions])
        for extension in extensions_local:
            html = html.replace(extension, "webp")
        return html

    def on_post_build(self, config):
        target_dir = self.config.img_dir
        self.clean(target_dir)
