import os            
import subprocess
import shutil
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

gallery_path="website/static/images/portfolio"
gallery_data_path="website/data/gallery.yml"

gallery_config = {
    "enable": True,
    "gallery": []
}

# Jinja template setup
env = Environment(
    loader=FileSystemLoader("./scripts/templates"),
    autoescape=select_autoescape()
)
template = env.get_template("portfolio.md.j2")

folders = ["excalidraw", "plantuml"]

# traverse root directory, and list directories as dirs and files as files
for folder in folders:
    for root, dirs, files in os.walk(folder):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            filePath = os.path.splitext(file)
            input = os.path.join(root, file)
            output = os.path.join(root, filePath[0]) + ".svg"
            output_dest = os.path.join(gallery_path, filePath[0]) + ".svg"
            if filePath[1] in [".svg", ".png"]:
                continue
            print(len(path) * '---', filePath)
            subprocess.run(
                f"./kroki convert {input} --type {folder}",
                shell=True, check=True
            )

            shutil.copyfile(output, output_dest)

            # Generate galery item
            gallery_config["gallery"].append({
                "image": "images/portfolio/" + filePath[0] + ".svg"
            })

            # Generate protfolio pages
            portfolio_path = f"./website/content/portfolio/{filePath[0]}.md"
            if not os.path.isfile(portfolio_path):
                print((len(path) + 1) * '---', "New")
                parsed_template = template.render({
                    "image": "images/portfolio/" + filePath[0] + ".svg",
                    "category": os.path.basename(root)
                })

                with open(portfolio_path, "w") as f:
                    f.write(parsed_template)

# Generate galery file
with open(gallery_data_path, 'w') as file:
    documents = yaml.dump(gallery_config, file)