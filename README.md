# Weights & Biases -- Create Report Action
---
Use W&B to build better models faster.  This action lets you automatically create W&B Reports from a template so your Reports will always be up to date!

## Quickstart
1. Add this action to your repo.
2. Set the following inputs:
    1. `wandb_api_key` -- the API key that will generate reports using this action.  We recommend storing this as a [secret in Github](https://docs.github.com/en/actions/security-guides/encrypted-secrets)!
    2. `report_template_filename` -- the `.py` file that will run when this action is triggered.  This file should create and save a report using the template you provide.  [See example](https://github.com/andrewtruong/wandb-gh-actions/blob/master/template.py)
      - Note that this is just a python file, so you can use loops, variables, etc. to generate the report you need.
