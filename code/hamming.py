# Hamming code (even parity): each ASCII char = 8 data bits -> 12-bit codeword
R = [1, 2, 4, 8]                      # parity bit positions (powers of 2)

def encode(byte):
    data = format(byte, "08b")
    code = [0] * 13                   # index 1..12 used
    j = 0
    for pos in range(1, 13):
        if pos not in R:
            code[pos] = int(data[j]); j += 1
    for p in R:                       # parity p covers positions having bit p set
        code[p] = sum(code[i] for i in range(1, 13) if i & p and i != p) % 2
    return "".join(map(str, code[1:]))

def decode(word):
    code = [0] + [int(b) for b in word]
    err = sum(p for p in R if sum(code[i] for i in range(1, 13) if i & p) % 2)
    if err:                           # syndrome = position of the wrong bit
        print("  error at position", err, "-> corrected")
        code[err] ^= 1
    return int("".join(str(code[i]) for i in range(1, 13) if i not in R), 2)

if __name__ == "__main__":
    text = input("Enter text: ")
    sent = [encode(ord(c)) for c in text]
    print("Sent    :", " ".join(sent))
    # SENDER writes to channel file; RECEIVER reads it back
    open("channel.txt", "w").write(" ".join(sent))
    recv = open("channel.txt").read().split()
    if input("Induce an error? (y/n): ").lower() == "y":
        w = list(recv[0]); w[4] = "1" if w[4] == "0" else "0"; recv[0] = "".join(w)
        print("Received:", " ".join(recv), "(bit 5 of 1st char flipped)")
    print("Decoded :", "".join(chr(decode(w)) for w in recv))
