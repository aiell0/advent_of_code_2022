
def inspect(packet: str, chars: int) -> tuple[bool, int]:
    for i in range(len(packet)):
        sliced_line = packet[i:i+chars]
        set_sliced_line = set(sliced_line)
        if len(sliced_line) == len(set_sliced_line):
            return True, i + chars

    return False, 0


with open("input.txt", "r") as file:
    packet = file.readline().strip()
    start_of_packet = inspect(packet, 4)
    start_of_message = inspect(packet, 14)

    if start_of_packet[0]:
        print("start of packet: ", start_of_packet[1])
    else:
        print("start of packet not found")

    if start_of_message[0]:
        print("start of message: ", start_of_message[1])
    else:
        print("start of message not found")
