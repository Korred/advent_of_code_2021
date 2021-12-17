def hexstr_to_binstr(hex):
    return f"{int(hex, 16):0>{len(hex)*4}b}"


def decode_packet(packet):

    # cosume packet version
    p_version = int(packet[:3], 2)
    p_version_sum = p_version
    packet = packet[3:]

    # consume packet type
    p_type = int(packet[:3], 2)
    packet = packet[3:]

    # literal value packet
    if p_type == 4:
        groups = []
        while True:
            # consume literal value group
            group = packet[1:5]
            num = packet[0]
            groups.append(group)
            packet = packet[5:]

            # last group - stop parsing
            if num == "0":
                break

        p_val = int("".join(groups), 2)
        return {"remaining": packet, "value": p_val, "version_sum": p_version_sum}

    # operator packet
    else:
        # consume operator id
        p_id = packet[0]
        packet = packet[1:]

        subpacket_vals = []

        if p_id == "0":
            # consume subpack length information
            p_total_length = int(packet[:15], 2)
            packet = packet[15:]

            # consume subpackages
            subpackets = packet[:p_total_length]
            while subpackets:
                res = decode_packet(subpackets)
                subpackets = res["remaining"]
                subpacket_vals.append(res["value"])
                p_version_sum += res["version_sum"]

            packet = packet[p_total_length:]

        else:
            # consume subpackages num
            p_subpack_num = int(packet[:11], 2)
            packet = packet[11:]

            # consume subpackages
            for _ in range(p_subpack_num):
                res = decode_packet(packet)
                packet = res["remaining"]
                subpacket_vals.append(res["value"])
                p_version_sum += res["version_sum"]

        return {"remaining": packet, "value": 0, "version_sum": p_version_sum}


bin_packet = hexstr_to_binstr(open("input.txt", "r").readline())
print(decode_packet(bin_packet))

