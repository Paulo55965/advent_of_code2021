#!/usr/bin/env python3

# original position of the submarine
aim = 0
x = 0
y = 0

# Type commands in strings such as first character is direction follows by distance value
#commands = [["forward","5"],["down", "5"],["forward","8"],["up","3"],["down","8"],["forward","2"]]


def get_lines():
    with open("input.txt", "r") as inputs:
        return inputs.read().split('\n')

def parse_commands(lines):
    return [line.split() for line in lines]

def resolve(commands):
    x = 0
    y = 0
    aim = 0
    for c in commands:
        direction = c[0][:1]
        distance = int(c[1])
        if direction == "u":
            #y += distance 
            aim -= distance
        if direction == "d":
            #y -= distance
            aim += distance
        if direction == "f":
            x += distance
            y -= (distance*aim)
    return x * abs(y)

lines = get_lines()
commands = parse_commands(lines)
result = resolve(commands)
print(result)
