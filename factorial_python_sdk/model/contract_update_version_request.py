# coding: utf-8

"""
    Factorial API

    Open Api Specifications available at [https://github.com/factorialco/oas](https://github.com/factorialco/oasLooking)  Guides and support available at [https://help.factorialhr.com/integrations](https://help.factorialhr.com/integrations)  # Authentication  The public API provides two methods of authentication, ApiKeys and OAuth2. The following sections provide information regarding each one and their intent.  ## OAuth2  > OAuth2 is used to identify individual users, not applications or platforms.  OAuth2 is available for authenticating to the public API and making requests via third parties **on behalf of a user**. All actions are authored on behalf of the user that creates the token. This means the intent is to be used mainly to do submit actions the actual user is performing on an alternative interface.  To generate a token you will require opening an authorization dialog that returns a code, this code can then be exchanged for a token.  ### Configuration  In order to create an OAuth application, you must be an admin, head over to your [personal repository of OAuth applications](https://api.factorialhr.com/oauth/applications), click on `New application` and follow the creation process.  The Factorial API enforces the same permissions at the user level than the Factorial web application. This means that Factorial API users will only be able to perform the same actions they are allowed to do in the Factorial platform.  Next step will be to generate the Authorization Code you will need in order to generate an OAuth2 Token.  ### OAuth2 Code Generation  Should be generated via browser by opening the following url. The user should be already logged in to Factorial beforehand.  `https://api.factorialhr.com/oauth/authorize?client_id=&redirect_uri=&response_type=code&scope=`  YOUR_CLIENT_ID: OAuth2 Application Id REDIRECT_URI: OAuth2 Redirect URL  #### State Parameter  An optional query parameter called `state` can be added to the code generation url. Any string can be used and will be sent on the callback url.  > Authorization protocols provide a `state` parameter that allows you to restore the previous state of your application. The `state` parameter preserves some state objects set by the client in the Authorization request and makes it available to the client in the response.  ### OAuth2 Token Generation  Once you have the authorization code, you can request their access token to Factorial.  `curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&code=&grant_type=authorization_code&redirect_uri='`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret AUTHORIZATION_CODE: OAuth2 CODE REDIRECT_URI: OAuth2 Redirect URL  > You can generate only one OAuth2 token per Code, that means that if you want to generate a new token for a Code that already have one you should refresh your token.  Every time a new token is generated a refresh token is generated as well, so that you can use it on the OAuth2 Refresh Token, and an expire date is also provided.  ### OAuth2 Refresh Token  You can generate a new token under the same Code with a new expire date (you can do it as many times as you need). A refresh token is also returned here so that you can use it on the OAuth2 Refresh Token again.  `curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&refresh_token=&grant_type=refresh_token'`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret REFRESH_TOKEN: OAuth2 Refresh Token  ### OAuth2 Revoke Token  You can revoke an access/refresh token if you do not want it to be active anylonger. This can happen in cases where you have refreshed your token and would like to revoke the previous token if you haven't used the new token yet, as using the new token automatically revokes the previous one.  `curl -X POST 'https://api.factorialhr.com/oauth/revoke' -d 'client_id=&client_secret=&token='`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret TOKEN: OAuth2 Access/Refresh Token (whichever you wish to revoke)  ### OAuth2 Token Usage  The generated token is the credential for performing authenticated requests to Factorial. This token should be included in the Authorization header prefixed with the word Bearer and a separating space. As an example, if your token is `12345` then the header content should be `Bearer 12345`.  ### Maintaining a persistent connection  To maintain a persistent connection, you should not let the token expire. You can avoid this by simply refreshing your token before the expiration date. This will give you another token with a new expiration date, before that token expires you should refresh it again, and so on... If you want to do this automatically, you should provide something in your code that will help you perform the update every time the token expires. Otherwise, you would have to do the update manually and make sure you refresh your token before the expiration date to maintain the connection.  ## ApiKeys  > API keys are used to identify systems, not the individual users that access.  ApiKeys have **TOTAL ACCESS** to everything and never expire. Its the creators responsibility to generate them and store them securely.  ### Generation  In the `Core>Keys` section of this documentation you can access the apis for managing this resource.  ### Usage  ApiKeys are a single string of symbols that must be added as a custom header on the request. The header name must be `x-api-key` and the key must be the value without any prefixes.  ### Disclaimer  ApiKey management require full admin permissions as the resource itself allows for full admin access to the entire platform on behalf of the company and not of a user, therefore any operations are not linked to any user in particular.  # Development  ## SDKs  Coming soon  ## Sandbox  A sandbox/demo environment is available for testing integrations via public API calls. Developers can request provisioning with full access to a demo company where to test code before actually interacting with a production environment.  Contact your account manager or account executive to request this environment and get OAuth2 credentials for generating tokens.  Note: the domain for sandbox is different than that from production. Sandbox base domain is `http://api.demo.factorialhr.com`  ## Postman  Click the \"Run in Postman\" button to open the full list of endpoints on your Postman workspace as a Postman Collection. Inside the collection lookout for the Collection's Variables, configure your variables accordingly.  ### Delegating Token Generation To Postman  Coming soon  # Changelog  Coming soon  # How to...  ## Custom Fields  Custom fields are useful when you want to add some fields that are not the default ones, to every employee of the company.  For that, you have to create via Factorial App the base custom field in order to have all the employees with it. That option is available in customization, inside the company menu  Once you have that, via API, you can [Create a value for a custom field](https://apidoc.factorialhr.com/#72f3f786-e37d-4e80-ada2-0beedd03b171) to each employee. You should know the custom field id in order to make that, you can check it by [getting a collection of custom fields](https://apidoc.factorialhr.com/#f98dae5a-a8d0-474e-a181-7e9603409b42)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from factorial_python_sdk import schemas  # noqa: F401


class ContractUpdateVersionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "effective_on",
        }
        
        class properties:
            effective_on = schemas.StrSchema
            employee_id = schemas.IntSchema
            starts_on = schemas.StrSchema
            ends_on = schemas.StrSchema
            
            
            class working_hours_frequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "week": "WEEK",
                        "day": "DAY",
                        "month": "MONTH",
                        "year": "YEAR",
                    }
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("week")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("day")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("month")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("year")
            working_week_days = schemas.StrSchema
            working_hours = schemas.IntSchema
            
            
            class salary_frequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "yearly": "YEARLY",
                        "monthly": "MONTHLY",
                        "weekly": "WEEKLY",
                        "hourly": "HOURLY",
                        "daily": "DAILY",
                    }
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("yearly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("monthly")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("weekly")
                
                @schemas.classproperty
                def HOURLY(cls):
                    return cls("hourly")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("daily")
            salary_amount = schemas.IntSchema
            job_title = schemas.StrSchema
            
            
            class es_cotization_group(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'es_cotization_group':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class es_professional_category_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'es_professional_category_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class es_education_level_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'es_education_level_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class es_contract_type_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'es_contract_type_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "effective_on": effective_on,
                "employee_id": employee_id,
                "starts_on": starts_on,
                "ends_on": ends_on,
                "working_hours_frequency": working_hours_frequency,
                "working_week_days": working_week_days,
                "working_hours": working_hours,
                "salary_frequency": salary_frequency,
                "salary_amount": salary_amount,
                "job_title": job_title,
                "es_cotization_group": es_cotization_group,
                "es_professional_category_id": es_professional_category_id,
                "es_education_level_id": es_education_level_id,
                "es_contract_type_id": es_contract_type_id,
            }
    
    effective_on: MetaOapg.properties.effective_on
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_on"]) -> MetaOapg.properties.effective_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_id"]) -> MetaOapg.properties.employee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starts_on"]) -> MetaOapg.properties.starts_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ends_on"]) -> MetaOapg.properties.ends_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["working_hours_frequency"]) -> MetaOapg.properties.working_hours_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["working_week_days"]) -> MetaOapg.properties.working_week_days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["working_hours"]) -> MetaOapg.properties.working_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary_frequency"]) -> MetaOapg.properties.salary_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary_amount"]) -> MetaOapg.properties.salary_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["es_cotization_group"]) -> MetaOapg.properties.es_cotization_group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["es_professional_category_id"]) -> MetaOapg.properties.es_professional_category_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["es_education_level_id"]) -> MetaOapg.properties.es_education_level_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["es_contract_type_id"]) -> MetaOapg.properties.es_contract_type_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["effective_on", "employee_id", "starts_on", "ends_on", "working_hours_frequency", "working_week_days", "working_hours", "salary_frequency", "salary_amount", "job_title", "es_cotization_group", "es_professional_category_id", "es_education_level_id", "es_contract_type_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_on"]) -> MetaOapg.properties.effective_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_id"]) -> typing.Union[MetaOapg.properties.employee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starts_on"]) -> typing.Union[MetaOapg.properties.starts_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ends_on"]) -> typing.Union[MetaOapg.properties.ends_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["working_hours_frequency"]) -> typing.Union[MetaOapg.properties.working_hours_frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["working_week_days"]) -> typing.Union[MetaOapg.properties.working_week_days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["working_hours"]) -> typing.Union[MetaOapg.properties.working_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary_frequency"]) -> typing.Union[MetaOapg.properties.salary_frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary_amount"]) -> typing.Union[MetaOapg.properties.salary_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title"]) -> typing.Union[MetaOapg.properties.job_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["es_cotization_group"]) -> typing.Union[MetaOapg.properties.es_cotization_group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["es_professional_category_id"]) -> typing.Union[MetaOapg.properties.es_professional_category_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["es_education_level_id"]) -> typing.Union[MetaOapg.properties.es_education_level_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["es_contract_type_id"]) -> typing.Union[MetaOapg.properties.es_contract_type_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["effective_on", "employee_id", "starts_on", "ends_on", "working_hours_frequency", "working_week_days", "working_hours", "salary_frequency", "salary_amount", "job_title", "es_cotization_group", "es_professional_category_id", "es_education_level_id", "es_contract_type_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        effective_on: typing.Union[MetaOapg.properties.effective_on, str, ],
        employee_id: typing.Union[MetaOapg.properties.employee_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        starts_on: typing.Union[MetaOapg.properties.starts_on, str, schemas.Unset] = schemas.unset,
        ends_on: typing.Union[MetaOapg.properties.ends_on, str, schemas.Unset] = schemas.unset,
        working_hours_frequency: typing.Union[MetaOapg.properties.working_hours_frequency, str, schemas.Unset] = schemas.unset,
        working_week_days: typing.Union[MetaOapg.properties.working_week_days, str, schemas.Unset] = schemas.unset,
        working_hours: typing.Union[MetaOapg.properties.working_hours, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        salary_frequency: typing.Union[MetaOapg.properties.salary_frequency, str, schemas.Unset] = schemas.unset,
        salary_amount: typing.Union[MetaOapg.properties.salary_amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        job_title: typing.Union[MetaOapg.properties.job_title, str, schemas.Unset] = schemas.unset,
        es_cotization_group: typing.Union[MetaOapg.properties.es_cotization_group, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        es_professional_category_id: typing.Union[MetaOapg.properties.es_professional_category_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        es_education_level_id: typing.Union[MetaOapg.properties.es_education_level_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        es_contract_type_id: typing.Union[MetaOapg.properties.es_contract_type_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractUpdateVersionRequest':
        return super().__new__(
            cls,
            *args,
            effective_on=effective_on,
            employee_id=employee_id,
            starts_on=starts_on,
            ends_on=ends_on,
            working_hours_frequency=working_hours_frequency,
            working_week_days=working_week_days,
            working_hours=working_hours,
            salary_frequency=salary_frequency,
            salary_amount=salary_amount,
            job_title=job_title,
            es_cotization_group=es_cotization_group,
            es_professional_category_id=es_professional_category_id,
            es_education_level_id=es_education_level_id,
            es_contract_type_id=es_contract_type_id,
            _configuration=_configuration,
            **kwargs,
        )
