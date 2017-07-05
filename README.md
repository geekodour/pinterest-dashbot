# pinterest-dashbot

## Requirements
- Read & Understand Pinterest API. ( https://developers.pinterest.com/docs/api/users/?)
- Write a script to specifically ( interest based) auto follow/auto unfollow boards, users and
save pins on a daily basis.
- Write a script to automate daily Pinterest Postings. All the content will be given.

# Installation
In a server, wget this install script [`installdeps.sh`](https://raw.githubusercontent.com/geekodour/pinterest-dashbot/master/installdeps.sh)
it will just install all the required dependencies(some dependencies are not needed, but installed).

```
$ wget https://raw.githubusercontent.com/geekodour/pinterest-dashbot/master/installdeps.sh
$ chmod u+x installdeps.sh
$ ./installdeps.sh
```

- The script is using my `ACCESS_TOKEN`, to use it with your account you have to generate a token from [here](https://developers.pinterest.com/tools/access_token/) just make sure you give it all `4` scopes.
- The script containing the `ACCESS_TOKEN` is `/src/bot/core.py`
- after updating the token with your token
- you can run the scripts by using `python3 <script_name>`
- there are **three** primary scripts, *(save pins script is not here)*
	- create_post_from_provided.py
	- follow_users_boards.py
	- unfollow_users_boards.py
- these three scripts need to run as required. running them periodically can done using cronjobs, celery other alternatives, will be using cronjobs for now(discussed later).
- these three scripts use data from `src/bot/pintrestBot.json` where all configuration is stored.

Here is a sample of a `pinterestBot.json` file
```json
{
"board": {
  "scrolls": 5,
  "follow": 5,
  "unfollow": 10
},
"pin": {
  "scrolls": 5,
  "save": 5 // no use now
},
"user": {
  "follow": 4,
  "unfollow": 10
},
"periods": {
  "post_to_post_per_day": 2,
  "follow_freq_per_day": 2, // no use now
  "unfollow_freq_per_week": 2 // no use now
},
"posts": [
  {"note":"I am a desc","imageUrl":"http://i.imgur.com/pAiW6Ta.jpg"},
  {"note":"I am a desc","imageUrl":"http://i.imgur.com/oylBqOd.jpg"}
],
"search_terms": [ "happy" ]
}
```
**three** fields are of no use as of now, they are commented in the above snippet.

there is another file in the `/src/bot/` directory called `done_pins.json`, it contains a list done imageUrls that are already uploaded. you don't have to update that, `create_post_from_provided.py` will update and use it to not upload the same image twice. Also, initially the `done_pins.json` file should look like this, just an empty array.
```
[]
```

## Usage

### create_post_from_provided.py
takes in `posts` from `pinterestBot.json` checks with if the imageUrl is in `done_pins.json`
if not then uploads the pin with the given `note`.
- `python3 create_post_from_provided.py`
- okay if ran twice a day with `periods.posts_to_post_per_day` less than 4 (just a guess)

### follow_users_boards.py
searches pinterest once for each term in the `search_terms` array in `pinterestBot.json` then
scrolls `board.scrolls` times and gathers all the boards and their users.
Then follows boards and users based on how many users and boards to follow from `board.follow` and `user.follow`
- `python3 follow_users_boards.py`
- okay if ran once a day with 2 or less `term` elements in `search_terms` and `board.follow` and `user.follow` set to less than 10
- Important note: in pinterest, if you follow a board, you automatically follow the user
- also, `scrolls` is the number of times the page is scrolled in pinterest infinite scroll pages, the lesser the faster results you'll get


### unfollow_users_boards.py
gets all the following boards and users, then unfollows them based on `board.unfollow` and `user.unfollow`
- `python3 unfollow_users_boards.py`
- okay if ran twice a week or something

## cronjobs

use `crontab -e` and put these lines in the bottom, just change the path to where you have kept the script
you can change the timings too,

- `create_post_from_provided` runs at 2:30am and 3:30pm everyday.
- `follow_users_boards` runs at 5:25am and 5:25pm everyday.
- `unfollow_users_boards` runs at 1:30am every week on sundays.

```
30 2,15 * * * python3 /root/pinterest-dashbot/src/bot/create_post_from_provided.py
25 5,17 * * * python3 /root/pinterest-dashbot/src/bot/follow_users_boards.py
30 1 * * 0 python3 /root/pinterest-dashbot/src/bot/unfollow_users_boards.py
```

## Instruction for heroku

The bot needs a few `buildpackages` in Heroku, buildpackages are just dependencies that you can install from packagemanager in traditional server boxes.
the dependencies are:

buildpackages
```
https://github.com/heroku/heroku-buildpack-apt (apt-get package)
heroku/python (official python)
https://github.com/geekodour/heroku-buildpack-phantomjs (custom phantomjs)
```

if the heroku app is not already created you can do `heroku create`, in our case it's already created.
so there's a remote link to a heroku git repository, if you cloned this repository there won't be a remote link to heroku, you'll have to explitly set that.
to do that do:

```
git remote add heroku https://git.heroku.com/pinstabot.git

```

after doing that we can start pushing changes to our heroku app. but before that, we need to put in our buildpackages in place.
you can do that `https://dashboard.heroku.com/apps/pinstabot/settings` page, just click `add buildpack` and put in the above links one by one.
Another way to do the same is from the command line(please do a check on `heroku/python`, it should work from the command line, it works perfectly from the heroku webapp):

```
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/geekodour/heroku-buildpack-phantomjs
```

after the `buildpacks` are added, it's time to push our changes, I've added a file named `Aptfile` inside `/src/bot`. Heroku will use that file to install dependencies.

update any changes, for example if you change configurations in `/src/bot/pinterestBot.json`

type in the following commands from project root
```
git add -A
git commit -m 'i am commit message'
git push origin master (optional)
git subtree push --prefix src/bot heroku master
```

The git subtree command puts the `src/bot` directory as the root directory for your app in heroku, after the last command, the heroku deploy should be successful and there will be an `application error` shown in the **browser** if you try to go to the heroku link, this is fine because it's not a webapp/website.

now to run the scripts you can simply do

```
heroku run python create_post_from_provided.py
heroku run python follow_users_boards.py
heroku run python unfollow_users_boards.py
```

Now if you want to change the frequency or follow count or something, you can just update the `src/bot/pinterestBot.json` file accordingly and `git push` it using the subtree command.
To run these three scripts periodically, you can use the `herokuscheduler` addon that has been already installed on the app, the same commands will work for the scheduler.
i.e, these 3 are valid commands for the scheduler, just set the timing as you wish.

```
python create_post_from_provided.py
python follow_users_boards.py
python unfollow_users_boards.py
```
