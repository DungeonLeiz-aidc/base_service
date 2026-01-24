# 💻 Source Code Overview - Tổng quan Mã Nguồn

**Mục đích / Purpose**: Danh mục `src/` chứa toàn bộ linh hồn của hệ thống, được phân lớp để bảo vệ các logic nghiệp vụ quan trọng khỏi những thay đổi của công nghệ bên ngoài. / The `src/` directory contains the essence of the system, layered to protect core business logic from external technological changes.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🛡️ Nguyên tắc Phụ thuộc (Dependency Rule)
Nguyên tắc vàng của Clean Architecture: **Sự phụ thuộc chỉ được hướng vào bên trong**.
- Các lớp bên trong (Domain) không được biết bất cứ điều gì về các lớp bên ngoài (Infrastructure/Interface).
- Điều này giúp bạn có thể thay đổi database từ PostgreSQL sang MongoDB mà không phải sửa một dòng code nào trong Domain.

### 🏛️ Cấu trúc Phân lớp (Example)
1. **domain/**: Trung tâm của hệ thống. Chứa Entities, Value Objects và các quy tắc nghiệp vụ bất biến.
2. **application/**: Tầng điều phối. Chứa các Services thực thi Use Cases, DTOs và Interfaces.
3. **infrastructure/**: Tầng kỹ thuật. Chứa code kết nối DB, Caching, Messaging và các Models ORM.
4. **interface/**: Tầng giao tiếp. Chứa API Routes, CLI commands và Background Workers.

---

## 🇺🇸 English Version

### 🛡️ The Dependency Rule
The golden rule of Clean Architecture: **Dependencies point only inwards**.
- Inner layers (Domain) must not know anything about outer layers (Infrastructure/Interface).
- This allows you to swap your database from PostgreSQL to MongoDB without changing a single line of Domain code.

### 🏛️ Layered Structure (Example)
1. **domain/**: The heart of the system. Contains Entities, Value Objects, and invariant business rules.
2. **application/**: The orchestration layer. Contains Services executing Use Cases, DTOs, and Interfaces.
3. **infrastructure/**: The technical layer. Contains DB connections, Caching, Messaging, and ORM Models.
4. **interface/**: The communication layer. Contains API Routes, CLI commands, and Background Workers.
