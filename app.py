from flask import Flask, request, send_file, jsonify, Response
import requests
import fitz  # PyMuPDF
import io
from PIL import Image

app = Flask(__name__)

@app.route('/PDFViewer')
def pdf_to_png():
    pdf_url = request.args.get('Url')
    page_index = request.args.get('PageIndex', default='1')
    try:
        page_index = int(page_index)
    except Exception:
        return Response('无效的参数', mimetype='text/plain')
    if not pdf_url:
        return jsonify({'error': '缺少Url参数'}), 400
    try:
        # 下载PDF文件
        resp = requests.get(pdf_url, timeout=15)
        if resp.status_code != 200:
            return jsonify({'error': 'PDF下载失败', 'status_code': resp.status_code}), 400
        pdf_bytes = resp.content
    except Exception as e:
        return jsonify({'error': f'PDF下载异常: {str(e)}'}), 400

    try:
        # 用PyMuPDF打开PDF
        pdf_doc = fitz.open(stream=pdf_bytes, filetype='pdf')
        page_count = pdf_doc.page_count
        if page_count == 0 or page_index < 1 or page_index > page_count:
            return Response('无效的参数', mimetype='text/plain')
        zoom = 300 / 72  # 300DPI
        mat = fitz.Matrix(zoom, zoom)
        page = pdf_doc[page_index - 1]  # 页码从1开始
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img = Image.open(io.BytesIO(pix.tobytes('png')))
        # 限制宽度为1920像素，高度等比缩放
        max_width = 1920
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.LANCZOS)
        # 输出为PNG
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=False, download_name=f'page{page_index}.png')
    except Exception:
        return Response('无效的参数', mimetype='text/plain')

@app.route('/GetPDFPageCount')
def get_pdf_page_count():
    pdf_url = request.args.get('Url')
    if not pdf_url:
        return Response('0', mimetype='text/plain')
    try:
        resp = requests.get(pdf_url, timeout=15)
        if resp.status_code != 200:
            return Response('0', mimetype='text/plain')
        pdf_bytes = resp.content
        pdf_doc = fitz.open(stream=pdf_bytes, filetype='pdf')
        count = pdf_doc.page_count
        return Response(str(count), mimetype='text/plain')
    except Exception:
        return Response('0', mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 