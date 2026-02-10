# 🔌 gRPC Interface - Giao tiếp hiệu năng cao / High-Performance Communication

**Mục đích / Purpose**: Tầng gRPC chịu trách nhiệm quản lý các kết nối nội bộ giữa các service với hiệu suất cao, sử dụng giao thức HTTP/2 và cơ chế serialization nhị phân. / The gRPC layer manages high-performance internal service-to-service communications using HTTP/2 and binary serialization.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Giao tiếp nội bộ**: Tối ưu hóa việc gọi hàm từ xa giữa các Microservices (Vd: Chatbot và Embedding).
2. **Quản lý Protobuf**: Định nghĩa các bản hợp đồng dữ liệu nghiêm ngặt qua file `.proto`.
3. **Hiệu năng**: Tận dụng HTTP/2 để multiplexing và nén dữ liệu nhị phân.
4. **Xác thực nội bộ**: Đảm bảo các kết nối giữa các service được xác thực và bảo mật.
5. **Interceptor Management (Middleware)**: Thực thi các bộ lọc chung (Logging, Auth, Error Handling) cho gRPC.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
grpc/
├── protos/             # Định nghĩa các tệp Protocol Buffers (.proto).
├── services/           # Triển khai logic điều hướng và xử lý yêu cầu gRPC.
├── interceptors/       # Middleware riêng cho gRPC (Logging, Auth, v.v.).
└── __init__.py         # Khởi tạo mô-đun gRPC với Audit Logging.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Khi hệ thống mở rộng, việc gọi API qua REST/JSON có thể gây overhead do kích thước dữ liệu lớn. gRPC giúp giảm thiểu băng thông và tăng tốc độ xử lý.
- **Why gRPC?**: Hỗ trợ streaming, mạnh về kiểu dữ liệu (Strongly typed) và cực kỳ tiết kiệm tài nguyên.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Contract First**: Phải định nghĩa `.proto` trước khi triển khai code.
- **Service Mapping**: Ánh xạ từ gRPC handlers sang Application Use Cases.
- **Audit Logging**: Mọi kết nối gRPC phải được ghi nhật ký để phục vụ giám sát.

### 🏛️ Ví dụ thực tế (Examples)
- **Protobuf**: Xem [protos/order.proto](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/grpc/protos/order.proto).
- **Service Handler**: [services/order_handler.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/grpc/services/order_handler.py).

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Internal Communication**: Optimizes remote procedure calls between microservices (e.g., Chatbot and Embedding).
2. **Protobuf Management**: Defines strict data contracts via `.proto` files.
3. **Performance**: Leverages HTTP/2 for multiplexing and binary data compression.
4. **Internal Authentication**: Ensures secure and authenticated connections between internal services.
5. **Interceptor Management (Middleware)**: Executes global filters (Logging, Auth, Error Handling) for gRPC.

### 📂 Directory Layout
```text
grpc/
├── protos/             # Protocol Buffers definition files (.proto).
├── services/           # Implementations of gRPC service handlers.
├── interceptors/       # gRPC-specific middlewares (Logging, Auth, etc.).
└── __init__.py         # gRPC module initialization with Audit Logging.
```

### 💡 Context & Why
- **Context**: As systems scale, REST/JSON APIs can introduce overhead. gRPC minimizes bandwidth usage and accelerates processing.
- **Why gRPC?**: Supports native streaming, provides strong typing, and is highly resource-efficient.

### ⚠️ Process & Constraints (CCE Template)
- **Contract First**: Always define `.proto` files before implementation.
- **Service Mapping**: Map gRPC handlers directly to Application Use Cases.
- **Audit Logging**: All gRPC connections must be logged for auditing and monitoring.

### 🏛️ Practical Examples
- **Protobuf**: Refer to [protos/order.proto](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/grpc/protos/order.proto).
- **Service Handler**: [services/order_handler.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/grpc/services/order_handler.py).
