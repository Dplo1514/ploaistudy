numbers = [1,1,3]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number %2 == 0:
        print("Found even number', number")
        break
    position += 1
else:#break문이 호출되지 않은경우
    print("No even number found")