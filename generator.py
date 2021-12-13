import os


def generatePattern(length: int) -> str:
    payload = os.popen(f"/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l {length}").read()
    return payload.replace('\n', '')


def findPatternOffset(length: int, lookfor: str) -> int:
    output = os.popen(f"/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l {length} -q {lookfor}").read()
    return int(output.split(" ")[-1])
