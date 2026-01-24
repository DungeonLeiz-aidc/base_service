# 🚀 Source Code Root - Trục xương sống Kiến trúc / Core Architectural Root

**Mục đích / Purpose**: Thư mục `src/` là nơi chứa toàn bộ mã nguồn nghiệp vụ và kỹ thuật của ứng dụng, được tổ chức theo cấu trúc phân tầng (Layered Architecture). / The `src/` directory houses all business and technical source code, organized into a clean, layered architecture.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Phân tầng Mã nguồn**: Tổ chức code theo các lớp: Domain, Application, Infrastructure, Interface.
2. **Quản lý Luồng dữ liệu**: Đảm bảo dữ liệu đi từ Interface -> Application -> Domain -> Infrastructure.
3. **Cách ly Logic**: Đảm bảo mỗi tầng chỉ thực hiện đúng một nhiệm vụ duy nhất (Single Responsibility).
4. **Cung cấp Entry Point**: Khởi chạy ứng dụng thông qua file `main.py` tại root của `src/`.
5. **Duy trì Tính khả chuyển**: Thiết lập để code có thể chạy được trên mọi môi trường qua cấu trúc module.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
src/
├── domain/             # Tầng nghiệp vụ (Entities, Events, Interfaces).
├── application/        # Tầng điều phối (Services, DTOs).
├── infrastructure/     # Tầng kỹ thuật (DB, Cache, Messaging, Models).
└── interface/          # Tầng giao tiếp (HTTP APIs, CLI, Middlewares).
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Nếu để toàn bộ code vào một chỗ, hệ thống sẽ trở nên cực kỳ khó bảo trì (Spaghetti code).
- **Why Layering?**: Việc chia tầng giúp chúng ta có ranh giới rõ ràng, dễ dàng thay thế linh kiện và kiểm thử biệt lập.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Dependency Flow**: Tuân thủ nghiêm ngặt quy tắc phụ thuộc: Tầng ngoài có thể biết tầng trong, tầng trong CẤM biết tầng ngoài.
- **Modularity**: Mỗi file nên giải quyết một vấn đề cụ thể, tránh các file "God Object" khổng lồ.

### 🏛️ Ví dụ thực tế (Examples)
- **Khởi động**: [main.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/main.py) là nơi khởi tạo FastAPI và nạp các routes.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Code Layering**: Organizes logic into Domain, Application, Infrastructure, and Interface.
2. **Data Flow Management**: Orchestrates movement from Interface towards the Domain core.
3. **Logic Isolation**: Enforces the Single Responsibility Principle within each architectural tier.
4. **Entry Point Provision**: Hosts [main.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/main.py) to launch the service ecosystem.
5. **Portability**: Ensures code execution consistency across all deployment environments.

### 📂 Directory Layout
```text
src/
├── domain/             # Business core (Entities, Events, Interfaces).
├── application/        # Use case logic (Services, DTOs).
├── infrastructure/     # Technical details (DB, Cache, Messaging, Models).
└── interface/          # Communication gateways (HTTP, CLI, Middlewares).
```

### 💡 Context & Why
- **Context**: Monolithic, flat code structures inevitably decay into "Spaghetti". Layering prevents this structural rot.
- **Why Layering?**: Defines clear boundaries, enabling independent component testing and seamless technological swapping.

### ⚠️ Process & Constraints (CCE Template)
- **Dependency Direction**: Outer layers depend on inner ones; inner layers remain strictly agnostic of implementation details.
- **Modularity**: Maintain high cohesion and low coupling; avoid "God Objects".

### 🏛️ Practical Examples
- **Startup**: [main.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/main.py) initializing the FastAPI app and mounting routers.
