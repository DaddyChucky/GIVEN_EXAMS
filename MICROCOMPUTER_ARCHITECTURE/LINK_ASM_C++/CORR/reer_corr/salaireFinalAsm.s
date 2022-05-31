# Approche possible
# Auteurs: 2052202 & 2148153
.data
OFFSET:
    .int 29
.data
.text
.globl _ZN4Reer15salaireFinalAsmEv
_ZN4Reer15salaireFinalAsmEv:
pushl %ebp
movl %esp, %ebp
pushl %ebx
pushl %esi
movl 8(%ebp), %esi
movl 24(%esi), %ecx
subl $1, %ecx
movl 8(%esi), %eax
movl 12(%esi),%ebx
addl $100, %ebx
mulpow:
    imul %ebx,%eax
    pushl %ebx
    movl $0, %edx
    movl $100, %ebx
    idiv %ebx
    popl %ebx
    loop mulpow
popl %esi
popl %ebx
addl OFFSET, %eax
retour:
leave
ret
