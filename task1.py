import argparse
import shutil
from pathlib import Path
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("src", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("dest", type=str, nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def sort_files_recursively(src_path: Path, dest_path: Path):
    """
    Рекурсивно обходить директорію, копіює файли та сортує їх у папки за розширеннями.
    """
    try:
        # Перебираємо всі елементи в поточній директорії
        for item in src_path.iterdir():
            if item.is_dir():
                # Якщо це директорія — викликаємо функцію рекурсивно
                sort_files_recursively(item, dest_path)
            elif item.is_file():
                # Якщо це файл — отримуємо його розширення
                # Якщо файл не має розширення, відносимо до папки 'unknown'
                extension = item.suffix[1:].lower() if item.suffix else 'unknown'
                
                # Створюємо шлях до цільової піддиректорії
                target_dir = dest_path / extension
                
                try:
                    # Створюємо піддиректорію, якщо її ще не існує
                    target_dir.mkdir(parents=True, exist_ok=True)
                    # Копіюємо файл
                    shutil.copy2(item, target_dir / item.name)
                    print(f"[+] Скопійовано: {item.name} -> {target_dir}")
                except PermissionError:
                    print(f"[!] Помилка доступу під час копіювання файлу: {item}")
                except Exception as e:
                    print(f"[!] Непередбачена помилка з файлом {item}: {e}")
                    
    except PermissionError:
        print(f"[!] Немає доступу до директорії: {src_path}")
    except FileNotFoundError:
        print(f"[!] Директорію не знайдено: {src_path}")
    except Exception as e:
        print(f"[!] Помилка доступу до {src_path}: {e}")

def main():
    args = parse_args()
    src_dir = Path(args.src)
    dest_dir = Path(args.dest)

    if not src_dir.exists() or not src_dir.is_dir():
        print(f"Помилка: Вихідна директорія '{src_dir}' не існує або не є папкою.")
        sys.exit(1)

    print(f"Початок сортування з '{src_dir}' до '{dest_dir}'...")
    sort_files_recursively(src_dir, dest_dir)
    print("Сортування завершено!")

if __name__ == "__main__":
    main()
