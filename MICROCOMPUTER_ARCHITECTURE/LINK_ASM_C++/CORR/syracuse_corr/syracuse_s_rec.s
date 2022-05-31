# Approche possible
# Auteurs: 2061595 & 2132752
.text
.globl syracuse_s_rec
.globl afficher
syracuse_s_rec:
pushl  %ebp
movl   %esp, %ebp
pushl %ebx
movl 8(%ebp), %eax
movl 12(%ebp), %ecx
pushl %eax
pushl %ecx
call afficher
popl %ecx
popl %eax
boucle: 
    cmpl $1, %eax
    je retour
    incl %ecx
    movl $2, %ebx
    pushl %eax
    movl $0, %edx
    divl %ebx
    cmpl $0, %edx
    je paire 
impaire:
    movl $3, %ebx
    popl %eax
    mull %ebx
    incl %eax
    pushl %ecx
    pushl %eax
    call syracuse_s_rec
    popl %eax
    popl %ecx 
    jmp retour
paire:
    popl %eax
    movl $0, %edx
    div %ebx
    pushl %ecx
    pushl %eax
    call syracuse_s_rec
    popl %eax
    popl %ecx 
retour:   
popl %ebx
leave
ret
