# 第一个博客网站

blog
基于django2.0和bootstrap3制作,基本完成于2018年8月28日,基本后台逻辑已经实现,包括用户注册登陆修改等以及博客的发表和评论.这个也算是自己做的第一个项目里面还有一些内容不是特别清楚,需要多加巩固,前端页面比较简陋,研究生刚开学还没有进行大面积的页面修改,希望在接下来的半年能对逻辑进行一定的修改然后把前端页面做的更好看多一点.                    ---2018.9.4

blog
1.django自带的数据库是sqlite，但是由于我自己学的是mysql而且杨老师的教程中也使用的是mysql我就把数据库换成了mysql。<br/>
2.修改了自定义的错误页面，在本地运行时不管什么错误都返回的是状态码为500的错误。（服务器上不好使？？？还在查明原因）
                                  ---2018.9.21

blog
1.服务器后台编辑博客无法上传图片，发现问题是由于没有给media文件权限.可以用 chmod -R 777 media。
2.生产环境中将debug=False，保证上线安全，而且可以自定义错误页面。
                                  ---2018.12.5
