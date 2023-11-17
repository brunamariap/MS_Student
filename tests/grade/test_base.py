import pytest
from main import prisma


class TestBase:
    
    @pytest.fixture
    def setUp(self):
        prisma.connect()
        yield
        prisma.execute_raw('DELETE FROM public."Grade"')
        prisma.disconnect()
