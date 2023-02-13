#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

mongodbwrapper = replwrap.REPLWrapper("mongosh --quiet", "> ", None)

def rmlines(solution):
    ret_val = ""
    solution = solution.split("\n")
    for i in range(1,len(solution)-1):
        ret_val = ret_val + solution[i] + "\n"
    return(ret_val)

class jansmongodbkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
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
            if ("quit" in code) or ("exit" in code):
                solution = f'"{code}" is now allowed in the mongodb kernel'
            else:
                solution = mongodbwrapper.run_command(code)
                solution = rmlines(solution)
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
