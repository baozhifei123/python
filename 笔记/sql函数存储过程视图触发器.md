## 1. 函数

MySQL中提供了很多函数，为我们的SQL操作提供便利，例如：

```
mysql> select * from d1;
+----+-----------+
| id | name      |
+----+-----------+
|  1 | 武沛齐    |
|  3 | xxx       |
|  4 | pyyu      |
+----+-----------+
3 rows in set (0.00 sec)

mysql> select count(id), max(id),min(id),avg(id) from d1;
+-----------+---------+---------+---------+
| count(id) | max(id) | min(id) | avg(id) |
+-----------+---------+---------+---------+
|         3 |       4 |       1 |  2.6667 |
+-----------+---------+---------+---------+
1 row in set (0.00 sec)

mysql>
mysql>
mysql> select id,reverse(name) from d1;
+----+---------------+
| id | reverse(name) |
+----+---------------+
|  1 | 齐沛武        |
|  3 | xxx           |
|  4 | uyyp          |
+----+---------------+
3 rows in set (0.00 sec)

mysql> select id, reverse(name),concat(name,name), NOW(), DATE_FORMAT( NOW(),'%Y-%m-%d %H:%i:%s')  from d1;
+----+---------------+--------------------+---------------------+-----------------------------------------+
| id | reverse(name) | concat(name,name)  | NOW()               | DATE_FORMAT( NOW(),'%Y-%m-%d %H:%i:%s') |
+----+---------------+--------------------+---------------------+-----------------------------------------+
|  1 | 齐沛武        | 武沛齐武沛齐       | 2021-05-27 09:18:07 | 2021-05-27 09:18:07                     |
|  3 | xxx           | xxxxxx             | 2021-05-27 09:18:07 | 2021-05-27 09:18:07                     |
|  4 | uyyp          | pyyupyyu           | 2021-05-27 09:18:07 | 2021-05-27 09:18:07                     |
+----+---------------+--------------------+---------------------+-----------------------------------------+
3 rows in set (0.00 sec)

mysql> select concat("alex","sb");
+---------------------+
| concat("alex","sb") |
+---------------------+
| alexsb              |
+---------------------+
1 row in set (0.00 sec)

mysql> select sleep(1);
+----------+
| sleep(1) |
+----------+
|        0 |
+----------+
1 row in set (1.00 sec)
```



部分函数列表：

```
CHAR_LENGTH(str)
    返回值为字符串str 的长度，长度的单位为字符。一个多字节字符算作一个单字符。
    对于一个包含五个二字节字符集, LENGTH()返回值为 10, 而CHAR_LENGTH()的返回值为5。

CONCAT(str1,str2,...)
    字符串拼接
    如有任何一个参数为NULL ，则返回值为 NULL。
CONCAT_WS(separator,str1,str2,...)
    字符串拼接（自定义连接符）
    CONCAT_WS()不会忽略任何空字符串。 (然而会忽略所有的 NULL）。

CONV(N,from_base,to_base)
    进制转换
    例如：
        SELECT CONV('a',16,2); 表示将 a 由16进制转换为2进制字符串表示

FORMAT(X,D)
    将数字X 的格式写为'#,###,###.##',以四舍五入的方式保留小数点后 D 位， 并将结果以字符串的形式返回。若  D 为 0, 则返回结果不带有小数点，或不含小数部分。
    例如：
        SELECT FORMAT(12332.1,4); 结果为： '12,332.1000'
INSERT(str,pos,len,newstr)
    在str的指定位置插入字符串
        pos：要替换位置其实位置
        len：替换的长度
        newstr：新字符串
    特别的：
        如果pos超过原字符串长度，则返回原字符串
        如果len超过原字符串长度，则由新字符串完全替换
INSTR(str,substr)
    返回字符串 str 中子字符串的第一个出现位置。

LEFT(str,len)
    返回字符串str 从开始的len位置的子序列字符。

LOWER(str)
    变小写

UPPER(str)
    变大写

LTRIM(str)
    返回字符串 str ，其引导空格字符被删除。
RTRIM(str)
    返回字符串 str ，结尾空格字符被删去。
SUBSTRING(str,pos,len)
    获取字符串子序列

LOCATE(substr,str,pos)
    获取子序列索引位置

REPEAT(str,count)
    返回一个由重复的字符串str 组成的字符串，字符串str的数目等于count 。
    若 count <= 0,则返回一个空字符串。
    若str 或 count 为 NULL，则返回 NULL 。
REPLACE(str,from_str,to_str)
    返回字符串str 以及所有被字符串to_str替代的字符串from_str 。
REVERSE(str)
    返回字符串 str ，顺序和字符顺序相反。
RIGHT(str,len)
    从字符串str 开始，返回从后边开始len个字符组成的子序列

SPACE(N)
    返回一个由N空格组成的字符串。

SUBSTRING(str,pos) , SUBSTRING(str FROM pos) SUBSTRING(str,pos,len) , SUBSTRING(str FROM pos FOR len)
    不带有len 参数的格式从字符串str返回一个子字符串，起始于位置 pos。带有len参数的格式从字符串str返回一个长度同len字符相同的子字符串，起始于位置 pos。 使用 FROM的格式为标准 SQL 语法。也可能对pos使用一个负值。假若这样，则子字符串的位置起始于字符串结尾的pos 字符，而不是字符串的开头位置。在以下格式的函数中可以对pos 使用一个负值。

    mysql> SELECT SUBSTRING('Quadratically',5);
        -> 'ratically'

    mysql> SELECT SUBSTRING('foobarbar' FROM 4);
        -> 'barbar'

    mysql> SELECT SUBSTRING('Quadratically',5,6);
        -> 'ratica'

    mysql> SELECT SUBSTRING('Sakila', -3);
        -> 'ila'

    mysql> SELECT SUBSTRING('Sakila', -5, 3);
        -> 'aki'

    mysql> SELECT SUBSTRING('Sakila' FROM -4 FOR 2);
        -> 'ki'

TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str) TRIM(remstr FROM] str)
    返回字符串 str ， 其中所有remstr 前缀和/或后缀都已被删除。若分类符BOTH、LEADIN或TRAILING中没有一个是给定的,则假设为BOTH 。 remstr 为可选项，在未指定情况下，可删除空格。

    mysql> SELECT TRIM('  bar   ');
            -> 'bar'

    mysql> SELECT TRIM(LEADING 'x' FROM 'xxxbarxxx');
            -> 'barxxx'

    mysql> SELECT TRIM(BOTH 'x' FROM 'xxxbarxxx');
            -> 'bar'

    mysql> SELECT TRIM(TRAILING 'xyz' FROM 'barxxyz');
            -> 'barx'   
```

