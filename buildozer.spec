[app]
title = استخدم عقلك بذكاء وحكمة
package.name = smart_mind_game
package.domain = org.roax
source.dir = .
# إضافة امتداد png لضمان قراءة الصورة
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.1
requirements = python3,kivy==2.1.0,kivmd,kivmob,pillow,pyjnius,android,hostpython3

# --- تعديل الأيقونة بناءً على صورتك ---
icon.filename = %(source.dir)s/1772036342043.png

orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:22.0.0'
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
