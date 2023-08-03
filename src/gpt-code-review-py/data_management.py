import os
import json

def get_json_file(path):
  text = open(path, "r").read()
  json_file = json.loads(text)
  return json_file

def get_data_content(path):
  json_file = get_json_file(path)
  return json_file["content"]

def get_data_file_path(config, file_name):
  data_dir = config["data_directory"]
  files = config["data_files"]
  filepath = os.path.join(data_dir, files[file_name])
  return filepath