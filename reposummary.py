#!/usr/bin/python
import glob
import sys
import os.path
import ConfigParser

import yaml

class RepoList:
    def __init__(self):
        self._files = {}

    def add_file(self, filename):
        base_name = os.path.basename(filename)[:-5]
        self._files[base_name] = {}

        ini = ConfigParser.ConfigParser()
        ini.read(filename)

        for repoid in ini.sections():
            self._files[base_name][repoid] = {}
            repo = self._files[base_name][repoid]

            repo['name'] = ini.get(repoid, 'name')

            baseurls = ini.get(repoid, 'baseurl').split('\n')
            baseurls.sort()
            repo['baseurl'] = baseurls[0]

            try:
                if ini.getboolean(repoid, 'enabled'):
                    enabled = 1
                else:
                    enabled = 0
            except ConfigParser.NoOptionError as err:
                enabled = 1
            repo['enabled'] = enabled

    def __str__(self):
        return yaml.dump(self._files, default_flow_style = False)

repo_list = RepoList()

for repo_filename in glob.glob(os.path.join(sys.argv[1], '*.repo')):
    repo_list.add_file(repo_filename)

print repo_list
