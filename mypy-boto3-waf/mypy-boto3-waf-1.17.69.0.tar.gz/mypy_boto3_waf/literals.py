"""
Type annotations for waf service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/literals.html)

Usage::

    ```python
    from mypy_boto3_waf.literals import ChangeAction

    data: ChangeAction = "DELETE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ChangeAction",
    "ChangeTokenStatus",
    "ComparisonOperator",
    "GeoMatchConstraintType",
    "GeoMatchConstraintValue",
    "GetRateBasedRuleManagedKeysPaginatorName",
    "IPSetDescriptorType",
    "ListActivatedRulesInRuleGroupPaginatorName",
    "ListByteMatchSetsPaginatorName",
    "ListGeoMatchSetsPaginatorName",
    "ListIPSetsPaginatorName",
    "ListLoggingConfigurationsPaginatorName",
    "ListRateBasedRulesPaginatorName",
    "ListRegexMatchSetsPaginatorName",
    "ListRegexPatternSetsPaginatorName",
    "ListRuleGroupsPaginatorName",
    "ListRulesPaginatorName",
    "ListSizeConstraintSetsPaginatorName",
    "ListSqlInjectionMatchSetsPaginatorName",
    "ListSubscribedRuleGroupsPaginatorName",
    "ListWebACLsPaginatorName",
    "ListXssMatchSetsPaginatorName",
    "MatchFieldType",
    "PositionalConstraint",
    "PredicateType",
    "RateKey",
    "TextTransformation",
    "WafActionType",
    "WafOverrideActionType",
    "WafRuleType",
)


ChangeAction = Literal["DELETE", "INSERT"]
ChangeTokenStatus = Literal["INSYNC", "PENDING", "PROVISIONED"]
ComparisonOperator = Literal["EQ", "GE", "GT", "LE", "LT", "NE"]
GeoMatchConstraintType = Literal["Country"]
GeoMatchConstraintValue = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AU",
    "AW",
    "AX",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BL",
    "BM",
    "BN",
    "BO",
    "BQ",
    "BR",
    "BS",
    "BT",
    "BV",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "GA",
    "GB",
    "GD",
    "GE",
    "GF",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GP",
    "GQ",
    "GR",
    "GS",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MQ",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NF",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PS",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "SS",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TF",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "UM",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
]
GetRateBasedRuleManagedKeysPaginatorName = Literal["get_rate_based_rule_managed_keys"]
IPSetDescriptorType = Literal["IPV4", "IPV6"]
ListActivatedRulesInRuleGroupPaginatorName = Literal["list_activated_rules_in_rule_group"]
ListByteMatchSetsPaginatorName = Literal["list_byte_match_sets"]
ListGeoMatchSetsPaginatorName = Literal["list_geo_match_sets"]
ListIPSetsPaginatorName = Literal["list_ip_sets"]
ListLoggingConfigurationsPaginatorName = Literal["list_logging_configurations"]
ListRateBasedRulesPaginatorName = Literal["list_rate_based_rules"]
ListRegexMatchSetsPaginatorName = Literal["list_regex_match_sets"]
ListRegexPatternSetsPaginatorName = Literal["list_regex_pattern_sets"]
ListRuleGroupsPaginatorName = Literal["list_rule_groups"]
ListRulesPaginatorName = Literal["list_rules"]
ListSizeConstraintSetsPaginatorName = Literal["list_size_constraint_sets"]
ListSqlInjectionMatchSetsPaginatorName = Literal["list_sql_injection_match_sets"]
ListSubscribedRuleGroupsPaginatorName = Literal["list_subscribed_rule_groups"]
ListWebACLsPaginatorName = Literal["list_web_acls"]
ListXssMatchSetsPaginatorName = Literal["list_xss_match_sets"]
MatchFieldType = Literal[
    "ALL_QUERY_ARGS", "BODY", "HEADER", "METHOD", "QUERY_STRING", "SINGLE_QUERY_ARG", "URI"
]
PositionalConstraint = Literal["CONTAINS", "CONTAINS_WORD", "ENDS_WITH", "EXACTLY", "STARTS_WITH"]
PredicateType = Literal[
    "ByteMatch",
    "GeoMatch",
    "IPMatch",
    "RegexMatch",
    "SizeConstraint",
    "SqlInjectionMatch",
    "XssMatch",
]
RateKey = Literal["IP"]
TextTransformation = Literal[
    "CMD_LINE", "COMPRESS_WHITE_SPACE", "HTML_ENTITY_DECODE", "LOWERCASE", "NONE", "URL_DECODE"
]
WafActionType = Literal["ALLOW", "BLOCK", "COUNT"]
WafOverrideActionType = Literal["COUNT", "NONE"]
WafRuleType = Literal["GROUP", "RATE_BASED", "REGULAR"]
