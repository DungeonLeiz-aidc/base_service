# 🔌 External Clients - Kết nối Ngoại vi / Service Integration

**Mục đích / Purpose**: Quản lý việc giao tiếp với các dịch vụ bên thứ ba và các hệ thống hỗ trợ kỹ thuật (Auth, Payment, Mail), đảm bảo các kết nối ra ngoài luôn an toàn và bền vững. / Manages communication with third-party services and technical support systems (Auth, Payment, Mail), ensuring all external connections remain secure and resilient.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Trừu tượng hóa Giao thức**: Che giấu sự phức tạp của HTTP/SDK bên dưới các hàm Python.
2. **Quản lý Định danh (Auth)**: Triển khai các cơ chế bảo mật như JWT Bearer Token.
3. **Chuẩn hóa Giao tiếp**: Áp dụng chung quy tắc về Timeout và Header bảo mật.
4. **Lá chắn Bảo vệ**: Tích hợp Circuit Breaker để ngắt kết nối khi dịch vụ ngoài bị lỗi.
5. **Tối ưu Tài nguyên**: Duy trì kết nối sẵn sàng (Connection Pooling) để tăng tốc độ.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Các dịch vụ bên ngoài (như cổng thanh toán) hoặc các cơ chế bảo mật (JWT) cần được đóng gói để dễ dàng thay thế mà không ảnh hưởng tới core.
- **Why Resilience Patterns?**: Chúng ta tích hợp Circuit Breaker để đảm bảo rằng nếu một dịch vụ ngoài sập, hệ thống của ta không bị "treo" theo.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Security First**: Các secret key và thuật toán mã hóa phải được nạp từ cấu hình hệ thống.
- **Timeout bắt buộc**: Không bao giờ được phép thực hiện một cuộc gọi mạng mà không có thời hạn trả lời.
- **Log Masking**: Thông tin nhạy cảm (Tokens, Keys) tuyệt đối không được xuất hiện trong nhật ký.

### 🏛️ Ví dụ thực tế (Examples)
- **Auth Provider**: [auth_provider.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/clients/auth_provider.py) xử lý JWT.
- **Stripe Client**: [payment_client.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/clients/payment_client.py) với mẫu Circuit Breaker.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Protocol Abstraction**: Encapsulates HTTP/SDK complexities within clean Python methods.
2. **Identity Management (Auth)**: Implements security mechanisms like JWT Bearer Tokens.
3. **Communication Standards**: Enforces unified Timeout and Security Header policies.
4. **System Protection**: Integrates Circuit Breakers to stop calls to failing external services.
5. **Resource Efficiency**: Leverages Connection Pooling for rapid request handling.

### 💡 Context & Why
- **Context**: External providers and security engines must be encapsulated to enable seamless swaps without core disruption.
- **Why Resilience Patterns?**: Circuit Breakers ensure that external failures don't ripple into internal system paralysis.

### ⚠️ Process & Constraints (CCE Template)
- **Security Governance**: All encryption algorithms and keys must be securely injected via configuration.
- **Mandatory Timeouts**: Networking calls must never be executed without a defined response window.
- **Log Masking**: Sensitive tokens and private keys must be strictly redacted from all system logs.

### 🏛️ Practical Examples
- **Auth Provider**: [auth_provider.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/clients/auth_provider.py) governing JWT logic.
- **Payment Client**: [payment_client.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/clients/payment_client.py).
