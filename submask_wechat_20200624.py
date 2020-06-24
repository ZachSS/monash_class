"""
/--author: Zachary Shi--/
/--version: 20200624---/
"""


def convert(arg):  # / to 255
    if arg <= 32:
        binary = ''
        while arg:
            binary += '1'
            arg -= 1
        while len(binary) <= 32:
            binary += '0'
        res = ''
        for i in range(8, 33, 8):
            res += str(int(binary[i - 8:i], 2))
            res += '.'
        return res[:-1]


def addr_to_b(addr):
    arr = addr.split('.')
    res = ''
    for i in range(0, 4):
        binary = bin(int(arr[i]))[2:]
        while len(binary) < 8:
            binary = '0' + binary
        res += binary
        res += '.'
    return res[:-1]


def identify_address(addr):
    first8 = addr.split('.')[0]
    if 0 <= int(first8) <= 126:
        return 'A'
    elif 128 <= int(first8) <= 191:
        return 'B'
    elif 192 <= int(first8) <= 223:
        return 'C'


def test1(addr, mask):
    """
    given one host address and subnet mask. request subnet and broadcast
    """
    addr_b = addr_to_b(addr)
    mask_b = addr_to_b(mask)
    temp_b = ''
    res_d_s = ''
    res_d_b = ''
    first_host_d = ''
    last_host_d = ''
    for i in range(len(addr_b)):
        if mask_b[i] == '1':
            temp_b += addr_b[i]
    res_b_s = temp_b
    res_b_b = temp_b
    first_host_b = temp_b
    last_host_b = temp_b
    while len(res_b_s) < 32:
        res_b_s += '0'
        res_b_b += '1'
    while len(first_host_b) < 31:
        first_host_b += '0'
        last_host_b += '1'
    first_host_b += '1'
    last_host_b += '0'
    for j in range(8, 33, 8):
        res_d_s += str(int(res_b_s[j - 8:j], 2))
        res_d_s += '.'
        res_d_b += str(int(res_b_b[j - 8:j], 2))
        res_d_b += '.'
        first_host_d += str(int(first_host_b[j - 8:j], 2))
        first_host_d += '.'
        last_host_d += str(int(last_host_b[j - 8:j], 2))
        last_host_d += '.'

    print(f'subnet: {res_d_s[:-1]}')
    print(f'broadcast: {res_d_b[:-1]}')
    print(f'host: {first_host_d[:-1]} through to {last_host_d[:-1]}')


def test2(addr, mask):
    """
    given network address and mask. request the number of subnets and hosts
    """
    network_type = identify_address(addr)
    mask_b = addr_to_b(mask)
    count_1 = 0
    count_0 = 0
    std = {'A': 9, 'B': 18, 'C': 27}
    for i in mask_b[std[network_type]:]:
        if i == '1':
            count_1 += 1
        if i == '0':
            count_0 += 1
    print(f'the number of subnets of this network: {2 ** count_1}')
    print(f'the number of valid hosts per subnet: {2 ** count_0 - 2}')


def test1_intmask(addr_mask):
    addr = addr_mask.split('/')[0]
    intmask = int(addr_mask.split('/')[1])
    mask = convert(intmask)
    test1(addr, mask)


def test2_intmask(addr_mask):
    addr = addr_mask.split('/')[0]
    intmask = int(addr_mask.split('/')[1])
    mask = convert(intmask)
    test2(addr, mask)


if __name__ == '__main__':
    while 1:
        print('given one host address and subnet mask. request subnet, broadcast, host range. please enter 1: ')
        print('given network address and mask. request the number of subnet and hosts. please enter 2: ')
        print('quit. please enter 3: ')
        try:
            choice1 = input()
            if choice1 == '1':
                print('if the format is - address: 192.168.0.1 , mask: 255.255.255.0. please enter 1: ')
                print('if the format is - address: 192.168.0.1/24. please enter 2: ')
                choice2 = input()
                if choice2 == '1':
                    addr = input('please enter the address (192.168.0.0): ')
                    mask = input('please enter the mask (255.255.255.0): ')
                    test1(addr, mask)
                if choice2 == '2':
                    addr_mask = input('please enter the address (192.168.0.0/24): ')
                    test1_intmask(addr_mask)
            elif choice1 == '2':
                print('if the format is - address: 192.168.0.1 , mask: 255.255.255.0. please enter 1: ')
                print('if the format is - address: 192.168.0.1/24. please enter 2: ')
                choice2 = input()
                if choice2 == '1':
                    addr = input('please enter the address (192.168.0.0): ')
                    mask = input('please enter the mask (255.255.255.0): ')
                    test2(addr, mask)
                if choice2 == '2':
                    addr_mask = input('please enter the address (192.168.0.0/24): ')
                    test2_intmask(addr_mask)
            elif choice1 == '3':
                break
        except:
            print('something wrong')
            continue
