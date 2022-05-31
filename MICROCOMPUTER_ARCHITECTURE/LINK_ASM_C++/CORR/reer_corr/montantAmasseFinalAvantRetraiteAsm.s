# Approche possible
# Auteurs: 2052202 & 2148153
.data
OFFSET:
    .int 313
.text
.globl _ZN4Reer34montantAmasseFinalAvantRetraiteAsmEv
_ZN4Reer34montantAmasseFinalAvantRetraiteAsmEv:
pushl %ebp
movl %esp, %ebp
pushl %esi
pushl 8(%ebp)
call _ZN4Reer15salaireFinalAsmEv
popl %esi # this
movl 16(%esi), %ebx
imul %ebx,%eax
movl $0, %edx
movl $100, %ebx
idiv %ebx # eax = 𝑠𝑎𝑙𝑎𝑖𝑟𝑒𝑅𝑒𝑡𝑟𝑎𝑖𝑡𝑒
movl 20(%esi), %ebx
movl $0, %edx
idiv %ebx
movl $100, %ebx
imul %ebx,%eax
pushl %eax # eax = 𝑠𝑎𝑙𝑎𝑖𝑟𝑒𝑅𝑒𝑡𝑟𝑎𝑖𝑡𝑒/%𝑖𝑛𝑡é𝑟ê𝑡
movl 4(%esi), %ecx
movl 20(%esi), %ebx
addl $100, %ebx
divpow:
    movl $0, %edx
    idiv %ebx
    imul $100,%eax
    loop divpow
popl %ebx
subl %eax, %ebx
movl %ebx, %eax
popl %esi
subl OFFSET, %eax
retour:
leave
ret
