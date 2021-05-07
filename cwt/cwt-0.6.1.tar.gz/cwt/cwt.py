from calendar import timegm
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from cbor2 import CBORTag

from .cbor_processor import CBORProcessor
from .claims import Claims
from .claims_builder import ClaimsBuilder
from .const import COSE_KEY_OPERATION_VALUES
from .cose import COSE
from .cose_key import COSEKey
from .exceptions import DecodeError, VerifyError
from .recipient import Recipient

_CWT_DEFAULT_EXPIRES_IN = 3600  # 1 hour
_CWT_DEFAULT_LEEWAY = 60  # 1 min


class CWT(CBORProcessor):
    """
    A CWT (CBOR Web Token) Implementaion, which is built on top of
    :class:`COSE <cwt.COSE>`

    ``cwt.cwt`` is a global object of this class initialized with default settings.
    """

    CBOR_TAG = 61

    def __init__(self, options: Optional[Dict[str, Any]] = None):
        """
        Constructor.

        Args:
            options (Optional[Dict[str, Any]]): Options for the initial
                configuration of CWT. At this time, ``expires_in`` (default
                value: ``3600`` ) and ``leaway`` (default value: ``60``) are
                only supported. See also :func:`expires_in <cwt.CWT.expires_in>`,
                :func:`leeway <cwt.CWT.leeway>`.

        Examples:

            >>> from cwt import CWT, claims, cose_key
            >>> ctx = CWT({"expires_in": 3600*24, "leeway": 10})
            >>> key = cose_key.from_symmetric_key("mysecret")
            >>> token = ctx.encode_and_mac(
            ...     claims.from_json({"iss": "coaps://as.example", "sub": "dajiaji", "cti": "123"}),
            ...     key,
            ... )
        """
        self._expires_in = _CWT_DEFAULT_EXPIRES_IN
        self._leeway = _CWT_DEFAULT_LEEWAY
        self._cose = COSE(options)
        self._claims = ClaimsBuilder()
        if not options:
            return

        if "expires_in" in options:
            if not isinstance(options["expires_in"], int):
                raise ValueError("expires_in should be int.")
            self._expires_in = options["expires_in"]
            if self._expires_in <= 0:
                raise ValueError("expires_in should be positive number.")
        if "leeway" in options:
            if not isinstance(options["leeway"], int):
                raise ValueError("leeway should be int.")
            self._leeway = options["leeway"]
            if self._leeway <= 0:
                raise ValueError("leeway should be positive number.")

    @property
    def expires_in(self) -> int:
        """
        The default lifetime in seconds of CWT.
        If `exp` is not found in claims, this value will be used with current time.
        """
        return self._expires_in

    @property
    def leeway(self) -> int:
        """
        The default leeway in seconds for validating ``exp`` and ``nbf``.
        """
        return self._leeway

    def encode(
        self,
        claims: Union[Claims, Dict[str, Any], Dict[int, Any], bytes, str],
        key: COSEKey,
        nonce: bytes = b"",
        tagged: bool = False,
        recipients: Optional[List[Recipient]] = None,
    ) -> bytes:
        """
        Encodes CWT with MAC, signing or encryption.
        This is a wrapper function of the following functions for easy use:

        * :func:`encode_and_mac <cwt.CWT.encode_and_mac>`
        * :func:`encode_and_sign <cwt.CWT.encode_and_sign>`
        * :func:`encode_and_encrypt <cwt.CWT.encode_and_encrypt>`

        Therefore, it must be clear whether the use of the specified key is for MAC,
        signing, or encryption. For this purpose, the key must have the ``key_ops``
        parameter set to identify the usage.

        Args:
            claims (Union[Claims, Dict[str, Any], Dict[int, Any], bytes, str]): A CWT
                claims object, or a JWT claims object, text string or byte string.
            key (COSEKey): A COSE key used to generate a MAC for the claims.
            recipients (List[Recipient]): A list of recipient information structures.
            tagged (bool): An indicator whether the response is wrapped by CWT tag(61)
                or not.
        Returns:
            bytes: A byte string of the encoded CWT.
        Raises:
            ValueError: Invalid arguments.
            EncodeError: Failed to encode the claims.
        """
        if isinstance(claims, Claims):
            return self._encode(claims, key, nonce, tagged, recipients)
        if isinstance(claims, str):
            claims = claims.encode("utf-8")
        if isinstance(claims, bytes):
            try:
                claims = self._claims.from_json(claims)
            except ValueError:
                return self._encode(claims, key, nonce, tagged, recipients)
        else:
            # Following code causes mypy error:
            # for k, v in claims.items():
            #     if isinstance(k, str):
            #         claims = self._claims.from_json(claims)
            #     break
            # To avoid the error:
            json_claims: Dict[str, Any] = {}
            for k, v in claims.items():
                if isinstance(k, str):
                    json_claims[k] = v
            if json_claims:
                claims = self._claims.from_json(json_claims)
        return self._encode(claims, key, nonce, tagged, recipients)

    def encode_and_mac(
        self,
        claims: Union[Claims, Dict[int, Any], bytes],
        key: COSEKey,
        tagged: bool = False,
        recipients: Optional[List[Recipient]] = None,
    ) -> bytes:
        """
        Encodes with MAC.

        Args:
            claims (Union[Claims, Dict[int, Any], bytes]): A CWT claims object or byte
                string.
            key (COSEKey): A COSE key used to generate a MAC for the claims.
            recipients (List[Recipient]): A list of recipient information structures.
            tagged (bool): An indicator whether the response is wrapped by CWT tag(61)
                or not.
        Returns:
            bytes: A byte string of the encoded CWT.
        Raises:
            ValueError: Invalid arguments.
            EncodeError: Failed to encode the claims.
        """
        if not isinstance(claims, Claims):
            self._validate(claims)
        else:
            claims = claims.to_dict()
        self._set_default_value(claims)
        protected: Dict[int, Any] = {1: key.alg}
        unprotected: Dict[int, Any] = {4: key.kid} if key.kid else {}
        res = self._cose.encode_and_mac(
            protected, unprotected, claims, key, recipients, out="cbor2/CBORTag"
        )
        if tagged:
            return self._dumps(CBORTag(CWT.CBOR_TAG, res))
        return self._dumps(res)

    def encode_and_sign(
        self,
        claims: Union[Claims, Dict[int, Any], bytes],
        key: Union[COSEKey, List[COSEKey]],
        tagged: bool = False,
    ) -> bytes:
        """
        Encodes CWT with signing.

        Args:
            claims (Claims, Union[Dict[int, Any], bytes]): A CWT claims object or byte
                string.
            key (Union[COSEKey, List[COSEKey]]): A COSE key or a list of the keys used
                to sign claims.
            tagged (bool): An indicator whether the response is wrapped by CWT tag(61)
                or not.
        Returns:
            bytes: A byte string of the encoded CWT.
        Raises:
            ValueError: Invalid arguments.
            EncodeError: Failed to encode the claims.
        """
        if not isinstance(claims, Claims):
            self._validate(claims)
        else:
            claims = claims.to_dict()
        self._set_default_value(claims)
        protected: Dict[int, Any] = {}
        unprotected: Dict[int, Any] = {}
        res = self._cose.encode_and_sign(
            protected, unprotected, claims, key, out="cbor2/CBORTag"
        )
        if tagged:
            return self._dumps(CBORTag(CWT.CBOR_TAG, res))
        return self._dumps(res)

    def encode_and_encrypt(
        self,
        claims: Union[Claims, Dict[int, Any], bytes],
        key: COSEKey,
        nonce: bytes = b"",
        tagged: bool = False,
        recipients: Optional[List[Recipient]] = None,
    ) -> bytes:
        """
        Encodes CWT with encryption.

        Args:
            claims (Claims, Union[Dict[int, Any], bytes]): A CWT claims object or byte
            string.
            key (COSEKey): A COSE key used to encrypt the claims.
            nonce (bytes): A nonce for encryption.
            recipients (List[Recipient]): A list of recipient information structures.
            tagged (bool): An indicator whether the response is wrapped by CWT tag(61)
                or not.
        Returns:
            bytes: A byte string of the encoded CWT.
        Raises:
            ValueError: Invalid arguments.
            EncodeError: Failed to encode the claims.
        """
        if not isinstance(claims, Claims):
            self._validate(claims)
        else:
            claims = claims.to_dict()
        self._set_default_value(claims)
        protected: Dict[int, Any] = {1: key.alg}
        unprotected: Dict[int, Any] = {4: key.kid} if key.kid else {}
        if not nonce:
            try:
                nonce = key.generate_nonce()
            except NotImplementedError:
                raise ValueError(
                    "Nonce generation is not supported for the key. Set a nonce explicitly."
                )

        unprotected[5] = nonce
        res = self._cose.encode_and_encrypt(
            protected, unprotected, claims, key, nonce, recipients, out="cbor2/CBORTag"
        )
        if tagged:
            return self._dumps(CBORTag(CWT.CBOR_TAG, res))
        return self._dumps(res)

    def decode(
        self, data: bytes, key: Union[COSEKey, List[COSEKey]], no_verify: bool = False
    ) -> Dict[int, Any]:
        """
        Verifies and decodes CWT.

        Args:
            data (bytes): A byte string of an encoded CWT.
            key (Union[COSEKey, List[COSEKey]]): A COSE key or a list of the keys
                used to verify and decrypt the encoded CWT.
            no_verify (bool): An indicator whether token verification is skiped
                or not.
        Returns:
            bytes: A byte string of the decoded CWT.
        Raises:
            ValueError: Invalid arguments.
            DecodeError: Failed to decode the CWT.
            VerifyError: Failed to verify the CWT.
        """
        cwt = self._loads(data)
        if isinstance(cwt, CBORTag) and cwt.tag == CWT.CBOR_TAG:
            cwt = cwt.value
        keys: List[COSEKey] = [key] if isinstance(key, COSEKey) else key
        while isinstance(cwt, CBORTag) or isinstance(cwt, bytes):
            cwt = self._cose.decode(cwt, keys)
        if not no_verify:
            self._verify(cwt)
        return cwt

    def set_private_claim_names(self, claim_names: Dict[str, int]):
        """
        Sets private claim definitions. This function call is redirected to the
        internal :class:`ClaimsBuilder <cwt.ClaimsBuilder>`'s
        :func:`set_private_claim_names <cwt.ClaimsBuilder.set_private_claim_names>`
        directly. The definitions will be used in :func:`encode <cwt.CWT.encode>`
        when it is called with JSON-based claims.

        Args:
            claims (Dict[str, int]): A set of private claim definitions which
                consist of a readable claim name(str) and a claim key(int).
                The claim key should be less than -65536.
        Raises:
            ValueError: Invalid arguments.
        """
        return self._claims.set_private_claim_names(claim_names)

    def _encode(
        self,
        claims: Union[Claims, Dict[Any, Any], bytes],
        key: COSEKey,
        nonce: bytes = b"",
        tagged: bool = False,
        recipients: Optional[List[Recipient]] = None,
    ) -> bytes:
        if COSE_KEY_OPERATION_VALUES["sign"] in key.key_ops:
            if [ops for ops in key.key_ops if ops in [3, 4, 9, 10]]:
                raise ValueError("The key operation could not be specified.")
            return self.encode_and_sign(claims, key, tagged)
        if COSE_KEY_OPERATION_VALUES["encrypt"] in key.key_ops:
            if [ops for ops in key.key_ops if ops in [1, 2, 9, 10]]:
                raise ValueError("The key operation could not be specified.")
            return self.encode_and_encrypt(claims, key, nonce, tagged, recipients)
        if COSE_KEY_OPERATION_VALUES["MAC create"] in key.key_ops:
            if [ops for ops in key.key_ops if ops in [1, 2, 3, 4]]:
                raise ValueError("The key operation could not be specified.")
            return self.encode_and_mac(claims, key, tagged, recipients)
        raise ValueError("The key operation could not be specified.")

    def _validate(self, claims: Union[Dict[int, Any], bytes]):
        if isinstance(claims, bytes):
            try:
                nested = self._loads(claims)
            except Exception:
                raise ValueError("Invalid claim format.")
            if not isinstance(nested, CBORTag):
                raise ValueError("A bytes-formatted claims needs CBOR(COSE) Tag.")
            if nested.tag not in [16, 96, 17, 97, 18, 98]:
                raise ValueError(f"Unsupported or unknown CBOR tag({nested.tag}).")
            return
        self._claims.validate(claims)
        return

    def _verify(self, claims: Dict[int, Any]):
        if not isinstance(claims, dict):
            raise DecodeError("Failed to decode.")

        now = timegm(datetime.utcnow().utctimetuple())
        if 4 in claims:  # exp
            if isinstance(claims[4], int) or isinstance(claims[4], float):
                if claims[4] < (now - self._leeway):
                    raise VerifyError("The token has expired.")
            else:
                raise ValueError("exp should be int or float.")

        if 5 in claims:  # nbf
            if isinstance(claims[5], int) or isinstance(claims[5], float):
                if claims[5] > (now + self._leeway):
                    raise VerifyError("The token is not yet valid.")
            else:
                raise ValueError("nbf should be int or float.")
        return

    def _set_default_value(self, claims: Union[Dict[int, Any], bytes]):
        if isinstance(claims, bytes):
            return
        now = timegm(datetime.utcnow().utctimetuple())
        if 4 not in claims:
            claims[4] = now + self._expires_in
        if 5 not in claims:
            claims[5] = now
        if 6 not in claims:
            claims[6] = now
        return


# export
_cwt = CWT()
encode = _cwt.encode
encode_and_mac = _cwt.encode_and_mac
encode_and_sign = _cwt.encode_and_sign
encode_and_encrypt = _cwt.encode_and_encrypt
decode = _cwt.decode
set_private_claim_names = _cwt.set_private_claim_names
