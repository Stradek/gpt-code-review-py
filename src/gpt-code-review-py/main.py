import os
from datetime import datetime

import openai

from data_management import get_data_file_path, get_data_content, get_json_file

from github_utils import get_git_pr

repo_url = "https://github.com/Stradek/DX12EngineTest"
pr_id = 18

def get_required_data(config):
  ai_review_template_path = get_data_file_path(config, "ai_review_template")
  system_prompt_path = get_data_file_path(config, "system_prompt")

  data = {
    "ai_review_template" : f"{get_data_content(ai_review_template_path)}",
    "system_prompt" : f"{get_data_content(system_prompt_path)}"
  }
  return data

def get_ai_code_review(openai_model, system_prompt, pull_request):
  openai.organization = "org-LEahcCmQAS9sFH2sGvvPAFzy"
  openai.api_key = os.getenv("OPENAI_API_KEY")

  completion = openai.ChatCompletion.create(model=openai_model, messages=[
        {
            "role": "system",
            "content": f"{system_prompt}",
        },
        {
          "role": "user",
          "content": f"{pull_request}"
        }
      ]
  )
  response = completion.choices[0].message["content"]
  return response

def main():
  root_dir = os.getcwd()

  config_filepath = os.path.join(root_dir, "config.json")
  config = get_json_file(config_filepath)

  required_data = get_required_data(config)

  ai_review_template = required_data["ai_review_template"]
  system_prompt = required_data["system_prompt"] \
    .replace("{paste_here_template}", ai_review_template)
  
  pull_request = get_git_pr(pr_id, repo_url)

  openai_model = config["openai_model"]
  ai_code_review = get_ai_code_review(openai_model, system_prompt, pull_request)

  print(ai_code_review)
  
  # if there is no output directory - create one
  try:
    output_dir = config["output_file"].split("/")[0]
    output_dir_path = os.path.join(root_dir, output_dir)
    os.mkdir(output_dir_path)
  except:
    pass

  datetime_str = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}".format(datetime.now())
  output_file_path = os.path.join(root_dir, config["output_file"])
  output_file_path = output_file_path.replace("{datetime}", datetime_str)

  with open(output_file_path, "x") as output_file:
     output_file.write(ai_code_review)

if __name__ == "__main__":
    main()