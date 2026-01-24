# ⚙️ Configuration - Quản lý Cấu hình và Môi trường / Environment & Settings Management

**Mục đích / Purpose**: Danh mục này tập trung tất cả các thông số cấu hình vào một nơi duy nhất để dễ dàng quản lý theo từng môi trường. / This directory centralizes all configuration parameters in one place for easy management across environments.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Tập trung Cấu hình**: Đảm bảo chỉ có một nguồn sự thật duy nhất cho mọi thiết lập.
2. **Tích hợp An toàn kiểu**: Biến chuỗi văn bản thuần thành đối tượng Python có kiểu dữ liệu.
3. **Quản lý Đa môi trường**: Cung cấp khả năng ghi đè cấu hình cho Dev/Test/Prod.
4. **Nạp dữ liệu Bảo mật**: Xử lý an toàn thông tin nhạy cảm từ file `.env`.
5. **Quy chuẩn Mở rộng**: Định nghĩa cách nạp mới các module cấu hình chuyên biệt.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
configs/
├── service_config.py   # Cấu hình lõi (Port, DB, Messaging).
├── logging_config.py   # Cấu hình chi tiết hệ thống nhật ký (Loguru).
├── client_config.py    # Cấu hình dịch vụ ngoại vi (Stripe, Mail).
├── llm_config.py       # Cấu hình AI/Model parameters.
└── __init__.py         # Điểm truy cập Settings tập trung.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Ứng dụng hiện đại phải chạy được ở mọi nơi mà không cần sửa code (The 12-factor app).
- **Why Pydantic-Settings?**: Giúp phát hiện sai sót cấu hình (thiếu biến, sai kiểu) ngay khi ứng dụng khởi động.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **No Secrets in Code**: Cấm tuyệt đối việc lưu mật khẩu hay keys trực tiếp trong mã nguồn.
- **Fail-Fast**: Ứng dụng không được phép khởi chạy nếu thiếu các cấu hình bắt buộc.
- **Environment Overrides**: Mọi tham số phải có khả năng bị ghi đè bởi biến môi trường của OS.

### 🏛️ Ví dụ thực tế (Examples)
- **Sử dụng**: `from configs import settings; print(settings.DATABASE_URL)`.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Centralized Control**: Established a single source of truth for application settings.
2. **Type-Safe Integration**: Converts raw strings into validated Python objects.
3. **Multi-Environment Support**: Facilitates seamless overrides for Dev, Test, and Prod.
4. **Secure Loading**: Safely decouples secrets from the source via `.env` files.
5. **Extension Protocol**: Provides a pattern for adding domain-specific config modules.

### 📂 Directory Layout
```text
configs/
├── service_config.py   # Core infra and networking settings.
├── logging_config.py   # Granular logging ecosystem configuration.
├── client_config.py    # Third-party integration details (Stripe, Mail).
├── llm_config.py       # AI and Model specific parameters.
└── __init__.py         # Centralized export hub for all settings.
```

### 💡 Context & Why
- **Context**: Modern apps must be deployable anywhere without code changes (12-factor app principles).
- **Why Pydantic-Settings?**: Enables immediate validation of settings at startup, preventing downstream errors.

### ⚠️ Process & Constraints (CCE Template)
- **Secrets Management**: Strictly prohibits hard-coding credentials in the source files.
- **Fail-Fast Policy**: The application must refuse to start if critical settings are missing.
- **OS Primacy**: Environment variables must always take precedence over file-based defaults.

### 🏛️ Practical Examples
- **Access**: `from configs import settings; print(settings.DATABASE_URL)`.
