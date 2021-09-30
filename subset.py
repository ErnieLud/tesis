# coding=utf-8
import os
import numpy as np
import open3d as o3d
import math
objects = [
'0001','0002','0003','0004','0005','0006','0007','0008','0009','0010','0011','0012','0013','0014','0015','0016','0017','0018','0019','0020','0021','0022','0023','0024','0025','0026','0028','0029','0030','0031','0032','0034',
'0035','0036','0037','0038','0039','0040','0041','0042','0043','0044','0045','0046','0048','0049','0050','0051','0052','0053','0054','0055','0057','0058','0060','0061','0062','0063','0064','0065','0066','0068','0070','0071',
'0072','0074','0075','0076','0077','0078','0079','0080','0081','0082','0083','0084','0086','0087','0088','0089','0090','0091','0092','0093','0094','0096','0097','0098','0099','0101','0103','0106','0107','0109','0110','0111',
'0112','0113','0114','0115','0116','0117','0118','0119','0120','0121','0122','0123','0124','0125','0126','0127','0128','0129','0130','0131','0132','0133','0134','0135','0136','0137','0138','0139','0140','0141','0142','0143',
'0144','0145','0146','0147','0148','0149','0150','0151','0152','0153','0154','0155','0156','0157','0158','0159','0160','0161','0162','0163','0164','0165','0166','0167','0168','0169','0170','0171','0172','0173','0174','0175',
'0176','0177','0178','0179','0180','0181','0182','0183','0184','0185','0186','0187','0188','0189','0190','0191','0192','0193','0194','0195','0196','0197','0198','0199','0201','0202','0203','0204','0205','0206','0207','0208',
'0209','0210','0211','0212','0213','0214','0215','0216','0217','0218','0219','0220','0221','0222','0225','0226','0227','0228','0230','0231','0234','0235','0236','0237','0238','0239','0240','0241','0242','0243','0244','0245',
'0246','0249','0250','0251','0252','0253','0258','0259','0260','0261','0262','0263','0264','0265','0266','0267','0268','0269','0271','0272','0273','0274','0275','0276','0277','0279','0280','0282','0283','0285','0286','0287',
'0288','0289','0290','0291','0292','0293','0294','0295','0296','0297','0298','0299','0300','0303','0304','0305','0306','0307','0308','0309','0311','0312','0313','0314','0315','0316','0317','0320','0321','0322','0324','0332',
'0333','0334','0335','0336','0337','0338','0339','0340','0341','0342','0350','0352','0353','0354','0355','0356','0357','0358','0359','0360','0361','0362','0363','0364','0365','0366','0367','0368','0369','0370','0371','0372',
'0373','0374','0375','0376','0377','0378','0379','0380','0381','0382','0383','0385','0386','0387','0388','0389','0390','0391','0392','0393','0394','0395','0396','0397','0398','0402','0403','0405','0406','0407','0409','0410',
'0411','0412','0413','0414','0415','0416','0417','0418','0420','0428','0430','0431','0432','0433','0434','0435','0437','0438','0439','0440','0442','0446','0447','0448','0450','0452','0453','0454','0457','0458','0464','0465',
'0467','0468','0470','0474','0477','0478','0481','0482','0483','0484','0485','0486','0487','0488','0489','0490','0491','0495','0496','0497','0499','0500','0501','0503','0505','0507','0512','0513','0514','0515','0516','0517',
'0518','0519','0520','0521','0523','0526','0527','0528','0530','0532','0533','0534','0535','0536','0538','0539','0541','0542','0543','0544','0545','0546','0547','0548','0549','0550','0551','0552','0553','0554','0556','0557',
'0558','0561','0571','0572','0574','0575','0576','0577','0578','0579','0581','0582','0583','0584','0585','0586','0587','0588','0590','0591','0593','0595','0596','0597','0598','0599','0600','0601','0602','0603','0604','0605',
'0606','0607','0608','0611','0612','0614','0615','0616','0617','0618','0619','0620','0621','0622','0623','0624','0625','0626','0627','0628','0629','0631','0632','0636','0637','0638','0639','0640','0642','0643','0644','0645',
'0646','0647','0648','0649','0650','0651','0652','0653','0654','0655','0656','0657','0658','0659','0660','0661','0662','0663','0664','0665','0666','0667','0668','0669','0670','0671','0672','0673','0674','0675','0676','0677',
'0679','0680','0681','0682','0683','0684','0685','0686','0687','0689','0690','0691','0692','0693','0697','0699','0700','0701','0702','0703','0704','0705','0707','0708','0709','0710','0711','0712','0713','0714','0715','0716',
'0717','0718','0719','0720','0721','0722','0723','0726','0727','0728','0729','0730','0731','0732','0733','0734','0735','0736','0737','0738','0739','0740','0741','0742','0743','0744','0745','0746','0747','0748','0749','0750',
'0751','0752','0753','0754','0755','0756','0757','0758','0759','0760','0761','0763','0764','0769','0770','0772','0773','0774','0776','0777','0778','0781','0784','0785','0786','0788','0790','0791','0792','0796','0798','0799',
'0804','0805','0806','0807','0808','0809','0810','0811','0812','0813','0814','0815','0816','0817','0818','0819','0820','0822','0823','0825','0826','0827','0828','0829','0830','0831','0832','0833','0842','0853','0855','0856',
'0857','0858','0859','0860','0861','0862','0863','0864','0865','0866','0867','0868','0869','0870','0871','0872','0873','0874','0876','0877','0878','0879','0880','0881','0882','0883','0884','0885','0886','0887','0888','0889',
'0890','0891','0893','0894','0895','0896','0897','0898','0899','0900','0901','0902','0903','0904','0905','0906','0907','0908','0909','0910','0911','0912','0913','0914','0915','0916','0917','0918','0919','0920','0923','0924',
'0926','0928','0929','0930','0931','0932','0933','0934','0935','0936','0937','0938','0939','0940','0941','0942','0943','0944','0946','0953','0954','0955','0956','0957','0958','0959','0960','0961','0962'
]
# objects = ['0001']
# definimos el path donde guardará el subset de pseudo-objetos
subset_path = "/data/esumoso/backups/objs/genPlys/70309660/ply"
category_path = "/data/esumoso/backups/objs/genPlys/70309660"
# definimos el path de donde se leerán los ply's y txt's originales
plys_path = "/data/esumoso/backups/objs/genPlys/70309649/ply"
# definimos variables: ángulo de rotación y cantidad de loops
sexagesimal = 60.0
loops = 6
# calculamos el valor de rotación por loop en radianes
# para realizar una rotación horaria necesitamos la diferencia con 360, pues la matriz de rotación es en sentido antihoraria
diferencia = 360.0 - sexagesimal
radian = diferencia * (math.pi / 180.0)
# creamos la matriz de rotación (sentido antihorario)
R = np.array([[math.cos(radian), 0.0, math.sin(radian)],
	[0.0, 1.0, 0.0],
	[-math.sin(radian), 0.0, math.cos(radian)]])
