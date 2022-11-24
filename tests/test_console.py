from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")