# GIT Config

## Inital basic configuration
	git --version
	git config --global user.name "John Doe"
	git config --global user.email johndoe@gmail.com
	code
	git config --global core.editor "code --wait"
	git config --global core.autocrlf input
	git config --global -e


#### Create a new repository on the command line
	git init
	git add README.md
	git commit -m "first commit"

#### Push repository from the command line
	git remote add origin https://github.com/<repo>.git
	git push -u origin main


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

![Fig 1](Git_fig_1.png?raw=true)


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

![Fig 2](Git_fig_2.png?raw=true)

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

![Fig 3](Git_fig_3.png?raw=true)

#### Creating Snapshots
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
