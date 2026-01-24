# 🛣️ API Versioning Hub - Điều hướng Phiên bản / API Strategic Routing

**Mục đích / Purpose**: Danh mục này là trung tâm điều hướng cho các phiên bản API của hệ thống, cho phép ứng dụng mở rộng tính năng mới mà không làm hỏng các phiên bản cũ. / This directory acts as the central hub for API versioning, enabling feature growth without breaking legacy client support.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Quản lý Phiên bản (Versioning Control)**: Phân tách logic giữa các phiên bản (Vd: v1, v2) một cách tường minh.
2. **Hợp nhất Router (Router Consolidation)**: Gom nhóm tất cả cá nhánh API v1, v2 vào một điểm truy cập duy nhất.
3. **Định danh Tài nguyên (Resource Naming)**: Đảm bảo các đường dẫn tuân thủ chuẩn danh từ RESTful.
4. **Cung cấp Metadata**: Thiết lập các thẻ (Tags) và thông tin mô tả cho Swagger tham chiếu.
5. **Cách ly Thay đổi (Change Isolation)**: Đảm bảo một thay đổi lớn ở v2 không bao giờ ảnh hưởng tới v1 đang chạy ổn định.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
api/
├── v1/                 # Phiên bản API hiện tại (Ổn định).
└── router.py           # Điểm hợp nhất toàn bộ các phiên bản API.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Khi một service phát triển, các thay đổi làm "gãy" cấu trúc (Breaking changes) là không thể tránh khỏi.
- **Why Versioning?**: Cho phép chúng ta duy trì song song cả cũ và mới. Khách hàng cũ dùng `/v1`, khách hàng mới tham gia dùng `/v2`.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Semantic Path**: Tiền tố phiên bản phải luôn xuất hiện trong URL (Vd: `/api/v1/...`).
- **Backward Compatibility**: Không được phép xóa bỏ hoặc sửa cấu trúc v1 sau khi đã công bố.
- **Registry**: Mọi router phiên bản mới phải được đăng ký (register) tại file `router.py` chính.

### 🏛️ Ví dụ thực tế (Examples)
- **Routing**: Xem [router.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/router.py) để thấy cách v1 được nạp vào hệ thống.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Versioning Control**: Cleary isolates logic between API versions (e.g., v1, v2).
2. **Router Consolidation**: Aggregates all version-specific routers into a single mount point.
3. **Resource Naming**: Enforces the use of RESTful nouns for all endpoints.
4. **Metadata Provisioning**: Configures the descriptions and tags used by Swagger/OpenAPI.
5. **Change Isolation**: Guarantees that major updates in v2 never disrupt stable v1 operations.

### 📂 Directory Layout
```text
api/
├── v1/                 # Current stable API implementation.
└── router.py           # Master merging point for all versioned routers.
```

### 💡 Context & Why
- **Context**: As services evolve, breaking changes are inevitable when requirements shift.
- **Why Versioning?**: Enables the concurrent existence of the old and the new. Legacy clients use `/v1`, while early adopters migrate to `/v2`.

### ⚠️ Process & Constraints (CCE Template)
- **Semantic Path**: Version prefixes must always appear in the URL path (e.g., `/api/v1/...`).
- **Backward Compatibility**: Deleting or altering public v1 structures is strictly prohibited.
- **Registry**: New version routers must be explicitly registered within the main `router.py` file.

### 🏛️ Practical Examples
- **Routing**: Refer to [router.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/router.py) to see how v1 is mounted into the FastAPI app.
