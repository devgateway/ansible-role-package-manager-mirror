# Package Manager Mirror

Configure a mirror of standard repositories for APT, YUM, and DNF. Useful if you have a caching proxy and want to ensure cache hits.

Role Variables
--------------

### `pkgmgr_proxy`

If defined, the role will configure the package manager to use this URL as a proxy.

### `pkgmgr_mirror`

A dictionary of repository settings with distribution names as keys. Values are different for different distributions.

#### Debian-like

Values are dictionaries in which either *default* key or the specific release name key must be present. The release name is taken from Ansible fact `ansible_lsb.codename`, and defaults to `ansible_distribution_release` if it's not set (varies by release).

Values are dictionaries where *url* member is the base URL (one level **above** subdirectories like *dists* and *pool*, see example below), and *components* member is a list of distribution components, such as *main*, *contrib*, or *non-free*.

#### RH-like

Values are base URLs (see example below). They should be one level **above** the following subdirectories:

* major release numbers in CentOS and Scientific
* *releases* in Fedora

### `pkgmgr_restore_enabled`

Whether to restore the enabled/disabled status as defined in original (from the RPM) repo configuration. Default is *true*.

Example Playbook
----------------

    ---
    - hosts: all
      roles:
        - role: package-manager-mirror
          pkgmgr_proxy: http://proxy.example.net:3128
          pkgmgr_mirror:
            Debian: 
              default:
                url: http://ftp.us.debian.org/debian/
                components:
                  - main
                  - contrib
              sid:
                components:
                  - main
                  - non-free
                  - contrib
            CentOS:
              default: http://mirror.centos.org/centos
            Scientific:
              default: http://ftp.scientificlinux.org/linux/scientific
            Fedora:
              default: http://download.fedoraproject.org/pub/fedora/linux
              v24: http://archives.fedoraproject.org/pub/archive/fedora/linux

License
-------

GPLv3+

Author Information
------------------

Copyright 2018, Development Gateway
