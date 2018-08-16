def get_word(webster):
    ''' (dict) -> str '''
    while True:
        choice = input('What word do you want to look up? ')
        if choice in webster.keys():
            return choice
        print('not an option!')
        print('choices are:', '-'.join(webster.keys()))


def main():
    webster = {
        "Aardvark": "A star of a popular children's cartoon show.",
        "Baa": "The sound a goat makes.",
        "Carpet": "Goes on the floor.",
        "Dab": "A small amount.",
        "Ray": "A Base Camp student"
    }

    choice = get_word(webster)
    print(webster[choice])


if __name__ == '__main__':
    main()
