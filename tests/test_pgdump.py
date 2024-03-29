import pytest
import subprocess

from pgbackup import pgdump
url="postgres://bob:password@example.com:5432/db_one"

def test_dump_calls_pg_dump(mocker):
#   Utilize pg_dump with the database URL

    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):

#   pgdump.dump returns a reasonable error if pg_dump isn't installed.
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

def test_dump_file_name_withouth_timestamp():
#pgdump.dump_file_name returns the name of the database
    timestamp="2019-07-31T:09:57:30"
    assert pgdump.dump_file_name(url,timestamp)==f"db_one-{timestamp}.sql"
