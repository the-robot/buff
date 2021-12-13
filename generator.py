import os


def generatePattern(length: int) -> str:
    payload = os.popen(f"/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l {length}").read()
    return payload.replace('\n', '')
