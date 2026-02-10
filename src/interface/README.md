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

---

## 🚀 Mở rộng: gRPC & HTTPS Strategy

Tầng Ngoài (External): Mobile/Web <--> REST/JSON <--> API Gateway.
Tầng Trong (Internal): API Gateway <--> gRPC <--> Chatbot Service <--> gRPC <--> Embedding Service.

### Bảng tổng hợp quyết định
| Kịch bản | Giao thức khuyên dùng | Lý do |
| :--- | :--- | :--- |
| Frontend gọi Backend | REST / GraphQL | Dễ tương thích, dễ debug. |
| Chatbot gọi Embedding | gRPC | Tốc độ cao, dữ liệu vector gọn nhẹ. |
| Service gọi Broker (Kafka/RabbitMQ) | Messaging (Events) | Bất đồng bộ, tăng khả năng chịu lỗi. |
| Tải file lớn(Ảnh, Âm thanh,.. )/Dữ liệu nhị phân | gRPC | Tối ưu hóa băng thông nhờ HTTP/2. |

### 🔒 HTTPS là gì?
HTTPS (HyperText Protocol Secure) là phiên bản bảo mật của HTTP. Nó sử dụng giao thức TLS (Transport Layer Security) — trước đây gọi là SSL — để mã hóa toàn bộ dữ liệu truyền tải giữa Client (Trình duyệt/Chatbot) và Server.
Mục tiêu của nó là đảm bảo 3 yếu tố mà một người cầu toàn như bạn chắc chắn sẽ quan tâm:
- **Encryption (Mã hóa)**: Người ngoài không thể "đọc trộm" dữ liệu (như nội dung chat hay API key).
- **Data Integrity (Toàn vẹn dữ liệu)**: Dữ liệu không bị chỉnh sửa trên đường truyền mà bạn không biết.
- **Authentication (Xác thực)**: Đảm bảo bạn đang kết nối đúng server thật chứ không phải một server giả mạo.

### 2. So sánh HTTP vs HTTPS
| Đặc điểm | HTTP | HTTPS |
| :--- | :--- | :--- |
| Cổng kết nối (Port) | 80 | 443 |
| Bảo mật | Không mã hóa (Plain text) | Có mã hóa (Encrypted) |
| Chứng chỉ | Không cần | Cần chứng chỉ SSL/TLS |
| Tốc độ | Nhanh hơn một chút (lý thuyết) | Chậm hơn một chút (bắt tay mã hóa) |

### 3. Cách HTTPS hoạt động (The Handshake)
Trước khi dữ liệu được gửi đi, Client và Server phải thực hiện một quy trình gọi là TLS Handshake.
1. **Client Hello**: Client gửi các phiên bản TLS và thuật toán mã hóa mà nó hỗ trợ.
2. **Server Hello & Certificate**: Server gửi lại chứng chỉ (Certificate) chứa Public Key.
3. **Key Exchange**: Client kiểm tra chứng chỉ, sau đó tạo ra một "Session Key" bí mật, mã hóa nó bằng Public Key của Server và gửi đi.
4. **Mã hóa đối xứng**: Từ lúc này, cả hai dùng Session Key đó để mã hóa mọi dữ liệu.

### 4. HTTPS có thay thế được gRPC hay không?
Thực tế, chúng không đối đầu nhau:
- **HTTP/HTTPS**: Là phương thức truyền tải (Transport).
- **gRPC**: Là cách định nghĩa hàm và dữ liệu (Framework).

**Lưu ý quan trọng**: gRPC bắt buộc chạy trên HTTP/2. Và trong hầu hết các môi trường thực tế (như khi bạn gọi API qua internet), gRPC thường được bọc trong HTTPS để đảm bảo an toàn.
Nói cách khác: **gRPC + TLS = Secure gRPC (chạy trên HTTPS)**.

### 🛡️ Triển khai HTTPS (SSL Termination)

Để chuyển đổi từ HTTP sang HTTPS, bạn có thể tiếp cận theo các cấp độ:

#### 1. Sử dụng Reverse Proxy / Load Balancer (SSL Termination)
Đây là cách chuyên nghiệp và phổ biến nhất trong Microservices. Bạn không cần cài đặt chứng chỉ cho từng service (Chatbot, Embedding), mà chỉ cần cài tại "cửa ngõ".
- **Cơ chế**: Client gọi HTTPS đến Nginx/Envoy. Nginx giải mã (decrypt) rồi gửi HTTP bình thường vào các service nội bộ.
- **Công cụ**: Nginx, HAProxy, Traefik, hoặc Envoy.
- **Ưu điểm**: Giảm tải cho các service con, quản lý chứng chỉ tập trung tại một nơi.

#### 2. Sử dụng Cloud API Gateway / CDN
Nếu bạn triển khai dự án trên Cloud (AWS, Google Cloud, Azure):
- **Cloud Load Balancer**: Tự động cấp chứng chỉ thông qua các dịch vụ như AWS Certificate Manager.
- **Cloudflare**: Cung cấp "Flexible SSL" (Mã hóa từ người dùng đến Cloudflare).
