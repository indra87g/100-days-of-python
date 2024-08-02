"""
Day 2 - Password Generator
"""

import random
import time

length = int(input("Enter the password length: "))
character = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
result = "".join(random.sample(character, length))


def main():
    print(
        f"""
          ====== RESULT ======
          Password generated!
          
          {result}
          
          The program will exited in 15 seconds.
          Please copy the generated password!
          ====================
          """
    )
    time.sleep(15)


if __name__ == "__main__":
    main()
