# 📂 Seed Data - Khởi tạo Dữ liệu / System Bootstrapping

**Mục đích / Purpose**: Seed data giúp hệ thống có sẵn các dữ liệu cần thiết ngay sau khi triển khai (ví dụ: các sản phẩm mẫu, cấu hình mặc định). Điều này cực kỳ quan trọng cho việc demo và testing. / Seed data ensures the system has necessary data immediately after deployment (e.g., sample products, default configs). This is critical for demos and testing.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Bootstrapping**: Quá trình đưa hệ thống từ trạng thái "trống rỗng" sang trạng thái có thể sử dụng được.
- **Dữ liệu tĩnh vs Dữ liệu động**: Seed data thường là dữ liệu tĩnh hoặc dữ liệu mẫu để hướng dẫn người dùng cách hệ thống vận hành.
- **Idempotency**: Quá trình seed nên có tính "lặp lại" - chạy nhiều lần không gây lỗi hoặc trùng lặp dữ liệu.

### 🏛️ Ví dụ thực tế (Example)
- `products.json`: Danh sách các sản phẩm điện tử mẫu để người dùng có thể bắt đầu đặt hàng ngay.
- `seed_products.py`: Script chịu trách nhiệm đọc file JSON và nạp vào PostgreSQL một cách an toàn.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Bootstrapping**: The process of taking a system from an "empty" state to a usable state.
- **Static vs Dynamic Data**: Seed data is usually static or sample data used to demonstrate how the system operates.
- **Idempotency**: Seeding should be "idempotent" - running it multiple times should not cause errors or duplicate data.

### 🏛️ Practical Example
- `products.json`: A list of sample electronic products so users can start placing orders immediately.
- `seed_products.py`: The script responsible for reading the JSON file and safely populating PostgreSQL.
