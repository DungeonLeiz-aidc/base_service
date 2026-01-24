# 🖼️ Static Assets - Tài nguyên Tĩnh / Public Files & Assets

**Mục đích / Purpose**: Thư mục `static/` chứa các tài nguyên được phục vụ trực tiếp cho người dùng mà không cần qua xử lý của logic nghiệp vụ. Đây là nơi lưu trữ hình ảnh, tài liệu hướng dẫn hoặc các file cấu hình công khai. / The `static/` directory contains assets served directly to users without business logic processing. It stores images, manuals, or public configuration files.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Public Accessibility**: Các file ở đây có thể truy cập trực tiếp qua URL (ví dụ: `http://localhost:8000/static/logo.png`).
- **Separation**: Tách biệt tài nguyên giao diện khỏi mã nguồn giúp việc quản lý và tối ưu hóa (như dùng CDN) trở nên dễ dàng hơn.
- **FastAPI Mounting**: Chúng tôi sử dụng tính năng `StaticFiles` của FastAPI để "gắn" thư mục này vào ứng dụng một cách an toàn.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- Bạn có thể lưu trữ sơ đồ kiến trúc hệ thống (`architecture.png`) ở đây để hiển thị trực tiếp trong các file tài liệu hoặc dashboard quản trị.
- Cấu hình robots.txt để hướng dẫn các bộ máy tìm kiếm (SEO).

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Public Accessibility**: Files here are directly accessible via URL (e.g., `http://localhost:8000/static/logo.png`).
- **Separation**: Isolating assets from source code simplifies management and optimization (like utilizing a CDN).
- **FastAPI Mounting**: We use FastAPI's `StaticFiles` functionality to safely "mount" this directory within the application.

### 🏛️ Practical Example
In this project:
- Store architectural diagrams (`architecture.png`) here for direct display in documentation or admin dashboards.
- Hosting `robots.txt` to provide instructions for search engine crawlers (SEO).
