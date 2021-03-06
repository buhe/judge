from .base_executor import CompiledExecutor
from judgeenv import env


class Executor(CompiledExecutor):
    ext = '.t'
    name = 'TUR'
    fs = ['.*\.(?:so|tbc$)']
    command = env['runtime'].get('tprologc')
    syscalls = ['getpid']
    test_program = '''\
var turing_sucks : string
get turing_sucks : *
put turing_sucks
'''

    def get_compile_args(self):
        return [self.get_command(), self._code, env['runtime']['turing_dir']]

    def get_cmdline(self):
        return [env['runtime']['tprolog'], self._code + 'bc']

    def get_executable(self):
        return None

    @classmethod
    def initialize(cls):
        if 'tprolog' not in env['runtime'] or 'tprologc' not in env['runtime'] or 'turing_dir' not in env['runtime']:
            return False
        return super(Executor, cls).initialize()

initialize = Executor.initialize