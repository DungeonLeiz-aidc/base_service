# 🏆 Repository Pattern - Trừu tượng hóa Dữ liệu / Data Abstraction

**Mục đích / Purpose**: Repository đóng vai trò như một bộ sưu tập (collection) các đối tượng Domain trong bộ nhớ. Nó ẩn đi toàn bộ sự phức tạp của việc truy vấn SQL hay các chi tiết của database. / The Repository pattern acts as a collection of Domain objects in memory. It hides all the complexity of SQL queries and database details.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Trừu tượng hóa**: Tầng Application chỉ gọi các phương thức như `save()` hay `get_by_id()` mà không cần biết bên dưới là PostgreSQL, MySQL hay thậm chí là lưu file.
- **Ánh xạ (Mapping)**: Chuyển đổi từ Database Models (ORM) sang Domain Entities và ngược lại. Điều này giúp Domain Layer luôn "sạch", không bị dính mã của framework như SQLAlchemy.

### 🏛️ Ví dụ thực tế (Example)
- `order_repository.py`: Sử dụng `AsyncSession` của SQLAlchemy để thực hiện các thao tác Unit of Work.
- `src/domain/repositories/interfaces.py`: Nơi định nghĩa các "bản hợp đồng" mà Repository này phải thực hiện.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Abstraction**: The Application layer only calls methods like `save()` or `get_by_id()` without knowing if the underlying storage is PostgreSQL, MySQL, or even a local file.
- **Mapping**: Converts Database Models (ORM) to Domain Entities and vice versa. This keeps the Domain Layer "clean" and free from framework-specific code like SQLAlchemy.

### 🏛️ Practical Example
- `order_repository.py`: Uses SQLAlchemy's `AsyncSession` to perform Unit of Work operations.
- `src/domain/repositories/interfaces.py`: Defines the "contracts" that this Repository must fulfill.
