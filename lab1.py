user@WIN-CLSTJ0U6L9V MINGW64 /
$ cd ~

user@WIN-CLSTJ0U6L9V MINGW64 ~
$ cd repo

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git status
On branch master
nothing to commit, working tree clean

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git log --oneline
35b43b3 (HEAD -> master) Merge branch 'cool_feature'
e710354 Add one more code block to code.txt
c14286b Add bahfkjhajhakjkjahankjcl to .gitignore
89be540 Add one more code block to code.txt
7b73e34 (cool_feature) Add module.txt with brand new feature
dff4985 Add .gitignore to ignore PNG files
87fc80a Updated code.txt with configuration reading
e70570c Added config.txt with configuration information
326e4a2 Updated code.txt with a new comment
75082b3 Update code.txt with a new comment
d7ee449 Updated code.txt with configuration reading
2179c8e Updated code.txt with a new comment
637eedd added some really great code

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ ls
bahfkjhajhakjkjahankjcl  code.txt  config.txt  img/  module.txt  repo/

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git merge cool_feature
Already up to date.

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git status
On branch master
nothing to commit, working tree clean

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git log --oneline
35b43b3 (HEAD -> master) Merge branch 'cool_feature'
e710354 Add one more code block to code.txt
c14286b Add bahfkjhajhakjkjahankjcl to .gitignore
89be540 Add one more code block to code.txt
7b73e34 (cool_feature) Add module.txt with brand new feature
dff4985 Add .gitignore to ignore PNG files
87fc80a Updated code.txt with configuration reading
e70570c Added config.txt with configuration information
326e4a2 Updated code.txt with a new comment
75082b3 Update code.txt with a new comment
d7ee449 Updated code.txt with configuration reading
2179c8e Updated code.txt with a new comment
637eedd added some really great code

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git branch experiment

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git checkout experiment
Switched to branch 'experiment'

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (experiment)
$ echo "some experimental code" >> code.txt

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (experiment)
$ git add code.txt
warning: in the working copy of 'code.txt', LF will be replaced by CRLF the next time Git touches it

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (experiment)
$ git commit -m "Add experimental code to code.txt"
[experiment a38af0c] Add experimental code to code.txt
 1 file changed, 1 insertion(+)

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (experiment)
$ git checkout master
Switched to branch 'master'

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ cat code.txt
some really great code
not so good as it could be but OK
not so good as it could be but OK
not so good as it could be but OK
not so good as it could be but OK
some configuration reading
one more nice code block
one more nice code block

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git merge experiment
Updating 35b43b3..a38af0c
Fast-forward
 code.txt | 1 +
 1 file changed, 1 insertion(+)

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git status
On branch master
nothing to commit, working tree clean

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git log --oneline
a38af0c (HEAD -> master, experiment) Add experimental code to code.txt
35b43b3 Merge branch 'cool_feature'
e710354 Add one more code block to code.txt
c14286b Add bahfkjhajhakjkjahankjcl to .gitignore
89be540 Add one more code block to code.txt
7b73e34 (cool_feature) Add module.txt with brand new feature
dff4985 Add .gitignore to ignore PNG files
87fc80a Updated code.txt with configuration reading
e70570c Added config.txt with configuration information
326e4a2 Updated code.txt with a new comment
75082b3 Update code.txt with a new comment
d7ee449 Updated code.txt with configuration reading
2179c8e Updated code.txt with a new comment
637eedd added some really great code


