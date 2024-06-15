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


Gallery.create_table()


image1 = Gallery(
    image_url="https://images.pexels.com/photos/4327024/pexels-photo-4327024.jpeg?auto=compress&cs=tinysrgb&w=400"
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

image6 = Gallery(
    image_url="https://images.pexels.com/photos/2261485/pexels-photo-2261485.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image7 = Gallery(
    image_url="https://images.pexels.com/photos/2011384/pexels-photo-2011384.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image8 = Gallery(
    image_url="https://images.pexels.com/photos/2475875/pexels-photo-2475875.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image9 = Gallery(
    image_url="https://images.pexels.com/photos/1638336/pexels-photo-1638336.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image10 = Gallery(
    image_url="https://images.pexels.com/photos/931321/pexels-photo-931321.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image11 = Gallery(
    image_url="https://images.pexels.com/photos/4662341/pexels-photo-4662341.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image12 = Gallery(
    image_url="https://images.pexels.com/photos/4162481/pexels-photo-4162481.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image13 = Gallery(
    image_url="https://images.pexels.com/photos/4047039/pexels-photo-4047039.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image14 = Gallery(
    image_url="https://images.pexels.com/photos/3838389/pexels-photo-3838389.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image15 = Gallery(
    image_url="https://images.pexels.com/photos/3768916/pexels-photo-3768916.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image16 = Gallery(
    image_url="https://images.pexels.com/photos/4047155/pexels-photo-4047155.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image17 = Gallery(
    image_url="https://images.pexels.com/photos/3912951/pexels-photo-3912951.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image18 = Gallery(
    image_url="https://images.pexels.com/photos/3764014/pexels-photo-3764014.jpeg?auto=compress&cs=tinysrgb&w=600"
)

image19 = Gallery(
    image_url="https://images.pexels.com/photos/4753996/pexels-photo-4753996.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image20 = Gallery(
    image_url="https://images.pexels.com/photos/3289711/pexels-photo-3289711.jpeg?auto=compress&cs=tinysrgb&w=400"
)

image1.save()
image2.save()
image3.save()
image4.save()
image5.save()
image6.save()
image7.save()
image8.save()
image9.save()
image10.save()
image11.save()
image12.save()
image13.save()
image14.save()
image15.save()
image16.save()
image17.save()
image18.save()
image19.save()
image20.save()

