import pymysql
con = pymysql.connect(\
						host='localhost', \
						user='gestor', \
						password='123', \
						database='db_teste', \
						cursorclass=pymysql.cursors.DictCursor\
						)

with con.cursor() as c:
	criar_tb_painel = """
						create table if not exists tb_painel
							(
								id int auto_increment, 
								nome varchar(255) not null, 
								primary key(id));
					  """
	
	c.execute(criar_tb_painel)

	con.commit()