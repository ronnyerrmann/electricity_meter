import subprocess


def execute(cmd):
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # process.wait()      # only needed if subprocess.Popen

    return process
