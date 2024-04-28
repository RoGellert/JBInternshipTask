# pip install gitpython
from git import Repo
import os
from collections import deque

Repo.clone_from("https://github.com/JetBrains/kotlin", "./raw_repos/kotlin")
Repo.clone_from("https://github.com/2dust/v2rayNG", "./raw_repos/v2rayNG")
Repo.clone_from("https://github.com/JunkFood02/Seal", "./raw_repos/Seal")
Repo.clone_from("https://github.com/tiann/KernelSU", "./raw_repos/KernelSU")
Repo.clone_from("https://github.com/vfsfitvnm/ViMusic", "./raw_repos/ViMusic")

os.makedirs("kotlin_files")
q = deque(["raw_repos"])
curr_num = 0
while q:
    curr = q.popleft()
    for root, dirs, files in os.walk(curr, topdown=True):
        for name in files:
            if name.endswith(".kt"):
                os.rename(os.path.join(root, name), "kotlin_files/"+str(curr_num)+name)
                curr_num += 1
        for name in dirs:
            q.append(name)
