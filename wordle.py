import random
if __name__ =="__main__":
    #user input
    user_input = input()

<<<<<<< HEAD
    #(2) specify an answer
    f = open("words.txt","r")
    dictionary = f.read().splitlines()
    f.close()
    
    answer = random.sample(dictionary,1)[0]
    print(answer)
    
=======

>>>>>>> 817f78da3129c3910ed0ece1065b166630ae8d73
    #compare user_input
    for i in range(len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
        elif user_input[i] in answer:
            print("B")
        else:
            print("X")