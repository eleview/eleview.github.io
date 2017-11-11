---
layout: post
title: Basic Git Tutorial
use_math: true
---

[Git][1] is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency (from the Git official website). Below are my personal opinions.

As a college weakchick in junior grade, I think of Git as an "efficient and convenient, but seldom used" tool. Not everyone knows what is "[version control][2]", and not everyone is glad to face the so-called "black window".

However, everyone faces the problems of needing-changes-more-than-you-can-bear documents such as papers, homework projects, etc. For example, I have a document homework.cpp and want to make some changes, in the meantime fearing that I may do something wrong. As a result, I create many cpp files named "homework1", "homework2", "homework-final", "homework-s**t", etc., which is a rather tiring and boring task. In this case, Git is to properly handle this kind of problems, and this kind of problems are called "version control".

I have the "Digital Image Processing" class, which recommends Git as the homework platform. Here we mainly talk about commands used in the class.

The class has a Git platform with 20 branches named C01 to C20(20 groups of students). We should upload weekly reports to specific branches and get the review from teaching assistant.

Note that Git repositories may have some branches, but they all have a trunk, which is often called "master".

There are some fundamental commands to complete this work.

### Git Installation

Git is a free software supporting [Windows][3], [Linux][4] and [Mac][5] OS.

Run the installation program and follow the instructions, or look at this sentence again.

### Git Commands

In Linux and Mac, simply run Git in terminal. In Windows, click the right mouse and choose "Git Bash here" to open a Git terminal.

#### git init

Every repository should be initialized in order to be version-controlled by Git. Run the "git init" command to initialize the repository. After this process, the repository should contain a hidden repository called .git and a hidden file called .gitignore. The .git repository contains all the information of the file of different versions, while the .gitignore file records whatever you do not want to be influenced by Git.

#### git add

If you just modified a file called "homework.cpp" and want Git to record the changes, use "git add homework.cpp" command. Use "git add -A" command to record changes of all the modified files. This command is often combined with "git commit".

#### git commit

Record is not Commit. Sometimes you do changes which you may not want to be recorded, in the meantime fearing that you may do something wrong and lose the changes. In this case, record significant changes by "git commit".

It is strongly recommended that you use an illustration for the submittal. Use "git commit -m" followed by the illustration to commit. For example, use "git commit -m "I will no longer give a f**k about this"".

Note that the "git commit" command is to commit all the changes after the "git add" process, so no file names are required.

#### git status

Use "git status" to view what you have modified but not added, and what you have added but not committed.

#### git clone

Git is often with [GitHub][6]. If you just found a good repository on GitHub and want to copy it into your computer, use "git clone" followed by the repository address (often ended with .git) to clone the repository. The cloned repository is already initialized.

#### git push

If you have a GitHub repository and its local form in your computer, and you just made some changes and want to update it on GitHub, use "git push" command.

Suppose the GitHub repository has 20 branches and a trunk, and you want to update your changes to a specific branch (or trunk), use "git push origin" followed by the branch (or trunk) name. For example, update the changes to branch C17 by "git push origin C17" and to the trunk by "git push origin master".

#### git pull

Assume that you cloned a repository which is not yours, and the host makes some changes to the repository. In this case, you have an old version of the repository locally. To update the local repository, use "git pull" command.

If the GitHub repository has branches, the commands are similar to the "git push" command. For example, update the changes of C17 to the local repository by "git pull origin C17" and update the changes of all the branches by "git pull".

#### git checkout

Note that the local repositories in "git pull" may not be local. For example, I am in branch C17 and run the "git pull" command, the result is, the changes are pulled into every local repository of the branches, but I do not have the other 19 branches, so I only have my C17 local repository updated, while some others will discover that their repositories are updated at a god-d**n-knows time by someone named not-me.

Use "git checkout" command to switch the local repository into the specific branch. For example, if I want to view the files in branch C01, use "git checkout C01" and "git pull origin C01" to view the latest version.

#### git log

Use "git log" to view all the changing process you have made.

#### Emmmmm...

Here are some fundamental commands which you should always know. However, you will still think of Git as a troublesome and unnecessary tool. You should know more about it.

To be continued...

By [zcc31415926][7].

[1]: https://git-scm.com/
[2]: https://en.wikipedia.org/wiki/Version_control
[3]: https://git-scm.com/downloads/win
[4]: https://git-scm.com/downloads/linux
[5]: https://git-scm.com/downloads/mac
[6]: https://github.com/
[7]: https://github.com/zcc31415926
