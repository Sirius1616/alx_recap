````markdown
# 0x0F. Python - Object-relational Mapping

## 📚 SE Foundations  
**Average Score:** 90.26%  
**Auto QA Review:** 155.0/165 mandatory | 0.0/32 optional  
**Altogether:** 93.94%  
**Mandatory:** 93.94%  
**Optional:** 0.0%  
**Calculation:** 93.94% + (93.94% × 0.0%) = **93.94%**

---

## 🧠 Background Context

In this project, we link two powerful technologies: **Databases** and **Python**.

- Part 1: Use the `MySQLdb` module to connect to a MySQL database and execute SQL queries.
- Part 2: Use the `SQLAlchemy` module, an **Object Relational Mapper (ORM)**, to interact with the database **without writing raw SQL**.

> The main difference:  
> With ORM, you focus on objects rather than SQL queries. Your code becomes **storage-agnostic**, which means it's easy to switch databases without rewriting logic.

### 📌 Without ORM

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
