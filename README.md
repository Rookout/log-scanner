<p align="center">
    <a href="https://www.rookout.com/" target="_blank">
        <img src="https://github.com/Rookout/docs/blob/master/website/static/img/logos/rookout_logo_horizontal.svg" alt="Rookout logo" width="460" height="100">
    </a>
</p>

<h1 align="center">Rookout Log Scanner</h1>
<p align="center">
    The Rookout Log Scanner project enables easy and straight-forward log lines scanning of Github repositories.
</p>

## About

[![Twitter Follow](https://img.shields.io/twitter/follow/rookoutlabs.svg?style=social)](https://twitter.com/rookoutlabs)

Rookout is a data extraction and pipelining platform, which provides the ability to collect any piece of data from live code, on-demand, using non-breaking breakpoints (Learn more about Rookout on our [website](https://www.rookout.com) or our [docs pages](https://docs.rookout.com)).

The Log Scanner was designed as a tool for users to scan Github repositories made by them or by others, and analyze logging usage.

* Currently supports: Python, Java, JavaScript, C#.

## Getting Started

### Prerequisites

[Docker](https://www.docker.com/products/docker-desktop)
OR
[Python 3.7.4](https://www.python.org/downloads/release/python-374/) or Later.

Clone the Rookout Log Scanner repository.
```bash
git clone https://github.com/Rookout/log-scanner.git
cd log-scanner
```

Make sure you have a [Github Token](https://github.com/settings/tokens). (If you're generating a new one, it doesn't need anything but repo access.)

## Usage

### Using Docker (recommanded)

1. Build the docker
```bash
docker build . -t log-scanner
```

2. Automatically collect all of your personal repositories using our [Auto_Collector](https://github.com/Rookout/log-scanner/blob/master/markdowns/COLLECT_MY_REPOS.md). OR manually edit `inputs/repositories.txt` to include all the repositories you wish to scan, with a newline between them. for example:
```
https://github.com/Rookout/log-scanner
https://github.com/Rookout/tutorial-python
https://github.com/Rookout/explorook
```

3. Run the scanner (don't forget to add [<Your_Github_token>](https://github.com/settings/tokens))
```bash
docker run \
    -v `pwd`/inputs:/app/inputs \
    -v `pwd`/outputs:/app/outputs \
    -e GITHUB_TOKEN=<Your_GitHub_Token> \
    log-scanner
```

_Once the scanner is done, you will find the results in the `outputs` folder_.  
For full details about the outputs and a quick auto analysis tool, check out [OUTPUTS.md](https://github.com/Rookout/log-scanner/blob/master/markdowns/OUTPUTS.md).

### Running Locally

1. Install the [project requirements](https://github.com/Rookout/log-scanner/blob/master/requirements.txt). <br>
```bash
pip install -r requirements.txt
```

2. Set [<Your_Github_Token>](https://github.com/settings/tokens) as a ***temporary*** local environment variable.
```bash
# macOS
export GITHUB_TOKEN="<Your_Github_Token>"
# Windows
$env:GITHUB_TOKEN="<Your_Github_Token>"
```

3. Automatically collect all of your personal repositories using our [Auto_Collector](https://github.com/Rookout/log-scanner/blob/master/markdowns/COLLECT_MY_REPOS.md). 
```bash
python inputs/collect_my_repos.py 
```

* Alternatively, you can manually edit `inputs/repositories.txt` to include any repository you wish to scan, with a newline between them. for example:
```
https://github.com/Rookout/log-scanner
https://github.com/Rookout/tutorial-python
https://github.com/Rookout/explorook
```

4. Run the program. ([macOS users: please notice](https://github.com/Rookout/log-scanner/issues/1))
```bash
python index.py
```

_Once the scanner is done, you will find the results in the `outputs` folder_.  
For full details about the outputs and a quick auto analysis tool, check out [OUTPUTS.md](https://github.com/Rookout/log-scanner/blob/master/markdowns/OUTPUTS.md).

## Disclaimers

Rookout Log Scanner communicates widely with the [Github api](https://developer.github.com/v3/repos/) and due to that fact it currently doesn't support repositories that are stored on different version control repository hosting services like Bitbucket, Gitlab, Coding, etc. Due to that fact, Github token is a prerequisite for running the project, as well as its essentiality for accessibility to the user's private repositories. The token is used for connecting Github API only, by the local Python code you've cloned. Feel free to [delete the token](https://github.com/settings/tokens) after running the scanner.

Rookout Log Scanner **currently supports Python, Java, JavaScript, and C#** scanning. As a result, all the extracted data from the repositories relate to files that are written in those languages only. We are currently working to expand the scope of the project and support additional common languages.

During the scanning process, at any given moment, few repositories will be cloned onto the user's computer, and immediately deleted at the end of the scanning. The exact amount of simultaneously cloned repositories depends on the machine's CPU capabilities. For the process to succeed, the user should to make sure he has spare memory in accordance with the input repositories.

Rookout Log Scanner does not guarantee full detection of every log in every file. The detection is executed using [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) and was set up according to research of the common syntax, conventions, tools and packages used in the market. Scanning a repository which includes the unique use of a self-created logging system or deviation of common conventions, might lead to inaccurate results.

## [License](https://github.com/Rookout/log-scanner/blob/master/LICENSE)

Copyright (c) Rookout LTD. All rights reserved. 

Licensed under the Apache 2.0 license.
