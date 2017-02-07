import datetime
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--new', '-n', help='New client', action='store_true')
parser.add_argument('--count', '-c', help='Count bases', action='store_true')
parser.add_argument('--show', '-s', help='Show updated bases', action='store_true')
parser.add_argument('--archive', '-a', metavar='Месяц', help='Use with caution! Archive current otchet.txt to месяц.txt and clean it')
args = parser.parse_args()

def count():
    s = []
    with open('otchet.txt', 'r') as inf:
        for line in inf:
            line = line.strip()
            s.append(line.split(','))
    return 'Всего за текущий период обновлено ' + str(sum([int(bases) for today, client, bases, ticket in s])) + ' баз'

def show():
    s = []
    with open('otchet.txt', 'r') as inf:
        for line in inf:
            line = line.strip()
            s.append(line.split(','))
        for a, b, c, d in s:
            print(a, b, c, d)

def new():
    now = datetime.datetime.now()
    today = str(now.day) + '.' + str(now.month) + '.' + str(now.year)
    client = input('Клиент: ')
    bases = input('Сколько баз? ')
    ticket = input('Номер тикета: ')
    with open('otchet.txt', 'a') as ouf:
        print(today, client, bases, str(ticket), sep=',', file=ouf)
    print('Успешно внесли в список обнов')

def archive():
    with open('otchet.txt') as fin:
        with open(args.archive + '.txt', 'w') as fout:
            for line in fin:
                fout.write(line)
            fout.write('\n')
            fout.write(count())
    print('Отчет за {} создан'.format(args.archive))
    with open('otchet.txt', "w"):
        pass

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

if args.new:
    new()

elif args.count:
    print(count())

elif args.show:
    show()

elif args.archive is not None:
    archive()
