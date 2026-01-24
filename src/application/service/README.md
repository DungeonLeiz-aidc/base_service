# ⚙️ Application Services - Thực thi Use Cases / Workflow Orchestrators

**Mục đích / Purpose**: Thư mục này chứa các Services - nơi thực hiện các luồng công việc của hệ thống. Mỗi Service thường đại diện cho một tính năng mà người dùng muốn thực hiện. / This directory contains Services - where the system's workflows are executed. Each Service typically represents a feature that a user wants to perform.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Stateless**: Các service nên là không trạng thái. Dữ liệu được truyền vào qua DTO và kết quả được trả ra qua DTO.
- **Transaction Boundary**: Service là nơi bắt đầu và kết thúc một transaction (trong bộ nhớ hoặc database).
- **Phối hợp**: Service không tự làm hết mọi việc. Nó hỏi Repository để lấy dữ liệu, bảo Entity thực hiện logic nghiệp vụ, và bảo Publisher gửi thông báo.

### 🏛️ Ví dụ thực tế (Example)
- `PlaceOrderService`: Một Service điển hình thực hiện quy trình 5 bước: Kiểm tra SP -> Giữ kho -> Tạo đơn -> Lưu DB -> Bắn Event.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Stateless**: Services should be stateless. Data flows in via DTOs and results flow out via DTOs.
- **Transaction Boundary**: The Service is where a transaction (in-memory or database) begins and ends.
- **Orchestration**: A Service doesn't do everything. It asks the Repository for data, tells the Entity to execute business logic, and tells the Publisher to send notifications.

### 🏛️ Practical Example
- `PlaceOrderService`: A typical Service implementing a 5-step workflow: Check Product -> Reserve Stock -> Create Order -> Save to DB -> Publish Event.
