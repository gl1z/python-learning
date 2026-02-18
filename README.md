# Python Learning Journey

This repository documents my structured progress through Python fundamentals.

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
- Working with Git & proper .gitignore setup

---

## Projects So Far
- Block Letters (ASCII Art)
- Receipts Project

---

## Goal
Strengthen Python fundamentals before moving into backend and data-focused projects.
## Git Problems I faced and how I solved them
Today I ran into several issues while working with Git and pushing my project to GitHub. At first, my push was rejected because the remote repository already had commits that did not exist in my local repository. I learned that this happens when the remote and local histories do not match. To fix this, I pulled the changes from the remote repository using the allow unrelated histories option, which allowed Git to merge the two histories.

During the merge process, I got stuck in the Vim editor without understanding what was happening. Git opened Vim so I could confirm the merge commit message, but I did not know how to exit it. After figuring it out, I learned that pressing Escape and typing :wq saves and exits Vim, which allowed the merge to complete successfully.

Another issue I faced was accidentally committing the .idea folder from PyCharm to the repository. These files should not be tracked because they are specific to my local development environment. I solved this by creating a proper .gitignore file and adding rules to ignore .idea, virtual environment folders, Python cache files, and other unnecessary system files. I then removed the .idea folder from Git tracking using the cached remove command and committed the cleanup.

After resolving the merge, cleaning the repository, and setting up the correct ignore rules, I was able to successfully merge and push my changes to GitHub. By the end of this process, I better understood how Git handles remote and local differences, how merges work, how to use Vim in a basic way, and how to properly configure a .gitignore file to keep a repository clean.
## Practical Notes (Quick Reference)

### Push rejected
Cause: Remote had commits that local did not have
Fix: git pull origin master --allow-unrelated-histories

### Stuck in Vim during merge
Fix: Press Esc, then type :wq and press Enter

### Accidentally committed .idea
Fix: Add .idea to .gitignore
Then run: git rm -r --cached .idea
Then commit and push
