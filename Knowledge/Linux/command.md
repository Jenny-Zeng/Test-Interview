# 常用 Linux 命令
来来来，我们一起回忆下常用的Linux命令
1. mkdir、touch、open -e、vim、cat、grep
2. ls、ls -a、ls -al、ll、ls -1 | tail -n 5 #列出最新5个文件
3. 端口 lsof
4. chmod +x、rm -rf、du +文件名、mv、cp、history、
5. ps -ef、ps -ef ｜ grep pid(进程名)
    使用ps命令结合排序选项来列出当前占用CPU最高的进程
    <ps -eo pid,pcpu,comm | sort -k2 -nr | head>
