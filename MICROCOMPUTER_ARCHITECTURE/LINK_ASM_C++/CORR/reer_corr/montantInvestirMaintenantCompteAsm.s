# Approche possible
# Auteurs: 2052202 & 2148153
.data
OFFSET:
    .int 861
.text
.globl _ZN6Compte29montantAInvestirMaintenantAsmEv
_ZN6Compte29montantAInvestirMaintenantAsmEv:
pushl %ebp
movl %esp, %ebp
pushl %esi
pushl 8(%ebp)
call _ZN4Reer15salaireFinalAsmEv
popl %esi
movl 24(%esi), %ecx
movl $104, %ebx
divpow:
    movl $0, %edx
    idiv %ebx
    imul $100,%eax
    loop divpow
subl 28(%esi), %eax
negl %eax
popl %esi
subl OFFSET, %eax
retour:
leave
ret
