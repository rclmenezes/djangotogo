from storages.backends.s3boto import S3BotoStorage
from django.utils.functional import SimpleLazyObject
from boto.utils import parse_ts

class ModifiedS3BotoStorage(S3BotoStorage):
    def modified_time(self, name):
        name = self._normalize_name(self._clean_name(name))
        entry = self.entries.get(name)
        if entry is None:
            entry = self.bucket.get_key(self._encode_name(name))
        # Parse the last_modified string to a local datetime object.
        return parse_ts(entry.last_modified)

StaticRootS3BotoStorage = lambda: ModifiedS3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: ModifiedS3BotoStorage(location='media')