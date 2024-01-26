#!/bin/python3

red = "red"
green = "green"
blue = "blue"


def read_file(path: str) -> list[str]:
	lines = []
	with open(path, "r") as f:
		while line := f.readline().strip():
			lines.append(line)

	return lines


def solve(games_arr: list[str]) -> int:
	game_power = []
	for game in games_arr:
		tmp = game.split(': ')

		# Calculate the minimum of each cube
		cubes = {
			red   : 0,
			green : 0,
			blue  : 0,
		}
		bags = tmp[-1].split(';')

		for bag in bags:
			bag = bag.split(',')
			for cube_color in bag:
				cube_color = cube_color.strip()
				cube_num = int(cube_color.split(' ')[0])

				if red in cube_color and cubes[red] < cube_num:
					cubes[red] = cube_num
				elif green in cube_color and cubes[green] < cube_num:
					cubes[green] = cube_num
				elif blue in cube_color and cubes[blue] < cube_num:
					cubes[blue] = cube_num

		game_power.append( cubes[red] * cubes[green] * cubes[blue] )

	return sum(game_power)


def main() -> None:
	lines = read_file("input.txt")
	print(f"RESULT: {solve(lines)}")


if __name__ == '__main__':
	main()