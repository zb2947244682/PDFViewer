# PDFViewer

本项目是一个基于 Flask 和 PyMuPDF 的 PDF 在线图片转换与信息获取服务。支持从指定 PDF URL 下载 PDF 文件，将第一页渲染为图片，并可获取 PDF 页数。

## 功能简介
- 提供 `/PDFViewer` 接口，将指定 PDF 的第一页转换为 PNG 图片（宽度最大1920像素，高度等比缩放）。
- 提供 `/GetPDFPageCount` 接口，获取指定 PDF 的总页数。
- 支持错误处理，接口健壮。

## 依赖安装

建议使用 Python 3.7 及以上版本。

```bash
pip install -r requirements.txt
```

## 启动服务

```bash
python app.py
```

默认监听 5000 端口。

## API 文档

### 1. PDF 转图片接口
- **接口地址**：`/PDFViewer`
- **请求方式**：GET
- **参数**：
  - `Url`（必填）：PDF 文件的网络地址
- **返回**：PDF 第一页的 PNG 图片（Content-Type: image/png）
- **图片宽度**：最大1920像素，超出则等比缩放，高度自适应
- **错误返回**：返回 JSON 格式错误信息

#### 示例
```
http://localhost:5000/PDFViewer?Url=https://upload-file-sjtu.edu-sjtu.cn/PDF/20250627/2025062714041161383290.pdf
```

### 2. 获取 PDF 页数接口
- **接口地址**：`/GetPDFPageCount`
- **请求方式**：GET
- **参数**：
  - `Url`（必填）：PDF 文件的网络地址
- **返回**：PDF 页数（纯数字，Content-Type: text/plain）。如有异常返回0。

#### 示例
```
http://localhost:5000/GetPDFPageCount?Url=https://upload-file-sjtu.edu-sjtu.cn/PDF/20250627/2025062714041161383290.pdf
```

## 注意事项
- 仅支持公网可访问的 PDF 文件 URL。
- 若 PDF 文件较大或页面复杂，处理时间和内存消耗会增加。
- `/PDFViewer` 仅返回第一页图片。
- `/GetPDFPageCount` 出现任何异常均返回0。

## 依赖列表
- flask
- requests
- PyMuPDF
- Pillow

---
如有问题欢迎反馈！ 