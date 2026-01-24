# ⚙️ Configuration - Quản lý Cấu hình và Môi trường / Environment & Settings Management

**Mục đích / Purpose**: Thư mục này đóng vai trò là "Trung tâm điều khiển" của ứng dụng. Nó tập trung tất cả các thông số cấu hình (DB URL, Redis port, API keys) vào một nơi duy nhất để dễ dàng quản lý và thay đổi theo từng môi trường (Dev, Staging, Prod). / This directory acts as the "Control Center" for the application. It centralizes all configuration parameters (DB URL, Redis port, API keys) in one place for easy management across environments (Dev, Staging, Prod).

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **12-Factor App**: Một ứng dụng tốt không bao giờ "hard-code" cấu hình trong mã nguồn. Chúng ta sử dụng biến môi trường (Environment Variables) để linh hoạt hóa hệ thống.
- **Type Safety**: Sử dụng `Pydantic-settings` giúp đảm bảo cấu hình bạn nhập vào luôn đúng kiểu dữ liệu (ví dụ: Port phải là số).
- **Global Access**: Các module khác chỉ cần import đối tượng `settings` đã được khởi tạo sẵn để sử dụng.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `service_config.py`: Định nghĩa class `Settings` tự động đọc file `.env`.
- `logging_config.py`: Quy định cách hệ thống ghi log (ghi ra file hay console, định dạng như thế nào).

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **12-Factor App**: A well-designed application never hard-codes configurations. We use Environment Variables to make the system flexible.
- **Type Safety**: Using `Pydantic-settings` ensures your configurations always have the correct data type (e.g., Port must be an integer).
- **Global Access**: Other modules simply import a pre-initialized `settings` object to access configuration data.

### 🏛️ Practical Example
In this project:
- `service_config.py`: Defines the `Settings` class that automatically reads the `.env` file.
- `logging_config.py`: Specifies how the system logs information (output destination, format, etc.).
