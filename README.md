# PDFViewer

本项目是一个基于 Flask 和 PyMuPDF 的 PDF 在线转换服务。它可以从指定的 PDF URL 下载 PDF 文件，将所有页面以 300 DPI 转为 PNG 图片，并纵向拼接为一张大图，供前端显示或下载。

## 功能简介
- 提供 `/PDF?Url=<pdf_url>` API 接口
- 下载指定 URL 的 PDF 文件
- 使用 PyMuPDF 将所有页面渲染为 PNG（300 DPI）
- 按页面顺序纵向拼接为一张图片
- 返回拼接后的 PNG 图片
- 错误处理完善，返回 JSON 格式错误信息

## 安装依赖

建议使用 Python 3.7 及以上版本。

```bash
pip install -r requirements.txt
```

## 启动服务

```bash
python app.py
```

默认监听 5000 端口。

## API 用法

- 请求方式：GET
- 接口地址：`/PDF?Url=<pdf_url>`
- 参数说明：
  - `Url`：PDF 文件的网络地址（必填）

### 示例

```
http://localhost:5000/PDF?Url=https://example.com/sample.pdf
```

- 成功时返回：拼接后的 PNG 图片，MIME 类型为 `image/png`
- 失败时返回：JSON 格式的错误信息和对应的 HTTP 状态码

## 依赖说明
- flask
- requests
- PyMuPDF
- Pillow

## 注意事项
- 仅支持公开可访问的 PDF 文件 URL。
- 若 PDF 文件较大或页面较多，处理时间和内存消耗会增加。

---
如有问题欢迎反馈！ 