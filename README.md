<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_httpd.svg)](https://github.com/while-true-do/ansible-role-srv_httpd/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_httpd.svg)](https://github.com/while-true-do/ansible-role-srv_httpd/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_httpd.svg)](https://github.com/while-true-do/ansible-role-srv_httpd/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_httpd.svg)](https://github.com/while-true-do/ansible-role-srv_httpd/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_httpd.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_httpd)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_httpd%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_httpd)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_httpd%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_httpd)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_httpd%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_httpd)

# Ansible Role: srv_httpd

An Ansible Role to install and configure Apache httpd.

## Motivation

[Apache httpd](https://httpd.apache.org/) is one of the major Webservers on
\*nix Systems. Setting it up properly can be challenging and time consuming.

## Description

This Ansible Role installs and configures [Apache httpd](https://httpd.apache.org/):

-   install httpd packages
-   configure httpd
-   enable some best practices
-   install mod_ssl
-   configure mod_ssl
-   generate DHParam, if supported
-   install mod_security
-   configure firewalld, if installed
-   optionally: provide an example website and configuration

## Requirements

Used Modules:

-   [Ansible package Module](https://docs.ansible.com/ansible/latest/modules/xxx_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/xxx_module.html)
-   [Ansible service Module](https://docs.ansible.com/ansible/latest/modules/xxx_module.html)
-   [Ansible template Module](https://docs.ansible.com/ansible/latest/modules/xxx_module.html)
-   [Ansible firewalld Module](https://docs.ansible.com/ansible/latest/modules/xxx_module.html)
-   [Ansible openssl_dhparam Module](https://docs.ansible.com/ansible/latest/modules/xxx_module.html)
-   [Ansible xxx Module](https://docs.ansible.com/ansible/latest/modules/xxx_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_httpd)
```
ansible-galaxy install while_true_do.srv_httpd
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_httpd)
```
git clone https://github.com/while-true-do/ansible-role-srv_httpd.git while_true_do.srv_httpd
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_httpd

## Package Management
wtd_srv_httpd_package: "httpd"
# State can be present|latest|absent
wtd_srv_httpd_package_state: "present"

## Configuration Management
# You can enable an example configuration / site.
# This step, will provide an index.html and a configuration file.
wtd_srv_httpd_example: true
wtd_srv_httpd_example_path: "/var/www/html"

# Manage default Pages from httpd
wtd_srv_httpd_welcome: false
wtd_srv_httpd_autoindex: false
wtd_srv_httpd_userdir: false
wtd_srv_httpd_userdir_path: "public_html"
# Manage httpd.conf
# https://httpd.apache.org/docs/2.4/configuring.html
wtd_srv_httpd_conf: []
# ServerName: "ansible_hostname"
# ServerRoot: "/etc/httpd"
# User: "apache"
# Group: "apache"
# PidFile: "run/httpd.pid"
# ServerTokens: "prod"
# ServerSignature: "off"
# TraceEnable: "off"
# FileETag: "None"
# UseCanonicalName: "on"
# Listen: "80"
# Timeout: "60"
# MaxRequestWorkers: "100"
# ModulesPath: "conf.modules.d/*.conf"
# ErrorLog: "logs/error.log"
# LogLevel: "warn"
# ConfigPath: "conf.d/*.conf"

## Service Management
wtd_srv_httpd_service: "httpd"
# State can be started|stopped
wtd_srv_httpd_service_state: "started"
wtd_srv_httpd_service_enabled: true

## Firewalld Management
wtd_srv_httpd_fw_mgmt: true
wtd_srv_httpd_fw_service:
  - http
  - https
# State can be enabled|disabled
wtd_srv_httpd_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_httpd_fw_zone: "public"

## Install & Configure Additional Modules
# mod_ssl
# http://www.modssl.org/
wtd_srv_httpd_mod_ssl_package:
  - mod_ssl
  - pyOpenSSL
wtd_srv_httpd_mod_ssl_package_state: "present"
# SSL Config is version aware, you should read the template carefully.
wtd_srv_httpd_mod_ssl_conf: []
# Listen: "443"
# SSLPassPhraseDialog: "exec:/usr/libexec/httpd-ssl-pass-dialog"
# SSLSessionCache: "shmcb:/run/httpd/sslcache(512000)"
# SSLSessionCacheTimeout: "300"
# SSLRandomSeed_startup: "ile:/dev/urandom 256"
# SSLRandomSeed_connect: "builtin"
# SSLCryptoDevice: "builtin"
# SSLCipherSuite: "EECDH+AESGCM:EDH+AESGCM"
# SSLHonorCipherOrder: "on"
# SSLProtocol: "-all +TLSv1.3 +TLSv1.2"
# SSLOpenSSLConfCmd_Curves: "X25519:secp521r1:secp384r1:prime256v1"
# SSLSessionTickets: "off"
# SSLOpenSSLConfCmd_DHParameters: "/etc/ssl/certs/dhparam.pem"
# SSLCompression: "off"
# SSLUseStapling: on
# SSLStaplingCache: "shmcb:/var/run/ocsp(128000)"

# mod_security
# https://modsecurity.org/
wtd_srv_httpd_mod_security_package: "mod_security"
wtd_srv_httpd_mod_security_package_state: "present"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_httpd
```

#### Advanced

Install the example page and change the Listen Port.

```
- hosts: all
  roles:
    - role: while_true_do.srv_httpd
      wtd_srv_httpd_conf:
        Listen: "8080"
      wtd_srv_httpd_example: true
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_httpd/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_httpd/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
