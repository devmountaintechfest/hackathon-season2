# hackathon-season2
## Story
สายการบิน DevMountain ถูก Take Over โดยสายการบิน DevClub ซึ่งจะต้องมีการย้ายพนักงานจาก DevMountain มา DevClub ซึ่งส่งผลกระทบกับทางแผนกไอทีต้องทำการย้ายข้อมูลมาลงในฐานข้อมูลใหม่ 
- ไฟล์ข้อมูลพนักงานของสายการบิน DevMountain จะอยู่ในรูปแบบ csv
- ไฟล์ข้อมูลพนักงานของสายการบิน DevClub จะอยู่ในรูปแบบ xml  
ให้ทำการย้ายข้อมูลลงในฐานข้อมูลใหม่เป็น sqlite โดยมีเงื่อนไข ดังนี้
- ย้ายพนักงานจากสายการบิน DevMountain ไป DevClub เฉพาะตำแหน่ง Air Hostess, Pilot และ Steward ที่มีสถานะ Active 
- สำหรับตำแหน่งอายุการทำงาน เกิน 3 ปี


## Migration Challenge 
- ย้ายพนักงานจากสายการบิน DevMountain ไป DevClub เฉพาะตำแหน่ง Air Hostess, Pilot และ Steward ที่มีสถานะ Active 
- สำหรับตำแหน่งอายุการทำงาน เกิน 3 ปี
- สร้างไฟล์ CSV แยกตามสัญชาติของพนักงาน
- สร้าง SQLite view ที่สามารถ query ตามประเทศที่ทำงาน
- สร้าง SQLite view สำหรับแบ่งตาม department
- สร้าง SQLite view ที่สามารถ query ตามสัญชาติของพนักงาน

## Clean anomalies information challenge
- ลบข้อมูลที่ซ้ำกัน
- ลบข้อมูลพนักงานที่ employeeId กับ passportNo เหมือนกัน
- ลบข้อมูลพนักงานที่ลาออกไปแล้ว

## Hackathon
- Fork Github repository
- Convert XML file to CSV (**Do not use lib to convert XML to CSV**)
- Create SQLlite db with data model that rely on XML file
- Develop tool to import CSV to SQLlite (Can be both basic command line or with UI)
- Develop tool to generate to json format belong to questions
- Create PR to submit your work Github repository

## Bonus (Optional)
จาก Data ที่มี ให้ visualize จะออกมาเป็น กราฟแท่ง แผนภูมิ ตาราง หรืออะไรก็ได้ตามที่ถนัดเลย
**ตัวอย่าง Data visualization**
[dev-mountain-visualization](https://dev-moutain-dataviz.netlify.app/)

## Useful information

### เลข Status จะมีตามนี้ครับ
- 1 = Active
- 2 = Resigned
- 3 = Retired
- ถ้าเป็นเลขอื่นๆจะถือว่าเป็น anomaly information(**ข้อมูลที่ไม่ถูกต้อง**)

### เลข GENDER จะมีตามนี้ครับ
- 0 = Male
- 1 = Female
- ถ้าเป็นเลขอื่นๆจะถือว่าเป็น anomaly information(**ข้อมูลที่ไม่ถูกต้อง**)

### กฎระเบียบ

- ห้ามใช้ library สำหรับการทำ transformation จาก XML ไปเป็น CSV
- สามารถใช้ Driver ของตัวภาษานั้นๆ เพื่อต่อ SQLlite ได้
- ไม่อนุญาตให้ใช้ Tool สำเร็จรูป
- Team member ไม่เกิน 3 คน หากทำเป็นทีม รบกวนใส่ชื่อเพื่อนๆ ใน Description ตอนส่ง PR

### เกณฑ์การให้คะแนน

- โค๊ดทำงานถูกต้อง
- Performance
  - Memory usage
  - Runtime benchmark 
- Code อ่านง่าย
- ส่งเร็ว
- Creative ตอนทำ Data visualization 
- ผลลัพธ์จาก SQLlite ต้องได้เป็น **JSON** format



### ไม่รู้วิธี Fork หรือ สร้าง PR สามารถฝึกได้จากที่นี่
https://github.com/firstcontributions/first-contributions 

## How to submit
- Create a PR to hackathon season 2 repository, add your name or team information and your repo link


## Q&A คำถามที่พบบ่อย
- ดูได้จาก issues 
https://github.com/devmountaintechfest/hackathon-season2/issues

## ทีม Dev mountain ที่ดูแลการแข่งครั้งนี้
สมาชิก
- [annibuliful](https://github.com/annibuliful)
- [lordbenz](https://github.com/lordbenz)
- [Issawat](https://github.com/Issawat)

Repo: [hackathon](https://github.com/devmountaintechfest/hackathon-season2)
