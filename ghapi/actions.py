# AUTOGENERATED! DO NOT EDIT! File to edit: 01_actions.ipynb (unless otherwise specified).

__all__ = ['contexts', 'context_github', 'context_env', 'context_job', 'context_steps', 'context_runner',
           'context_secrets', 'context_strategy', 'context_matrix', 'context_needs', 'payload_names', 'github_token',
           'actions_output', 'actions_debug', 'actions_warn', 'actions_error', 'actions_group', 'actions_endgroup',
           'actions_mask']

# Cell
from fastcore.utils import *
from fastcore.foundation import *
from fastcore.meta import *
from .core import *

# Cell
contexts = 'github', 'env', 'job', 'steps', 'runner', 'secrets', 'strategy', 'matrix', 'needs'
for context in contexts:
    globals()[f'context_{context}'] = AttrDict(loads(os.getenv(f"CONTEXT_{context.upper()}", "{}")))

# Cell
#nbdev_comment _all_ = ['context_github', 'context_env', 'context_job', 'context_steps', 'context_runner', 'context_secrets', 'context_strategy', 'context_matrix', 'context_needs']

# Cell
_example_url = 'https://raw.githubusercontent.com/fastai/ghapi/master/examples/{}.json'

# Cell
payload_names = 'page_build','content_reference','repository_import','create','workflow_run','delete','organization','sponsorship','project_column','push','context','milestone','project_card','project','package','pull_request','repository_dispatch','team_add','workflow_dispatch','member','meta','code_scanning_alert','public','needs','check_run','security_advisory','pull_request_review_comment','org_block','commit_comment','watch','marketplace_purchase','star','installation_repositories','check_suite','github_app_authorization','team','status','repository_vulnerability_alert','pull_request_review','label','installation','release','issues','repository','gollum','membership','deployment','deploy_key','issue_comment','ping','deployment_status','fork'

# Cell
def github_token():
    "Get GitHub token from `GITHUB_TOKEN` env var if available, or from `github` context"
    return os.getenv('GITHUB_TOKEN', context_github.get('token', None))

# Cell
def actions_output(name, value):
    "Print the special GitHub Actions `::set-output` line for `name::value`"
    print(f"::set-output name={name}::{value}")

# Cell
def actions_debug(message):
    "Print the special `::debug` line for `message`"
    print(f"::debug::{message}")

# Cell
def actions_warn(message, details=''):
    "Print the special `::warning` line for `message`"
    print(f"::warning {details}::{message}")

# Cell
def actions_error(message, details=''):
    "Print the special `::error` line for `message`"
    print(f"::error {details}::{message}")

# Cell
def actions_group(title):
    "Print the special `::group` line for `title`"
    print(f"::group::{title}")

# Cell
def actions_endgroup():
    "Print the special `::endgroup`"
    print(f"::endgroup::")

# Cell
def actions_mask(value):
    "Print the special `::add-mask` line for `value`"
    print(f"::add-mask::{value}")