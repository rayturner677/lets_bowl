def main():
    game = []
    total_frames = []
    final = sum(total_frames)
    while True:
        turn = int(input('How many pins did you knock down?'))
        second_turn = int(input('How many pins did knock down this time?'))
        if turn > 11:
            for frame in range(1, 10):
                print('frame', frame)
                game.append([turn])
                total = turn + second_turn
                final = sum(total_frames)
                print('frame', frame, ':', total)
                print(game)
            else:
                print('invalid response')

            if second_turn > 11:
                for frame in range(1, 10):
                    print('frame', frame)
                    game.append([second_turn])
                    total = turn + second_turn
                    final = sum(total_frames)

                    print('frame', frame, ':', total)
                    print(game)
                else:
                    print('invalid response')

                    total_frames.append(total)

        print(final)


if __name__ == '__main__':
    main()
