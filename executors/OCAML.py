import os
import re
import subprocess

from cptbox import CHROOTSecurity, SecurePopen, PIPE, ALLOW
from cptbox.syscalls import *
from error import CompileError
from .utils import test_executor
from .resource_proxy import ResourceProxy
from judgeenv import env

OCAML_FS = ['.*\.so']


class Executor(ResourceProxy):
    def __init__(self, problem_id, source_code):
        super(Executor, self).__init__()
        source_code_file = self._file('%s.ml' % problem_id)
        self.name = self._file(problem_id)
        with open(source_code_file, 'wb') as fo:
            fo.write(source_code)
        ghc_args = [env['runtime']['ocaml'], source_code_file, '-o', problem_id]
        ghc_process = subprocess.Popen(ghc_args, stderr=subprocess.PIPE, cwd=self._dir)
        _, compile_error = ghc_process.communicate()
        if ghc_process.returncode != 0:
            raise CompileError(compile_error)

    def _get_security(self):
        sec = CHROOTSecurity(GO_FS)

        sec[sys_getpid] = ALLOW
        sec[sys_getppid] = ALLOW
        sec[sys_clock_getres] = ALLOW
        sec[sys_timer_create] = ALLOW
        sec[sys_timer_settime] = ALLOW
        sec[sys_timer_delete] = ALLOW
        sec[sys_modify_ldt] = ALLOW

        return sec

    def launch(self, *args, **kwargs):
        return SecurePopen([self.name] + list(args),
                           executable=self.name,
                           security=CHROOTSecurity(OCAML_FS),
                           address_grace=131072,
                           time=kwargs.get('time'),
                           memory=kwargs.get('memory'),
                           stderr=(PIPE if kwargs.get('pipe_stderr', False) else None),
                           env={}, cwd=self._dir, nproc=-1)

    def launch_unsafe(self, *args, **kwargs):
        return subprocess.Popen([self.name] + list(args),
                                executable=self.name,
                                env={},
                                cwd=self._dir,
                                **kwargs)


def initialize():
    if 'ocaml' not in env['runtime']:
        return False
    if not os.path.isfile(env['runtime']['ocaml']):
        return False
    return test_executor('OCAML', Executor, '''\
print_endline "Hello, World!"
''')