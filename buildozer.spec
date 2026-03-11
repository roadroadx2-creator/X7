[app]
title = استخدم عقلك بذكاء وحكمة
package.name = smart_mind_game
package.domain = org.roax
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.1

# المتطلبات الصحيحة
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pillow, pyjnius, android

# تم تعديل المسار ليكون أكثر أماناً
icon.filename = 1772036342043.png

orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:22.0.0'
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

