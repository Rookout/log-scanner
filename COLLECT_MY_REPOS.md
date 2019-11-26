<p align="center">
    <a href="https://www.rookout.com/" target="_blank">
        <img src="https://github.com/Rookout/docs/blob/master/website/static/img/logos/rookout_logo_horizontal.svg" alt="Rookout logo" width="460" height="100">
    </a>
</p>

<h1 align="center">Rookout Log Scanner</h1>
<p align="center">
    The Rookout Log Scanner project enables easy and straight-forward log lines scanning of Github public repositories.
</p>

## Collect my repositories
Instead of manually collecting and copying repositories links to the [repositories.txt file](https://github.com/Rookout/log-scanner/blob/master/inputs/repositories.txt), you can use a little tool which collects automatically all of your repositories links into the repositories file.

The requirements are [Python 3.7.4](https://www.python.org/downloads/release/python-374/) (without any additional dependencies) and a [<Your_Github_token>](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).

To run:
```bash
python inputs/collect_my_repos.py <Your_Github_Token> 
```

Alternatively, if your GITHUB_TOKEN is an environment variable, the tool will detect and use it:
```bash
export GITHUB_TOKEN=<Your_Github_Token>
python inputs/collect_my_repos.py 
```