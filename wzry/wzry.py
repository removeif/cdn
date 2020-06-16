# encoding: utf-8
import requests
import json
import os
import time

if __name__ == '__main__':
	# 程序开始时间
	st = time.time()
	url = 'http://pvp.qq.com/web201605/js/herolist.json'
	# 获取 json 内容
	response = requests.get(url).content

	# 提取 Json 信息
	jsonData = json.loads(response)
	# 打印查看
	print(jsonData)

	# 初始化下载数量
	x = 0

	# 设置存储图片的目录
	hero_dir = '/Users/xxx/IdeaProjects/django_test/images/1/'
	# 目录不存在则创建
	if not os.path.exists(hero_dir):
		os.mkdir(hero_dir)

	for m in range(len(jsonData)):
		# 英雄编号
		ename = jsonData[m]['ename']
		# 英雄名称
		cname = jsonData[m]['cname']
		# 循环遍历处理
		for bigskin in range(1, 15):
			# 拼接下载图片url
			picUrl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(
				ename) + '-bigskin-' + str(bigskin) + '.jpg'
			# 获取图片内容
			try:
				picture = requests.get(picUrl).content
				print picUrl
				if picture.startswith('404 page not found') or picture.startswith('The requested'): break
				# 保存图片
				jpg_ = hero_dir + cname + "-" + str(bigskin) + '.jpg'
				print jpg_
				with open(jpg_, 'wb') as f:
					f.write(picture)
					x = x + 1
					print("当前英雄【" + str(ename) + "】下载第" + str(x) + "张皮肤")
			except:
				print str(ename) + str(bigskin)
				break

print("下载" + str(x) + "张图片,总共用时" + "%.2f".format(str(time.time() - st)) + "秒。")
