# Approche possible
# Auteurs: 2061595 & 2132752
.text
.globl syracuse_s_iter
.globl afficher
syracuse_s_iter:
pushl %ebp
movl %esp, %ebp
pushl %ebx
movl 8(%ebp), %eax
movl $0, %ecx
boucle:
    pushl %eax
    pushl %ecx
    call afficher
    popl %ecx
    popl %eax
    cmpl $1, %eax
    je retour
    incl %ecx
    movl $2, %ebx
    pushl %eax
    movl $0, %edx
    divl %ebx
    cmpl $0, %edx
    je pair 
impair:
    movl $3, %ebx
    popl %eax
    mull %ebx
    incl %eax
    jmp boucle
pair:
    popl %eax
    movl $0, %edx
    divl %ebx
    jmp boucle
retour:   
popl %ebx
leave
ret
