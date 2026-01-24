# 🌐 Interface Layer - Cổng Giao Tiếp / Gateways & Entry Points

**Mục đích / Purpose**: Tầng Interface là nơi hệ thống "mở cửa" đón nhận yêu cầu từ thế giới bên ngoài. Nó chịu trách nhiệm nhận dữ liệu, kiểm tra định dạng cơ bản và chuyển đổi chúng thành các yêu cầu mà tầng Application có thể hiểu được. / The Interface layer provides entry points for external requests. It is responsible for receiving data, basic validation, and converting it into requests that the Application layer can process.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Drivers (Entry Points)**: Các phương thức khác nhau để khởi động một Use Case (ví dụ: HTTP Request, CLI Command, Message từ Queue).
- **Schemas**: Định nghĩa hợp đồng dữ liệu với người dùng (Input/Output). Khác với DTO, Schemas thường chứa các ràng buộc của framework (như Pydantic cho FastAPI).
- **Middlewares**: Các bộ lọc xử lý chung cho mọi yêu cầu (Logging, Auth, Error Handling).

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `http/`: Chứa các API RESTful xây dựng bằng FastAPI.
- `cli/`: Chứa các lệnh quản trị hệ thống (`Typer`).
- `worker.py`: Tiến trình nền lắng nghe sự kiện từ RabbitMQ để thực hiện các tác vụ nặng.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Drivers (Entry Points)**: Different ways to trigger a Use Case (e.g., HTTP Request, CLI Command, Message from a Queue).
- **Schemas**: Define data contracts with users (Input/Output). Unlike DTOs, Schemas often contain framework-specific constraints (like Pydantic for FastAPI).
- **Middlewares**: Filters for common request processing (Logging, Auth, Error Handling).

### 🏛️ Practical Example
In this project:
- `http/`: Contains RESTful APIs built with FastAPI.
- `cli/`: Contains administration commands built with `Typer`.
- `worker.py`: Background process listening to RabbitMQ events for heavy lifting tasks.
