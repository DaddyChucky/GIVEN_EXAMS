.text
.globl syracuse_s_rec
.globl afficher
syracuse_s_rec:
pushl  %ebp
movl   %esp, %ebp
pushl %ebx
# DEBUT COMPLETION

# FIN COMPLETION
# NE RIEN MODIFIER APRES CETTE LIGNE
retour:   
popl %ebx
leave
ret
