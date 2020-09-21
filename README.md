1.	개발환경
-	Python 3.7.7
-	MySQL 5.6.49  (root pw : 1234)
-	PyMySQL 0.10.1

2. DB 설명
- DB name : capston_test
- TABLE name : tensor
- 컬럼
id : int
layer : int
data : mediumblob (8MB까지 저장할 수 있는 이진데이터 타입)
+----+-------+------------+
| id | layer | data       |
+----+-------+------------+


3. class 설명
import pymysql

class DBcontroller:
    def __init__(self) : user, passwd, host, db, charset 설정
    def push(self,id,layer,data) : id, layer, data를 인자로 DB에 삽입
    def pull(self,id,layer) : id, layer를 인자로 DB에서 조회 후 dict 형태로 return {id:"..",layer:"..",data:".."}
    def delete(self,id,layer) : id, layer를 인자로 해당 데이터를 DB에서 삭제