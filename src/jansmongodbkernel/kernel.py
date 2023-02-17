#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

mongodbwrapper = replwrap.REPLWrapper("mongosh --quiet", "> ", None, "... ")

def rmlines(solution,loc_printout):
    ret_val = ""
    solution = solution.split("\n")
    for i in range(1,len(solution)):
        if i != len(solution)-1:
            ret_val = ret_val + solution[i] + "\n"
        elif loc_printout:
            ret_val = ret_val + "\n<<You are in db: " + solution[i] + ">>"
    return ret_val

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
            if (code[0:4] == "quit") or (code[0:4] == "exit"):
                solution = f'"{code}" is now allowed in the mongodb kernel'
            else:
                code = code.replace("\n"," ")
                solution = mongodbwrapper.run_command(code)
                if "SyntaxError" in solution:
                    mongodbwrapper._expect_prompt()
                    solution = rmlines(solution, False)
                else:
                    solution = rmlines(solution, True)
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
