# 🏗️ Domain Interfaces - Các Bản hợp đồng Nghiệp vụ / Business Contracts

**Mục đích / Purpose**: Danh mục `interfaces/` trong Domain là nơi định nghĩa các "bản hợp đồng" (Protocols) mà các tầng bên ngoài phải tuân thủ. Nó cho phép tầng Domain yêu cầu thực hiện các hành động (như lưu dữ liệu) mà không cần biết chi tiết kỹ thuật bên dưới. / The `interfaces/` directory within the Domain layer defines "contracts" (Protocols) that external layers must fulfill. It allows the Domain to request actions (like data persistence) without knowing the underlying technical details.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Inversion of Control (IoC)**: Thay vì Domain phụ thuộc vào DB, chúng ta đảo ngược sự phụ thuộc: Tầng Infrastructure sẽ phụ thuộc vào các Interface được định nghĩa ở đây.
- **Pure Entities**: Giúp các thực thể Domain hoàn toàn sạch bóng các mã nguồn liên quan đến framework hay IO.
- **Testability**: Nhờ có Interface, chúng ta có thể dễ dàng tạo ra các bản "Fake" hoặc "Mock" để kiểm thử logic nghiệp vụ mà không cần chạy database thật.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `repositories.py`: Định nghĩa `IOrderRepository` và `IProductRepository`. Tầng Application sẽ sử dụng những interface này để làm việc với dữ liệu, còn tầng Infrastructure sẽ chịu trách nhiệm "hiện thực hóa" (implement) chúng bằng SQLAlchemy.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Inversion of Control (IoC)**: Instead of the Domain depending on a database, we invert the dependency: the Infrastructure layer depends on the Interfaces defined here.
- **Pure Entities**: Ensures Domain entities remain completely free of framework-specific or IO-related code.
- **Testability**: Interfaces allow us to easily create "Fakes" or "Mocks" to test business logic without needing a live database.

### 🏛️ Practical Example
In this project:
- `repositories.py`: Defines `IOrderRepository` and `IProductRepository`. The Application layer uses these interfaces to work with data, while the Infrastructure layer is responsible for implementing them using SQLAlchemy.