counter = 0 # contador externo 1 - 4082
for obj in objects:
	# leemos el ply
	os.chdir(plys_path)
	ply_file = o3d.io.read_point_cloud(obj+".points.ply")
	os.chdir(subset_path)
	for loop in range(loops):
		# actualizamos contador externo
		counter += 1
		str_counter = str(counter).zfill(4)
		# rotamos el objeto (la rotación afecta la malla original)
		if loop != 0:
			ply_file.rotate(R, ply_file.get_center())
		# guardamos el nuevo ply rotado
		o3d.io.write_point_cloud(str_counter+"_temp.points.ply", ply_file, write_ascii=True)
		# aplicamos formato al ply (reescribimos ply)
		new_ply_file = open(str_counter+"_temp.points.ply") # abrimos ply rotado
		modified_new_ply_file = open(str_counter+".points.ply", "x") # creamos nuevo ply vacío
		for index, line in enumerate(new_ply_file):
			if index in [0,1,3]:
				modified_new_ply_file.write(line)
			if index == 4:
				modified_new_ply_file.write("property float x\n")
				modified_new_ply_file.write("property float y\n")
				modified_new_ply_file.write("property float z\n")
				modified_new_ply_file.write("property float nx\n")
				modified_new_ply_file.write("property float ny\n")
				modified_new_ply_file.write("property float nz\n")
				modified_new_ply_file.write("element face 0\n")
				modified_new_ply_file.write("property list uchar int vertex_indices\n")
				modified_new_ply_file.write("end_header\n")
			if index not in [0,1,2,3,4,5,6,7,8,9,10]:
				point = [float(line.strip().split()[0]), float(line.strip().split()[1]), float(line.strip().split()[2]), float(line.strip().split()[3]), float(line.strip().split()[4]), float(line.strip().split()[5])]
				modified_new_ply_file.write(format(point[0],".6f")+" "+format(point[1],".6f")+" "+format(point[2],".6f")+" "+format(point[3],".6f")+" "+format(point[4],".6f")+" "+format(point[5],".6f")+"\n")
		modified_new_ply_file.close()
		new_ply_file.close()
		# copiamos el txt correspondiente
		os.system("cp "+plys_path+"/"+obj+".points.ply2.txt "+subset_path+"/"+str_counter+".points.ply2.txt")
		# generamos el archivo npy
		new_ply = o3d.io.read_point_cloud(str_counter+".points.ply")
		npy_data = np.asarray(new_ply.points)
		os.chdir(category_path)
		np.save(str_counter+".points.ply.npy",npy_data)
		os.chdir(subset_path)
		# imprimimos el progreso
		print(str_counter)
# borramos todos los ply temporales (4GB aprox.)
os.system("rm *_temp*")