import os



def print_hi(name):
    try:
        for count, filename in enumerate(os.listdir("rename")):
            print ("count" + str(count))
            print("filename" + filename)
            dst = "rename/" + str(count) + ".png"
            print ("destination" + dst)
            src = "rename/" + filename

            # rename() function will
            # rename all the files
            os.rename(src, dst)
    except():
        print("An exception was thrown")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
