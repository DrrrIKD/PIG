[app]
title = HeadphoneRecorderApp
package.name = headphone_recorder
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer,speechrecognition,requests,gtts
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.11.1
android.api = 30
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.permissions = RECORD_AUDIO,INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
