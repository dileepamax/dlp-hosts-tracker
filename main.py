from host import Host


def print_hi(name):
    print(f'Hi, {name}')
    h1 = Host('192.168.100.100', 26, 'user_name-1', 0)
    h2 = Host('192.168.100.101', 26, 'user_name-2', 0)
    h3 = Host('192.168.100.102', 26, 'user_name-3', 0)
    h4 = Host('192.168.100.103', 26, 'user_name-4', 0)
    h5 = Host('192.168.100.104', 26, 'user_name-5', 0)
    h6 = Host('192.168.100.105', 26, 'user_name-6', 0)
    h7 = Host('192.168.100.106', 26, 'user_name-7', 0)
    h8 = Host('192.168.100.107', 26, 'user_name-8', 0)
    h9 = Host('192.168.100.108', 26, 'user_name-9', 0)
    h10 = Host('192.168.100.109', 26, 'user_name-10', 0)
    h11 = Host('192.168.100.110', 26, 'user_name-11', 0)
    h12 = Host('192.168.100.111', 26, 'user_name-12', 0)
    h13 = Host('192.168.100.112', 26, 'user_name-13', 0)
    h14 = Host('192.168.100.112', 26, 'user_name-14', 0)
    print(h1.ip_address)
    print(h2)
    print(h3)
    print(h4)
    print(h5)
    print(h6)
    print(h7)
    print(h8)
    print(h9)
    print(h10)
    print(h11)
    print(h12)
    print(h13)
    print(h14)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
