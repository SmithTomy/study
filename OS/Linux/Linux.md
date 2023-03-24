# Linux系统命令

### 学习路线

![学习路线](D:\Workspace\study\OS\Linux\学习路线.png)



### 系统进化史

![UNIX进化史](D:\Workspace\study\OS\Linux\UNIX进化史.png)

### 文件目录

![Linux文件目录](D:\Workspace\study\OS\Linux\Linux文件目录.png)





### 文件查找

​	whereis

​	which

​	locate

​	find

​	

### 文件打包与解压缩

​	

#### 	zip

```shell
#压缩
cd /home/shiyanlou
zip -r -q -o -e shiyanlou.zip /home/shiyanlou/Desktop 
//r表示递归打包其子目录下的所有内容， -q表示安静模式 ,-o 表示输出文件, -e表示加密压缩
du -h shiyanlou.zip   //查看打包后文件的大小
file shiyanlou.zip  //查看文件的属性

zip -r -l -o shiyanlou.zip /home/shiyanlou/Desktop  
// -l 参数将 LF 转换为 CR+LF 来达到以上目的。 Windows 为 CR+LF（Carriage-Return+Line-Feed：回车加换行），而在 Linux/Unix 上为 LF（换行），

#解压缩
unzip filepath/filename

unzip -q shiyanlou.zip  #解压缩到当前目录
unzip -q shiyanlou.zip -d ziptest #解压缩到指定的目录，没有该目录则创建该目录
unzip -l shiyanlou.zip #查看压缩包的内容
unzip -O GBK 中文压缩文件.zip #指定编码格式
```

#### 	tar



```shell
tar -P -vcf shiyanlou.tar /home/shiyanlou/Desktop #-P 保留绝对路径符，-c 表示创建一个 tar 包文件，-f 用于指定创建的文件名，-v 可视化输出打包的文件
tar -xf shiyanlou.tar -C tarlib #x 解压缩 -C指定路径已存在的目录
```

​	

| 压缩文件格式 | 参数 |
| ------------ | ---- |
| `*.tar.gz`   | `-z` |
| `*.tar.xz`   | `-J` |
| `*tar.bz2`   | `-j` |

​	创建 tar 文件的基础上添加 `-z` 参数，使用 `gzip` 来压缩文件

```shell
tar -czf shiyanlou.tar.gz /home/shiyanlou/Desktop
tar -xzf shiyanlou.tar.gz #z表示*.tar.gz
#更改压缩文件格式的参数即可指定压缩工具
```