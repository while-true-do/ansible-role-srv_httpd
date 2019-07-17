# Some examples are given below.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_httpd_package(host):
    pkg = host.package('httpd')

    assert pkg.is_installed


def test_mod_ssl_package(host):
    pkg = host.package('httpd')

    assert pkg.is_installed


def test_mod_security_package(host):
    pkg = host.package('httpd')

    assert pkg.is_installed


def test_httpd_service(host):
    srv = host.service('httpd')

    assert srv.is_running
    assert srv.is_enabled


def test_http_socket(host):
    sock = host.socket('tcp://80')

    with host.sudo():
        assert sock.is_listening


def test_https_socket(host):
    sock = host.socket('tcp://443')

    with host.sudo():
        assert sock.is_listening
