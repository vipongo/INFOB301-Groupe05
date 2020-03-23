import zipfile

ex2Zip = zipfile.ZipFile("SecretFilesHere.zip")
dictionary = "cain.txt"


def bruteForce():
    attempts = 0
    flag = 0
    with open(dictionary, 'r') as listPassword:
        for password in listPassword:
            try:
                passwd = password.strip('\n')
                ex2Zip.extractall(pwd=str.encode(passwd))
            except Exception:
                pass
            else:
                print("Password Found: %s" % (passwd))
                found = 1
                break

        if found == 0:
            print("Password not found")


if __name__ == "__main__":
    bruteForce()