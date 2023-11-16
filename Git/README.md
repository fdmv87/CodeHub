# GIT

**usage**: 

    git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

start a working area (see also: git help tutorial)

    clone             Clone a repository into a new directory
    init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)

    add               Add file contents to the index
    mv                Move or rename a file, a directory, or a symlink
    restore           Restore working tree files
    rm                Remove files from the working tree and from the index
    sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)

    bisect            Use binary search to find the commit that introduced a bug
    diff              Show changes between commits, commit and working tree, etc
    grep              Print lines matching a pattern
    log               Show commit logs
    show              Show various types of objects
    status            Show the working tree status

grow, mark and tweak your common history

    branch            List, create, or delete branches
    commit            Record changes to the repository
    merge             Join two or more development histories together
    rebase            Reapply commits on top of another base tip
    reset             Reset current HEAD to the specified state
    switch            Switch branches
    tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   
    fetch             Download objects and refs from another repository
    pull              Fetch from and integrate with another repository or a local branch
    push              Update remote refs along with associated objects

## Inital basic configuration
	git --version
	git config --global user.name "John Doe"
	git config --global user.email johndoe@gmail.com
	code
	git config --global core.editor "code --wait"
	git config --global core.autocrlf input
	git config --global -e
 	git config --list

#### Create a new repository on the command line
	git init
	git add README.md
	git commit -m "first commit"

#### Push repository from the command line
	git remote add origin https://github.com/<repo>.git
	git push -u origin main

## GitHub config

> **_NOTE:_** GitHub has deprecated password authentication for Git operations over HTTPS. To resolve this, you should switch to using either a Personal Access Token or SSH for authentication. Here's how you can do that:

### Option 1: Use a Personal Access Token (Recommended)

Generate a Personal Access Token:

Visit your GitHub account settings.
Go to "Developer settings" > "Personal access tokens."
Click "Generate token" and follow the prompts to create a new token.
Choose the necessary permissions (typically "repo" and "public_repo" for public repositories, or "repo" and "repo:status" for private repositories).
Update the Remote URL:

In your local repository, you need to update the remote URL to include your Personal Access Token. Open your terminal and navigate to your repository.

Use the following command to set the remote URL, replacing <your_username> with your GitHub username and <your_access_token> with the Personal Access Token you generated:

	git remote set-url origin https://<your_access_token>@github.com/<your_username>/<repository>.git
	Make sure to replace both occurrences of <your_username> with your GitHub username and <repository> with your repository name.

example:
	git remote set-url origin https://<token>@github.com/fdmv87/CodeHub


### Option 2: Use SSH Authentication

Set Up SSH Authentication:

If you haven't already, generate an SSH key pair on your computer and add the public key to your GitHub account (follow the SSH key generation steps I provided in a previous response).
Update the Remote URL:

In your local repository, you need to update the remote URL to use SSH. Use the following command, replacing <your_username> with your GitHub username and <repository> with your repository name:

	git remote set-url origin git@github.com:<your_username>/<repository>.git
	With either of these options, you'll be able to push to your GitHub repository without encountering the password authentication error. It's recommended to use the first option (Personal Access Token) as it provides an additional layer of security.



***

# Git Fundamentals

<img width="628" alt="Git_fig_1" src="https://github.com/fdmv87/CodeHub/assets/149420235/6ec3a599-fd73-4437-a7c8-b2270e6b175a">

## Git: Your First Git Repository

#### versão
	git version

#### criar novo repositorio Git
	git init

#### para ver .git
	ls -a


## Git: Your First Commit in Git 

##### criar um ficheiro e adicionar ao Index (staging area):
	git add <ficheiro>
	git status

##### commit:
	git commit -m "comentario"
##### -m: message

## Git: Working with diff

##### ver log do repositório git:
    git log --graph --oneline --all

##### ver diferenças entre versões (antes do add ao Index)
    git diff    

##### após add ao Index
    git add <file>
    git diff --cached

##### esta variação do comando diff command compara o conteúdo do ficheiro com a ultima versão que fizemos commit

##### após fazer commit
    git commit -m "description"
    git log --graph --oneline --all
    git diff 2840221 4861c2b

#### ou

    FIRST_COMMIT_ID=$(git rev-parse --short HEAD~1)
    SECOND_COMMIT_ID=$(git rev-parse --short HEAD)
    git diff $FIRST_COMMIT_ID $SECOND_COMMIT_ID

## Git: Using Branches in Git

#### ver branches:
    git branch

#### criar branch:
    git branch <nome>

#### mudar de branch:
    git switch <branch_name>

#### criar branch e mudar para esse branch:
    git switch -c new-branch-name

#### ou
    git switch --create new-branch-name

#### ou
    git checkout -b <branch_name>

## Git: Fixing Your Mistakes: Files and Branches in Git 

<img width="706" alt="Git_fig_2" src="https://github.com/fdmv87/CodeHub/assets/149420235/7fdab76a-f10f-4367-ba52-21767c1cb35b">

##### Editei ficheiros, mas ainda não fiz add. Ou reverto pelo editor, ou pelo Git.
##### Pelo editor posso ter perdido as alterações (ao fechar o ficheiro perco o undo) ou ser muitos ficheiros -> neste caso editava no editor e fazia add novamente.
##### Pelo git reverte logo tudo para a ultima versão
####
##### restaurar ficheiros
    git restore <file>

