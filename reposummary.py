#!/usr/bin/python
# USAGE: reposummary.py /path/to/yum.repos.d > vars/myvars.yml
import glob
import sys
import os.path
import ConfigParser

import yaml

class RepoList:
    def __init__(self):
        self._repos = []
        self._prefix = None

    def add_file(self, filename):
        base_name = os.path.basename(filename)

        ini = ConfigParser.ConfigParser()
        ini.read(filename)

        for repoid in ini.sections():
            repo = {}
            repo['name'] = repoid
            repo['file'] = base_name

            baseurls = ini.get(repoid, 'baseurl').split('\n')
            baseurls.sort()
            repo['uri'] = baseurls[0]
            self._repos.append(repo)

    def __str__(self):
        if self._prefix is None:
            self._find_prefix()
            sys.stderr.write(self._prefix + '\n')

        return yaml.dump({'pkgmgr_repos': self._repos}, default_flow_style = False)

    def _find_prefix(self):
        prefix = None
        for repo in self._repos:
            uri = repo['uri'].split('/')
            if prefix is None:
                prefix = uri
            else:
                for i in range(0, min(len(prefix), len(uri)) - 1):
                    if prefix[i] != uri[i] or '$' in uri[i]:
                        del prefix[i:]
                        break

        self._prefix = '/'.join(prefix)
        start = len(self._prefix)

        for repo in self._repos:
            repo['uri'] = repo['uri'][start:]

repo_list = RepoList()

for repo_filename in glob.glob(os.path.join(sys.argv[1], '*.repo')):
    repo_list.add_file(repo_filename)

print '---\n' + str(repo_list)[:-1]
