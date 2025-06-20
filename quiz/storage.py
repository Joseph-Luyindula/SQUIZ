from django.core.files.storage import FileSystemStorage

class NoLockFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        # Ignore file locks
        return super()._save(name, content)