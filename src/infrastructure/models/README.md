# 🗄️ Database Models - Cấu trúc Dữ liệu Vật lý / Physical Data Models

**Mục đích / Purpose**: Thư mục này định nghĩa cấu trúc vật lý của các bảng trong Database (SQLAlchemy models), phản ánh cách dữ liệu được lưu trữ thực sự trên đĩa. / This directory defines the physical database schema (SQLAlchemy models), reflecting how data is actually structured on disk.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Định nghĩa Sơ đồ**: Mô tả cấu trúc vật lý của bảng, cột và kiểu dữ liệu tương ứng.
2. **Ràng buộc Toàn vẹn**: Thiết lập các quy tắc bảo vệ dữ liệu ở mức vật lý (Unique, ForeignKey, Check).
3. **Quản lý Quan hệ**: Định nghĩa cách các bảng móc nối với nhau (One-to-Many, Many-to-Many).
4. **Tối ưu Hiệu năng**: Đánh chỉ mục (Indexing) lên các cột được truy vấn thường xuyên.
5. **Chiến lược Nạp dữ liệu**: Cấu hình Eager hoặc Lazy loading để tối ưu hóa truy vấn.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: DB Models là "bộ xương" của hệ thống về mặt lưu trữ. Chúng cần được thiết kế để tối ưu hóa tốc độ đọc/ghi của database engine.
- **Why SQLAlchemy?**: Cung cấp một lớp trừu tượng mạnh mẽ (ORM) giúp chúng ta làm việc với database dưới dạng các đối tượng Python mà vẫn kiểm soát được các tính năng đặc thù của SQL.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Không nghiệp vụ**: Model không nên chứa logic xử lý nghiệp vụ hay phương thức tính toán tiền nong.
- **Tính nhất quán**: Mọi cột nhạy cảm (PII) phải được đánh dấu rõ ràng để các tầng trên có thể xử lý masking.
- **Ràng buộc cứng**: Ưu tiên sử dụng Database Constraints thay vì kiểm tra bằng code khi có thể.

### 🏛️ Ví dụ thực tế (Examples)
- **Order Model**: [models.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/models/models.py) định nghĩa cấu trúc bảng `orders` với các ràng buộc về `id` và `customer_id`.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Schema Definition**: Describes the physical structure of tables, columns, and data types.
2. **Data Integrity**: Enforces physical rules via Unique keys, Foreign keys, and Checks.
3. **Relationship Mapping**: Manages table associations (One-to-Many, Many-to-Many).
4. **Performance Optimization**: Implements Indexing on high-traffic data columns.
5. **Loading Strategy**: Defines Eager vs. Lazy loading policies for relation retrieval.

### 💡 Context & Why
- **Context**: DB Models are the storage "skeleton" of the system, optimized for the database engine's read/write efficiency.
- **Why SQLAlchemy?**: Offers a powerful ORM abstraction, allowing Pythonic interaction with databases while maintaining deep control over SQL features.

### ⚠️ Process & Constraints (CCE Template)
- **No Business Logic**: Models must be pure data structures, devoid of business calculations.
- **Privacy Awareness**: Sensitive (PII) columns should be clearly identifiable for upper-layer masking.
- **Hard Constraints**: Prioritize Database-level constraints over application code checks where applicable.

### 🏛️ Practical Examples
- **Order Model**: [models.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/models/models.py) defines the `orders` table structure with mandatory identity constraints.
