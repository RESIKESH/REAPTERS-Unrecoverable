# Secure Coding Unrecoverable solution by Resikeh MR
# Author: Resikesh M R
# Enter the file path and it will remove the file 


from os import remove, urandom, path
import ctypes
import sys


def write_nulls(file_ptr, file_size):
    try:
        file_ptr.write(b"\x00"*file_size)
    except Exception as e:
        print(f"[-] Cannot write nulls to the file due to error - {e}")


def write_ones(file_ptr, file_size):
    try:
        file_ptr.write(b"\x01"*file_size)
    except Exception as e:
        print(f"[-] Cannot write ones to the file due to error - {e}")


def write_random(file_ptr, file_size):
    try:
        file_ptr.write(urandom(file_size))
    except Exception as e:
        print(f"[-] Cannot write randoms to the file due to error - {e}")
    
def remove_file(file_path):
    try:
        remove(file_path)
    except Exception as e:
        print(f"[-] Cannot remove file due to error - {e}")


def check_file(file_path):
    return path.exists(file_path)


def driver(passes):
    print(f"[+] Number of passes {passes}")

    file_path = input("[+] Enter full path to the file you want to delete - ").strip()

    if check_file(file_path):

        if input("[+] Are you sure you want to remove the file? .(y/N)").lower() != 'y':
            return
        else:
            chk_2 = input(f"Type in '{file_path}' to delete the file - ")
            if chk_2 != file_path:
                print("[-] Incorrect input. Aborting.")
                return
            else:
                file_ptr = open(file_path, "wb")
                file_size = path.getsize(file_path)

                print("[+] Removing file.")
                for i in range(passes):
                    print(f"\t[+] Pass: {i}")
                    print(f"\t\t[+] Writing Nulls")
                    write_nulls(file_ptr, file_size)
                    print(f"\t\t[+] Writing ones")
                    write_ones(file_ptr, file_size)
                    print(f"\t\t[+] Writing randoms")
                    write_random(file_ptr, file_size)
                    print(f"\t\t[+] Writing Nulls")
                    write_nulls(file_ptr, file_size)
                
                file_ptr.close()
                print("[+] Removing file.")
                remove_file(file_path)

                print("[+]  removed the file from the system")
    else:
        print("[-] File not found.")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    passes=int(input("[+] Enter number of passes (default is 14) (Max 20) - "))
    if passes < 14:
        print("[+] Anything less than 14 is not secure. Defaulting to 14 passes.")
        passes = 14
    if passes > 20:
        print("[+] Input exceeding maximum  limit, defaulting to max limit of 20")
        passes = 20
    driver(passes)


if __name__ == "__main__":
    main()
