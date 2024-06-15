from db import cursor, conn

class MembershipDetails:
    TABLE_NAME = 'membershipdetails'

    def __init__(self, name: str, description: str, image_url: str, price: int):
        self.id = None
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = price

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (name, description, image_url, price)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.image_url, self.price))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted membership with ID: {self.id}")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
            'price': self.price,
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
        membership = cls(name=row[1], description=row[2], image_url=row[3], price=row[4])
        membership.id = row[0]
        return membership

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
            image_url TEXT,
            price INTEGER
        )
        """
        cursor.execute(sql_create)
        conn.commit()


MembershipDetails.create_table()


card1 = MembershipDetails(
    name="Monthly",
    description="Access to gym services and equipment for one month",
    image_url="https://images.pexels.com/photos/416717/pexels-photo-416717.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=6500
)

card2 = MembershipDetails(
    name="3 Months",
    description="Access to gym services and equipment for three months",
    image_url="https://images.pexels.com/photos/703014/pexels-photo-703014.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=15000
)

card3 = MembershipDetails(
    name="6 Months",
    description="Access to gym services and equipment for six months",
    image_url="https://images.pexels.com/photos/3490348/pexels-photo-3490348.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=27000
)

card4 = MembershipDetails(
    name="12 Months",
    description="Access to gym services and equipment for twelve months",
    image_url="https://images.pexels.com/photos/1552252/pexels-photo-1552252.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=48000
)

card5 = MembershipDetails(
    name="Duo Monthly",
    description="Access to gym services and equipment for one month for two people",
    image_url="https://images.pexels.com/photos/2204196/pexels-photo-2204196.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=9000
)

card6 = MembershipDetails(
    name="Student Monthly",
    description="Discounted access to gym services and equipment for students for one month",
    image_url="https://images.pexels.com/photos/28080/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600",
    price=4500
)

card7 = MembershipDetails(
    name="Family Monthly",
    description="Access to gym services and equipment for a family for one month",
    image_url="https://images.pexels.com/photos/703012/pexels-photo-703012.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=12000
)

card8 = MembershipDetails(
    name="Senior Monthly",
    description="Discounted access to gym services and equipment for seniors for one month",
    image_url="https://images.pexels.com/photos/949129/pexels-photo-949129.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=6000
)

card9 = MembershipDetails(
    name="Corporate Monthly",
    description="Access to gym services and equipment for corporate employees for one month",
    image_url="https://images.pexels.com/photos/903171/pexels-photo-903171.jpeg?auto=compress&cs=tinysrgb&w=600",
    price=8000
)

card1.save()
card2.save()
card3.save()
card4.save()
card5.save()
card6.save()
card7.save()
card8.save()
card9.save()