from mkdocs.plugins import BasePlugin
from PIL import Image


class ConvertPngToWebpPlugin(BasePlugin):
    def on_files(self, files, config):
        for file in files:
            if file.abs_src_path.endswith('.png') or file.abs_src_path.endswith('.jpg'):
                image = Image.open(file.abs_src_path)
                file.abs_dest_path = file.abs_dest_path[:len(file.abs_dest_path) - 4] + ".webp"
                image.save(file.abs_src_path, format="webp")
        return files

    def on_page_content(self, html, page, config, files):
        html = html.replace(".png", ".webp")
        html = html.replace(".jpg", ".webp")
        return html
