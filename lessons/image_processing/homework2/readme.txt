测试步骤在报告中

各文件对应函数解释
cut.py

  cut_by_thr(pic)  将图片根据其灰度图进行切割
  bool_black(li)    判断图中黑色的点
  cut_pic(fil)         裁剪图片且将图片存入cutout文件夹
  write_dir(st)      获得cutout文件夹应该创建的路径


histogram.py

  cnt(li, top, del_white, turn_li)  统计列表中出现次数最多的像素点
    li     		输入列表，由图片转化而来
    top 		设置像素点的个数
    del_white	是否删除图中的白点
    turn_li		是则将返回结果转为列表，否则将原始结果返回，格式是[int,tuple]

  get_pix(li)   将cnt()中的结果转为纯列表
  del_wh(li)   将cnt()处理过程中的白点去掉
  get_rgb(fil) 将图片中的红黄蓝三通道各数值出现次数进行统计
  get_shi(num)  返回输入数字所在的十位段，比如255在250段，136在130段


feature.py
  
  write_file(li, filename) 	能把三通道像素点写入文件中
  write_file_new(li, filename) 	能把三通道像素点进行转换，写入文件中，一个像素点只写一个数字
  write_features(in_file, out_file, nl, nt)  把出现次数最多的前nt个像素点写入文件中
  write_rgb_f(in_fil, out_fil, nl)    把根据get_rgb()函数得到的结果写入文件中，nl=0则不写入类标，直接写入特征，否则nl需是一个列表，存放了类标的中文名字
  read_pix_old(file)                    能把根据write_file()函数写入文件的像素读出来，返回一个列表
  write_file_li(li,name)		write_rgb_f()函数中用来写文件的函数


text_op.py
  
  get_dir(fil_nam)		根据输入返回一个目录
  get_sub_or_elem(si, li) 	输入是字符串时返回li的下标，输入整数时返回li中对应字符串


file_op.py
  
  each_file_or_dir_name(path)   根据输入路径返回其中所有目录和文件的名称
  