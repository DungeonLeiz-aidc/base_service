# 🌐 Interface Layer - Điểm tiếp nhận & Hợp đồng / Entry Points & Contracts

**Mục đích / Purpose**: Tầng Interface là "mặt tiền" và "biên giới" của ứng dụng, chịu trách nhiệm tiếp nhận yêu cầu và định nghĩa các bản hợp đồng kỹ thuật cho toàn hệ thống. / The Interface layer is the application's "façade" and "boundary", receiving requests and defining technical contracts for the entire system.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Môi giới Yêu cầu/Phản hồi**: Tiếp nhận dữ liệu từ các giao thức (HTTP, CLI) và trả về kết quả.
2. **Định nghĩa Hợp đồng (Protocols)**: Thiết lập các Port kỹ thuật cho Repositories và Infrastructure.
3. **Làm sạch & Ánh xạ Dữ liệu**: Kiểm tra tính hợp lệ thô của request và chuyển Schema thành DTO.
4. **Quản lý Chiến lược Giao tiếp**: Định nghĩa cách thức hệ thống phản hồi (JSON, HTML).
5. **Phòng thủ Biên giới**: Chặn đứng lỗi kỹ thuật và bảo vệ thông tin máy chủ nhạy cảm.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
interface/
├── http/               # Các cổng giao tiếp qua giao thức HTTP (API).
├── protocols/          # Các bản hợp đồng kỹ thuật (Repository/Infra protocols).
├── cli/                # Các công cụ điều khiển qua dòng lệnh.
└── schema/             # Định nghĩa dữ liệu truyền tải dùng chung.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Một hệ thống tốt cần có ranh giới rõ ràng. Tầng Interface tập hợp tất cả những gì thuộc về "Giao tiếp" — dù là giao tiếp với người dùng hay giao tiếp giữa các tầng code.
- **Why Protocols here?**: Giúp tập trung hóa mọi định nghĩa về "Port" vào một chỗ, giúp lập trình viên dễ dàng tra cứu mọi điểm chạm kỹ thuật của dự án.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Zero Logic**: Tuyệt đối không thực hiện bất kỳ phép tính nghiệp vụ nào tại đây.
- **Contract Driven**: Mọi Inbound (HTTP) và Outbound (Protocols) phải được định nghĩa rõ ràng.
- **Separation**: Schema dùng để giao tiếp với Client phải tách biệt với Entity lưu vào Database.

### 🏛️ Ví dụ thực tế (Examples)
- **Protocols**: Xem [protocols/repositories.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/protocols/repositories.py).

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Request/Response Mediation**: Receives data via protocols (HTTP, CLI) and dispatches responses.
2. **Contract Definition (Protocols)**: Establishes technical Ports for Repositories and Infrastructure.
3. **Schema Sanitization & Mapping**: Validates raw input and transforms Schemas into DTOs.
4. **Communication Strategy**: Determines the system's output format (JSON, HTML).
5. **Border Defense**: Intercepts low-level failures to protect sensitive server internals.

### 📂 Directory Layout
```text
interface/
├── http/               # HTTP protocol communication gateways (APIs).
├── protocols/          # Technical contracts (Repository/Infra protocols).
├── cli/                # Command-line control tools (Admin tasks).
└── schema/             # Shared communication data definitions.
```

### 💡 Context & Why
- **Context**: A robust system requires clear boundaries. The Interface layer aggregates everything related to "Communication" — whether with users or between code layers.
- **Why Protocols here?**: Centralizes all "Port" definitions, enabling developers to easily audit every technical touchpoint in the project.

### ⚠️ Process & Constraints (CCE Template)
- **Stateless/Logic-Free**: Strictly prohibits business calculations; focus entirely on communication logistics.
- **Contract Driven**: All Inbound (HTTP) and Outbound (Protocols) must be explicitly defined.
- **Protocol Separation**: Communication Schemas must remain strictly decoupled from Persistence Entities.

### 🏛️ Practical Examples
- **Protocols**: Refer to [protocols/repositories.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/protocols/repositories.py).
