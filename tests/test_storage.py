import pytest
import tempfile
from pgbackup import storage

@pytest.fixture
def infile():
    f= tempfile.TemporaryFile()
    f.write(b'Testing')
    f.seek(0)
    return f

def test_storing_file_locally(infile):
# Write content from one file-like another
    outfile=tempfile.NamedTemporaryFile(delete=False)
    storage.local(infile, outfile)
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing'

def test_storing_file_on_s3(mocker, infile):
# Writes content
    client = mocker.Mock()
    storage.s3(client, infile, "bucket", "file_name")
    client.upload_fileobj.assert_called_with(infile, "bucket", "file_name")
