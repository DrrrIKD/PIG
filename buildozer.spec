[app]
title = HeadphoneRecorderApp
package.name = headphone_recorder
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer,speechrecognition,requests,gtts,setuptools,cython
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.11.1
android.api = 30
android.minapi = 23
android.ndk = 23b
android.sdk = 30
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.add_jars = true
android.jvm_args = -Xmx1024M

[buildozer]
log_level = 1
warn_on_root = 1
