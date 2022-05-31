.text
iteration:
ld a
brz fin
sub weight
st a
ld p
brnz sub_p
add_p:
add weight
st p
br iteration
sub_p:
sub weight
st p
br iteration
fin:
ld p
st res
stop
.data
a:65535
res:0
weight:1
p:0