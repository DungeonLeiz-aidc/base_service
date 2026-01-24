# 🗄️ Database Models - Cấu trúc Lưu trữ / Persistence Models

**Mục đích / Purpose**: Models là các lớp định nghĩa cách dữ liệu được lưu trữ trong cơ sở dữ liệu thật. Chúng là công cụ để ORM (như SQLAlchemy) hiểu cách ánh xạ các đối tượng Python vào các bảng SQL. / Models are classes defining how data is stored in the actual database. They enable ORMs (like SQLAlchemy) to map Python objects to SQL tables.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Persistence-First**: Khác với Domain Entities (tập trung vào logic), Models tập trung vào hiệu năng truy vấn, kiểu dữ liệu DB và các khóa ngoại (Foreign Keys).
- **Mapping (Ánh xạ)**: Models thường chứa các annotations của framework (ví dụ: `Mapped`, `mapped_column`) để tự động sinh schema.
- **Tương quan**: Định nghĩa các mối quan hệ vật lý như `One-to-Many` (Một Order có nhiều Items) để tối ưu hóa việc tải dữ liệu.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `OrderModel`: Định nghĩa bảng `orders` với các cột ID, customer_id và quan hệ `items` trỏ tới `OrderItemModel`.
- Các file ở đây chỉ nên được biết đến bởi tầng **Infrastructure**.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Persistence-First**: Unlike Domain Entities (logic-focused), Models focus on query performance, database types, and Foreign Keys.
- **Mapping**: Models contain framework-specific annotations (e.g., `Mapped`, `mapped_column`) to automatically generate schemas.
- **Relationships**: Defines physical relations like `One-to-Many` (One Order has many Items) to optimize data loading.

### 🏛️ Practical Example
In this project:
- `OrderModel`: Defines the `orders` table with ID, customer_id, and an `items` relationship pointing to `OrderItemModel`.
- These files should ideally only be known within the **Infrastructure** layer.
