import pymysql

class DBcontroller:
    def __init__(self):
        # db connect
        self.DB = pymysql.connect(
            user='root',
            passwd='1234',
            host='127.0.0.1',  #mysql ip address
            db='capston_test', #db name
            charset='utf8'
        )

        #dict 형태로 데이터를 조회하기 위해 cursor 설정
        self.cursor = self.DB.cursor(pymysql.cursors.DictCursor)


    def push(self,id,layer,data):
        id=str(id)
        layer=str(layer)
        data=str(data)

        sql='INSERT INTO tensor(id,layer,data)VALUE('+id+','+layer+','+data+');'
        self.cursor.execute(sql)
        self.DB.commit()

    def pull(self,id,layer):
        id=str(id)
        layer=str(layer)

        sql='SELECT * FROM tensor WHERE id='+id+' AND layer='+layer+';'
        print(sql)
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def delete(self,id,layer):
        id=str(id)
        layer=str(layer)

        sql = 'DELETE FROM tensor WHERE id=' + id + ' AND layer=' + layer + ';'
        self.cursor.execute(sql)


#main function
if __name__=="__main__":
    DB=DBcontroller();

    DB.push(1,1,1010101010)

    temp=DB.pull(1,1)
    print(temp)

    DB.delete(1,1)

