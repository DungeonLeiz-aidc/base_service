# 🏗️ Infrastructure Layer - Chi tiết Kỹ thuật / Technical Implementation

**Mục đích / Purpose**: Tầng Infrastructure là nơi hiện thực hóa các "bản hợp đồng" từ Domain. Nó chứa mã nguồn liên quan đến Database, Cache, Messaging và các dịch vụ bên thứ ba. / The Infrastructure layer provides the concrete implementation of Domain contracts. It contains all code related to Databases, Caching, Messaging, and third-party services.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tại sao lại để Database ở ngoài cùng? Để logic nghiệp vụ không bị phụ thuộc vào SqlAlchemy hay Redis. Khi cần thay đổi thư viện, bạn chỉ cần sửa ở tầng này.
- **Why Mapping?**: Đây là nơi chúng ta thực hiện việc "ánh xạ" (Mapping) từ các Model của Database (vốn có nhiều ràng buộc kỹ thuật) sang các Entity của Domain (vốn chỉ quan tâm đến nghiệp vụ).

### ⚠️ Ràng buộc (Constraints)
1. **Implementation-Focused**: Tầng này chỉ chứa mã thực thi các Interface đã định nghĩa ở Domain.
2. **Framework Boundary**: Đây là nơi duy nhất được phép chứa các thư viện nặng về IO (SQLAlchemy, Redis-py, Aio-pika).

### 🏛️ Ví dụ thực tế (Examples)
- **Repositories**: [OrderRepository](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/order_repository.py) sử dụng SQLAlchemy.
- **Clients**: [RedisInventoryCache](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) xử lý Distributed Locking.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: Why keep the Database on the outermost layer? To prevent business logic from depending on SQLAlchemy or Redis. When libraries change, modifications are localized here.
- **Why Mapping?**: This is where we perform "Mapping" between Database Models (with technical constraints) and Domain Entities (focused solely on business).

### ⚠️ Constraints
1. **Implementation-Focused**: This layer only implements Interfaces defined in the Domain.
2. **Framework Boundary**: This is the only place allowed to contain IO-heavy libraries (SQLAlchemy, Redis-py, Aio-pika).

### 🏛️ Practical Examples
- **Repositories**: [OrderRepository](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/order_repository.py) uses SQLAlchemy.
- **Clients**: [RedisInventoryCache](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) handles Distributed Locking.
