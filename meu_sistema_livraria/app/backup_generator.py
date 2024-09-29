from pathlib import Path
from datetime import datetime
import zipfile

# Função para criar um backup do banco de dados
def create_backup():
    base_dir = Path(__file__).resolve().parent.parent.parent

    db_path = base_dir / "meu_sistema_livraria" / "data" / "livros.db"
    backup_dir = base_dir / "meu_sistema_livraria" / "backups"
    
    if not backup_dir.exists():
        backup_dir.mkdir(parents=True, exist_ok=True)
    
    date_str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    backup_filename = f"backup_livraria_{date_str}.db"
    backup_path = backup_dir / backup_filename
    
    with open(db_path, "rb") as db_file:
        with open(backup_path, "wb") as backup_file:
            backup_file.write(db_file.read())
    
    manage_backups(backup_dir)

# Função para gerenciar os backups
def manage_backups(backup_dir):
    backups = sorted(backup_dir.glob("backup_livraria_*.db"), key=lambda p: p.stat().st_mtime, reverse=True)

    #adicional, o professor nao pediu mas eu fiz um essa parte para zipar os backups antigos ao invez de descartar
    #assim o usuario pode manter os backups antigos e nao ocupar muito
    if len(backups) > 5:
        with zipfile.ZipFile(backup_dir / "old_backups.zip", "a") as zipf:
            for old_backup in backups[5:]:
                zipf.write(old_backup, old_backup.name)
                old_backup.unlink()

create_backup()