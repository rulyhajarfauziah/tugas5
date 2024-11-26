1. Implementasi Stack
stack = []

# Push elemen ke stack
stack.append (10)
stack.append (20)
stack.append (30)
print("Stack setelah push",stack)

# Pop elemen dari stack
elemen = stack.pop (10)
print("Elemen yang di-pop",elemen)
print("Stack setelah di-pop",stack)

# Peek elemen teratas
if stack:
	print("Elemen teratas",stack[-1])
else:
	print("Stack kosong")

