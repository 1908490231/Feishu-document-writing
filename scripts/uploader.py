# -*- coding: utf-8 -*-
"""
飞书图片上传模块
"""

import mimetypes
from pathlib import Path
from typing import Optional

import requests

from .auth import FeishuAuth


class FeishuImageUploader:
    """飞书图片上传模块"""

    UPLOAD_URL = "https://open.feishu.cn/open-apis/drive/v1/medias/upload_all"

    def __init__(self, auth: FeishuAuth):
        self.auth = auth

    def upload(self, image_path: str, parent_node: str) -> Optional[str]:
        """
        上传图片到飞书

        Args:
            image_path: 本地图片路径
            parent_node: 图片块的 block_id（必需）

        Returns:
            file_token 或 None（失败时）
        """
        if not parent_node:
            print(f"警告: 缺少 parent_node 参数")
            return None

        path = Path(image_path)
        if not path.exists():
            print(f"警告: 图片不存在 - {image_path}")
            return None

        # 获取 MIME 类型
        mime_type, _ = mimetypes.guess_type(str(path))
        if not mime_type:
            mime_type = "application/octet-stream"

        headers = {
            "Authorization": f"Bearer {self.auth.get_token()}"
        }

        with open(path, "rb") as f:
            files = {
                "file": (path.name, f, mime_type)
            }
            data = {
                "file_name": path.name,
                "parent_type": "docx_image",
                "parent_node": parent_node,
                "size": str(path.stat().st_size)
            }

            try:
                resp = requests.post(self.UPLOAD_URL, headers=headers, files=files, data=data)
                resp.raise_for_status()
                result = resp.json()

                if result.get("code") != 0:
                    print(f"警告: 图片上传失败 - {image_path}: {result.get('msg')}")
                    return None

                return result.get("data", {}).get("file_token")
            except Exception as e:
                print(f"警告: 图片上传异常 - {image_path}: {e}")
                return None
