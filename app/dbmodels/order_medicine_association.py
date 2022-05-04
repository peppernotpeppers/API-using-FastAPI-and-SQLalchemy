from sqlalchemy import Integer, Column, ForeignKey, Table


from db.base import Base


# Bảng csdl nối bảng "tbl_orders" với "tbl_medicines"
order_medicine = Table(
    "tbl_order_medicine",
    Base.metadata,
    Column("orders_id", ForeignKey("tbl_orders.id"), primary_key=True),
    Column("medicines_id", ForeignKey("tbl_medicines.id"), primary_key=True),
    Column("quantity", Integer),
)
