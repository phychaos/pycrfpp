# pycrfpp
python CRF++实现分词

# train and test
#### 训练
>训练数据采用1998年1月份人民日报的标注数据
>
>tag => B M E S
>
>训练模型调用接口
>
>crf_model = CRFModel(model='model/model')
>
>crf_model.crf_learn(filename='data/199801人民日报.data')
>
>参数model为保存模型的路径, filename为标注数据路径
>
>
#### 测试
>
>crf_model = CRFModel(model='model/model')
>
>data = crf_model.crf_test(tag_data=data)
>
#### 测试结果
>既往青霉素、链霉素、磺胺类药物过敏史<@>既_往_青霉素_、_链_霉素_、_磺_胺类_药物_过敏史
>
>对“鸡蛋”等多种食物过敏<@>对_“_鸡蛋_”_等_多种_食物_过敏
>
>对降脂药“非诺贝特”过敏<@>对_降脂_药_“_非诺贝特_”_过敏
>
>有“青霉素”过敏史、食物过敏史<@>有_“_青霉素_”_过敏史_、_食物_过敏史
>
>对磺胺类、青霉素类及巴比妥类药物过敏<@>对_磺胺类_、_青霉_素类_及_巴比_妥类_药物_过敏
>
>
# CRF++-0.58, python3安装方法
>
### 安装CRF++
>
>解压CRF++-0.58.zip
>
>cd CRF++-0.58
>
>./configure
>
>make
>
>make install
>
>终端输入： crf_learn, 出现如下信息则安装成功.
>
>
>CRF++: Yet Another CRF Tool Kit
>
>Copyright (C) 2005-2013 Taku Kudo, All rights reserved.
>
>Usage: crf_learn [options] files
>
>
> -f, --freq=INT              use features that occuer no less than INT(default 1)
>
> -m, --maxiter=INT           set INT for max iterations in LBFGS routine(default 10k)
>
> -c, --cost=FLOAT            set FLOAT for cost parameter(default 1.0)
>
> -e, --eta=FLOAT             set FLOAT for termination criterion(default 0.0001)
>
> -C, --convert               convert text model to binary model
>
> -t, --textmodel             build also text model file for debugging
>
> -a, --algorithm=(CRF|MIRA)  select training algorithm
>
> -p, --thread=INT            number of threads (default auto-detect)
>
> -H, --shrinking-size=INT    set INT for number of iterations variable needs to  be optimal before considered for shrinking. (default 20)
>
> -v, --version               show the version and exit
>
> -h, --help                  show this help and exit
>
>
###### 问题1
>crf_learn
>
>libcrfpp.so--cannot open shared object file: No such file or directory
>
>
>1、用ln将需要的so文件链接到/usr/lib或者/lib这两个默认的目录下边
>
> ln -s /where/you/install/lib/*.so /usr/lib
>
> sudo ldconfig
>
>
>2、修改LD_LIBRARY_PATH
>
>export LD_LIBRARY_PATH=/where/you/install/lib:$LD_LIBRARY_PATH
>
>sudo ldconfig
>
>
>3、修改/etc/ld.so.conf，然后刷新
>
>vim /etc/ld.so.conf
>
>add /where/you/install/lib
>
>sudo ldconfig
>
>默认安装路径为 /usr/local/lib
>
###### 问题2
>
>/usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.20' not found (required by */3rd-party/protobuf-2.4.1/src/.libs/libprotoc.so.7)
>
>
>解决方案步骤：
>
>1、下载：libstdc++.so.6.0.20， 复制到/usr/local/lib64/     
>
>(libstdc++.so.6.0.20在test目录下)
>
>
>2、sudo cp /usr/local/lib64/libstdc++.so.6.0.20 /usr/lib64
>
>
>3、sudo rm -rf /usr/lib64/libstdc++.so.6
>
>
>4、sudo ln -s /usr/lib64/libstdc++.so.6.0.20 /usr/lib64/libstdc++.so.6
>
>
### 安装python3 CRFPP接口
>
>cd python
>
>python3 setup.py build
>
>python3 setup.py install
>
>测试, cd test
>
>python3 test.py
>
>结果:
>
>
>测试python3 CRFPP...
>
>
>只	B
>
>有	E
>
>站	S
>
>在	S
>
>百	B
>
>姓	E
>
>的	S
>
>出	B
>
>发	M
>
>点	E
>
>，	S
>
>达	B
>
>到	E
>
>“	S
>
>你	S
>
>就	S
>
>是	S
>
>我	S
>
>、	S
>
>我	S
>
>就	S
>
>是	S
>
>你	S
>
>”	S
>
>，	S
>
>才	S
>
>可	B
>
>能	E
>
>把	S
>
>工	B
>
>作	E
>
>真	B
>
>正	E
>
>做	S
>
>到	B
>
>位	E
>
>。	S
>
>
>已成功安装python3 CRFPP！
>
>
###### 问题1：
>
>running install
>
>running build
>
>running build_py
>
>running build_ext
>
>building '_CRFPP' extension
>
>x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/usr/include/python3.5m -c CRFPP_wrap.cxx -o build/temp.linux-x86_64-3.5/CRFPP_wrap.o
>
>cc1plus: warning: command line option ‘-Wstrict-prototypes’ is valid for C/ObjC but not for C++
>
>CRFPP_wrap.cxx:149:20: fatal error: Python.h: 没有那个文件或目录
>
>compilation terminated.
>
>error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
>
>
>解决方法
>
>安装apt-get install python3-dev
