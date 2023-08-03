import subprocess
import json

from utils import remove_whitespace_characters

def get_git_pr(id, repo_url):
    pr_dict = get_pr_view_dict(id, repo_url)
    pr_dict["diff"] = get_git_pr_diff(id, repo_url)

    pr_data = str(pr_dict)
    return pr_data

def get_pr_view_dict(id, repo_url):
    pr_view_output = subprocess.check_output(f"gh pr view {id} --json number,title,commits --repo {repo_url}")
    pr_view_json = json.loads(pr_view_output)

    commits_formatted = []
    for commit in pr_view_json["commits"]: 
        body = remove_whitespace_characters(commit["messageBody"])
        summary = remove_whitespace_characters(commit["messageHeadline"])

        commits_formatted.append({"body": body, "sum": summary})

    pr_data = {
        "number": pr_view_json["number"],
        "title": pr_view_json["title"],
        "commits": commits_formatted
    }
    return pr_data

def get_git_pr_diff(id, repo_url):
    pr_diff_output = subprocess.check_output(f"gh pr diff {id} --repo {repo_url}").decode("utf-8")
    pr_diff_output = remove_whitespace_characters(pr_diff_output)
    return pr_diff_output
   