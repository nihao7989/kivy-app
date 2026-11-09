[app]

# 应用名称
title = 我的小工具

# 包名（必须是英文，格式：com.xxx.xxx）
package.name = mytool
package.domain = org.example

# 版本号
version = 1.0

# 源码目录
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# 要求的Python库
requirements = python3,kivy

# 安卓相关
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 24
android.arch = arm64-v8a
android.accept_sdk_license = True

# 图标（暂时不用，用默认）
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
