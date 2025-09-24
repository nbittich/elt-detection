import time

def banner():
    print("*"*50)
    print("\nWELCOME\n")
    print("*"*50)


def backdoor():
    print("ACCES AU SYSTEME EN COURS")
    for i in range(100):
        print(f"Infection en cours : {i} %")
        time.sleep(0.1)



if __name__ == "__main__":
    banner()
    time.sleep(3)
    backdoor()
