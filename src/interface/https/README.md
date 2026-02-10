# 🔒 HTTPS & Proxy Infrastructure - Hạ tầng Bảo mật / Security Infrastructure

**Mục đích / Purpose**: Thư mục này chứa các cấu hình cho Proxy và Load Balancer nhằm thực hiện SSL Termination, đảm bảo an toàn cho toàn bộ luồng dữ liệu truyền tải. / This directory contains configurations for Proxies and Load Balancers to perform SSL Termination and ensure transport-level security.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **SSL Termination**: Giải mã HTTPS tại Proxy để giảm tải cho các ứng dụng nội bộ.
2. **Quản lý Chứng chỉ**: Tập trung hóa việc quản lý SSL/TLS certificates tại một điểm duy nhất.
3. **Phòng thủ Biên giới**: Sử dụng các công cụ như Nginx, Envoy để ngăn chặn các cuộc tấn công tầng hạ tầng.
4. **Cân bằng Tải**: Điều phối lưu lượng truy cập giữa các instance của service.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
https/
├── nginx/              # Cấu hình mẫu cho Nginx.
├── haproxy/            # Cấu hình mẫu cho HAProxy.
├── envoy/              # Cấu hình mẫu cho Envoy Proxy.
├── traefik/            # Cấu hình mẫu cho Traefik.
└── __init__.py         # Khởi tạo mô-đun HTTPS với Audit Logging.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Bảo mật là ưu tiên hàng đầu. Việc sử dụng HTTPS đảm bảo tính toàn vẹn và bảo mật của dữ liệu người dùng.
- **Why Reverse Proxy?**: Giúp hệ thống linh hoạt hơn, dễ dàng mở rộng và bảo trì chứng chỉ mà không cần can thiệp vào mã nguồn ứng dụng.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Security First**: Luôn ưu tiên các chuẩn mã hóa hiện đại (TLS 1.3).
- **Centralized Config**: Duy trì cấu hình tập trung để dễ dàng audit và cập nhật.
- **Audit Logging**: Mọi thay đổi về hạ tầng bảo mật phải được ghi lại.

### 🏛️ Ví dụ thực tế (Examples)
- **Nginx Config**: Xem [nginx/ssl_termination.conf](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/https/nginx/ssl_termination.conf).
- **Envoy Config**: [envoy/envoy.yaml](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/https/envoy/envoy.yaml).

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **SSL Termination**: Decrypts HTTPS at the Proxy level to offload application services.
2. **Certificate Management**: Centralizes SSL/TLS certificate handling in a single location.
3. **Edge Defense**: Utilizes tools like Nginx and Envoy to mitigate infrastructure-level attacks.
4. **Load Balancing**: Distributes traffic across multiple service instances.

### 📂 Directory Layout
```text
https/
├── nginx/              # Nginx configuration examples.
├── haproxy/            # HAProxy configuration examples.
├── envoy/              # Envoy Proxy configuration examples.
├── traefik/            # Traefik configuration examples.
└── __init__.py         # HTTPS module initialization with Audit Logging.
```

### 💡 Context & Why
- **Context**: Security is paramount. HTTPS ensures data integrity and user privacy.
- **Why Reverse Proxy?**: Provides flexibility, scalability, and simplified certificate management without modifying application code.

### ⚠️ Process & Constraints (CCE Template)
- **Security First**: Prioritize modern encryption standards (e.g., TLS 1.3).
- **Centralized Config**: Maintain centralized configurations for easier auditing and updates.
- **Audit Logging**: All security-related infrastructure changes must be logged.

### 🏛️ Practical Examples
- **Nginx Config**: Refer to [nginx/ssl_termination.conf](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/https/nginx/ssl_termination.conf).
- **Envoy Config**: [envoy/envoy.yaml](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/https/envoy/envoy.yaml).
