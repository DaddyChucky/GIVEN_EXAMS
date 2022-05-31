.text
ld data
st data_tmp
get_length:
brz deep_copy
shr
st data_tmp
ld len
add adder
st len
ld data_tmp
br get_length
deep_copy:
ld len
st len_tmp
ld data
st data_tmp
shift_l:
ld len
sub adder
brz shift_r
st len
ld data_tmp
shl
st data_tmp
br shift_l
shift_r:
ld len_tmp
sub adder
brz fin
st len_tmp
ld data_tmp
shr
st data_tmp
br shift_r
fin:
ld data_tmp
sub adder
brz alt
stop
alt:
add adder
st res
stop
.data
data:65535
data_tmp:0
len:0
len_tmp:0
adder:1
res:0