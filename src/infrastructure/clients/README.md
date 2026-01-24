# 🔌 External Clients - Kết nối Ngoại vi / Service Integration

**Mục đích / Purpose**: Quản lý việc giao tiếp với các dịch vụ bên thứ ba (Stripe, Mail API, v.v.), đảm bảo các kết nối ra ngoài luôn an toàn và bền vững. / Manages communication with third-party services (Stripe, Mail APIs, etc.), ensuring all external connections remain secure and resilient.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Trừu tượng hóa Giao thức**: Che giấu sự phức tạp của HTTP/SDK bên dưới các hàm Python.
2. **Chuẩn hóa Giao tiếp**: Áp dụng chung quy tắc về Timeout và Header bảo mật.
3. **Lá chắn Bảo vệ**: Tích hợp Circuit Breaker để ngắt kết nối khi dịch vụ ngoài bị lỗi.
4. **Quản lý Định danh**: Tự động xử lý API Key và Bearer Tokens một cách an toàn.
5. **Tối ưu Tài nguyên**: Duy trì kết nối sẵn sàng (Connection Pooling) để tăng tốc độ.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Các dịch vụ bên ngoài (như cổng thanh toán) là thứ chúng ta không kiểm soát được. Chúng có thể sập hoặc phản hồi chậm bất cứ lúc nào.
- **Why Resilience Patterns?**: Chúng ta tích hợp Circuit Breaker để đảm bảo rằng nếu Stripe sập, hệ thống của ta không bị "treo" theo khi cố gắng chờ đợi vô ích.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Timeout bắt buộc**: Không bao giờ được phép thực hiện một cuộc gọi mạng mà không có thời hạn trả lời (Timeout).
- **Log Masking**: Thông tin nhạy cảm (API Keys) tuyệt đối không được xuất hiện trong nhật ký.
- **Interface Driven**: Phải tuân thủ theo hợp đồng đã định nghĩa tại Domain Layer.

### 🏛️ Ví dụ thực tế (Examples)
- **Stripe Client**: [payment_client.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/clients/payment_client.py) với mẫu Circuit Breaker cơ bản.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Protocol Abstraction**: Encapsulates HTTP/SDK complexities within clean Python methods.
2. **Communication Standards**: Enforces unified Timeout and Security Header policies.
3. **System Protection**: Integrates Circuit Breakers to stop calls to failing external services.
4. **Identity Management**: Safely manages API Keys and Bearer Tokens.
5. **Resource Efficiency**: Leverages Connection Pooling for rapid request handling.

### 💡 Context & Why
- **Context**: External services are outside our direct control; they can fail or lag unpredictably.
- **Why Resilience Patterns?**: Circuit Breakers ensure that a failure in a third-party (like Stripe) doesn't cascade and crash our own internal workers.

### ⚠️ Process & Constraints (CCE Template)
- **Mandatory Timeouts**: Networking calls must never be executed without a defined response window.
- **Log Masking**: Sensitive keys and secrets must never leak into system logs.
- **Interface Loyalty**: Direct implementations must honor contracts defined at the Domain layer.

### 🏛️ Practical Examples
- **Stripe Client**: [payment_client.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/clients/payment_client.py) featuring the Circuit Breaker pattern.
