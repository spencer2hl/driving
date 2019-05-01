country = input('请问你是哪国人：')
age = input('请输入你的年龄：')
age = int(age)
if country == '台湾':
	if age >= 18:
		print('你可以考驾照')
	else:
		print('你还不能考驾照')