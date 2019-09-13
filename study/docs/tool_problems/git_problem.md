1.Often used command in git:

    git clone https://..... or git://......
    git pull origin master

    git add [single file]
    git add -A  EQUALS TO  git add .;git add -u

    git commit -m "some message"

    git push
    
2.Git push requires username and password
    
    账号保存

    如果不做设置的话，每次提交的时候，都会询问你填写密码。于是我们先来把这个设置好。

    【Step3.1-添加环境变量】

    我的电脑 - 属性 - 高级系统设置 - 环境变量 - 新建变量

    变量名HOME，变量值%USERPROFILE%

    【Step3.2-创建账号文件】

    开始 - 运行 中打开%Home%，即windows的管理员账号文件夹。

    新建一个名为“_netrc”的文件，填写你要保存的服务器地址及账号密码，保存。

    machine github.com
    login jdz1993
    password secret

    machine api.github.com
    login jdz1993
    password secret

3.安装git for windows，以及之后的一系列配置

    http://www.cnblogs.com/iruxu/p/gitgui.html
    
4.git配置代理

    git config --global https.proxy http://xxx.company.com:port
    git config --global http.proxy http://xxx.company.com:port
   
5.git中文乱码问题
    
    git config --global core.quotepath false          # 显示 status 编码
    git config --global gui.encoding utf-8            # 图形界面编码
    git config --global i18n.commit.encoding utf-8    # 提交信息编码
    git config --global i18n.logoutputencoding utf-8  # 输出 log 编码
    export LESSCHARSET=utf-8
    
    alias ls="ls --show-control-chars --color"

    参考 http://howiefh.github.io/2014/10/11/git-encoding/