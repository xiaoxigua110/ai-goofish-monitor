#!/usr/bin/env python3
"""
Helper script to check if all required files exist for running the scraper
"""
import os

def check_required_files():
    """Check if all required files exist"""
    required_files = [
        "xianyu_state.json",
        "config.json"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ 缺少以下必需文件:")
        for file in missing_files:
            print(f"  - {file}")
        
        print("\n💡 解决方案:")
        if "xianyu_state.json" in missing_files:
            print("  1. 运行 'python login.py' 生成登录状态文件")
            print("  2. 或通过Web UI的系统设置页面手动更新登录状态")
        if "config.json" in missing_files:
            print("  3. 复制 'config.json.example' 到 'config.json'")
            print("     Windows: copy config.json.example config.json")
            print("     Mac/Linux: cp config.json.example config.json")
    else:
        print("✅ 所有必需文件都已存在")
        print("   - xianyu_state.json: 登录状态文件")
        print("   - config.json: 任务配置文件")

if __name__ == "__main__":
    check_required_files()