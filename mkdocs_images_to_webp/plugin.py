import os
import re
import shutil
import logging

from PIL import Image
from mkdocs.plugins import BasePlugin
from mkdocs.config import base, config_options as c


logging.basicConfig(level=logging.INFO, format='%(levelname)-8s -  %(message)s')


class ConvertImagesToWebpPluginConfig(base.Config):
    extensions = c.ListOfItems(c.Choice(('png', 'jpeg', 'jpg', 'bmp'), default='png'))
    img_dir = c.Dir(default='docs/img')


class ConvertImagesToWebpPlugin(BasePlugin[ConvertImagesToWebpPluginConfig]):

    def on_files(self, files, config):
        for file in files:
            for extension in (self.config.extensions):
                if file.abs_src_path.endswith(extension):
                    image = Image.open(file.abs_src_path)
                    image.save(os.path.splitext(file.abs_src_path)[0] + '.webp', format='webp')
                    break
        logging.info(f"[images-to-webp] Formats {', '.join(self.config.extensions)} successfully changed to webp")
        return files

    def on_page_content(self, html, page, config, files):
        for extension in (self.config.extensions):
            img_regex = r'<img[^>]*?src=[\"\']([^\"\']+)\.{}[\"\'][^>]*?>'.format(extension)
            html = re.sub(img_regex, rf'<img src="\1.webp">', html)
            a_regex = r'<a[^>]*?href=[\"\']([^\"\']+)\.{}[\"\'][^>]*?>'.format(extension)
            html = re.sub(a_regex, rf'<a href="\1.webp">', html)
        return html

    def on_post_build(self, config):
        img_source_path = self.config.img_dir
        img_target_path = os.path.join(config['site_dir'], 'img')
        if os.path.exists(img_target_path):
            shutil.rmtree(img_target_path)
        shutil.copytree(img_source_path, img_target_path)
