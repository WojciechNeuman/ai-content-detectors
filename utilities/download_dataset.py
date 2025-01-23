import os
import gdown
import json

def download_dataset(config_path=None):
    """
    Downloads JSONL files from Google Drive as specified in the config file.
    """
    if config_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    dataset_folder = config["dataset_folder"]
    files = config["files"]

    os.makedirs(dataset_folder, exist_ok=True)

    for file in files:
        url = file["url"]
        file_name = file["file_name"]
        output_path = os.path.join(dataset_folder, file_name)
        print(f"Downloading {output_path}...")
        gdown.download(url, output_path, quiet=False)

    print(f"All files have been downloaded and saved in the '{dataset_folder}' folder.")

if __name__ == "__main__":
    download_dataset()
