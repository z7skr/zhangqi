# linux 命令格式
```
command [options] [arguments]
```

# 文件目录操作

## ls

list, 查看文件, 文件权限, 目录信息

options:
- -l, long format
- -a, all
- -A, all 但不列出 . 和 ..
- -1, 单行显示
- -lh, long format, human-readable
- -i, 显示 inode number
- -R, recursive
- -r, reverse
- -S, 按大小降序
- -t, 按时间递增
- -F, 目录加 /

examples:
- `ls -lhSr` 按大小递增
- `ls -ltr p*` p 开头, 按时间降序
- `ls -lR /home/peidachang` 递归列出子文件夹的内容
- `ls -l t*` 列出所有 t 开头的文件和文件夹
- `ls -F ~ | grep /$` 只列出 home 里的目录
- `ls -l ~ | grep ^d` 列出 home 里子目录的详细情况


## cd

change directory

options:
- -L, 如果切换的目标目录是一个符号链接, 则直接切换到符号链接名所在的目录
- -P, 如果切换的目标目录是一个符号链接, 则直接切换到符号链接指向的目标目录

examples:
- `cd -`, 回到跳转之前的目录


## pwd

print working directory

options:
- -P, 显示出实际路径, 而非使用连接（link）路径


## mkdir

make directories

options:
- -p, 递归创建多级目录
- -m, mode, 建立目录的同时设置目录的权限
- -v, verbose

examples:
- `mkdir -vp scf/{lib/, bin/, doc/{info, product}, logs/{info, product}, service/deploy/{info, product}}`


## rm

remove

options:
- -f, force, 不提示
- -i, interactive, 交互式
- -r, recursive
- -v, verbose

examples:
- `rm *.jpg` 删除所有 jpg 格式文件
- `rm result*` 删除所有 result 开头的文件


## rmdir

remove directories, 删除空目录

options:
- -p, 递归删除空目录


## mv

move or rename

options:
- -f, force, 默认覆盖
- -i, interactive, 询问是否覆盖
- -n, 默认不覆盖


## cp

copy

options:
- -f, force
- -i, interactive
- -r, -R, recursive
- -L, 跟随源文件中的符号链接
- -P, default, 不跟随源文件中的符号链接

examples:
- `cp -R dir1 dir2/`, 复制目录
- `cp -r file1 file2 file3 dir` 复制多个文件到 dir


## touch

touch命令有两个功能：一是创建新的空文件, 二是改变已有文件的时间戳属性. 

options:
- -a, 改读取时间
- -m, 改修改时间
- -d, 指定时间

examples:
- `touch file{1..5}.txt` 批量创建


## cat

concatenate and print files, 连接文件或标准输入并打印, 常用来显示文件内容, 或者将几个文件连接起来显示, 或者从标准输入读取内容并显示, 它常与重定向符号配合使用. 

options:
- -b, 显示行号（非空)
- -n, 显示行号
- -v, 显示不可打印的字符
- -e, 显示不可打印字符, 结尾$

examples:
- `cat -n file1 file2` 连接两个文件并显示行号
- `cat -n file1 > newfile` 显示 file1 和行号, 并写入 newfile(包括行号)
```
# heredoc 创建文本
cat > log.txt << EOF
> Hello
> World
> pwd: $(pwd) # $(command) 可以输入 bash 命令
> EOF # 输入 EOF 结束并创建文件
```

tac, 就是 cat 反过来


## nl

计算行号


## more

类似于 cat, 不过是逐页阅读

options:
- +n, 从第 n 行开始显示
- +/pattern, 搜索
- -p, 清屏换页. 默认是滚屏换页.
- -s, 空行合并

operations:
- space/f/ctrl+f, 下一页
- b/ctrl+b, 上一页
- =, 输出当前行号
- :f, 输出文件名和行号
- !<command>, shell 命令
- q, quit


## less

类似于 more, 但是功能更加强大. 而且不会像 more 一样一次加载整个文件. 

