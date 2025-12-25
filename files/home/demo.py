#!/usr/bin/env python3
"""Sample Python script for ZynqOS"""

def main():
    print("🐍 Hello from Python on ZynqOS!")
    print("=" * 40)

    # Demo calculations
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum of {numbers} = {sum(numbers)}")
    print(f"Squares: {[x**2 for x in numbers]}")

    # Demo VFS integration
    print("\nTry: python /home/demo.py")
    print("Or start REPL with: python")

if __name__ == "__main__":
    main()
