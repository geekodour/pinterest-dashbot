from instapy import InstaPy

# in `link_by_tags` the `amounts` refers to how many pictures of
# each search results should the bot interact with
# if `search_term` has 2 terms in it, and amounts is set to 2
# then the bot will interact with 2*2=4 pictures total

# the bot will comment if `.set_do_comment` is True as in the following example
# the bot will follow if `.set_do_follow` is True as in the following example

# the comment and follow percentages are set accordingly in the `.set_do*` methods, if you are interacting with more
# pictures, you'll want to lower the percentage, here the percentage is set to 100 because we're
# only interacting with 4 pictures anyway

search_terms = ['#cat','#dog']
ignore_words = ['#bbf']
comments_pool = ['Cool!', 'Awesome!', 'Nice!']

InstaPy(username="geekodour",password="strongpassword",nogui=True)\
  .login()\
  .set_do_follow(enabled=True, percentage=100, times=2) \
  .set_do_comment(True, percentage=100) \
  .set_comments(comments_pool) \
  .set_ignore_if_contains(ignore_words) \
  .like_by_tags(search_terms, amount=2) \
  .end()
