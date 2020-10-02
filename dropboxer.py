import re, sys, requests, pyperclip

# py dropboxer.py <dropbox link> <alias>
def main(argv):
    dropboxlink, alias = argv[0], argv[1]
    ptn = re.match(r"https:\/\/www\.dropbox\.com\/s\/(.+\/.+)\?dl=0", dropboxlink)

    if (ptn[1]):
        dropboxdl = f'https://dl.dropboxusercontent.com/s/{ptn[1]}'
        resp = requests.get(f'https://tinyurl.com/api-create.php?url={dropboxdl}&alias={alias}')
        
        if (resp.status_code == 200):
            pyperclip.copy(resp.text)
            print(f'{pyperclip.paste()} was copied to the clipboard')
        else:
            print(f'{resp.status_code}: {resp.text}')
    else:
        print("Link doesn't match pattern")


if __name__ == "__main__":
    main(sys.argv[1:])
