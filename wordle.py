if __name__ =="__main__":
    #(1) user input
    user_input = input()

    #(2) specify an answer
    answer = "apple"

    for i in range(len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
        elif user_input[i] in answer:
            print("B")
        else:
            print("X")

