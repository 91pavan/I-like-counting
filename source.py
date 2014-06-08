import praw
import re
from time import sleep
from getpass import getpass

def main(r, done):
    comments =   r.get_comments('Insert subreddits appended by a '+' sign')
    last_comment = list(comments)[0]
    try:
        last_no = re.search(r'[\d,]+', last_comment.body).group()
        last_no = int(last_no.replace(',',''))
    except ValueError:
        return
    except AttributeError:
        return

    if str(last_comment.author) != 'I_like_counting' \
            and last_comment.id not in done:
        last_comment.reply('{:,}'.format(last_no+1)), last_comment.upvote()
        print 'Last number: ' + str(last_no)
        print 'replied with: ' + str(last_no+1)
        done.append(last_comment.id)

if __name__ == '__main__':
    r = praw.Reddit(user_agent='counting bot')
    r.login('I_like_counting', 'INSERTPASSWORD')

    print 'Exit with CTRL-C'
    done =[]
    while True:
        main(r, done)
        sleep(7)
