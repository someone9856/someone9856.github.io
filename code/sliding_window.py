# Sliding window (Go-Back-N) simulation - 1 character per frame
msg = input("Enter message: ")
w = int(input("Enter window size: "))
bad = input("Frame number to damage once (blank = none): ")
bad = int(bad) if bad else -1

base = 0                              # oldest un-acknowledged frame
while base < len(msg):
    top = min(base + w, len(msg))
    print(f"\nSender window [{base}..{top - 1}]")
    expected = base
    for n in range(base, top):
        print(f"  Send  frame {n} : DATA='{msg[n]}'")
        if n == bad:                  # receiver gets a damaged frame
            bad = -1
            print(f"  Recv  frame {n} : ERROR -> NACK {n}")
            break
        print(f"  Recv  frame {n} : OK    -> ACK {n}")
        expected = n + 1
    if expected < top:
        print(f"  Go-Back-N: resend from frame {expected}")
    base = expected
print("\nAll frames delivered:", msg)
