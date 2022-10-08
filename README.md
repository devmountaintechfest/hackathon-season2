
curl -o amm.bat -k -L https://github.com/com-lihaoyi/Ammonite/releases/download/2.5.4/2.12-2.5.4

chmod 755 scala-ammo.bin
export PATH=$PATH:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0/

set JAVA_HOME=C:\jdk-11.0.13+8
set PATH=C:\Program Files\Git\cmd;%JAVA_HOME%\bin;C:\Windows\System32\WindowsPowerShell\v1.0\

# Check User Profile : .ammonite folder for sure
./amm.bat main.sc

# Check Visualization
main-visualize.ipynb

# Check SQLite
result.sqlite
 - table: dev_club_old, dev_club, dev_club_[by country], dev_club_[by dept], dev_club_[by nationality]

# Check JSON Fiile from SQLite
devclub.json - refer to main.sc line: 107

=======
# hackathon-season2

## เลข Status จะมีตามนี้ครับ
- 1 = Active
- 2 = Resigned
- 3 = Retired
- ถ้าเป็นเลขอื่นๆจะถือว่าเป็น anomaly information(**ข้อมูลที่ไม่ถูกต้อง**)

## เลข GENDER จะมีตามนี้ครับ
- 0 = Male
- 1 = Female
- ถ้าเป็นเลขอื่นๆจะถือว่าเป็น anomaly information(**ข้อมูลที่ไม่ถูกต้อง**)

=======
## กฎระเบียบ

- ห้ามใช้ library สำหรับการทำ transformation จาก XML ไปเป็น CSV
- สามารถใช้ Driver ของตัวภาษานั้นๆ เพื่อต่อ SQLlite ได้
- ไม่อนุญาตให้ใช้ Tool สำเร็จรูป

## เกณฑ์การให้คะแนน

- โค๊ดทำงานถูกต้อง
- Performance
  - Memory usage
  - Runtime benchmark 
- Code อ่านง่าย
- ส่งเร็ว
- Creative ตอนทำ Data visualization 
- ผลลัพธ์จาก SQLlite ต้องได้เป็น **JSON** format

**ตัวอย่าง Data visualization**

[dev-mountain-visualization](https://dev-moutain-dataviz.netlify.app/)


## ตัวอย่างการสร้าง PR
ทีม Dev mountain
สมาชิก
- [annibuliful](https://github.com/annibuliful)
- [lordbenz](https://github.com/lordbenz)

Repo: [hackathon](https://github.com/devmountaintechfest/hackathon-season2)
