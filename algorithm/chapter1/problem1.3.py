#URL화 : 문자열에 들어 있는 모든 공백을 '%20'으로 바꿔주는 메서드를 작성하라. 
#최종적으로 모든 문자를 다 담을 수 있을 만큼 충분한 공간이 이미 확보되어 있으며 문자열의 최종 길이가 함께 주어진다고 가정해도 된다.

#입력 : "Mr John Smith",13
#출력 : "Mr%20John%20Smith"
inputstring = input("입력 : ")
outputstring=inputstring.replace(" ", "%20");
print(outputstring)


'''모범답안
def urlify(string, length):
    #function replaces single spaces with %20 and removes trailing spaces
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string
'''