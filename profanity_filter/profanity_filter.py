import urllib
def read_text():
    file = open("/Users/michaelzarate/Documents/workspace_FullStack/small_projects/profanity_filter/movie_quotes.txt")
    contents = file.read()
    file.close()
    check_profanity(contents)
    return

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("There was no profanity in the document.")
    else:
        print("The could not scan the document properly...")

    return

read_text()
