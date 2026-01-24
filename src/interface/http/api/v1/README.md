# 🛣️ API Routing & v1 - Thiết kế RESTful / Professional API Design

**Mục đích / Purpose**: Danh mục này định nghĩa sơ đồ đường đi của các yêu cầu HTTP cho phiên bản v1, tuân thủ nghiêm ngặt các tiêu chuẩn RESTful quốc tế. / Defines HTTP routing for API version 1, strictly adhering to global RESTful design standards.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Phơi bày Hợp đồng**: Mở các cổng HTTP để thế giới bên ngoài tương tác với nghiệp vụ.
2. **Điều hướng Yêu cầu**: Ánh xạ URL và phương thức (GET, POST...) tới hàm xử lý.
3. **Quản lý Phiên bản**: Phân tách v1 để không làm hỏng các ứng dụng khách cũ.
4. **Cung cấp Tài liệu**: Là nguồn dữ liệu chính cho hệ thống Swagger/OpenAPI.
5. **Dịch giao thức**: Chuyển đổi JSON thành đối tượng Python và ngược lại.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: API là bộ mặt của hệ thống. Nếu API lộn xộn, các lập trình viên Frontend sẽ rất khó tích hợp.
- **Why RESTful?**: Là ngôn ngữ chung của Internet. Sử dụng Danh từ cho tài nguyên (Vd: `/orders`) giúp API trở nên dễ hiểu và mang tính dự đoán cao.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Nouns, not Verbs**: Sử dụng `/orders` thay vì `/getOrders`.
- **Status Codes**: Luôn trả về đúng mã trạng thái (201 cho Create, 400 cho Bad Request, 404 cho Not Found).
- **Immutability**: Khi API v1 đã public, không bao giờ được thay đổi cấu trúc của nó (breaking changes).

### 🏛️ Ví dụ thực tế (Examples)
- **Endpoints**: [order_router.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/v1/order_router.py) định nghĩa các luồng xử lý đơn hàng.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Contract Exposure**: Opens HTTP gateways for external interaction with business services.
2. **Request Routing**: Precision mapping of URLs and Methods to internal handlers.
3. **Versioning**: Maintains v1 isolation to protect legacy client integrations.
4. **Documentation**: Serves as the primary source for interactive Swagger/OpenAPI docs.
5. **Protocol Translation**: Seamlessly bridges JSON payloads and Python structures.

### 💡 Context & Why
- **Context**: The API is the system's external face. Messy endpoints frustrate frontend developers and slow down integration.
- **Why RESTful?**: The lingua franca of the web. Using Nouns for resources (e.g., `/orders`) makes the API intuitive and predictable.

### ⚠️ Process & Constraints (CCE Template)
- **Noun Focus**: Prioritize `/orders` over action-based paths like `/createOrder`.
- **Semantic Status Codes**: Return 201 for success creation, 400 for structural errors, and 404 for missing items.
- **Immunity**: Once v1 is public, structural breaking changes are strictly prohibited.

### 🏛️ Practical Examples
- **Endpoints**: [order_router.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/v1/order_router.py) managing the order lifecycle endpoints.
