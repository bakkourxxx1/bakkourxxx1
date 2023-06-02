from Lomino import Client

from json import load

from time import sleep

timesleep = input('TimeSleep:')

client = Client()

client.comId = client.get_code(input('Community Link:'))['linkInfoV2']['extensions']['community']['ndcId']

accounts = load(open(input('File Name:')))

count = 0

run_object = 0

while True:

	run_object += 1	for account in accounts:

		count += 1

		client.device = account['device']

		email = account['email']

		try:

			print(f'\n\033[7m[{email}][{client.sign_in(email,account["password"])["api:message"]}]\t[{count}][{run_object}]')

			for i in range(24):

				sleep(int(timesleep))

				print(f'\033[0;33m[generating coins{i+1}][{client.send_time_object()["api:message"]}]')

		except Exception as Error:

			print(Error)

			continue
