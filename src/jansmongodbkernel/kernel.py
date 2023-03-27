#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

mongodbwrapper = replwrap.REPLWrapper("mongosh --quiet", "mongosh>>> ", None)

not_allowed = ["quit","exit"]

class jansmongodbkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.11.0'
    language = 'mongodb'
    language_version = '6.0.4'
    language_info = {
        'name': 'mongodb',
        'mimetype': 'application/json',
        'file_extension': '.json',
    }
    banner = "MongoDB - The Developer Data Platform"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            if code[0:4] in not_allowed:
                solution = f'"{code}" is not allowed in the mongodb kernel'
            else:
                code = code.replace("\n"," ")
                solution = mongodbwrapper.run_command(code)
                while "\n" not in solution:
                    mongodbwrapper._expect_prompt()
                    solution = mongodbwrapper.child.before
                solution = solution[solution.index("\n")+1:]
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
