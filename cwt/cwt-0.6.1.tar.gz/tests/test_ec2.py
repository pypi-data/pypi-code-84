"""
Tests for EC2Key.
"""
import pytest

from cwt.exceptions import VerifyError
from cwt.key_types.ec2 import EC2Key


class TestEC2Key:
    """
    Tests for EC2Key.
    """

    def test_ec2_key_constructor_with_es256_key(self):
        private_key = EC2Key(
            {
                1: 2,
                3: 1,
                -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                -4: b'\xe9\x16\x0c\xa96\x8d\xfa\xbc\xd5\xda"ua\xec\xf7\x96\r\x15\xf7_\xf3rb{\xb1\xde;\x99\x88\xafNh',
                -1: 1,
            }
        )
        public_key = EC2Key(
            {
                1: 2,
                3: 1,
                -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                -1: 1,
            }
        )
        assert private_key.kty == 2
        assert private_key.kid is None
        assert private_key.alg == 1
        assert private_key.crv == 1
        assert len(private_key.key_ops) == 2
        assert 1 in private_key.key_ops
        assert 2 in private_key.key_ops
        assert private_key.base_iv is None
        assert public_key.kty == 2
        assert public_key.kid is None
        assert public_key.alg == 1
        assert public_key.crv == 1
        assert len(public_key.key_ops) == 1
        assert 2 in public_key.key_ops
        assert public_key.base_iv is None
        try:
            sig = private_key.sign(b"Hello world!")
            public_key.verify(b"Hello world!", sig)
        except Exception:
            pytest.fail("sign/verify should not fail.")

    def test_ec2_key_constructor_with_es384_key(self):
        private_key = EC2Key(
            {
                1: 2,
                3: 2,
                -2: b"\xec\xe6\xd0\xc1-\xd4>%\xb6\x0f\x9d\xbf\xe2\x89qB\xd7\x8f\xba\xa4\xe0\x97\xd0\x91\xcd\xbb\x90\x92,\xaa\xd4\x10D\xc35\xfe\x89\xbfs\xae,&\x8d\xef\xfa\xb0\xc0Q",
                -3: b'\xc9F\xd4\xc8\x97\xd9G\xb80Z\x96E:\x89U/\x89|c\xb2\x9d\x1e\x0ep\xf1\xc4\xedl\x99K9.\x882\x06"\xb2\xa5\xdd\x17HW\x1f-r>Fg',
                -4: b"Q/x\xf6;9\xb7\xfb\x8d\xc3l\xc1\x1dx6Z4\xfa\x99=8Nj\x05g\xde\xb45\x00'VY\xab,\x92\x82{\x08\xd6\xe5\xff\xe3\xc4\xee\xacu>\x96",
                -1: 2,
            }
        )
        public_key = EC2Key(
            {
                1: 2,
                3: 2,
                -2: b"\xec\xe6\xd0\xc1-\xd4>%\xb6\x0f\x9d\xbf\xe2\x89qB\xd7\x8f\xba\xa4\xe0\x97\xd0\x91\xcd\xbb\x90\x92,\xaa\xd4\x10D\xc35\xfe\x89\xbfs\xae,&\x8d\xef\xfa\xb0\xc0Q",
                -3: b'\xc9F\xd4\xc8\x97\xd9G\xb80Z\x96E:\x89U/\x89|c\xb2\x9d\x1e\x0ep\xf1\xc4\xedl\x99K9.\x882\x06"\xb2\xa5\xdd\x17HW\x1f-r>Fg',
                -1: 2,
            }
        )
        assert private_key.kty == 2
        assert private_key.kid is None
        assert private_key.alg == 2
        assert private_key.crv == 2
        assert len(private_key.key_ops) == 2
        assert 1 in private_key.key_ops
        assert 2 in private_key.key_ops
        assert private_key.base_iv is None
        assert public_key.kty == 2
        assert public_key.kid is None
        assert public_key.alg == 2
        assert public_key.crv == 2
        assert len(public_key.key_ops) == 1
        assert 2 in public_key.key_ops
        assert public_key.base_iv is None
        try:
            sig = private_key.sign(b"Hello world!")
            public_key.verify(b"Hello world!", sig)
        except Exception:
            pytest.fail("sign/verify should not fail.")

    def test_ec2_key_constructor_with_es512_key(self):
        private_key = EC2Key(
            {
                1: 2,
                3: 3,
                -2: b"\x01iP\xcb*\xb4\x04\xa2\xf9d\x0f0{\n\x07>}|KZ\x81\xbd8\xb3N\x90\xb0\x10\xebk\xd2TBxR\xf6lNE\x92S\x80\xd0k|\xd9l\x044\xd8f\xee\xa6KQ\xcf\xa0\x01?g\x87\xcc\xb4\xd1\xce\x95",
                -3: b"\x00\r\xa0;\xcb\xae\x1f\x8e\xad\xc2\x82\xc8\x8e%\x94,\xd9\xe2t\xebG]\xc0\xb3I\xeec\xdf\xc5\x02\xd6c\xd9\xb4\xcd\xb8h\xc7l7\x07u`\xc3\x91\rl)\xb2\x07\x00\x10\xa07\xcd\x02N#\xac=L\x91~\xa2\xb26",
                -4: b'\x00V\xe5\x80\x13u\xc1\xb0\x8e\xf0\x98K\x0f\xc5\x14\xc55T\xb9\xbf\xd5o\xdc\xfa\x01\xf6\x91\xee\x85\x7fa,\x821\xdf\xdc\x17^\xd9G\x973V\xe9\xdd"s\xf4\x12\xd9:$\xbe\xc3\xad\xf7\x80"\x187\xc1\xa1\x9a\x1e@\xd2',
                -1: 3,
            }
        )
        public_key = EC2Key(
            {
                1: 2,
                3: 3,
                -2: b"\x01iP\xcb*\xb4\x04\xa2\xf9d\x0f0{\n\x07>}|KZ\x81\xbd8\xb3N\x90\xb0\x10\xebk\xd2TBxR\xf6lNE\x92S\x80\xd0k|\xd9l\x044\xd8f\xee\xa6KQ\xcf\xa0\x01?g\x87\xcc\xb4\xd1\xce\x95",
                -3: b"\x00\r\xa0;\xcb\xae\x1f\x8e\xad\xc2\x82\xc8\x8e%\x94,\xd9\xe2t\xebG]\xc0\xb3I\xeec\xdf\xc5\x02\xd6c\xd9\xb4\xcd\xb8h\xc7l7\x07u`\xc3\x91\rl)\xb2\x07\x00\x10\xa07\xcd\x02N#\xac=L\x91~\xa2\xb26",
                -1: 3,
            }
        )
        assert private_key.kty == 2
        assert private_key.kid is None
        assert private_key.alg == 3
        assert private_key.crv == 3
        assert len(private_key.key_ops) == 2
        assert 1 in private_key.key_ops
        assert 2 in private_key.key_ops
        assert private_key.base_iv is None
        assert public_key.kty == 2
        assert public_key.kid is None
        assert public_key.alg == 3
        assert public_key.crv == 3
        assert len(public_key.key_ops) == 1
        assert 2 in public_key.key_ops
        assert public_key.base_iv is None
        try:
            sig = private_key.sign(b"Hello world!")
            public_key.verify(b"Hello world!", sig)
        except Exception:
            pytest.fail("sign/verify should not fail.")

    def test_ec2_(self):
        private_key = EC2Key(
            {
                1: 2,
                3: 3,
                -2: b"\x01iP\xcb*\xb4\x04\xa2\xf9d\x0f0{\n\x07>}|KZ\x81\xbd8\xb3N\x90\xb0\x10\xebk\xd2TBxR\xf6lNE\x92S\x80\xd0k|\xd9l\x044\xd8f\xee\xa6KQ\xcf\xa0\x01?g\x87\xcc\xb4\xd1\xce\x95",
                -3: b"\x00\r\xa0;\xcb\xae\x1f\x8e\xad\xc2\x82\xc8\x8e%\x94,\xd9\xe2t\xebG]\xc0\xb3I\xeec\xdf\xc5\x02\xd6c\xd9\xb4\xcd\xb8h\xc7l7\x07u`\xc3\x91\rl)\xb2\x07\x00\x10\xa07\xcd\x02N#\xac=L\x91~\xa2\xb26",
                -4: b'\x00V\xe5\x80\x13u\xc1\xb0\x8e\xf0\x98K\x0f\xc5\x14\xc55T\xb9\xbf\xd5o\xdc\xfa\x01\xf6\x91\xee\x85\x7fa,\x821\xdf\xdc\x17^\xd9G\x973V\xe9\xdd"s\xf4\x12\xd9:$\xbe\xc3\xad\xf7\x80"\x187\xc1\xa1\x9a\x1e@\xd2',
                -1: 3,
            }
        )
        public_key = EC2Key(
            {
                1: 2,
                3: 3,
                -2: b"\x01iP\xcb*\xb4\x04\xa2\xf9d\x0f0{\n\x07>}|KZ\x81\xbd8\xb3N\x90\xb0\x10\xebk\xd2TBxR\xf6lNE\x92S\x80\xd0k|\xd9l\x044\xd8f\xee\xa6KQ\xcf\xa0\x01?g\x87\xcc\xb4\xd1\xce\x95",
                -3: b"\x00\r\xa0;\xcb\xae\x1f\x8e\xad\xc2\x82\xc8\x8e%\x94,\xd9\xe2t\xebG]\xc0\xb3I\xeec\xdf\xc5\x02\xd6c\xd9\xb4\xcd\xb8h\xc7l7\x07u`\xc3\x91\rl)\xb2\x07\x00\x10\xa07\xcd\x02N#\xac=L\x91~\xa2\xb26",
                -1: 3,
            }
        )
        assert private_key.kty == 2
        assert private_key.kid is None
        assert private_key.alg == 3
        assert len(private_key.key_ops) == 2
        assert 1 in private_key.key_ops
        assert 2 in private_key.key_ops
        assert private_key.base_iv is None
        assert public_key.kty == 2
        assert public_key.kid is None
        assert public_key.alg == 3
        assert len(public_key.key_ops) == 1
        assert 2 in public_key.key_ops
        assert public_key.base_iv is None
        try:
            sig = private_key.sign(b"Hello world!")
            public_key.verify(b"Hello world!", sig)
        except Exception:
            pytest.fail("sign/verify should not fail.")

    def test_cose_key_constructor_without_cose_key(self):
        with pytest.raises(TypeError):
            EC2Key()
            pytest.fail("EC2Key should fail.")

    @pytest.mark.parametrize(
        "invalid, msg",
        [
            (
                {},
                "kty(1) not found.",
            ),
            (
                {1: 1},
                "kty(1) should be EC2(2).",
            ),
            (
                {1: b"invalid"},
                "kty(1) should be int or str(tstr).",
            ),
            (
                {1: {}},
                "kty(1) should be int or str(tstr).",
            ),
            (
                {1: []},
                "kty(1) should be int or str(tstr).",
            ),
            (
                {1: 2},
                "x(-2) not found.",
            ),
            (
                {1: 2, -2: "xxxxxxxxxxxxxxxx"},
                "x(-2) should be bytes(bstr).",
            ),
            (
                {1: 2, -2: {}},
                "x(-2) should be bytes(bstr).",
            ),
            (
                {1: 2, -2: []},
                "x(-2) should be bytes(bstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                },
                "y(-3) not found.",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: "yyyyyyyyyyyyyyyy",
                },
                "y(-3) should be bytes(bstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: {},
                },
                "y(-3) should be bytes(bstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: [],
                },
                "y(-3) should be bytes(bstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                },
                "crv(-1) not found.",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -1: 0,
                },
                "Unsupported or unknown crv: 0",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -1: {},
                },
                "crv(-1) should be int or str(tstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -1: [],
                },
                "crv(-1) should be int or str(tstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -1: b"P-256",
                },
                "crv(-1) should be int or str(tstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"invalid-length-x",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -1: 1,
                },
                "Coords should be 32 bytes for crv P-256",
            ),
            (
                {
                    1: 2,
                    3: 2,
                    -2: b"invalid-length-x",
                    -3: b'\xc9F\xd4\xc8\x97\xd9G\xb80Z\x96E:\x89U/\x89|c\xb2\x9d\x1e\x0ep\xf1\xc4\xedl\x99K9.\x882\x06"\xb2\xa5\xdd\x17HW\x1f-r>Fg',
                    -1: 2,
                },
                "Coords should be 48 bytes for crv P-384",
            ),
            (
                {
                    1: 2,
                    3: 3,
                    -2: b"invalid-length-x",
                    -3: b"\x00\r\xa0;\xcb\xae\x1f\x8e\xad\xc2\x82\xc8\x8e%\x94,\xd9\xe2t\xebG]\xc0\xb3I\xeec\xdf\xc5\x02\xd6c\xd9\xb4\xcd\xb8h\xc7l7\x07u`\xc3\x91\rl)\xb2\x07\x00\x10\xa07\xcd\x02N#\xac=L\x91~\xa2\xb26",
                    -1: 3,
                },
                "Coords should be 66 bytes for crv P-521",
            ),
            (
                {
                    1: 2,
                    3: 8,
                    -2: b"invalid-length-x",
                    -3: b'6\x00\x14\xfd\x13\t\x07\xdc,\t\xda\x1c}G\x0f\xd5\x11\xb2H\xe8\xc9\x05\xa8\x1f\xf3Q?\xa3"\xec7A',
                    -1: 8,
                },
                "Coords should be 32 bytes for crv secp256k1",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -4: "tstr-d",
                    -1: 1,
                },
                "d(-4) should be bytes(bstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -4: {},
                    -1: 1,
                },
                "d(-4) should be bytes(bstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -4: [],
                    -1: 1,
                },
                "d(-4) should be bytes(bstr).",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -4: b"invalid-length-d",
                    -1: 1,
                },
                "d(-4) should be 32 bytes for curve 1",
            ),
            (
                {
                    1: 2,
                    -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                    -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                    -4: b"dddddddddddddddddddddddddddddddd",
                    -1: 1,
                },
                "Invalid private key.",
            ),
        ],
    )
    def test_ec2_key_constructor_with_invalid_args(self, invalid, msg):
        with pytest.raises(ValueError) as err:
            EC2Key(invalid)
            pytest.fail("EC2Key should fail.")
        assert msg in str(err.value)

    def test_ec2_key_sign_with_es256_public_key(self):
        public_key = EC2Key(
            {
                1: 2,
                3: 1,
                -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                -1: 1,
            }
        )
        with pytest.raises(ValueError) as err:
            public_key.sign(b"Hello world!")
            pytest.fail("sign should not fail.")
        assert "Public key cannot be used for signing." in str(err.value)

    def test_ec2_key_verify_with_another_es256_public_key(self):
        private_key = EC2Key(
            {
                1: 2,
                3: 1,
                -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                -4: b'\xe9\x16\x0c\xa96\x8d\xfa\xbc\xd5\xda"ua\xec\xf7\x96\r\x15\xf7_\xf3rb{\xb1\xde;\x99\x88\xafNh',
                -1: 1,
            }
        )
        public_key2 = EC2Key(
            {
                1: 2,
                3: 1,
                -1: 1,
                -2: b"\xd6\xdfNb\xfa-U\xab#\x85\xf4\xd1\xb5Z\x17m5WPN\xd12*\xe1\xc9\xdb_\xdcD!\xd1Y",
                -3: b"(\x8bw\x1d\xf5\xbe\x9a\xf3\x11\xbb\xe7\xa9\x98\xc9\xf9\\\xee\x862\x10\xae\x83\xb2\x97\xa9/\xd5\xb6~d\x85\x85",
                # -4: b'>\x89\xb8[2\xe3\xf1\xf9x\xea%\xa9\xaes\xf1\xb5\xfeo;\xfa\xb4\x13\xb33\x068j\x04\xfd\x03[\xe8'
            }
        )
        sig = private_key.sign(b"Hello world!")
        with pytest.raises(VerifyError) as err:
            public_key2.verify(b"Hello world!", sig)
            pytest.fail("verify should not fail.")
        assert "Failed to verify." in str(err.value)

    def test_ec2_key_verify_with_invalid_signature(self):
        private_key = EC2Key(
            {
                1: 2,
                3: 1,
                -2: b"\xa7\xddc*\xff\xc2?\x8b\xf8\x9c:\xad\xccDF\x9cZ \x04P\xef\x99\x0c=\xe6 w1\x08&\xba\xd9",
                -3: b"\xe2\xdb\xef\xfe\xb8\x8a\x12\xf27\xcb\x15:\x8a\xb9\x1a90B\x1a\x19^\xbc\xdc\xde\r\xb9s\xc1P\xf3\xaa\xdd",
                -4: b'\xe9\x16\x0c\xa96\x8d\xfa\xbc\xd5\xda"ua\xec\xf7\x96\r\x15\xf7_\xf3rb{\xb1\xde;\x99\x88\xafNh',
                -1: 1,
            }
        )
        sig = private_key.sign(b"Hello world!")
        with pytest.raises(VerifyError) as err:
            private_key.verify(b"Hello world!", sig + b"xxx")
            pytest.fail("verify should not fail.")
        assert "Invalid signature." in str(err.value)
