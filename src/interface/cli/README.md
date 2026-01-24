# ⌨️ CLI - Điều khiển Hệ thống bằng Dòng lệnh / System Command-Line Control

**Mục đích / Purpose**: CLI cung cấp một phương pháp trực tiếp và mạnh mẽ để tương tác với hệ thống mà không cần giao diện web. Nó thường được dùng cho các tác vụ quản trị, bảo trì hoặc seed dữ liệu. / The CLI provides a direct and powerful way to interact with the system without a web interface. It is typically used for administrative tasks, maintenance, or data seeding.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Power Users**: CLI dành cho các kỹ sư vận hành hệ thống. Nó cho phép thực hiện các lệnh phức tạp một cách nhanh chóng.
- **Automation Friendly**: Các lệnh CLI dễ dàng được gọi từ các script bash hoặc cron jobs để tự động hóa quy trình.
- **Framework (Typer)**: Chúng tôi sử dụng Typer để biến các hàm Python thành các lệnh CLI có hỗ trợ gợi ý (autocomplete) và hướng dẫn sử dụng chuyên nghiệp.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `main.py` trong thư mục `cli/` là điểm vào chính. Bạn có thể dùng nó để kiểm tra trạng thái hoặc thực hiện các lệnh cứu hộ dữ liệu khi cần.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Power Users**: Designed for operations engineers. It allows complex commands to be executed rapidly.
- **Automation Friendly**: CLI commands can be easily integrated into bash scripts or cron jobs for workflow automation.
- **Framework (Typer)**: We use Typer to transform Python functions into professional CLI commands with autocomplete and help documentation.

### 🏛️ Practical Example
In this project:
- The `main.py` within the `cli/` directory is the entry point. Use it to check system health or perform data recovery operations.
