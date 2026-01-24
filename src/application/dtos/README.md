# 📄 Data Transfer Objects (DTOs) - Vật chứa Dữ liệu / Data Containers

**Mục đích / Purpose**: DTO là các đối tượng dùng để đóng gói dữ liệu và gửi đi giữa các tầng của ứng dụng. Chúng giúp bảo vệ tầng Domain khỏi bị "ô nhiễm" bởi cấu trúc dữ liệu của API hoặc Database. / DTOs are objects used to package and transfer data between application layers. They protect the Domain layer from being "polluted" by API or Database data structures.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Biên giới (Boundary)**: DTO xác định những gì tầng Application sẵn sàng nhận vào và trả ra.
- **Không chứa Logic**: DTO chỉ là các class chứa thuộc tính (như Data Classes), không được chứa logic nghiệp vụ.
- **Tính linh hoạt**: Bạn có thể đổi tên trường trong Database (Model) mà không làm thay đổi API response (DTO), nhờ vào một bước chuyển đổi (Mapping) ở giữa.

### 🏛️ Ví dụ thực tế (Example)
- `PlaceOrderRequestDTO`: Chỉ chứa `customer_id` và danh sách sản phẩm, không chứa các logic kiểm tra kho.
- `OrderResponseDTO`: Chứa thông tin đơn hàng đã được định dạng để trả về cho người dùng.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Boundary**: DTOs define what the Application layer is willing to accept and return.
- **Logic-free**: DTOs are simple data containers (like Data Classes); they must not contain business logic.
- **Flexibility**: You can change a field name in the Database (Model) without changing the API response (DTO), thanks to a mapping step in between.

### 🏛️ Practical Example
- `PlaceOrderRequestDTO`: Contains only `customer_id` and item list, with no inventory check logic.
- `OrderResponseDTO`: Contains order information formatted specifically for the end-user.
