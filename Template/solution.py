#!/bin/python3

def read_file(path: str) -> list[str]:
	lines = []
	with open(path, "r") as f:
		while line := f.readline().strip():
			lines.append(line)

	return lines


def solve(lines: list[str]) -> int:
	pass


def main() -> None:
	lines = read_file("input.txt")
	print(f"RESULT: {solve(lines)}")


if __name__ == '__main__':
	main()