# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hanuman",  # 项目名称
    version="0.1.0",  # 初始版本
    author="CZHanoi",  # 作者名称
    author_email="21301010003@m.fudan.edu.cn",  # 作者邮箱
    description="Typhoon Animation Generator",  # 简短描述
    long_description_content_type="text/markdown",
    url="https://github.com/CZHanoi/hanuman",  # 项目主页（如 GitHub 仓库）
    packages=find_packages(),  # 自动查找包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 根据 LICENSE 文件选择合适的许可证
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python 版本要求
    install_requires=[
        "numpy",
        "opencv-python",
        "tqdm",
        # 其他依赖项
    ],
    entry_points={
        'console_scripts': [
            'hanuman=hanuman.main:main',  # 创建命令行工具 'hanuman'，指向 hanuman/main.py 的 main 函数
        ],
    },
    include_package_data=True,  # 包含 MANIFEST.in 中指定的额外文件
)
