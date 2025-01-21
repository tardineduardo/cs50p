# function "parse" expects a str of HTML as input,
# extracts a YouTube URL
# - The URL must be value of a src attribute of an iframe element
# return value of "parse" is a "youtu.be" equivalent as a str
# The URL will be in one of the formats below.
# Assume that the value of src will be surrounded by double quotes.
# And assume that the input will contain no more than one such URL.
# If the input does not contain any such URL at all, return None.

import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'<iframe.*https?://(?:www\.)?youtube\.com/embed/(\w*)".*</iframe>', s):
        return "https://youtu.be/" + matches.group(1)
    else:
        return "None"




#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#<iframe width="560" height="315" src="http://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>

#http://youtube.com/embed/xvFZjo5PgG0
#https://youtube.com/embed/xvFZjo5PgG0
#https://www.youtube.com/embed/xvFZjo5PgG0


if __name__ == "__main__":
    main()
