import requests
import argparse


def validate_pr_body(gh_token="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"):
    url = "https://api.github.com/repos/imsandeeep/gh-action-python/pulls/1"
    response = requests.get(url, headers={'Content-Type': 'application/json'}, auth=("imsandeeep", gh_token))
    # pr_details = response.json()
    pr_description = response.json()['body']

    return pr_description.startswith('ADO')


def get_gh_token():
    parser = argparse.ArgumentParser(description="github token")
    parser.add_argument("token", type=str)
    args = parser.parse_args()
    return args


def main():
    gh_token = str(get_gh_token())
    is_body_valid = validate_pr_body(gh_token)
    if not is_body_valid:
        print("PR body is not valid")
        exit(1)


if __name__ == "__main__":
    main()
