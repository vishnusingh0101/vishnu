from app.database.models import Memory
class MemoryManager:
 def save(self,db,category,key,value):
  m=db.query(Memory).filter(Memory.key==key).first()
  if m:m.value=value
  else: db.add(Memory(category=category,key=key,value=value))
  db.commit()
 def get(self,db,key):
  m=db.query(Memory).filter(Memory.key==key).first();return m.value if m else None
