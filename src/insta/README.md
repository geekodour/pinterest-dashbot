```
$ apt-get install git
$ git clone https://github.com/timgrossmann/InstaPy.git
$ cd InstaPy/scripts/
$ ./unix.sh
```
after the installation is done, navigate to the root directory.
you'll see `./insta_follow_like_comment.py` and `./insta_unfollow.py`
they do what they are named, succient comments are added to both the files to explain how to configure it.

## conjobs
you can put the two scripts on cron
the guide is here: https://github.com/timgrossmann/InstaPy#automate
an example:
this will run the follow script at 4:45 and the unfollow script at 3:45

```
45 4 * * * cd /home/user/InstaPy && /usr/bin/python3 ./insta_follow_like_comment.py
45 3 * * * cd /home/user/InstaPy && /usr/bin/python3 ./insta_unfollow.py
```



