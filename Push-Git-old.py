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
        if "Untracked files" in a or "Changes not staged for commit" in a:
            aa = [i.strip() for i in a.splitlines()]
            print("**********" , repo , "**********")
            for i in aa:
	            if i and i.startswith("Untracked files") or i.startswith("Changes not staged for commit"):
	            	os.system("git add . ; git commit -m 'updated'; git push origin master")
            print("\n\n")
        os.chdir("..")
os.system("rm -r /home/amir/Desktop/temprory-github-folder")