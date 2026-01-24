# 🏗️ Alembic - Cơ chế Quản lý Phiên bản Cơ sở Dữ liệu / Database Schema Versioning

**Mục đích / Purpose**: Alembic đóng vai trò là "Git cho database", cho phép lập trình viên theo dõi, quản lý và triển khai các thay đổi cấu trúc bảng một cách đồng bộ và có thể đảo ngược. / Alembic serves as "Git for databases", enabling developers to track, manage, and deploy schema changes synchronously and reversibly.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Migration Script**: Một tập tin Python chứa logic để nâng cấp (`upgrade`) hoặc hạ cấp (`downgrade`) cấu trúc DB.
- **Revision ID**: Mã định danh duy nhất cho mỗi trạng thái của database, giúp đảm bảo tính thứ tự khi triển khai.
- **Autogenerate**: Khả năng tự động so sánh đối tượng `Base` của SQLAlchemy với DB hiện tại để sinh mã migration.

### 🏛️ Ví dụ thực tế (Cấu trúc hiện tại)
Trong dự án này, Alembic được cấu hình để hỗ trợ môi trường không đồng bộ (Async):
- `env.py`: Cấu hình engine kết nối, nạp Metadata từ `src.infrastructure.models`.
- `versions/`: Chứa các script như `001_initial_migration.py` để tạo bảng `products`, `orders`.

### 🚀 Lệnh cơ bản
1. **Tạo migration mới**: `uv run alembic revision --autogenerate -m "thông điệp"`
2. **Cập nhật lên bản mới nhất**: `uv run alembic upgrade head`

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Migration Script**: A Python file containing logic to `upgrade` or `downgrade` the database schema.
- **Revision ID**: A unique identifier for each database state, ensuring sequential deployment.
- **Autogenerate**: The ability to compare SQLAlchemy's `Base` with the live DB to automatically generate code.

### 🏛️ Practical Example (Current Setup)
In this project, Alembic is configured specifically for asynchronous environments (Async):
- `env.py`: Connects the engine and loads Metadata from `src.infrastructure.models`.
- `versions/`: Stores scripts like `001_initial_migration.py` for creating `products` and `orders` tables.

### 🚀 Common Commands
1. **Generate migration**: `uv run alembic revision --autogenerate -m "message"`
2. **Apply migrations**: `uv run alembic upgrade head`
