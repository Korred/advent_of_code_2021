integer = "D2FE28"
bin_rep = f'{int(integer, 16):0>{len(integer)*4}b}'

p_version = int(bin_rep[0:3].zfill(4), 2)
p_type = int(bin_rep[3:6].zfill(4), 2)

print(p_version, p_type)

# literal value packet
if p_type == 4:
    groups = []
    pos = 6
    while True:
        group = bin_rep[pos:pos+5]
        print(group)
        groups.append(group[1:])
        # last group - stop parsing
        if group[0] == "0":
            break
        
        pos += 5
            
    p_val = int("".join(groups), 2)
    
    
# operator packet
else:
    pass


print(p_val)
    