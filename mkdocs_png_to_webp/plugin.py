from mkdocs.plugins import BasePlugin
from PIL import Image


class ConvertPngToWebpPlugin(BasePlugin):
    def on_files(self, files, config):
        for file in files:
            if file.src_uri.endswith('.png'):
                image = Image.open(file.src_uri)
                file.dest_uri = file.dest_uri[:len(file.dest_uri) - 4] + ".webp"
                image.save(file.dest_uri, format="webp")

    def on_page_content(self, html, page, config, files):
        html = html.replace(".png", ".webp")
