from db import cursor, conn

class Gallery:
    TABLE_NAME = 'gallery'

    def __init__(self, image_url: str):
        self.id = None
        self.image_url = image_url

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (image_url)
        VALUES (?)
        """
        cursor.execute(sql, (self.image_url,))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted image with ID: {self.id}")

    def to_dict(self):
        return {
            'id': self.id,
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
        gallery = cls(image_url=row[1])
        gallery.id = row[0]
        return gallery

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
            image_url TEXT NOT NULL
        )
        """
        cursor.execute(sql_create)
        conn.commit()

    @classmethod
    def get_by_id(cls, gallery_id):
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE id = ?"
        cursor.execute(sql, (gallery_id,))
        row = cursor.fetchone()
        return cls.row_to_instance(row)

# Create the table
Gallery.create_table()

# Add initial data
image1 = Gallery(
    image_url="https://images.pexels.com/photos/416717/pexels-photo-416717.jpeg?auto=compress&cs=tinysrgb&w=600"
)

image2 = Gallery(
    image_url="https://images.pexels.com/photos/703014/pexels-photo-703014.jpeg?auto=compress&cs=tinysrgb&w=600"
)

image3 = Gallery(
    image_url="https://images.pexels.com/photos/3490348/pexels-photo-3490348.jpeg?auto=compress&cs=tinysrgb&w=600"
)

image4 = Gallery(
    image_url="https://images.pexels.com/photos/416717/pexels-photo-416717.jpeg?auto=compress&cs=tinysrgb&w=600"
)

image5 = Gallery(
    image_url="https://images.pexels.com/photos/2204196/pexels-photo-2204196.jpeg?auto=compress&cs=tinysrgb&w=600"
)

image1.save()
image2.save()
image3.save()
image4.save()
image5.save()
