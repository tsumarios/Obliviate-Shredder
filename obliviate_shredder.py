#!/usr/bin/env python3
"""
🔥🪄 Obliviate Shredder - Magic File Erasure 🔥🪄
A secure file shredder that overwrites, encrypts, and renames files before deletion.
Inspired by the "Obliviate" spell from Harry Potter, it makes files unrecoverable.
It can shred individual files or entire folders using multithreading.
It supports different overwrite methods (random, crypto, hash) and AES-256 encryption.
It also destroys file metadata, timestamps, and extended attributes to cover tracks.
Author: tsumarios
"""

import os
import shutil
import argparse
import random
import string
import time
import hashlib
import logging
import threading
from queue import Queue
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# 🪄 Setup Logging 🪄
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


# 🪄 MAGIC SPELL ANIMATION 🪄
def spell_animation(file_path):
    """
    Displays a magical spell-casting effect for file shredding.

    Args:
        file_path (str): The file being erased.
    """
    spell_text = f"🪄 Obliviate! 💀💨 Erasing: {file_path} ..."
    logging.info(f"\033[1;35m{spell_text}\033[0m")


def disappearing_effect(file_path):
    """
    Simulates a disappearing effect when the file is deleted.

    Args:
        file_path (str): The path of the file being deleted.
    """
    logging.info(f"\033[1;31m{file_path} gone. 💀\033[0m\n")


# 🔥 SECURE FILE OVERWRITE 🔥
def overwrite_file(file_path, method="random", passes=3):
    """
    Overwrites a file securely to prevent data recovery.

    Args:
        file_path (str): The path of the file to overwrite.
        method (str): Overwriting method ('random', 'crypto', 'hash').
        passes (int): Number of overwrite passes.
    """
    if not os.path.isfile(file_path):
        return

    size = os.path.getsize(file_path)
    with open(file_path, "wb") as f:
        for _ in range(passes):
            f.seek(0)
            if method == "random":
                f.write(os.urandom(size))
            elif method == "crypto":
                f.write(get_random_bytes(size))
            elif method == "hash":
                hasher = hashlib.sha512()
                for _ in range(size // 64):
                    chunk = os.urandom(64)
                    hasher.update(chunk)
                    f.write(hasher.digest())
    logging.debug(f"✅ Overwritten {file_path} using method: {method}")


# 🔥 AES-256 FILE ENCRYPTION BEFORE DELETION 🔥
def encrypt_file(file_path):
    """
    Encrypts a file with AES-256 before shredding it.

    Args:
        file_path (str): The path of the file to encrypt.
    """
    if not os.path.isfile(file_path):
        return

    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, "rb") as f:
        plaintext = f.read()

    pad_length = 16 - (len(plaintext) % 16)
    plaintext += bytes([pad_length]) * pad_length

    with open(file_path, "wb") as f:
        f.write(iv + cipher.encrypt(plaintext))
    logging.debug(f"🔐 File encrypted before deletion: {file_path}")


# 🔥 RANDOM FILE RENAMING 🔥
def rename_file_randomly(file_path, times=3):
    """
    Renames a file multiple times to prevent forensic tracking.

    Args:
        file_path (str): The path of the file to rename.
        times (int): Number of renaming iterations.

    Returns:
        str: Final renamed file path.
    """
    directory, _ = os.path.split(file_path)
    for _ in range(times):
        random_length = random.randint(8, 32)
        random_name = "".join(
            random.choices(string.ascii_letters + string.digits, k=random_length)
        )
        new_path = os.path.join(directory, random_name)
        os.rename(file_path, new_path)
        file_path = new_path
    logging.debug(f"🔄 File renamed multiple times to: {file_path}")
    return file_path


# 🔥 METADATA DESTRUCTION 🔥
def destroy_metadata(file_path):
    """
    Scrambles file metadata, timestamps, and removes extended attributes.

    Args:
        file_path (str): The path of the file whose metadata will be destroyed.
    """
    if not os.path.exists(file_path):
        return

    random_time = random.randint(0, int(time.time()))
    os.utime(file_path, (random_time, random_time))

    if os.name == "nt":
        import ctypes

        FILE_ATTRIBUTE_HIDDEN = 0x02
        ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN)
    else:
        os.chmod(file_path, 0o777)
        try:
            import xattr

            attrs = xattr.listxattr(file_path)
            for attr in attrs:
                xattr.removexattr(file_path, attr)
        except ImportError:
            pass
    logging.debug(f"🛑 Metadata destroyed for: {file_path}")


