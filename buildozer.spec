[app]
# Основная информация о приложении
title = HeadphoneRecorderApp
package.name = headphone_recorder
package.domain = org.example
version = 0.1

# Директория с исходным кодом и используемые типы файлов
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Платформенные зависимости
requirements = python3,kivy,plyer,speechrecognition,requests,gtts,setuptools,cython

# Ориентация экрана
orientation = portrait

# Настройки для macOS (опционально)
osx.python_version = 3
osx.kivy_version = 1.11.1

# Настройки для Android
android.api = 33  # Рекомендуется использовать последнюю доступную версию API
android.minapi = 23  # Минимальный уровень API, поддерживаемый приложением
android.ndk = 23b
android.sdk = 30
# Путь к установленному Android NDK
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25c

# (опционально) Укажите путь к SDK, если нужно
android.sdk_path = ~/.buildozer/android/platform/android-sdk

android.archs = arm64-v8a, armeabi-v7a  # Архитектуры, поддерживаемые вашим приложением
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.add_jars = false  # Укажите false, если не используется дополнительный JAR
android.jvm_args = -Xmx1024M  # Java Virtual Machine параметры

# Дополнительно для разрешений и устройств
# Использование всех разрешений для записи, чтения и работы с сетью
android.allow_backup = 1
android.provide_extra_permissions = 1

# Настройки для упаковки AAB (если вы планируете публиковать в Google Play)
android.build_type = apk  # По умолчанию APK. Для Google Play укажите 'aab'

# Дополнительные библиотеки и плагины для Android
android.extra_packages = androidx.appcompat, androidx.multidex  # Поддержка Modern Android API

[buildozer]
# Параметры для отладки и логов
log_level = 2  # Повышенный уровень логов
warn_on_root = 1  # Предупреждение при запуске от root
