[app]
title = استخدم عقلك بذكاء وحكمة
package.name = smart_mind_game
package.domain = org.roax
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.1

# المتطلبات (تم تصحيحها لتعمل مع GitHub Actions بدون تعارض)
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pillow, pyjnius, android, openssl

icon.filename = 1772036342043.png
orientation = portrait

# تصاريح الإنترنت والإعلانات (مضافة وجاهزة)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID

# إعدادات الأندرويد لعام 2026 (API 33)
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# --- الجزء الخاص بالإعلانات (AdMob) ---
# إضافة مكتبة الإعلانات
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.0.0
android.enable_androidx = True

# سطر حاسم: استبدل "ca-app-pub-XXXXXXXXXXXXXXXX~XXXXXXXXXX" بمعرف تطبيقك الحقيقي من AdMob
# إذا لم تضعه، سيتوقف التطبيق عن العمل بمجرد محاولة تحميل الإعلان
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-XXXXXXXXXXXXXXXX~XXXXXXXXXX

fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1


