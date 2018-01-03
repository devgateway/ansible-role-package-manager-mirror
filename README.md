# Package Manager Mirror

Configure a mirror of standard repositories for APT, YUM, and DNF. Useful if you have a caching proxy and want to ensure cache hits.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Example Playbook
----------------

    ---
    - hosts: all
      roles:
        - role: package-manager-mirror
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
              v7: http://mirror.centos.org/centos
            Scientific:
              default: http://ftp.scientificlinux.org/linux/scientific
              v6: http://ftp.scientificlinux.org/linux/scientific

License
-------

GPLv3+

Author Information
------------------

Copyright 2018, Development Gateway