options:
- -b, 设置缓冲区的大小
- -e, 当文件显示结束后, 自动离开
- -f, 强迫打开特殊文件, 例如外围设备代号、目录和二进制文件
- -g, 只标志最后搜索的关键词
- -i, 忽略搜索时的大小写
- -m, 显示类似more命令的百分比
- -N, 显示每行的行号
- -o, 将 less 输出的内容在指定文件中保存起来
- -s, 显示连续空行为一行
- -S, 在单行显示较长的内容, 而不换行显示

examples:
- `ps -ef |less` 查看进程信息传给 less 查看
- `history | less`


## head

options:
-c <字节>, 字节数, 可以像 python 的索引一样用负数
-n <行数>, 行数


## tail

options:
- -f, 循环读取


# 文件查找命令

## which

查看可执行文件的位置. which 指令会在 PATH 变量指定的路径中, 搜索某个系统命令的位置, 并且返回第一个搜索结果. 

options:
- -n, 指定文件名长度, 指定的长度必须大于或等于所有文件中最长的文件名. 
- -p, 与-n参数相同, 但此处的包括了文件的路径. 
- -w, 指定输出时栏位的宽度. 
- -V, 显示版本信息


## whereis

whereis 命令只能用于程序名的搜索, 而且只搜索二进制文件（参数-b）、man说明文件（参数-m）和源代码文件（参数-s）. 如果省略参数, 则返回所有信息. 

options:
- -b, for binaries
- -m, for manuals
- -s, for sources
- -B, -M, -S, 分别指定路径


## locate

快速查找档案, 索引表由 cron daemon 每天建立一次, 所以最新的文件可能搜不到, 最近删除的文件还能匹配到. 配置在 /etc/crobtab, 可以改. 也可以强制更新. 

locate [OPTION]... PATTERN1 PATTERN2 ...

options:
- -A, all 匹配所有 PATTERN, 默认只需要匹配一个即可
- -w, wholename 匹配完整的 PATTERN
- -c, count 输出匹配到的文件数
- -e, existing 只匹配此刻仍存在的文件
- -L, follow -e 时跟踪符号链接
- -P, nofollow
- -l n, limit 只列出 n 个就停止
- -r, regex

examples:
- `locate /etc/sh` 搜索etc目录下所有以sh开头的文件


## find

在目录中查找

find pathname -options [-print -exec -ok ...]

- pathname: 省略就是当前 
- -exec: 后面跟的是 command 命令, 以 `\;` 终止, {} 表示找到的文件名
- -ok: 交互式 exec

options:
- -name, 按文件名查找文件
- -perm, 权限
- -user
- -group
- -mtime -n/+n, -n 表示 n 天以内, +n 表示 n 天以前
- -newer file1 ! file2, 比 file2 新但比 file2 旧的文件
- -type, d for dir, f for file, p for 管道文件, l for link
- -size n[cwbkMG], 大小在 n 块以内的文件. 改单位: c for byte, w for two-byte words, k for Kibibytes, M for Mebibytes, G for Gibibytes 
- -follow
- amin n, 最后 n 分钟访问过的文件
- atime n, 最后 n 天访问过的文件
- cmin n, 最后 n 分钟被改变文件状态的文件
- ctime n
- mmin n, 最后 n 分钟被改变文件数据的文件
- mtime n

examples:
- `find -amin -20` 最近 20 分钟内访问过的文件
- `find . -name *.sh` 目录下的 sh 文件
- `find /opt/soft/test/ -perm 777`
- `find . -type f -name "*.log"`
- `find . -type d | sort` 并排序
- `find . -size +1000c`
- `find . -type f -exec ls -l {} \;` 找出普通文件并 ls -l {files}
- `find . -type f -mtime +14 -exec rm {} \; ` 查找更改时间在n日以前的文件并删除它们
- `find . -name *.log -mtime +5 -ok rm {} \;` 查找更改时间在n日以前的文件并删除它们, 在删除之前先给出提示
- `find /etc -name passwd* -exec grep root {} \;`
- `find . -name *.log -exec mv {} .. \;` 查找文件移动到指定目录
- `find . -name *.log -exec cp {} test3 \;` 


# 归档打包

## tar

打包

tar [必要参数] [选择参数] [文件] 

