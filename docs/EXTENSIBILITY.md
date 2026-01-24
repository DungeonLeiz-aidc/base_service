# 🚀 Developer Extensibility Guide - Hướng dẫn Mở rộng Hệ thống

Dự án được thiết kế để dễ dàng mở rộng theo chiều ngang. Khi muốn thêm một tính năng mới (ví dụ: `Cập nhật tồn kho`), hãy tuân theo quy trình "Domain-First" dưới đây. / The project is designed for easy horizontal scaling. When adding a new feature (e.g., `Update Stock`), follow this "Domain-First" workflow.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🔄 Quy trình 4 bước (The 4-Step Flow)

1.  **Tầng Domain (Trái tim)**: 
    *   Xác định Entity hoặc Event mới (Vd: `StockUpdated` event).
    *   Định nghĩa Interface cho Repository mới trong `src/domain/interfaces/`.
2.  **Tầng Application (Điều phối)**: 
    *   Tạo DTO cho yêu cầu mới.
    *   Tạo Service thực thi Use Case. Service này sẽ sử dụng Interface đã định nghĩa ở bước 1.
3.  **Tầng Infrastructure (Kỹ thuật)**:
    *   Triển khai thực tế Interface (ví dụ: dùng SQLAlchemy).
    *   Đăng ký component mới vào `src/container.py`.
4.  **Tầng Interface (Mặt tiền)**:
    *   Tạo API Route mới trong `src/interface/http/api/v1/`.
    *   Định nghĩa Pydantic Schema cho Request/Response.

### 💡 Quy tắc Quan trọng
- **Không bao giờ** import trực tiếp từ `infrastructure` vào `domain`.
- Luôn kiểm thử logic nghiệp vụ bằng **Unit Tests** trước khi viết API.

---

## 🇺🇸 English Version

### 🔄 The 4-Step Flow

1.  **Domain Layer (The Heart)**: 
    *   Define new Entities or Events (e.g., `StockUpdated`).
    *   Define new Repository Interfaces in `src/domain/interfaces/`.
2.  **Application Layer (Orchestration)**: 
    *   Create DTOs for the new request.
    *   Create a Service to execute the Use Case, using the interfaces from Step 1.
3.  **Infrastructure Layer (Technical Detail)**:
    *   Provide the concrete implementation (e.g., SQLAlchemy logic).
    *   Register the new component in `src/container.py`.
4.  **Interface Layer (The Façade)**:
    *   Create new API Routes in `src/interface/http/api/v1/`.
    *   Define Pydantic Schemas for Request/Response validation.

### 💡 Golden Rules
- **Never** import from `infrastructure` directly into the `domain`.
- Always verify business logic via **Unit Tests** before exposing the API.
