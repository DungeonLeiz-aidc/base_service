# 📜 Logs - Nhật ký Vận hành Hệ thống / System Operational Logs

**Mục đích / Purpose**: Thư mục này là nơi lưu giữ toàn bộ nhật ký hoạt động của hệ thống, giúp chẩn đoán lỗi, theo dõi hiệu năng và đảm bảo tính bảo mật. / This directory stores all system operation logs, aiding in diagnostics, performance monitoring, and security auditing.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Lưu vết Vận hành**: Ghi lại chi tiết mọi yêu cầu và phản hồi qua hệ thống.
2. **Chẩn đoán Lỗi**: Cung cấp Stack Trace và ngữ cảnh để kỹ sư nhanh chóng tìm nguyên nhân sự cố.
3. **Bảo vệ Quyền riêng tư**: Tự động che dấu (Masking) thông tin nhạy cảm như Email, Customer ID.
4. **Quản lý Lưu trữ**: Tự động phân tách file hàng ngày (Rotation) và dọn dẹp bản ghi cũ (Retention).
5. **Giám sát Hiệu năng**: Ghi lại thời gian xử lý của các Use Case để phát hiện nút thắt cổ chai.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Trong hệ thống phân tán, việc biết "ai đã làm gì khi nào" là sống còn để giải quyết các tranh chấp dữ liệu và lỗi bất ngờ.
- **Why Loguru?**: Cung cấp khả năng cấu hình cực kỳ linh hoạt, hỗ trợ ghi log bất đồng bộ (Thread-safe) và cơ chế Filtering/Masking rất mạnh mẽ.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Masking bắt buộc**: Không bao giờ được phép ghi dữ liệu thô nhạy cảm (PII) vào log.
- **Cấp độ Log**: Sử dụng đúng cấp độ (DEBUG cho phát triển, INFO cho vận hành, ERROR cho sự cố).
- **Rotation Group**: Phải cấu hình xoay vòng file để tránh làm tràn ổ cứng server.

### 🏛️ Ví dụ thực tế (Examples)
- **Cấu hình**: Xem [logging_config.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/configs/logging_config.py).
- **Nhật ký**: Các file `.log` sinh ra trong thư mục này chứa thông báo theo định dạng JSON hoặc text chuẩn.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Operational Tracing**: Detailed recording of all system requests and responses.
2. **Error Diagnostics**: Deep stack traces and contextual info for rapid root-cause analysis.
3. **Privacy Enforcement**: Automated masking of sensitive fields (Emails, IDs) within logs.
4. **Log Storage Management**: Daily file rotation and policy-based log retention.
5. **Performance Monitoring**: Tracking execution times to identify system bottlenecks.

### 💡 Context & Why
- **Context**: In distributed architectures, knowing "who did what and when" is vital for debugging data disputes and unexpected failures.
- **Why Loguru?**: Offers extreme configuration flexibility, thread-safe asynchronous logging, and superior filtering/masking capabilities.

### ⚠️ Process & Constraints (CCE Template)
- **Mandatory Masking**: PII data must never be stored in its raw format within logs.
- **Severity Levels**: Use standard levels correctly (DEBUG for dev, INFO for ops, ERROR for crashes).
- **Disc Management**: Rotation policies must be enabled to prevent disk space exhaustion.

### 🏛️ Practical Examples
- **Configuration**: Refer to [logging_config.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/configs/logging_config.py).
- **Output**: `.log` files in this directory formatted as structured JSON or standard text.
