with open("../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# keyword = w (for write), a (append), r (read)
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")