# 🚚 Infrastructure Migrations - Tiến hóa Dữ liệu trong Code / Source-Controlled Schema Evolution

**Mục đích / Purpose**: Khác với thư mục `alembic/` (chứa cấu hình công cụ), thư mục `migrations/` trong `src/` là nơi chứa logic nghiệp vụ và cấu hình engine dành riêng cho việc migration bên trong ứng dụng. Nó đảm bảo việc "dây dợ" (wiring) giữa model và database được thiết lập đúng đắn. / Unlike the `alembic/` directory (tool configuration), the `migrations/` directory in `src/` contains business logic and engine configurations specifically for application-side migrations, ensuring proper wiring between models and the database.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Metadata Bridge**: Đây là cây cầu kết nối các class Python (Models) với các bảng thực trong SQL. Nếu không có bridge này, Alembic sẽ không biết bạn vừa thêm một cột mới.
- **Environment Handling**: Đảm bảo migration chạy đúng dù bạn đang dùng SQLite (khi test) hay PostgreSQL (khi chạy thật).
- **Automation**: Cho phép tự động hóa việc nâng cấp database khi server start (nếu được cấu hình).

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `env.py`: Chứa logic để Alembic "soi" vào toàn bộ thư mục `models/` và phát hiện ra sự thay đổi của bảng `orders`.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Metadata Bridge**: Connects Python classes (Models) to actual SQL tables. Without this bridge, Alembic wouldn't know when you've added a new column.
- **Environment Handling**: Ensures migrations work correctly whether using SQLite (testing) or PostgreSQL (production).
- **Automation**: Enables automated database upgrades upon server startup if configured.

### 🏛️ Practical Example
In this project:
- `env.py`: Contains the logic enabling Alembic to "inspect" the `models/` directory and detect changes in the `orders` table.
