# import sys
# ​
# """
# Get the file path from the command line
# Sanitize the data from that file
# 	Ignore blank lines, whitespace, comments
# 	Splitting the input file per line
# 	Turn into program instructions (str->int)
# """
# # These all mean the same thing:
# #   Index into the memory array
# #   Address
# #   Location
# #   Pointer
# ​
# memory = [0] * 256
# ​
# if len(sys.argv) != 2:
# 	print("usage: comp.py filename")
# 	sys.exit(1)
# ​
# try:
# 	address = 0
# ​
# 	with open(sys.argv[1]) as f:
# 		for line in f:
# 			t = line.split('#')
# 			n = t[0].strip()
# ​
# 			if n == '':
# 				continue
# ​
# 			try:
# 				n = int(n)
# 			except ValueError:
# 				print(f"Invalid number '{n}'")
# 				sys.exit(1)
# ​
# 			memory[address] = n
# 			address += 1
# ​
# except FileNotFoundError:
# 	print(f"File not found: {sys.argv[1]}")
# 	sys.exit(2)
# ​
# registers = [0] * 8  # R0-R7
# ​
# # "Variables" in hardware. Known as "registers".
# # There are a fixed number of registers
# # They have fixed names
# #  R0, R1, R2, ... , R6, R7
# ​
# pc = 0  # Program Counter, address of the currently-executing instuction
# ​
# running = True
# ​
# while running:
# 	ir = memory[pc]  # Instruction Register, copy of the currently-executing instruction
# ​
# 	if ir == 1:  # PRINT_BEEJ
# 		print("Beej!")
# 		pc += 1
# ​
# 	elif ir == 2:
# 		running = False
# ​
# 	elif ir == 3:  # SAVE_REG (LDI on the LS8)
# 		reg_num = memory[pc + 1]
# 		value = memory[pc + 2]
# 		registers[reg_num] = value
# 		pc += 3
# ​
# 	elif ir == 4:  # PRINT_REG
# 		reg_num = memory[pc + 1]
# 		print(registers[reg_num])
# 		pc += 2
# ​
# 	else:
# 		print(f"Unknown instruction {b}")
# ​
# 	"""
# 	# For the LS-8 to move the PC
# ​
# 	number_of_operands = (ir & 0b11000000) >> 6
# ​
# 	how_far_to_move_pc = number_of_operands + 1
# ​
# 	pc += how_far_to_move_pc
# 	"""
