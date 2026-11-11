import json
import time
import shlex
from network import User
from data  import Packet

# ==== CONSTANTS ====
DELAY = 1
DOTS  = 3

def start(name):
    for d in range(1, DOTS + 1):
        print(f"\r\033[Kstarting {name} {'.' * d}", end="", flush=True)
        time.sleep(DELAY)

    print(f"\r\033[K{name} has started!")

def cli(name):
    status = "disconnected"
    ip = "0.0.0.0"
    
    banner = f"""
\033[36m _   ___   ___  __
| \\ | \\ \\ / / \\/ /
|  \\| |\\ V / \\  /
| |\\  | | |  /  \\
|_| \\_| |_| /_/\\_\\\033[0m
  nyx v0.1 | status: {status}
  commands: ip, exit
"""
    print(banner)

    error_code = 0

    while error_code == 0:
        command = input(f"\033[32m{name}\033[0m \033[34m* >>\033[0m ")

        words = command.split(" ", maxsplit=1)
        arg   = words[0]

        if arg == "exit":
            print("\033[33mexitting nyx gracefully!!!!\033[0m")
            error_code = 1

        if arg == "ip":
            if status == "disconnected":
                print(f"{name} is NOT connected to any network!")

            else:
                print(f"{ip}")

        if arg == "connect":
            foo = words[1].split(", ")
            device = User()
            device_ip = device.issue_ip(name, foo[0], foo[1])
            status = "connected"
            ip = device_ip

            print(f"{name} connected to interent, ISP {foo[0]}, IP {device_ip}")

        if arg == "send":
            try:
                parts = shlex.split(words[1])
                assert parts[1] == "to"
                data, dest = parts[0], parts[2]
            except (IndexError, AssertionError):
                print('usage: send "data" to username')
                continue

            if status != "connected":
                print(f"{name} is NOT connected to any network!")
                continue

            dest_ip = None
            with open("network/ips/users_ips.json") as f:
                for line in f:
                    if line.strip():
                        r = json.loads(line)
                        if r["name"] == dest:
                            dest_ip = r["ip"]

            if dest_ip is None:
                print(f"{dest}: user not found")
            else:
                for d in range(1, DOTS + 1):
                    print(f"\r\033[Ksending to {dest} {'.' * d}", end="", flush=True)
                    time.sleep(0.5)
                print("\r\033[K", end="")
                packet = Packet(data).send_packet(ip, dest_ip)
                print(f"data sent to {dest}({dest_ip})")
                print(f"\033[36m{packet}\033[0m")
