import datetime
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--new', '-n', help='New client', action='store_true')
parser.add_argument('--count', '-c', help='Count bases', action='store_true')
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

if args.new:
    now = datetime.datetime.now()
    today = str(now.day) + '.' + str(now.month) + '.' + str(now.year)
    client = input('Клиент: ')
    bases = input('Сколько баз? ')
    ticket = input('Номер тикета: ')
    with open('otchet.txt', 'a') as ouf:
        print(today, client, bases, str(ticket), sep=',', file=ouf)
    print('Успешно внесли в список обнов')

elif args.count:
    s = []
    with open('otchet.txt', 'r') as inf:
        for line in inf:
            line = line.strip()
            s.append(line.split(','))
    for a, b, c, d in s:
        print(a, b, c, d)
    print('А всего на данный момент обновлено ' + str(sum([int(bases) for today, client, bases, ticket in s])) + ' баз')