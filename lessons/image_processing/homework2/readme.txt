���Բ����ڱ�����

���ļ���Ӧ��������
cut.py

  cut_by_thr(pic)  ��ͼƬ������Ҷ�ͼ�����и�
  bool_black(li)    �ж�ͼ�к�ɫ�ĵ�
  cut_pic(fil)         �ü�ͼƬ�ҽ�ͼƬ����cutout�ļ���
  write_dir(st)      ���cutout�ļ���Ӧ�ô�����·��


histogram.py

  cnt(li, top, del_white, turn_li)  ͳ���б��г��ִ����������ص�
    li     		�����б���ͼƬת������
    top 		�������ص�ĸ���
    del_white	�Ƿ�ɾ��ͼ�еİ׵�
    turn_li		���򽫷��ؽ��תΪ�б�����ԭʼ������أ���ʽ��[int,tuple]

  get_pix(li)   ��cnt()�еĽ��תΪ���б�
  del_wh(li)   ��cnt()��������еİ׵�ȥ��
  get_rgb(fil) ��ͼƬ�еĺ������ͨ������ֵ���ִ�������ͳ��
  get_shi(num)  ���������������ڵ�ʮλ�Σ�����255��250�Σ�136��130��


feature.py
  
  write_file(li, filename) 	�ܰ���ͨ�����ص�д���ļ���
  write_file_new(li, filename) 	�ܰ���ͨ�����ص����ת����д���ļ��У�һ�����ص�ֻдһ������
  write_features(in_file, out_file, nl, nt)  �ѳ��ִ�������ǰnt�����ص�д���ļ���
  write_rgb_f(in_fil, out_fil, nl)    �Ѹ���get_rgb()�����õ��Ľ��д���ļ��У�nl=0��д����ֱ꣬��д������������nl����һ���б������������������
  read_pix_old(file)                    �ܰѸ���write_file()����д���ļ������ض�����������һ���б�
  write_file_li(li,name)		write_rgb_f()����������д�ļ��ĺ���


text_op.py
  
  get_dir(fil_nam)		�������뷵��һ��Ŀ¼
  get_sub_or_elem(si, li) 	�������ַ���ʱ����li���±꣬��������ʱ����li�ж�Ӧ�ַ���


file_op.py
  
  each_file_or_dir_name(path)   ��������·��������������Ŀ¼���ļ�������
  