def get_number(array, command):
    new_array=sorted(array[command[0]-1:command[1]])
    return new_array[command[2]-1]

def solution(array, commands):
    answer = []
    command_length=len(commands)
    for i in range(command_length):
        answer.append(get_number(array,commands[i]))
    return answer