import sys

A,B=map(int,sys.stdin.readline().split())
N,M=map(int,sys.stdin.readline().split())

robots_init=[]
for i in range(N):
    a,b,c=map(str,sys.stdin.readline().split())
    a=int(a)
    b=int(b)
    robots_init.append(((a,b),c))




# 방향에 따른 이동 벡터 (dx, dy)
directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

# 방향 전환 로직
def turn_left(direction):
    return {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}[direction]

def turn_right(direction):
    return {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]

# 로봇의 현재 상태를 저장
robots = {i+1: {'position': robots_init[i][0], 'direction': robots_init[i][1]} for i in range(N)}

# 명령 실행
def execute_commands(A, B, robots, commands):
    for command in commands:
        robot_number, action, repeat = command
        for _ in range(repeat):
            if action == 'F':
                dx, dy = directions[robots[robot_number]['direction']]
                new_position = (robots[robot_number]['position'][0] + dx, robots[robot_number]['position'][1] + dy)

                # 벽에 충돌하는 경우
                if not (1 <= new_position[0] <= A and 1 <= new_position[1] <= B):
                    return f"Robot {robot_number} crashes into the wall"

                # 다른 로봇과 충돌하는 경우
                for other_robot in robots:
                    if other_robot != robot_number and robots[other_robot]['position'] == new_position:
                        return f"Robot {robot_number} crashes into robot {other_robot}"

                robots[robot_number]['position'] = new_position
            elif action == 'L':
                robots[robot_number]['direction'] = turn_left(robots[robot_number]['direction'])
            elif action == 'R':
                robots[robot_number]['direction'] = turn_right(robots[robot_number]['direction'])

    return "OK"

# 명령 실행하고 결과 출력
commands=[]
for i in range(M):
    botnum,where,num=map(str,sys.stdin.readline().split())
    botnum=int(botnum)
    num=int(num)
    commands.append((botnum,where,num))
result = execute_commands(A, B, robots, commands)
print(result)
#
# print(robot)
#
#
# for i in range(m):
#     botnum,where,num=map(str,sys.stdin.readline().split())
#     botnum=int(botnum)-1
#     num=int(num)
#     if where=='F':
#         if robot[botnum][1]=='E':
#             for _ in range(num):
#                 x,y=robot[botnum][0]
#                 print(x,y)
#                 if x+1>=bx:
#                     print(333)
#                     sys.exit()
#                 if (x+1,y) in robot[botnum][0]:
#                     print(444)
#                     sys.exit()
#                 robot[botnum]=((x+1,y),'E')
#         if robot[botnum][1]=='W':
#             for _ in range(num):
#                 x,y=robot[botnum][0]
#                 print(x,y)
#                 if x-1<0:
#                     print(333)
#                     sys.exit()
#                 if (x-1,y) in robot[botnum][0]:
#                     print(444)
#                     sys.exit()
#                 robot[botnum]=((x-1,y),'W')
#         if robot[botnum][1]=='S':
#             for _ in range(num):
#                 x,y=robot[botnum][0]
#                 print(x,y)
#                 if y-1<0:
#                     print(333)
#                     sys.exit()
#                 if (x,y-1) in robot[botnum][0]:
#                     print(444)
#                     sys.exit()
#                 robot[botnum]=((x,y-1),'S')
#         if robot[botnum][1]=='N':
#             for _ in range(num):
#                 x,y=robot[botnum][0]
#                 print(x,y)
#                 if y+1>=by:
#                     print(333)
#                     sys.exit()
#                 if (x,y+1) in robot[botnum][0]:
#                     print(444)
#                     sys.exit()
#                 robot[botnum]=((x,y+1),'N')
#     if where=='R':
#         a=robot[botnum][1]
#         if a=='E':
#             a='S'
#         elif a=='S':
#             a='W'
#         elif a=='W':
#             a='N'
#         else:
#             a='E'
#         robot[botnum][1]=a
#     if where=='L':
#
#
#
#
#
#

