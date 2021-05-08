# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['OrganizationApiproductRateplanArgs', 'OrganizationApiproductRateplan']

@pulumi.input_type
class OrganizationApiproductRateplanArgs:
    def __init__(__self__, *,
                 apiproducts_id: pulumi.Input[str],
                 organizations_id: pulumi.Input[str],
                 rateplans_id: pulumi.Input[str],
                 apiproduct: Optional[pulumi.Input[str]] = None,
                 billing_period: Optional[pulumi.Input[str]] = None,
                 consumption_pricing_rates: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RateRangeArgs']]]] = None,
                 consumption_pricing_type: Optional[pulumi.Input[str]] = None,
                 currency_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 fixed_fee_frequency: Optional[pulumi.Input[int]] = None,
                 fixed_recurring_fee: Optional[pulumi.Input['GoogleTypeMoneyArgs']] = None,
                 payment_funding_model: Optional[pulumi.Input[str]] = None,
                 revenue_share_rates: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RevenueShareRangeArgs']]]] = None,
                 revenue_share_type: Optional[pulumi.Input[str]] = None,
                 setup_fee: Optional[pulumi.Input['GoogleTypeMoneyArgs']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationApiproductRateplan resource.
        :param pulumi.Input[str] apiproduct: Name of the API product that the rate plan is associated with.
        :param pulumi.Input[str] billing_period: Frequency at which the customer will be billed.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RateRangeArgs']]] consumption_pricing_rates: API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200.
        :param pulumi.Input[str] consumption_pricing_type: Pricing model used for consumption-based charges.
        :param pulumi.Input[str] currency_code: Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard.
        :param pulumi.Input[str] description: Description of the rate plan.
        :param pulumi.Input[str] display_name: Display name of the rate plan.
        :param pulumi.Input[str] end_time: Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire.
        :param pulumi.Input[int] fixed_fee_frequency: Frequency at which the fixed fee is charged.
        :param pulumi.Input['GoogleTypeMoneyArgs'] fixed_recurring_fee: Fixed amount that is charged at a defined interval and billed in advance of use of the API product. The fee will be prorated for the first billing period.
        :param pulumi.Input[str] payment_funding_model: Flag that specifies the billing account type, prepaid or postpaid.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RevenueShareRangeArgs']]] revenue_share_rates: Details of the revenue sharing model.
        :param pulumi.Input[str] revenue_share_type: Method used to calculate the revenue that is shared with developers.
        :param pulumi.Input['GoogleTypeMoneyArgs'] setup_fee: Initial, one-time fee paid when purchasing the API product.
        :param pulumi.Input[str] start_time: Time when the rate plan becomes active in milliseconds since epoch.
        :param pulumi.Input[str] state: Current state of the rate plan (draft or published).
        """
        pulumi.set(__self__, "apiproducts_id", apiproducts_id)
        pulumi.set(__self__, "organizations_id", organizations_id)
        pulumi.set(__self__, "rateplans_id", rateplans_id)
        if apiproduct is not None:
            pulumi.set(__self__, "apiproduct", apiproduct)
        if billing_period is not None:
            pulumi.set(__self__, "billing_period", billing_period)
        if consumption_pricing_rates is not None:
            pulumi.set(__self__, "consumption_pricing_rates", consumption_pricing_rates)
        if consumption_pricing_type is not None:
            pulumi.set(__self__, "consumption_pricing_type", consumption_pricing_type)
        if currency_code is not None:
            pulumi.set(__self__, "currency_code", currency_code)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if fixed_fee_frequency is not None:
            pulumi.set(__self__, "fixed_fee_frequency", fixed_fee_frequency)
        if fixed_recurring_fee is not None:
            pulumi.set(__self__, "fixed_recurring_fee", fixed_recurring_fee)
        if payment_funding_model is not None:
            pulumi.set(__self__, "payment_funding_model", payment_funding_model)
        if revenue_share_rates is not None:
            pulumi.set(__self__, "revenue_share_rates", revenue_share_rates)
        if revenue_share_type is not None:
            pulumi.set(__self__, "revenue_share_type", revenue_share_type)
        if setup_fee is not None:
            pulumi.set(__self__, "setup_fee", setup_fee)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="apiproductsId")
    def apiproducts_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "apiproducts_id")

    @apiproducts_id.setter
    def apiproducts_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "apiproducts_id", value)

    @property
    @pulumi.getter(name="organizationsId")
    def organizations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organizations_id")

    @organizations_id.setter
    def organizations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organizations_id", value)

    @property
    @pulumi.getter(name="rateplansId")
    def rateplans_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rateplans_id")

    @rateplans_id.setter
    def rateplans_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rateplans_id", value)

    @property
    @pulumi.getter
    def apiproduct(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the API product that the rate plan is associated with.
        """
        return pulumi.get(self, "apiproduct")

    @apiproduct.setter
    def apiproduct(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "apiproduct", value)

    @property
    @pulumi.getter(name="billingPeriod")
    def billing_period(self) -> Optional[pulumi.Input[str]]:
        """
        Frequency at which the customer will be billed.
        """
        return pulumi.get(self, "billing_period")

    @billing_period.setter
    def billing_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_period", value)

    @property
    @pulumi.getter(name="consumptionPricingRates")
    def consumption_pricing_rates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RateRangeArgs']]]]:
        """
        API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200.
        """
        return pulumi.get(self, "consumption_pricing_rates")

    @consumption_pricing_rates.setter
    def consumption_pricing_rates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RateRangeArgs']]]]):
        pulumi.set(self, "consumption_pricing_rates", value)

    @property
    @pulumi.getter(name="consumptionPricingType")
    def consumption_pricing_type(self) -> Optional[pulumi.Input[str]]:
        """
        Pricing model used for consumption-based charges.
        """
        return pulumi.get(self, "consumption_pricing_type")

    @consumption_pricing_type.setter
    def consumption_pricing_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consumption_pricing_type", value)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[pulumi.Input[str]]:
        """
        Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard.
        """
        return pulumi.get(self, "currency_code")

    @currency_code.setter
    def currency_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "currency_code", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the rate plan.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the rate plan.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter(name="fixedFeeFrequency")
    def fixed_fee_frequency(self) -> Optional[pulumi.Input[int]]:
        """
        Frequency at which the fixed fee is charged.
        """
        return pulumi.get(self, "fixed_fee_frequency")

    @fixed_fee_frequency.setter
    def fixed_fee_frequency(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "fixed_fee_frequency", value)

    @property
    @pulumi.getter(name="fixedRecurringFee")
    def fixed_recurring_fee(self) -> Optional[pulumi.Input['GoogleTypeMoneyArgs']]:
        """
        Fixed amount that is charged at a defined interval and billed in advance of use of the API product. The fee will be prorated for the first billing period.
        """
        return pulumi.get(self, "fixed_recurring_fee")

    @fixed_recurring_fee.setter
    def fixed_recurring_fee(self, value: Optional[pulumi.Input['GoogleTypeMoneyArgs']]):
        pulumi.set(self, "fixed_recurring_fee", value)

    @property
    @pulumi.getter(name="paymentFundingModel")
    def payment_funding_model(self) -> Optional[pulumi.Input[str]]:
        """
        Flag that specifies the billing account type, prepaid or postpaid.
        """
        return pulumi.get(self, "payment_funding_model")

    @payment_funding_model.setter
    def payment_funding_model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payment_funding_model", value)

    @property
    @pulumi.getter(name="revenueShareRates")
    def revenue_share_rates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RevenueShareRangeArgs']]]]:
        """
        Details of the revenue sharing model.
        """
        return pulumi.get(self, "revenue_share_rates")

    @revenue_share_rates.setter
    def revenue_share_rates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1RevenueShareRangeArgs']]]]):
        pulumi.set(self, "revenue_share_rates", value)

    @property
    @pulumi.getter(name="revenueShareType")
    def revenue_share_type(self) -> Optional[pulumi.Input[str]]:
        """
        Method used to calculate the revenue that is shared with developers.
        """
        return pulumi.get(self, "revenue_share_type")

    @revenue_share_type.setter
    def revenue_share_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "revenue_share_type", value)

    @property
    @pulumi.getter(name="setupFee")
    def setup_fee(self) -> Optional[pulumi.Input['GoogleTypeMoneyArgs']]:
        """
        Initial, one-time fee paid when purchasing the API product.
        """
        return pulumi.get(self, "setup_fee")

    @setup_fee.setter
    def setup_fee(self, value: Optional[pulumi.Input['GoogleTypeMoneyArgs']]):
        pulumi.set(self, "setup_fee", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time when the rate plan becomes active in milliseconds since epoch.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Current state of the rate plan (draft or published).
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class OrganizationApiproductRateplan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apiproduct: Optional[pulumi.Input[str]] = None,
                 apiproducts_id: Optional[pulumi.Input[str]] = None,
                 billing_period: Optional[pulumi.Input[str]] = None,
                 consumption_pricing_rates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1RateRangeArgs']]]]] = None,
                 consumption_pricing_type: Optional[pulumi.Input[str]] = None,
                 currency_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 fixed_fee_frequency: Optional[pulumi.Input[int]] = None,
                 fixed_recurring_fee: Optional[pulumi.Input[pulumi.InputType['GoogleTypeMoneyArgs']]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 payment_funding_model: Optional[pulumi.Input[str]] = None,
                 rateplans_id: Optional[pulumi.Input[str]] = None,
                 revenue_share_rates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1RevenueShareRangeArgs']]]]] = None,
                 revenue_share_type: Optional[pulumi.Input[str]] = None,
                 setup_fee: Optional[pulumi.Input[pulumi.InputType['GoogleTypeMoneyArgs']]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a rate plan that is associated with an API product in an organization. Using rate plans, API product owners can monetize their API products by configuring one or more of the following: - Billing frequency - Initial setup fees for using an API product - Payment funding model (postpaid only) - Fixed recurring or consumption-based charges for using an API product - Revenue sharing with developer partners An API product can have multiple rate plans associated with it but *only one* rate plan can be active at any point of time. **Note: From the developer's perspective, they purchase API products not rate plans.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] apiproduct: Name of the API product that the rate plan is associated with.
        :param pulumi.Input[str] billing_period: Frequency at which the customer will be billed.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1RateRangeArgs']]]] consumption_pricing_rates: API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200.
        :param pulumi.Input[str] consumption_pricing_type: Pricing model used for consumption-based charges.
        :param pulumi.Input[str] currency_code: Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard.
        :param pulumi.Input[str] description: Description of the rate plan.
        :param pulumi.Input[str] display_name: Display name of the rate plan.
        :param pulumi.Input[str] end_time: Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire.
        :param pulumi.Input[int] fixed_fee_frequency: Frequency at which the fixed fee is charged.
        :param pulumi.Input[pulumi.InputType['GoogleTypeMoneyArgs']] fixed_recurring_fee: Fixed amount that is charged at a defined interval and billed in advance of use of the API product. The fee will be prorated for the first billing period.
        :param pulumi.Input[str] payment_funding_model: Flag that specifies the billing account type, prepaid or postpaid.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1RevenueShareRangeArgs']]]] revenue_share_rates: Details of the revenue sharing model.
        :param pulumi.Input[str] revenue_share_type: Method used to calculate the revenue that is shared with developers.
        :param pulumi.Input[pulumi.InputType['GoogleTypeMoneyArgs']] setup_fee: Initial, one-time fee paid when purchasing the API product.
        :param pulumi.Input[str] start_time: Time when the rate plan becomes active in milliseconds since epoch.
        :param pulumi.Input[str] state: Current state of the rate plan (draft or published).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationApiproductRateplanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a rate plan that is associated with an API product in an organization. Using rate plans, API product owners can monetize their API products by configuring one or more of the following: - Billing frequency - Initial setup fees for using an API product - Payment funding model (postpaid only) - Fixed recurring or consumption-based charges for using an API product - Revenue sharing with developer partners An API product can have multiple rate plans associated with it but *only one* rate plan can be active at any point of time. **Note: From the developer's perspective, they purchase API products not rate plans.

        :param str resource_name: The name of the resource.
        :param OrganizationApiproductRateplanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationApiproductRateplanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apiproduct: Optional[pulumi.Input[str]] = None,
                 apiproducts_id: Optional[pulumi.Input[str]] = None,
                 billing_period: Optional[pulumi.Input[str]] = None,
                 consumption_pricing_rates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1RateRangeArgs']]]]] = None,
                 consumption_pricing_type: Optional[pulumi.Input[str]] = None,
                 currency_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 fixed_fee_frequency: Optional[pulumi.Input[int]] = None,
                 fixed_recurring_fee: Optional[pulumi.Input[pulumi.InputType['GoogleTypeMoneyArgs']]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 payment_funding_model: Optional[pulumi.Input[str]] = None,
                 rateplans_id: Optional[pulumi.Input[str]] = None,
                 revenue_share_rates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1RevenueShareRangeArgs']]]]] = None,
                 revenue_share_type: Optional[pulumi.Input[str]] = None,
                 setup_fee: Optional[pulumi.Input[pulumi.InputType['GoogleTypeMoneyArgs']]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationApiproductRateplanArgs.__new__(OrganizationApiproductRateplanArgs)

            __props__.__dict__["apiproduct"] = apiproduct
            if apiproducts_id is None and not opts.urn:
                raise TypeError("Missing required property 'apiproducts_id'")
            __props__.__dict__["apiproducts_id"] = apiproducts_id
            __props__.__dict__["billing_period"] = billing_period
            __props__.__dict__["consumption_pricing_rates"] = consumption_pricing_rates
            __props__.__dict__["consumption_pricing_type"] = consumption_pricing_type
            __props__.__dict__["currency_code"] = currency_code
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["end_time"] = end_time
            __props__.__dict__["fixed_fee_frequency"] = fixed_fee_frequency
            __props__.__dict__["fixed_recurring_fee"] = fixed_recurring_fee
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__.__dict__["organizations_id"] = organizations_id
            __props__.__dict__["payment_funding_model"] = payment_funding_model
            if rateplans_id is None and not opts.urn:
                raise TypeError("Missing required property 'rateplans_id'")
            __props__.__dict__["rateplans_id"] = rateplans_id
            __props__.__dict__["revenue_share_rates"] = revenue_share_rates
            __props__.__dict__["revenue_share_type"] = revenue_share_type
            __props__.__dict__["setup_fee"] = setup_fee
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["state"] = state
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_modified_at"] = None
            __props__.__dict__["name"] = None
        super(OrganizationApiproductRateplan, __self__).__init__(
            'google-native:apigee/v1:OrganizationApiproductRateplan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationApiproductRateplan':
        """
        Get an existing OrganizationApiproductRateplan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationApiproductRateplanArgs.__new__(OrganizationApiproductRateplanArgs)

        __props__.__dict__["apiproduct"] = None
        __props__.__dict__["billing_period"] = None
        __props__.__dict__["consumption_pricing_rates"] = None
        __props__.__dict__["consumption_pricing_type"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["currency_code"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["fixed_fee_frequency"] = None
        __props__.__dict__["fixed_recurring_fee"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["payment_funding_model"] = None
        __props__.__dict__["revenue_share_rates"] = None
        __props__.__dict__["revenue_share_type"] = None
        __props__.__dict__["setup_fee"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["state"] = None
        return OrganizationApiproductRateplan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def apiproduct(self) -> pulumi.Output[str]:
        """
        Name of the API product that the rate plan is associated with.
        """
        return pulumi.get(self, "apiproduct")

    @property
    @pulumi.getter(name="billingPeriod")
    def billing_period(self) -> pulumi.Output[str]:
        """
        Frequency at which the customer will be billed.
        """
        return pulumi.get(self, "billing_period")

    @property
    @pulumi.getter(name="consumptionPricingRates")
    def consumption_pricing_rates(self) -> pulumi.Output[Sequence['outputs.GoogleCloudApigeeV1RateRangeResponse']]:
        """
        API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200.
        """
        return pulumi.get(self, "consumption_pricing_rates")

    @property
    @pulumi.getter(name="consumptionPricingType")
    def consumption_pricing_type(self) -> pulumi.Output[str]:
        """
        Pricing model used for consumption-based charges.
        """
        return pulumi.get(self, "consumption_pricing_type")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time that the rate plan was created in milliseconds since epoch.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> pulumi.Output[str]:
        """
        Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard.
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the rate plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Display name of the rate plan.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="fixedFeeFrequency")
    def fixed_fee_frequency(self) -> pulumi.Output[int]:
        """
        Frequency at which the fixed fee is charged.
        """
        return pulumi.get(self, "fixed_fee_frequency")

    @property
    @pulumi.getter(name="fixedRecurringFee")
    def fixed_recurring_fee(self) -> pulumi.Output['outputs.GoogleTypeMoneyResponse']:
        """
        Fixed amount that is charged at a defined interval and billed in advance of use of the API product. The fee will be prorated for the first billing period.
        """
        return pulumi.get(self, "fixed_recurring_fee")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[str]:
        """
        Time the rate plan was last modified in milliseconds since epoch.
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the rate plan.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="paymentFundingModel")
    def payment_funding_model(self) -> pulumi.Output[str]:
        """
        Flag that specifies the billing account type, prepaid or postpaid.
        """
        return pulumi.get(self, "payment_funding_model")

    @property
    @pulumi.getter(name="revenueShareRates")
    def revenue_share_rates(self) -> pulumi.Output[Sequence['outputs.GoogleCloudApigeeV1RevenueShareRangeResponse']]:
        """
        Details of the revenue sharing model.
        """
        return pulumi.get(self, "revenue_share_rates")

    @property
    @pulumi.getter(name="revenueShareType")
    def revenue_share_type(self) -> pulumi.Output[str]:
        """
        Method used to calculate the revenue that is shared with developers.
        """
        return pulumi.get(self, "revenue_share_type")

    @property
    @pulumi.getter(name="setupFee")
    def setup_fee(self) -> pulumi.Output['outputs.GoogleTypeMoneyResponse']:
        """
        Initial, one-time fee paid when purchasing the API product.
        """
        return pulumi.get(self, "setup_fee")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        Time when the rate plan becomes active in milliseconds since epoch.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Current state of the rate plan (draft or published).
        """
        return pulumi.get(self, "state")

