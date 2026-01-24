# 🛣️ API Routing - Điều hướng Yêu cầu / API Endpoint Management

**Mục đích / Purpose**: Thư mục `api/` là nơi định nghĩa sơ đồ đường đi (Routing) cho các yêu cầu HTTP. Nó giúp tách biệt phiên bản API (Version) và phân nhóm các tính năng một cách khoa học. / The `api/` directory defines the routing for HTTP requests, isolating API versions and grouping features logically.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **API Versioning**: Chúng ta sử dụng phiên bản (như `v1`, `v2`) để có thể nâng cấp hệ thống mà không làm hỏng các ứng dụng cũ đang sử dụng API.
- **Hierarchical Routing**: Cấu trúc thư mục tương ứng với đường dẫn URL (ví dụ: `/api/v1/orders`). Điều này giúp việc tìm kiếm code cực kỳ nhanh chóng.
- **Router Composition**: Mỗi module (như Orders, Products) có router riêng, sau đó được gộp lại ở router cha.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `v1/`: Chứa các định nghĩa API đầu tiên của hệ thống. Đây là nơi bạn sẽ tìm thấy cách các URL được ánh xạ vào các hàm xử lý.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **API Versioning**: We use versions (e.g., `v1`, `v2`) to allow system upgrades without breaking legacy client applications.
- **Hierarchical Routing**: The directory structure mirrors the URL paths (e.g., `/api/v1/orders`), making code navigation intuitive.
- **Router Composition**: Each module (Orders, Products) has its own router, which is then aggregated into a parent router.

### 🏛️ Practical Example
In this project:
- `v1/`: Contains the system's initial API definitions. This is where URL mapping to handler functions is defined.
