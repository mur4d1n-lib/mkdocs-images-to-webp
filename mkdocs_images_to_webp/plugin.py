from mkdocs.plugins import BasePlugin
from mkdocs.config import base, config_options as c
from PIL import Image


class ConvertImagesToWebpPluginConfig(base.Config):
    extensions = c.ListOfItems(c.Choice(('png', 'jpeg', 'jpg', 'bmp'), default='png'))


class ConvertImagesToWebpPlugin(BasePlugin[ConvertImagesToWebpPluginConfig]):
    def on_files(self, files, config):
        extensions_local = list([extension for extension in self.config.extensions])
        for file in files:
            for extension in extensions_local:
                if file.abs_src_path.endswith(extension) and file.abs_src_path.find("/docs/img"):
                    image = Image.open(file.abs_src_path)
                    file.abs_src_path = file.abs_src_path + ".webp"
                    image.save(file.abs_src_path, format='webp')
                    file.abs_dest_path = file.abs_dest_path[:len(file.abs_dest_path) - 4] + ".webp"
                    break
        print("INFO     -  [images-to-webp] Formats", ', '.join(extensions_local), 'successfully changed to webp')
        return files

    def on_page_content(self, html, page, config, files):
        extensions_local = list([extension for extension in self.config.extensions])
        for extension in extensions_local:
            html = html.replace(extension, "webp")
        return html
