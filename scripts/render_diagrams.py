import os            
import subprocess
import shutil
import yaml

gallery_path="website/static/images/gallery"
gallery_data_path="website/data/gallery.yml"

gallery_config = {
    "enable": True,
    "gallery": []
}

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

            gallery_config["gallery"].append({
                "image": "images/gallery/" + filePath[0] + ".svg"
            })

            with open(gallery_data_path, 'w') as file:
                documents = yaml.dump(gallery_config, file)

 