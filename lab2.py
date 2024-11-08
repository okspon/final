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

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git branch test_feature

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git checkout test_feature
Switched to branch 'test_feature'

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (test_feature)
$ echo "testing some feature" >> code.txt

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (test_feature)
$ git add code.txt
warning: in the working copy of 'code.txt', LF will be replaced by CRLF the next time Git touches it

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (test_feature)
$ git commit -m "Add testing feature to code.txt"
[test_feature 72ca3c2] Add testing feature to code.txt
 1 file changed, 1 insertion(+)

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (test_feature)
$ git checkout master
Switched to branch 'master'

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ echo "another test code" >> code.txt

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git add code.txt
warning: in the working copy of 'code.txt', LF will be replaced by CRLF the next time Git touches it

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git commit -m "Add another test code to code.txt"
[master 9a5c39a] Add another test code to code.txt
 1 file changed, 1 insertion(+)

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git merge test_feature
Auto-merging code.txt
CONFLICT (content): Merge conflict in code.txt
Automatic merge failed; fix conflicts and then commit the result.

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master|MERGING)
$ git add code.txt

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master|MERGING)
$ git commit -m "Resolve merge conflict, keep test_feature changes"
[master 0d32f63] Resolve merge conflict, keep test_feature changes

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git status
On branch master
nothing to commit, working tree clean

user@WIN-CLSTJ0U6L9V MINGW64 ~/repo (master)
$ git log --oneline
0d32f63 (HEAD -> master) Resolve merge conflict, keep test_feature changes
9a5c39a Add another test code to code.txt
72ca3c2 (test_feature) Add testing feature to code.txt
a38af0c (experiment) Add experimental code to code.txt
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

