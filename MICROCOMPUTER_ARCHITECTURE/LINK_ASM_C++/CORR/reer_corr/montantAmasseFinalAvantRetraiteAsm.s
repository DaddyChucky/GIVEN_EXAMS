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
idiv %ebx # eax = ๐ ๐๐๐๐๐๐๐๐๐ก๐๐๐๐ก๐
movl 20(%esi), %ebx
movl $0, %edx
idiv %ebx
movl $100, %ebx
imul %ebx,%eax
pushl %eax # eax = ๐ ๐๐๐๐๐๐๐๐๐ก๐๐๐๐ก๐/%๐๐๐กรฉ๐รช๐ก
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
