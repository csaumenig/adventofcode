YEAR = 2021
DAY = 17

START_POS = (0, 0)


def part1(file_name_str: str) -> None:
    target_area = read_file(file_name_str)
    highest_y_position = 0
    winning_trajectories: list[tuple[int, int]] = []
    max_x = max(target_area.get('x')) // 2
    max_y = abs(min(target_area.get('y')))
    for x in range(max_x + 1, 1, -1):
        for y in range(1, max_y + 1):
            cur_pos = START_POS
            trajectory = (x, y)
            cur_max_y = cur_pos[1]
            cur_trajectory = trajectory
            i = 1
            while is_past_target_area(cur_pos, target_area) is False:
                cur_pos = (cur_pos[0] + cur_trajectory[0], cur_pos[1] + cur_trajectory[1])
                if cur_pos[1] > cur_max_y:
                    cur_max_y = cur_pos[1]

                if is_in_target_area(cur_pos, target_area):
                    print(f'Start: {START_POS}, Start Trajectory: {trajectory}, '
                          f'Target Area: {target_area}, Step: {i}, '
                          f'Current Position: {cur_pos}, Current Trajectory: {cur_trajectory}, '
                          f'max_y: {cur_max_y}')
                    if cur_max_y >= highest_y_position:
                        winning_trajectories.append(trajectory)
                        highest_y_position = cur_max_y

                    break
                traj_x = cur_trajectory[0]
                traj_y = cur_trajectory[1]

                if traj_x > 0:
                    traj_x -= 1
                traj_y -= 1
                cur_trajectory = (traj_x, traj_y)
                i += 1
    print(f'Day {DAY} Part 1: Highest Y Pos: {highest_y_position}, Successful Trajectories: {winning_trajectories}')


def part2(file_name_str: str) -> None:
    target_area = read_file(file_name_str)
    winning_trajectories: list[tuple[int, int]] = []
    max_x = max(target_area.get('x'))
    min_y = min(target_area.get('y'))
    max_y = abs(min_y)
    for x in range(0, max_x + 1):
        for y in range(min_y, max_y + 1):
            cur_pos = START_POS
            trajectory = (x, y)
            cur_trajectory = trajectory
            i = 1
            while is_past_target_area(cur_pos, target_area) is False:
                cur_pos = (cur_pos[0] + cur_trajectory[0], cur_pos[1] + cur_trajectory[1])
                if is_in_target_area(cur_pos, target_area):
                    print(f'Start: {START_POS}, Start Trajectory: {trajectory}, '
                          f'Target Area: {target_area}, Step: {i}, '
                          f'Current Position: {cur_pos}, Current Trajectory: {cur_trajectory}')
                    winning_trajectories.append(trajectory)
                    break
                traj_x = cur_trajectory[0]
                traj_y = cur_trajectory[1]

                if traj_x > 0:
                    traj_x -= 1
                traj_y -= 1
                cur_trajectory = (traj_x, traj_y)
                i += 1
    print(f'Day {DAY} Part 2: Number of Successful Trajectories: {len(winning_trajectories)}')


def is_in_target_area(point: tuple[int, int], target_area: dict[str, tuple[int, int]]) -> bool:
    return point[0] in range(target_area.get('x')[0], target_area.get('x')[1] + 1) and (
            point[1] in range(target_area.get('y')[0], target_area.get('y')[1] + 1))


def is_past_target_area(point: tuple[int, int], target_area: dict[str, tuple[int, int]]) -> bool:
    if point[1] < min(target_area.get('y')) or point[0] > max(target_area.get('x')):
        return True
    if point[1] == min(target_area.get('y')) and range(target_area.get('x')[0], target_area.get('x')[1] + 1):
        return True
    return False


def read_file(file_name_str: str) -> dict[str, tuple[int, int]]:
    target_area: dict[str, tuple[int, int]] = {}
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]
    coords = lines[0].split(': ')[1].strip().split(',')
    x_coords = (int(coords[0].split('=')[1].strip().split('..')[0]), int(coords[0].split('=')[1].strip().split('..')[1]))
    y_coords = (int(coords[1].split('=')[1].strip().split('..')[0]), int(coords[1].split('=')[1].strip().split('..')[1]))
    return {
        'x': x_coords,
        'y': y_coords
    }


if __name__ == '__main__':
    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    part1(file_name)
    part2(file_name)

    file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    part1(file_name)
    part2(file_name)