更多函数：https://dev.mysql.com/doc/refman/5.7/en/functions.html



当然，MySQL中也支持让你去自定义函数。

- 创建函数

  ```sql
  delimiter $$
  create function f1(
      i1 int,
      i2 int)
  returns int
  BEGIN
      declare num int;
      declare maxId int;
      select max(id) from big into maxId;
      
      set num = i1 + i2 + maxId;
      return(num);
  END $$
  delimiter ;
  ```

- 执行函数

  ```sql
  select f1(11,22);
  
  select f1(11,id),name from d1;
  ```

- 删除函数

  ```sql
  drop function f1;
  ```



## 2. 存储过程

存储过程，是一个存储在MySQL中的SQL语句集合，当主动去调用存储过程时，其中内部的SQL语句会按照逻辑执行。

![image-20210531174813902](assets/image-20210531174813902.png)

- 创建存储过程

  ```sql
  delimiter $$
  create procedure p1()
  BEGIN
      select * from d1;
  END $$
  delimiter ;
  ```

- 执行存储过程

  ```sql
  call p1();
  ```

  ```python
  #!/usr/bin/env python
  # -*- coding:utf-8 -*-
  import pymysql
  
  conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root123', db='userdb')
  cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
  # 执行存储过程
  cursor.callproc('p1')
  result = cursor.fetchall()
  
  cursor.close()
  conn.close()
  
  print(result)
  ```

- 删除存储过程

  ```sql
  drop procedure proc_name;
  ```

  

### 3.1 参数类型

存储过程的参数可以有如下三种：

- in，仅用于传入参数用
- out，仅用于返回值用(相当于一个内存地址，在存储过程中修改后，内存地址的值也会修改)
- inout，既可以传入又可以当作返回值

```sql
delimiter $$
create procedure p2(
    in i1 int,
    in i2 int,
    inout i3 int,
    out r1 int
)
BEGIN
    DECLARE temp1 int;
    DECLARE temp2 int default 0;
    
    set temp1 = 1;

    set r1 = i1 + i2 + temp1 + temp2;
    
    set i3 = i3 + 100;

end $$
delimiter ;
```

```sql
# 使用
set @t1 =4;
set @t2 = 0;
CALL p2 (1, 2 ,@t1, @t2);
SELECT @t1,@t2;
```

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root123', db='userdb')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行存储过程
cursor.callproc('p2',args=(1, 22, 3, 4))

# 获取执行完存储的参数
cursor.execute("select @_p2_0,@_p2_1,@_p2_2,@_p2_3")
result = cursor.fetchall()
# {"@_p2_0":11 }

cursor.close()
conn.close()

print(result)
```



### 3.2 返回值 & 结果集（在存储过程中执行的sql语句）

```sql
delimiter $$
create procedure p3(
    in n1 int,
    inout n2 int,
    out n3 int
)
begin
    set n2 = n1 + 100;
    set n3 = n2 + n1 + 100;
    select * from d1;
end $$
delimiter ;
```

```sql
set @t1 =4;
set @t2 = 0;
CALL p3 (1,@t1, @t2);
SELECT @t1,@t2;
```

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root123', db='userdb')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行存储过程
cursor.callproc('p3',args=(22, 3, 4))
table = cursor.fetchall() # 得到执行存储过中的结果集

# 获取执行完存储的参数
cursor.execute("select @_p3_0,@_p3_1,@_p3_2")
rets = cursor.fetchall()

cursor.close()
conn.close()

print(table)
print(rets)
```