##### editei ficheiro mas fiz add (para o index - zona de staging)
##### remove a edição do index e voltamos ao working directory!
    git restore --staged <file>

####
##### depois de adicionar um ficheiro à Staging Area

##### agora posso editar ou reverter como no step anterior (restore)
####
##### Para ver os branchs:
    git branch

##### para renomear o branch:
    git branch -m <branch_name> <new_branch_name>

##### flag -m (ou --move): comando "move" que recebe dois argumentos:
##### nome do branch a renomear
##### novo nome do branch

#### para apagar branch:
    git branch -D <branch_name>

## Git: Creating and Merging Branches in Git

##### imaginemos que temos dois branches:
    master
    branch1

##### e queremos fazer merge do branch1 no master
##### ir para o master
    git switch master

##### merge branches
    git merge -m "Merge branch '<branch name>'" <branch name>

##### em caso de conflito, ver editor
##### <<<<<<<< HEAD
##### >>>>> 

##### fazer as correções

##### add do ficheiro ao Index
    git add <ficheiro>

##### commit do merge
    git commit --no-edit


***

# Git Cheat Sheet

![Git_fig_3](https://github.com/fdmv87/CodeHub/assets/149420235/3ac6086a-b227-4fad-80d8-41f5edae9583)

![Git_Commands_Cheat_Sheet](https://github.com/fdmv87/CodeHub/assets/149420235/64ea62c6-b470-4bf9-be63-078d8854a8ef)

##### Initializing a repository
    git init

##### Staging files
    git add file1.js # Stages a single file
    git add file1.js file2.js # Stages multiple files
    git add *.js # Stages with a pattern
    git add . # Stages the current directory and all its content

##### Viewing the status
    git status # Full status
    git status -s # Short status
    git status --untracked-files=all

##### Committing the staged files
    git commit -m “Message” # Commits with a one-line message
    git commit # Opens the default editor to type a long message

##### Skipping the staging area
    git commit -am “Message”

##### Removing files
    git rm file1.js # Removes from working directory and staging area
    git rm --cached file1.js # Removes from staging area only

##### Renaming or moving files
    git mv file1.js file1.txt

##### Viewing the staged/unstaged changes
    git diff # Shows unstaged changes
    git diff --staged # Shows staged changes
    git diff --cached # Same as the above

##### Viewing the history
    git log # Full history
    git log --oneline # Summary
    git log --reverse # Lists the commits from the oldest to the newest

##### Viewing a commit
    git show 921a2ff # Shows the given commit
    git show HEAD # Shows the last commit
    git show HEAD~2 # Two steps before the last commit
    git show HEAD:file.js # Shows the version of file.js stored in the last commit

##### Unstaging files (undoing git add)
    git restore --staged file.js # Copies the last version of file.js from repo to index

##### Discarding local changes
    git restore file.js # Copies file.js from index to working directory
    git restore file1.js file2.js # Restores multiple files in working directory
    git restore . # Discards all local changes (except untracked files)
    git clean -fd # Removes all untracked files

##### Restoring an earlier version of a file
    git restore --source=HEAD~2 file.js

##### .gitignore
    add the files to be ignored by git
    example, adding the following lines will ignore .bak files and temporary files:
    *.bak
    *~
    
##### .git-keep
    used to track empty folders. If you have an empty folder and want to commit, you need to create the .git-keep file inside that empty folder.	
    mkdir somefolder
    cd somefolder
    touch .git-keep

##### Amend the last commit without changing the commit message
    git commit --amend --no-edit

##### Recovery a local deleted file by asking for it to Git
    git checkout -- <filename>

##### Recovery a deleted file after a git rm to the most recent commit or HEAD
    git reset HEAD <filename>

##### Recovery from a commit (changes on this commit has bugs for example or deletes a file)
    git reset --hard HEAD^
    git checkout -- <folder/filename>

##### Creates a new commit that undoes everything that you just did
    git revert --no-edit HEAD

##### Revert to a specific commit. This will keep the commit log
    git checkout <commit_hash> .

##### Create pull requests (git request-pull)
    git request-pull -p origin/main .
    #This pull request is essentially the same thing as a pull request on GitHub

##### git pull
    git request-pull -p origin/main .
    #git pull is a combination of git fetch, which gets the changes, and git merge, which merges those changes into your repository.

##### **HEAD**
1. **Current Commit**: HEAD always points to the latest commit in the branch you are currently working on. If you switch branches, HEAD will be updated to point to the latest commit of the newly checked-out branch.

2. **Working Directory**: The commit that HEAD points to represents the version of the project that is currently in your working directory. Any changes you make will be applied to this version.

3. **Detached HEAD State**: In Git, you can also have a "detached HEAD" state, where HEAD is not pointing to the latest commit of a branch but directly to a specific commit. This happens, for example, when you check out a specific commit, tag, or branch that is not the latest commit of a branch.

4. **Branch Manipulation**: When you create a new commit, the branch that HEAD points to is updated to point to the new commit. This is how branches are moved forward in Git.

5. **Symbolic Reference**: HEAD is a symbolic reference, meaning it points to another reference (like a branch name) rather than directly to a commit. This allows it to easily switch between different branches.



## References
[Introduction to Git by Microsoft](https://learn.microsoft.com/en-us/training/modules/intro-to-git/)
[Introduction to Git Recap | Learn with Dr G](https://www.youtube.com/watch?v=9uGS1ak_FGg&ab_channel=MicrosoftDeveloper)

