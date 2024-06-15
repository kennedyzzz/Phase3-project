from db import cursor, conn

class Trainers:
    TABLE_NAME = 'trainers'

    def __init__(self, name: str, description: str, image_url: str):
        self.id = None
        self.name = name
        self.description = description
        self.image_url = image_url

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (name, description, image_url)
        VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.image_url))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted trainer with ID: {self.id}")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
        }

    @classmethod
    def get_all(cls):
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls.row_to_instance(row) for row in rows]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        trainer = cls(name=row[1], description=row[2], image_url=row[3])
        trainer.id = row[0]
        return trainer

    @classmethod
    def create_table(cls):
        sql_drop = f"""
        DROP TABLE IF EXISTS {cls.TABLE_NAME}
        """
        cursor.execute(sql_drop)
        conn.commit()

        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT
        )
        """
        cursor.execute(sql_create)
        conn.commit()


Trainers.create_table()


trainer1 = Trainers(
    name="John Doe",
    description="Certified personal trainer specializing in strength training and conditioning.",
    image_url="https://images.pexels.com/photos/416717/pexels-photo-416717.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer2 = Trainers(
    name="Jane Smith",
    description="Expert in yoga and pilates with over 10 years of experience.",
    image_url="https://images.pexels.com/photos/703014/pexels-photo-703014.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer3 = Trainers(
    name="Mike Johnson",
    description="Specialist in HIIT and cardiovascular fitness.",
    image_url="https://images.pexels.com/photos/3490348/pexels-photo-3490348.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer4 = Trainers(
    name="Emily Davis",
    description="Nutritionist and wellness coach with a focus on holistic health.",
    image_url="https://images.pexels.com/photos/1552252/pexels-photo-1552252.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer5 = Trainers(
    name="David Brown",
    description="Strength and conditioning coach for athletes of all levels.",
    image_url="https://images.pexels.com/photos/2204196/pexels-photo-2204196.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer6 = Trainers(
    name="Sophia Martinez",
    description="Specializes in weight loss and body transformation programs.",
    image_url="https://images.pexels.com/photos/28080/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600"
)

trainer7 = Trainers(
    name="James Wilson",
    description="Experienced in functional fitness and mobility training.",
    image_url="https://images.pexels.com/photos/703012/pexels-photo-703012.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer8 = Trainers(
    name="Olivia Thomas",
    description="Senior fitness expert focusing on low-impact exercises.",
    image_url="https://images.pexels.com/photos/949129/pexels-photo-949129.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer9 = Trainers(
    name="Lucas Garcia",
    description="Corporate wellness trainer with programs tailored for office workers.",
    image_url="https://images.pexels.com/photos/903171/pexels-photo-903171.jpeg?auto=compress&cs=tinysrgb&w=600"
)

trainer1.save()
trainer2.save()
trainer3.save()
trainer4.save()
trainer5.save()
trainer6.save()
trainer7.save()
trainer8.save()
trainer9.save()
