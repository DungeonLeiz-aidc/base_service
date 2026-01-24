# 🕒 Migration Versions - Lịch sử Biến đổi Cấu trúc / Chronological Schema Evolution

**Mục đích / Purpose**: Danh mục này chứa các "bản ghi" về sự thay đổi của cơ sở dữ liệu. Mỗi tập tin đại diện cho một bước tiến hóa của cấu trúc bảng, cho phép hệ thống đồng bộ hóa dữ liệu giữa các môi trường khác nhau. / This directory contains "records" of database changes. Each file represents an evolutionary step in the schema, allowing the system to synchronize data across different environments.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Incremental Changes**: Thay vì sửa trực tiếp database, chúng ta viết các script để thực hiện thay đổi. Điều này giúp mọi thành viên trong team có cấu trúc DB giống hệt nhau.
- **Thứ tự thực thi**: Các file được đặt tên kèm theo một mã băm (hash) hoặc số thứ tự để Alembic biết file nào chạy trước, file nào chạy sau.
- **Tính an toàn**: Mỗi bản migration đều có hàm `upgrade` để lên đời và `downgrade` để quay lại bản cũ nếu gặp lỗi.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `001_initial_migration.py`: Chứa các lệnh SQL đầu tiên để tạo ra bảng `products` và `orders`. Nếu bạn xóa database, chỉ cần chạy nâng cấp là cấu trúc sẽ được tái lập hoàn toàn.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Incremental Changes**: Instead of making direct database edits, we write scripts. This ensures all team members share the exact same database structure.
- **Execution Order**: Files are named with a hash or sequence number so Alembic knows which one runs first.
- **Safety**: Every migration includes an `upgrade` function to apply changes and a `downgrade` function to revert them if an error occurs.

### 🏛️ Practical Example
In this project:
- `001_initial_migration.py`: Contains the initial SQL commands to create the `products` and `orders` tables. If you delete the database, simply running an upgrade will fully reconstruct the schema.
