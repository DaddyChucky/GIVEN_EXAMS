# Approche possible
# Auteurs: 1985949 & 2144722
.data
CUTOFF: 
.int 2
.text
.globl quicksort_s
quicksort_s:
pushl %ebp
movl %esp, %ebp
pushl %ebx
movl 8(%ebp), %esi      # pointeur T
movl 12(%ebp), %ebx     # left
movl 16(%ebp), %ecx     # right
movl %ebx, %edx
movl %ecx, %edi
IF:
addl CUTOFF, %ebx
cmpl %ebx, %ecx
jbe fin
movl %edx, %ebx         # left (deep)
pushl %ecx
pushl %ebx
pushl %esi
call medianOfThree 
popl %esi
popl %ebx
popl %ecx
movl %edi, %ecx         # right (deep)
subl $1, %ecx           # right - 1
b1:
    addl $1, %ebx
    cmpl %eax, %esi     # %eax = pivot
    jbe b1
b2:
    subl $2, %ecx                 
    cmpl %eax, %esi     # %eax = pivot
    jbe b2
    cmpl %ecx, %ebx
    jae alt
    pushl %eax 
    pushl %ecx 
    pushl %ebx 
    pushl %esi 
    call swapRefs 
    popl %esi
    popl %ebx
    popl %ecx
    popl %eax
    jmp  b1
alt:
    movl %edi, %ecx     # right (deep)
    sub $1, %ecx
    pushl %ecx          # right - 1
    pushl %ebx
    pushl %eax  
    push %esi   
    call swapRefs 
    popl %esi
    popl %eax
    popl %ebx
    popl %ecx
    subl $1, %eax
    pushl %eax   
    pushl %ebx
    pushl %ecx
    pushl %esi
    call quicksort 
    popl %esi
    popl %ecx
    popl %ebx
    popl %eax
    movl %edi, %ecx     # right (deep)
    addl $1, %eax
    pushl %ecx          # right - 1
    pushl %eax
    pushl %esi
    call quicksort    
    popl %esi
    popl %eax
    popl %ecx
fin:
popl %ebx
leave
ret
