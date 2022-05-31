# Approche possible
# Auteurs: 2052202 & 2148153
.data
OFFSET:
    .int 834
.text
.globl	_ZN4Reer30montantAEpargnerChaqueAnneeAsmEv
_ZN4Reer30montantAEpargnerChaqueAnneeAsmEv:
pushl %ebp
movl %esp, %ebp
pushl %esi
pushl 8(%ebp)
call _ZN4Reer34montantAmasseFinalAvantRetraiteAsmEv
popl %esi # this
movl 20(%esi), %ebx
imul %ebx,%eax
movl $100, %ebx
movl $0, %edx
idiv %ebx
# eax = 
pushl %eax # 𝑚𝑜𝑛𝑡𝑎𝑛𝑡𝐴𝑐𝑐𝑢𝑚𝑢𝑙𝑒𝑟 * % 𝑖𝑛𝑡é𝑟ê𝑡
movl $10000, %eax
movl 24(%esi), %ecx
movl 20(%esi), %ebx
addl $100, %ebx
mulpow:
    imul %ebx,%eax
    push %ebx
    movl $0, %edx
    movl $100, %ebx
    idiv %ebx
    pop %ebx
    loop mulpow
subl $10000, %eax
movl $10000, %ebx
movl $0, %edx
idiv %ebx
movl %eax, %ebx
popl %eax
movl $0, %edx
idiv %ebx
popl %esi
subl OFFSET, %eax
retour:
leave
ret
