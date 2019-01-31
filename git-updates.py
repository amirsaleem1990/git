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
            print(repo)
        os.chdir("..")
os.system("rm -r /home/amir/Desktop/temprory-github-folder")