# 🔥 SECURE FILE SHREDDING 🔥
def shred_file(file_path, passes=3, method="random", encrypt=False):
    """
    Securely shreds a file by encrypting, overwriting, renaming, and deleting it.

    Args:
        file_path (str): The file to be shredded.
        passes (int): Number of overwrite passes.
        method (str): Overwriting method ('random', 'crypto', 'hash').
        encrypt (bool): Whether to encrypt the file before shredding.
    """
    if not os.path.isfile(file_path):
        logging.error(f"❌ File not found: {file_path}")
        return

    try:
        if encrypt:
            encrypt_file(file_path)

        spell_animation(file_path)
        overwrite_file(file_path, method, passes)
        destroy_metadata(file_path)
        file_path = rename_file_randomly(file_path)
        os.remove(file_path)
        disappearing_effect(file_path)
    except Exception as e:
        logging.error(f"❌ Failed to shred file {file_path}: {e}")


# 🔥 MULTITHREADED FOLDER SHREDDING 🔥
def worker(queue, passes, method, encrypt):
    """
    Worker thread for parallel file shredding.

    Args:
        queue (Queue): Queue containing file paths to shred.
        passes (int): Number of overwrite passes.
        method (str): Overwriting method.
        encrypt (bool): Whether to encrypt files before deletion.
    """
    while True:
        file_path = queue.get()
        if file_path is None:
            break
        shred_file(file_path, passes, method, encrypt)
        queue.task_done()


def shred_folder(folder_path, passes=3, method="random", encrypt=False, threads=4):
    """
    Shreds all files in a folder using multithreading.

    Args:
        folder_path (str): The folder to be shredded.
        passes (int): Number of overwrite passes.
        method (str): Overwriting method.
        encrypt (bool): Whether to encrypt files before deletion.
        threads (int): Number of worker threads.
    """
    if not os.path.isdir(folder_path):
        logging.error(f"❌ Path not found: {folder_path}")
        return

    queue = Queue()
    workers = []

    for _ in range(threads):
        thread = threading.Thread(target=worker, args=(queue, passes, method, encrypt))
        thread.start()
        workers.append(thread)

    for root, _, files in os.walk(folder_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            queue.put(file_path)

    queue.join()

    for _ in workers:
        queue.put(None)
    for thread in workers:
        thread.join()

    shutil.rmtree(folder_path)
    logging.info(f"\033[1;31mFolder shredded: {folder_path} 🔥\033[0m\n")


# 🔥 Master Shred Function 🔥
def shred(path, passes=3, method="random", encrypt=False, threads=4):
    """Shred a file or folder securely."""
    if os.path.isfile(path):
        shred_file(path, passes, method, encrypt)
    elif os.path.isdir(path):
        shred_folder(path, passes, method, encrypt, threads)
    else:
        logging.error(f"❌ Error path not found: {path}")
        return


# 🔥 CLI SUPPORT 🔥
def main():
    """Command-line interface for the Obliviate Shredder."""
    parser = argparse.ArgumentParser(
        description="🔥 🪄 Obliviate Shredder - Magic File Erasure 🔥"
    )
    parser.add_argument("path", help="File or folder to shred")
    parser.add_argument("-p", "--passes", type=int, default=3)
    parser.add_argument(
        "-m", "--method", choices=["random", "crypto", "hash"], default="random"
    )
    parser.add_argument("-e", "--encrypt", action="store_true")
    parser.add_argument("-t", "--threads", type=int, default=4)
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Enable debug mode for detailed logging",
    )
    # Parse command-line arguments
    args = parser.parse_args()

    logging.info("\033[1;36m🔥🪄 Obliviate Shredder - Magic File Erasure🔥🪄\033[0m")

    if args.debug:  # Enable debug mode
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug(
            "\033[1;34m🛠 Debug mode enabled! Verbose logging activated.\033[0m"
        )

    shred(args.path, args.passes, args.method, args.encrypt, args.threads)

    logging.info(f"\033[1;32m✅ Obliviate shredding completed! 🪄 💀\033[0m")


if __name__ == "__main__":
    main()
