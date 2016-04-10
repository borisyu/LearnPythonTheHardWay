"""
    Flaskr Tests
    ~~~~~~~~~~~~

    Tests the Flaskr application.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import pytest
import os
import flaskr
import tempfile

@pytest.fixture
def client(request):
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()
    with flaskr.app.app_context():
        flaskr.init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(flaskr.app.config['DATABASE'])
    request.addfinalizer(teardown)

    return client

def test_empty_db(client):
    rv = client.get('/')
    assert b'No entries here so far' in rv.data