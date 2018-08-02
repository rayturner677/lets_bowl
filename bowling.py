def main():
    game = []
    total_frames = []
    final = sum(total_frames)

    for frame in range(1, 10):
        print('frame', frame)
        turn = int(input('How many pins did you knock down?'))
        second_turn = int(input('How many pins did knock down this time?'))

        while turn < 11 and second_turn < 11:
            game.append([turn, second_turn])
            total = turn + second_turn
            total_frames.append(total)
            final = sum(total_frames)
            print('frame', frame, ':', total)
            print(game)
            print(final)
            break
        else:
            print('invalid response')


if __name__ == '__main__':
    main()