### 3.3 事务 & 异常（事务可以单独使用）

事务，成功都成功，失败都失败。

```sql
delimiter $$
create PROCEDURE p4(
    OUT p_return_code tinyint
)
BEGIN 
  DECLARE exit handler for sqlexception    #定义报错后执行的sql语句
  BEGIN 
    -- ERROR 
    set p_return_code = 1; 
    rollback; # 还原操作之前的数据库
  END; 
 
  DECLARE exit handler for sqlwarning     #定义警告后执行的sql语句
  BEGIN 
    -- WARNING 
    set p_return_code = 2; 
    rollback;  # 还原操作之前的数据库
  END; 
 
  START TRANSACTION;  -- 开启事务（如果不提交也不回滚，执行的DML只是在当前会话有效，所以要么以commit结束，要么以rollback结束。）
    delete from d1;
    insert into tb(name)values('seven');
  COMMIT;  -- 提交事务
 
  -- SUCCESS 
  set p_return_code = 0; 
 
  END $$
delimiter ; 
```

```sql
set @ret =100;
CALL p4(@ret);
SELECT @ret;
```

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root123', db='userdb')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行存储过程
cursor.callproc('p4',args=(100))

# 获取执行完存储的参数
cursor.execute("select @_p4_0")
rets = cursor.fetchall()

cursor.close()
conn.close()

print(table)
print(rets)
```



### 3.4 游标（效率低）

```sql
delimiter $$
create procedure p5()
begin 
    declare sid int;
    declare sname varchar(50); 
    declare done int default false;


    declare my_cursor CURSOR FOR select id,name from d1;  # 声明了一个游标 游标: 和一张表关联
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE; # 游标循环的过程当中如果循环结束找不到值后，会将done设置为true
    
    open my_cursor; # 打开游标
        xxoo: LOOP # 开始循环 xxoo循环的名字(用于停止循环)
            fetch my_cursor into sid,sname; # 获取每一行数据
            IF done then 
                leave xxoo;
            END IF;
            insert into t1(name) values(sname);
        end loop xxoo;
    close my_cursor;
end $$
delimiter ; 
```

```sql
call p5();
```



## 3.视图

视图其实是一个虚拟表（非真实存在），其本质是【根据SQL语句获取动态的数据集，并为其命名】，用户使用时只需使用【名称】即可获取结果集，并可以将其当作表来使用。

```sql
SELECT
    *
FROM
    (SELECT nid,name FROM tb1 WHERE nid > 2) AS A
WHERE
    A.name > 'alex';
```

- 创建视图

  ```sql
  create view v1 as select id,name from d1 where id > 1;
  ```

- 使用视图

  ```sql
  select * from v1;
  
  -- select * from (select id,name from d1 where id > 1) as v1;
  ```

- 删除视图

  ```sql
  drop view v1;
  ```

- 修改视图

  ```sql
  alter view v1 as SQL语句
  ```



注意：基于视图只能查询，针对视图不能执行 增加、修改、删除。 如果源表发生变化，视图表也会发生变化。



## 4.触发器

![image-20210531181738177](assets/image-20210531181738177.png)

对某个表进行【增/删/改】操作的前后如果希望触发某个特定的行为时，可以使用触发器。

```sql
# 插入前
CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 插入后
CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除前
CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除后
CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新前
CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新后
CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END
```

```sql
DROP TRIGGER tri_after_insert_tb1;
```



示例：

- 在 t1 表中插入数据之前，先在 t2 表中插入一行数据。

  ```sql
  delimiter $$
  CREATE TRIGGER tri_before_insert_t1 BEFORE INSERT ON t1 FOR EACH ROW
  BEGIN
  	-- NEW.id  NEW.name  NEW.email
  	-- INSERT INTO t2 (name) VALUES();
  	IF NEW.name = 'alex' THEN
          INSERT INTO t2 (name) VALUES(NEW.id);
      END IF;
  
  END $$
  delimiter ;
  ```

  ```
  insert into t1(id,name,email)values(1,"alex","xxx@qq.com")
  ```

- 在t1表中删除数据之后，再在t2表中插入一行数据。

  ```sql
  delimiter $$
  CREATE TRIGGER tri_after_insert_t1 AFTER DELETE ON t1 FOR EACH ROW
  BEGIN
  
  IF OLD.name = 'alex' THEN
      INSERT INTO t2 (name) VALUES(OLD.id);
  END IF;
  
  END $$
  delimiter ;
  ```

特别的：NEW表示新数据，OLD表示原来的数据。



## 总结

对于Python开发人员，其实在开发过程中触发器、视图、存储过程用的很少（以前搞C#经常写存储过程），最常用的其实就是正确的使用索引以及常见的函数。

- 函数，提供了一些常见操作 & 配合SQL语句，执行后返回结果。
- 存储过程，一个SQL语句的集合，可以出发复杂的情况，最终可以返回结果 + 数据集。
- 视图，一个虚拟的表。
- 触发器，在表中数据行执行前后自定义一些操作。



























