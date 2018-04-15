#!/usr/bin/python
N = 3

# Round-Robin Scheduling

def rr_select():
	last = N - 1
	while True:
		current = (last + 1) % N
		last = current
		yield current

rr_test = rr_select()
for i in range(100):
    print(next(rr_test))	