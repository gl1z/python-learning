# Python Learning Journey

This repository documents my structured progress through Python fundamentals as I build a strong foundation before moving into backend and data-focused development.

---

## Progress Log

### Day 1
- Variables  
- Data types  
- Basic input/output  
- Notes and small exercises  

### Day 2
- Control Flow (Introduction)  
- ASCII Block Letters project  
- Receipt formatting project  
- Working with Git and proper `.gitignore` setup  

---

## Projects So Far

- Block Letters (ASCII Art)  
- Receipts Project  

---

## Goal

Strengthen Python fundamentals before moving into backend and data-focused projects.

---

## Git Problems I Faced and How I Solved Them

While working on pushing my project to GitHub, I ran into several issues that forced me to understand Git more deeply instead of just using basic commands.

The first problem was a push rejection. My local repository and the remote repository had different histories, which caused Git to block the push. I learned that this happens when the remote contains commits that do not exist locally. To fix it, I pulled from the remote repository using the `--allow-unrelated-histories` option, which allowed Git to merge both histories.

During the merge process, Git opened Vim to confirm the merge commit message. I did not understand what was happening and got stuck inside the editor. After researching, I learned that pressing `Esc`, then typing `:wq`, and pressing Enter saves and exits Vim.

Another mistake I made was accidentally committing the `.idea` folder from PyCharm. These files are environment-specific and should not be tracked. I solved this by creating a proper `.gitignore` file and adding rules to ignore `.idea`, virtual environments, Python cache files, and other unnecessary system files. I then removed `.idea` from Git tracking using the cached remove command and committed the cleanup.

By the end of this process, I better understood how Git handles remote and local differences, how merges work, how to exit Vim safely, and how to properly configure a `.gitignore` file to keep a repository clean.

---

## Practical Notes (Quick Reference)

### Push Rejected

Cause: Remote had commits that local did not have  

Fix:
- git pull origin master --allow-unrelated-histories

---

### Stuck in Vim During Merge

Fix:
- Press Esc
- Type :wq
- Press Enter

---

### Accidentally Committed `.idea`

Fix:
```
Add .idea to .gitignore
git rm -r --cached .idea
git commit -m "Remove .idea from tracking"
git push
```
