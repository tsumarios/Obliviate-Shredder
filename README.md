# 🔥🪄 **Obliviate Shredder** - Magic File Erasure 💀  

> **_"Not just deletion—total memory erasure."_**  

Obliviate Shredder is a **secure anti-forensics tool** that **obliterates** files and folders beyond recovery. Inspired by the **"Obliviate" spell** from Harry Potter, this tool ensures that no digital trace remains after shredding.

---

## 🚀 **Features**

| **Feature** | **Description** |
|------------|----------------|
| 🔥 **AES-256 Encryption** | Encrypts files before deletion to prevent data reconstruction. |
| 🔄 **Multi-Pass Overwriting** | Overwrites data multiple times using **random, cryptographic, or hash-based methods**. |
| 🛡 **Random Filename Renaming** | Renames files several times with **randomized names** before deleting them. |
| 🕵️ **Metadata & Timestamp Scrubbing** | Modifies file attributes to remove forensic traces. |
| ⚡ **Multithreading for Speed** | Uses **multiple CPU threads** to shred large folders quickly. |
| 🎨 **Colorful, Magic-Themed Logging** | Features **spell animations** and **color-coded logs** for an immersive experience. |
| 🛠 **Debug Mode** | Enables **detailed logging** to track the shredding process. |

---

## 🎩 **Installation**

### **📌 Prerequisites**

Ensure you have **Python 3.6+** installed.  
Install dependencies using `pip`:  

```sh
pip install pycryptodome
```

### 🔧 Manual Installation

1️⃣ Clone the repository:

```sh
git clone https://github.com/tsumarios/obliviate-shredder.git
cd obliviate-shredder
```

2️⃣ Install dependencies:

```sh
pip install -r requirements.txt
```

3️⃣ Run the shredder:

```sh
python3 obliviate_shredder.py --help
```

#### 🛠️ (Optional) Build a Standalone Executable with Nuitka

You can also compile the shredder into a single executable (no Python interpreter required).

Install nuitka:

```sh
pip install nuitka
```

Build the executable:

```sh
nuitka --standalone --no-deployment-flag=self-execution --onefile obliviate_shredder.py
```

This will generate a standalone binary in the current directory.
Move the binary to a desired location for convenient use, e.g., `/usr/local/bin/`:

```sh
mv obliviate_shredder.bin /usr/local/bin/obliviate_shredder
```

_You can now run it from anywhere in your terminal!_

## 🪄 Usage

### Basic File Shredding

```sh
obliviate_shredder /path/to/file
```

###  Shred an Entire Folder

```sh
obliviate_shredder /path/to/folder
```

### Options

#### Enable AES-256 Encryption Before Shredding

```sh
obliviate_shredder /path/to/file -e
```

#### Use a Different Overwrite Method

```sh
obliviate_shredder /path/to/file -m [random|crypto|hash]
```

#### Custom Overwrite Passes

```sh
obliviate_shredder /path/to/file -p 5
```

_(Runs 5 overwrite passes.)_

#### Enable Debug Mode

```sh
obliviate_shredder /path/to/file -d
```

#### Use Multithreading for Large Folders

```sh
obliviate_shredder /path/to/folder -t 8
```

_(Uses 8 threads for faster deletion.)_

### 🎨 Example Output

```sh
2025-03-06 15:45:10 | INFO  | 🔥🪄 Obliviate Shredder - Magic File Erasure🔥🪄
2025-03-06 15:45:10 | DEBUG | 🛠 Debug mode enabled! Verbose logging activated.
2025-03-06 15:45:11 | INFO  | 🪄 Obliviate! 💀💨 Erasing: /path/to/secret.txt ...
2025-03-06 15:45:12 | DEBUG | 🔐 File encrypted before deletion: /path/to/secret.txt
2025-03-06 15:45:12 | DEBUG | ✅ Overwritten /path/to/secret.txt using method: random
2025-03-06 15:45:13 | DEBUG | 🔄 File renamed multiple times to: /randomly/named/file123
2025-03-06 15:45:14 | INFO  | /randomly/named/file123 gone. 💀
2025-03-06 15:45:15 | INFO  | ✅ Obliviate shredding completed! 🪄 💀
```

### 🛑 ⚠️ WARNING: IRREVERSIBLE ACTIONS ⚠️

Once a file is shredded using Obliviate Shredder, it CANNOT be recovered—not even with forensic tools.
Use with extreme caution! 💀🔥

#### Contacts

- Email: <marioraciti@pm.me>
- LinkedIn: linkedin.com/in/marioraciti
- Twitter: twitter.com/tsumarios

_If you want to support me, I would be grateful ❤️_

<a href="https://www.buymeacoffee.com/tsumarios" target="_blank"><img
        src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="40"></a>

💀🔥 _Now go forth, and cast the ultimate Obliviate spell on your files!_ 🪄💨
