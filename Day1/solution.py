#!/bin/python3
valid_numbers = {
	"one"    : "1",
	"two"    : "2",
	"three"  : "3",
	"four"   : "4",
	"five"   : "5",
	"six"    : "6",
	"seven"  : "7",
	"eight"  : "8",
	"nine"   : "9",
	"1"      : "1",
	"2"      : "2",
	"3"      : "3",
	"4"      : "4",
	"5"      : "5",
	"6"      : "6",
	"7"      : "7",
	"8"      : "8",
	"9"      : "9",
}


def read_file(path: str) -> list[str]:
	lines = []

	with open(path, "r") as f:
		while line := f.readline().strip():
			lines.append(line)

	return lines


def solve(lines: list[str]) -> int:
	solution = []

	for line in lines:
		earliest_idx, earliest_digit = 999999999, ""
		last_idx, last_digit = -1, ""

		# Find first digit
		for key, val in valid_numbers.items():
			if (idx := line.find(key)) != -1:
				if idx < earliest_idx:
					earliest_idx = idx
					earliest_digit = val

			if (idx := line.rfind(key)) != -1:
				if idx > last_idx:
					last_idx = idx
					last_digit = val

		solution.append(int(f"{earliest_digit}{last_digit}"))

	return sum(solution)


def main() -> None:
	lines = read_file("input.txt")
	print(f"RESULT: {solve(lines)}")


if __name__ == '__main__':
	main()