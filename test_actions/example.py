#!/usr/bin/env python
import os

def main():
    my_secret = os.environ.get('MY_SECRET')
    print(f"Secret value: {my_secret}")


if __name__ == "__main__":
    main()
