#!/usr/bin/python
import glob
import sys
import os.path
import ConfigParser

import yaml

class RepoList:
    def __init__(self):
        self._repos = {}
        self._baseurls = set()

    def add_file(self, filename):
        base_name = os.path.basename(filename)

        ini = ConfigParser.ConfigParser()
        ini.read(filename)

        for repoid in ini.sections():
            self._repos[repoid] = {'file': base_name}

            baseurls = ini.get(repoid, 'baseurl').split('\n')
            baseurls.sort()
            self._repos[repoid]['baseurl'] = baseurls[0]
            self._baseurls.add(baseurls[0].split('/'))

    def __str__(self):
        return yaml.dump(self._repos, default_flow_style = False)

    def find_prefix(self):
        for i in range(0, len(self._baseurls[0]) - 1):
            pass

repo_list = RepoList()

for repo_filename in glob.glob(os.path.join(sys.argv[1], '*.repo')):
    repo_list.add_file(repo_filename)

print repo_list
