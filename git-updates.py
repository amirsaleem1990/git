import os
ls = []
os.chdir("/home/amir/github/")
repos = os.listdir()
try:
    os.mkdir("/home/amir/Desktop/temprory-github-folder")
except:
    os.system("rm -r /home/amir/Desktop/temprory-github-folder")
    os.mkdir("/home/amir/Desktop/temprory-github-folder")
for repo in repos:
    if not repo.startswith("."):
        os.chdir(repo)
        os.system("git status > /home/amir/Desktop/temprory-github-folder/{}.txt".format(repo))
        a = open("/home/amir/Desktop/temprory-github-folder/{}.txt".format(repo), 'r').read()
        if not "nothing to commit, working tree clean" in a:
            aa = [i.strip() for i in a.splitlines()]
            print("**********" , repo , "**********")
            for i in aa:
                if i :
                    if i.startswith("On branch") or i.startswith("Your branch")  or i.startswith("Changes not staged") or i.startswith("(") or i.startswith("no changes added to") or i.startswith("Untracked files") or i.startswith("nothing added to commit"):
                        pass
                    else:
                        print(i)
            print("\n\n")
        os.chdir("..")
os.system("rm -r /home/amir/Desktop/temprory-github-folder")
