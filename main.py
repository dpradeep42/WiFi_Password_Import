import subprocess


def getpasswords():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    conn = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    for i in conn:
        accounts = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8').split('\n')
        accounts = [b.split(":")[1][1:-1] for b in accounts if "Key Content" in b]
        #print("{:<30}| {:<}".format(i, accounts[0]))
        try:
            print("{:<30}| {:<}".format(i, accounts[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))


if __name__ == '__main__':
    getpasswords()