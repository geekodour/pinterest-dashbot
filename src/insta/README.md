```
$ apt-get install git
$ git clone https://github.com/timgrossmann/InstaPy.git
$ cd InstaPy/scripts/
$ ./unix.sh
```
after the installation is done, copy `./insta_follow_like_comment.py` and `./insta_unfollow.py` from this directory(`/src/insta/`) to the (`InstaPy/`) directory.
now navigate to the root directory of `InstaPy`(the cloned diretory), you should see the two follow and unfollow scripts that you just copied there along with other files and directory.
they do what they are named, sufficient comments are added to both the files to explain how to configure it, so please read both the files to understand how to configure.

## conjobs
you can put the two scripts on cron
the guide is here: https://github.com/timgrossmann/InstaPy#automate
an example:
this will run the follow script at 4:45 and the unfollow script at 3:45

```
45 4 * * * cd /home/user/InstaPy && /usr/bin/python3 ./insta_follow_like_comment.py
45 3 * * * cd /home/user/InstaPy && /usr/bin/python3 ./insta_unfollow.py
```