options:
-c, create 建立新的压缩文件
-r, append 添加文件到已经压缩的文件
-u, update 添加改变了和现有的文件到已经存在的压缩文件
-x, extract 从压缩的文件中提取文件
-z 支持gzip解压文件
-j 支持zip2解压文件
-Z 支持compress解压文件
-v, verbose 显示操作过程
-f 指定压缩文件

examples:
```
# .tar
解包：tar xvf FileName.tar
打包：tar cvf FileName.tar DirName
# .tar.gz 和 .tgz
解压：tar zxvf FileName.tar.gz
压缩：tar zcvf FileName.tar.gz DirName
# .tar.bz2
解压：tar jxvf FileName.tar.bz2
压缩：tar jcvf FileName.tar.bz2 DirName
# .tar.Z
解压：tar Zxvf FileName.tar.Z
压缩：tar Zcvf FileName.tar.Z DirName
# .gz
解压1：gunzip FileName.gz
解压2：gzip -d FileName.gz
压缩：gzip FileName
# .bz2
解压1：bzip2 -d FileName.bz2
解压2：bunzip2 FileName.bz2
压缩： bzip2 -z FileName
# .Z
解压：uncompress FileName.Z
压缩：compress FileName
# .zip
解压：unzip FileName.zip
压缩：zip FileName.zip DirName
压缩一个目录使用 -r 参数
# .rar
解压：rar x FileName.rar
压缩：rar a FileName.rar DirName
```


## gzip


# 权限

## chmod

change the permissions mode of a file, change mode

chmod 用于修改修改访问控制权限。有两种模式，一种是采用权限字母和操作符表达式，另一种是采用数字。

权限所属和权限种类见 <basic.md>

chmod [-cfvR] mode file

权限范围：
- u ：目录或者文件的当前的用户
- g ：目录或者文件的当前的群组
- o ：除了目录或者文件的当前用户或群组之外的用户或者群组
- a ：所有的用户及群组

权限代号：
- r ：读权限，用数字4表示
- w ：写权限，用数字2表示
- x ：执行权限，用数字1表示
- \- ：删除权限，用数字0表示
- s ：特殊权限 

options:
- -c 当发生改变时，报告处理信息
- -f, force 错误信息不输出
- -R, recursive 处理指定目录以及其子目录下的所有文件
- -v, verbose 运行时显示详细处理信息
- mode, 有两种设定方法:
    - 文字设定法, chmod [who][+-=][mode] file
    - 数字设定法, chmod [mode] file

examples:
- `chmod a+x file` 给所有用户增加可执行
- `chmod ug+w,o-x file` 分别增减权限
- `chmod u=x file` 撤销 u 的权限，重新赋予 u x 权限
- `chmod -R u+x dir`
- `chmod 751 file` 给 u rwx, 给 g rx, 给 o x


## chgrp

change group


## chown

change owner


# 磁盘

## df

df [options]

显示指定磁盘文件的可用空间。如果没有文件名被指定，则所有当前被挂载的文件系统的可用空间将被显示。

options:
- -a, all
- -h, human-readable, 1KB=1024B
- -H, 同上, but 1KB=1000B
- -i, inode
- -l, local 只显示本地


## du

du [options] [file]

显示文件夹文件占用空间, 可以多个文件

-a, all
-b, byte, 太小时, 以 byte 为单位
-c, total, 还显示总和
-s, summary, 只显示总和
-k, KB
-m, MB
-h
-H
--exclude=<.>, 跳过某些


# 性能监控和优化命令

## htop

## free

显示Linux系统中空闲的、已用的物理内存及swap内存,及被内核使用的buffer.

free [options]

options:
-[bkmg]
-s n, 每 n 秒刷新一次
-t, total

desc:
- total:总计物理内存的大小。
- used:已使用多大。
- free:可用有多少。
- Shared:多个进程共享的内存总额。
- Buffers/cached:磁盘缓存的大小。


## vmstat

Virtual Meomory Statistics


## lsof


# 网络命令

## ifconfig 

interfaces config


## route

显示和操作 IP 路由表


## ping


## netstat


## ss

socket statistics


## 




