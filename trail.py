def main():

    game = []
    total_frames = []
    final = sum(total_frames)

    for frame in range(1, 10):
        print('frame', frame)
        first_roll = int(input('How many pins did you knock down?'))
        second_roll = int(input('How many pins did knock down this time?'))
        while first_roll < 11 and second_roll < 11:
            game.append([first_roll, second_roll])
            total = first_roll + second_roll
            total_frames.append(total)
            print('frame', frame, ':', total)
            print(game)
            break

        if first_roll == 10:
            print('strike')
            if frame + 1 < len(game):
                total = 0
                next_ball = game[frame + 1][0]
                next_ball2 = game[frame + 1][1]
                total += 10 + next_ball + next_ball2
                total_frames.append(total)
                print(total)

        if second_roll == 10 - first_roll:
            print('spare')
            if frame + 1 < len(game):
                total = 0
                next_ball = game[frame + 1][0]
                total += 10 + next_ball
                total_frames.append(total)
                print(total_frames)

        else:
            print('invalid response')

        final = sum(total_frames)
        print(final)


if __name__ == '__main__':
    main()
