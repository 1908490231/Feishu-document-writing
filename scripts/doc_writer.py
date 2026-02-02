# -*- coding: utf-8 -*-
"""
飞书文档写入模块
"""

from typing import Dict, List, Tuple, Optional

import requests

from .auth import FeishuAuth


class FeishuDocWriter:
    """飞书文档写入模块"""

    BASE_URL = "https://open.feishu.cn/open-apis"

    def __init__(self, auth: FeishuAuth):
        self.auth = auth

    def _headers(self) -> Dict:
        return {
            "Authorization": f"Bearer {self.auth.get_token()}",
            "Content-Type": "application/json"
        }

    def create_document(self, title: str, folder_token: Optional[str] = None) -> Tuple[str, str]:
        """
        创建文档

        Returns:
            (document_id, document_block_id)
        """
        url = f"{self.BASE_URL}/docx/v1/documents"
        data = {"title": title}
        if folder_token:
            data["folder_token"] = folder_token

        resp = requests.post(url, headers=self._headers(), json=data)
        resp.raise_for_status()
        result = resp.json()

        if result.get("code") != 0:
            raise Exception(f"创建文档失败: {result.get('msg')}")

        doc = result.get("data", {}).get("document", {})
        return doc.get("document_id"), doc.get("document_id")  # document_id 同时是根 block_id

    def get_document_block_id(self, document_id: str) -> str:
        """获取文档的根 block_id"""
        url = f"{self.BASE_URL}/docx/v1/documents/{document_id}"
        resp = requests.get(url, headers=self._headers())
        resp.raise_for_status()
        result = resp.json()

        if result.get("code") != 0:
            raise Exception(f"获取文档信息失败: {result.get('msg')}")

        return result.get("data", {}).get("document", {}).get("document_id")

    def append_blocks(self, document_id: str, block_id: str, blocks: List[Dict]) -> bool:
        """向文档追加内容块"""
        if not blocks:
            return True

        url = f"{self.BASE_URL}/docx/v1/documents/{document_id}/blocks/{block_id}/children"

        # 飞书 API 限制每次最多 50 个 block
        batch_size = 50
        for i in range(0, len(blocks), batch_size):
            batch = blocks[i:i + batch_size]
            data = {"children": batch}

            resp = requests.post(url, headers=self._headers(), json=data)
            resp.raise_for_status()
            result = resp.json()

            if result.get("code") != 0:
                print(f"警告: 写入部分内容失败: {result.get('msg')}")
                return False

        return True

    def list_documents_in_folder(self, folder_token: str) -> List[Dict]:
        """列出文件夹中的文档"""
        url = f"{self.BASE_URL}/drive/v1/files"
        params = {
            "folder_token": folder_token,
            "page_size": 200
        }

        resp = requests.get(url, headers=self._headers(), params=params)
        resp.raise_for_status()
        result = resp.json()

        if result.get("code") != 0:
            return []

        return result.get("data", {}).get("files", [])

    def delete_document_content(self, document_id: str) -> bool:
        """清空文档内容（用于更新）"""
        # 获取文档所有 block
        url = f"{self.BASE_URL}/docx/v1/documents/{document_id}/blocks"
        resp = requests.get(url, headers=self._headers())
        resp.raise_for_status()
        result = resp.json()

        if result.get("code") != 0:
            return False

        blocks = result.get("data", {}).get("items", [])

        # 删除所有子 block（跳过根 block）
        for block in blocks:
            block_id = block.get("block_id")
            if block_id and block_id != document_id:
                delete_url = f"{self.BASE_URL}/docx/v1/documents/{document_id}/blocks/{block_id}"
                requests.delete(delete_url, headers=self._headers())

        return True

    def move_to_wiki(self, document_id: str, space_id: str, parent_node_token: Optional[str] = None) -> bool:
        """将文档移动到知识库（已废弃，建议使用 create_wiki_document）

        Args:
            document_id: 文档 ID
            space_id: 知识库 space_id（数字）
            parent_node_token: 父节点 token（可选，用于放到指定节点下）
        """
        url = f"{self.BASE_URL}/wiki/v2/spaces/{space_id}/nodes"
        data = {
            "obj_type": "docx",
            "obj_token": document_id,
            "node_type": "origin"
        }
        if parent_node_token:
            data["parent_node_token"] = parent_node_token

        resp = requests.post(url, headers=self._headers(), json=data)
        resp.raise_for_status()
        result = resp.json()

        return result.get("code") == 0

    def create_wiki_document(self, title: str, space_id: str, parent_node_token: Optional[str] = None) -> Tuple[str, str]:
        """直接在知识库中创建文档

        Args:
            title: 文档标题
            space_id: 知识库 space_id
            parent_node_token: 父节点 token（可选）

        Returns:
            (obj_token, node_token) - obj_token 用于写入内容，node_token 用于访问链接
        """
        url = f"{self.BASE_URL}/wiki/v2/spaces/{space_id}/nodes"
        data = {
            "obj_type": "docx",
            "node_type": "origin",
            "title": title
        }
        if parent_node_token:
            data["parent_node_token"] = parent_node_token

        resp = requests.post(url, headers=self._headers(), json=data)
        resp.raise_for_status()
        result = resp.json()

        if result.get("code") != 0:
            raise Exception(f"创建知识库文档失败: {result.get('msg')}")

        node = result.get("data", {}).get("node", {})
        obj_token = node.get("obj_token")
        node_token = node.get("node_token")

        return obj_token, node_token

    def get_wiki_space_id(self, node_token: str) -> Optional[str]:
        """通过节点 token 获取知识库 space_id"""
        url = f"{self.BASE_URL}/wiki/v2/spaces/get_node"
        params = {"token": node_token}

        resp = requests.get(url, headers=self._headers(), params=params)
        if resp.status_code != 200:
            return None

        result = resp.json()
        if result.get("code") != 0:
            return None

        return result.get("data", {}).get("node", {}).get("space_id")

    def create_image_block(self, document_id: str, block_id: str) -> Optional[str]:
        """
        创建空的图片块占位符

        Args:
            document_id: 文档 ID
            block_id: 父块 ID（通常是文档根 block_id）

        Returns:
            创建的图片块 block_id，失败返回 None
        """
        url = f"{self.BASE_URL}/docx/v1/documents/{document_id}/blocks/{block_id}/children"
        data = {
            "children": [
                {
                    "block_type": 27,
                    "image": {}
                }
            ]
        }

        try:
            resp = requests.post(url, headers=self._headers(), json=data)
            resp.raise_for_status()
            result = resp.json()

            if result.get("code") != 0:
                print(f"警告: 创建图片块失败: {result.get('msg')}")
                return None

            # 返回创建的图片块 block_id
            children = result.get("data", {}).get("children", [])
            if children:
                return children[0].get("block_id")
            return None
        except Exception as e:
            print(f"警告: 创建图片块异常: {e}")
            return None

    def replace_image_token(self, document_id: str, block_id: str, file_token: str) -> bool:
        """
        更新图片块的 token（使用 replace_image）

        Args:
            document_id: 文档 ID
            block_id: 图片块 ID
            file_token: 上传图片后获得的 file_token

        Returns:
            是否成功
        """
        url = f"{self.BASE_URL}/docx/v1/documents/{document_id}/blocks/{block_id}"
        data = {
            "replace_image": {
                "token": file_token
            }
        }

        try:
            resp = requests.patch(url, headers=self._headers(), json=data)
            resp.raise_for_status()
            result = resp.json()

            if result.get("code") != 0:
                print(f"警告: 更新图片块失败: {result.get('msg')}")
                return False

            return True
        except Exception as e:
            print(f"警告: 更新图片块异常: {e}")
            return False
