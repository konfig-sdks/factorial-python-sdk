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


class Attendance(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            employee_id = schemas.IntSchema
            clock_in = schemas.StrSchema
            clock_out = schemas.StrSchema
            observations = schemas.StrSchema
            
            
            class location_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "office": "OFFICE",
                        "business_trip": "BUSINESS_TRIP",
                        "work_from_home": "WORK_FROM_HOME",
                    }
                
                @schemas.classproperty
                def OFFICE(cls):
                    return cls("office")
                
                @schemas.classproperty
                def BUSINESS_TRIP(cls):
                    return cls("business_trip")
                
                @schemas.classproperty
                def WORK_FROM_HOME(cls):
                    return cls("work_from_home")
            
            
            class half_day(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "beginning_of_day": "BEGINNING_OF_DAY",
                        "end_of_day": "END_OF_DAY",
                    }
                
                @schemas.classproperty
                def BEGINNING_OF_DAY(cls):
                    return cls("beginning_of_day")
                
                @schemas.classproperty
                def END_OF_DAY(cls):
                    return cls("end_of_day")
            in_location_latitude = schemas.Float32Schema
            in_location_longitude = schemas.Float32Schema
            in_location_accuracy = schemas.Float32Schema
            out_location_latitude = schemas.Float32Schema
            out_location_longitude = schemas.Float32Schema
            out_location_accuracy = schemas.Float32Schema
            workable = schemas.BoolSchema
            automatic_clock_in = schemas.BoolSchema
            automatic_clock_out = schemas.BoolSchema
            
            
            class time_settings_break_configuration_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'time_settings_break_configuration_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "employee_id": employee_id,
                "clock_in": clock_in,
                "clock_out": clock_out,
                "observations": observations,
                "location_type": location_type,
                "half_day": half_day,
                "in_location_latitude": in_location_latitude,
                "in_location_longitude": in_location_longitude,
                "in_location_accuracy": in_location_accuracy,
                "out_location_latitude": out_location_latitude,
                "out_location_longitude": out_location_longitude,
                "out_location_accuracy": out_location_accuracy,
                "workable": workable,
                "automatic_clock_in": automatic_clock_in,
                "automatic_clock_out": automatic_clock_out,
                "time_settings_break_configuration_id": time_settings_break_configuration_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_id"]) -> MetaOapg.properties.employee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clock_in"]) -> MetaOapg.properties.clock_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clock_out"]) -> MetaOapg.properties.clock_out: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["observations"]) -> MetaOapg.properties.observations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_type"]) -> MetaOapg.properties.location_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["half_day"]) -> MetaOapg.properties.half_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in_location_latitude"]) -> MetaOapg.properties.in_location_latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in_location_longitude"]) -> MetaOapg.properties.in_location_longitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in_location_accuracy"]) -> MetaOapg.properties.in_location_accuracy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["out_location_latitude"]) -> MetaOapg.properties.out_location_latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["out_location_longitude"]) -> MetaOapg.properties.out_location_longitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["out_location_accuracy"]) -> MetaOapg.properties.out_location_accuracy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workable"]) -> MetaOapg.properties.workable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["automatic_clock_in"]) -> MetaOapg.properties.automatic_clock_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["automatic_clock_out"]) -> MetaOapg.properties.automatic_clock_out: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_settings_break_configuration_id"]) -> MetaOapg.properties.time_settings_break_configuration_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "employee_id", "clock_in", "clock_out", "observations", "location_type", "half_day", "in_location_latitude", "in_location_longitude", "in_location_accuracy", "out_location_latitude", "out_location_longitude", "out_location_accuracy", "workable", "automatic_clock_in", "automatic_clock_out", "time_settings_break_configuration_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_id"]) -> typing.Union[MetaOapg.properties.employee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clock_in"]) -> typing.Union[MetaOapg.properties.clock_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clock_out"]) -> typing.Union[MetaOapg.properties.clock_out, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["observations"]) -> typing.Union[MetaOapg.properties.observations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_type"]) -> typing.Union[MetaOapg.properties.location_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["half_day"]) -> typing.Union[MetaOapg.properties.half_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in_location_latitude"]) -> typing.Union[MetaOapg.properties.in_location_latitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in_location_longitude"]) -> typing.Union[MetaOapg.properties.in_location_longitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in_location_accuracy"]) -> typing.Union[MetaOapg.properties.in_location_accuracy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["out_location_latitude"]) -> typing.Union[MetaOapg.properties.out_location_latitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["out_location_longitude"]) -> typing.Union[MetaOapg.properties.out_location_longitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["out_location_accuracy"]) -> typing.Union[MetaOapg.properties.out_location_accuracy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workable"]) -> typing.Union[MetaOapg.properties.workable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["automatic_clock_in"]) -> typing.Union[MetaOapg.properties.automatic_clock_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["automatic_clock_out"]) -> typing.Union[MetaOapg.properties.automatic_clock_out, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_settings_break_configuration_id"]) -> typing.Union[MetaOapg.properties.time_settings_break_configuration_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "employee_id", "clock_in", "clock_out", "observations", "location_type", "half_day", "in_location_latitude", "in_location_longitude", "in_location_accuracy", "out_location_latitude", "out_location_longitude", "out_location_accuracy", "workable", "automatic_clock_in", "automatic_clock_out", "time_settings_break_configuration_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        employee_id: typing.Union[MetaOapg.properties.employee_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        clock_in: typing.Union[MetaOapg.properties.clock_in, str, schemas.Unset] = schemas.unset,
        clock_out: typing.Union[MetaOapg.properties.clock_out, str, schemas.Unset] = schemas.unset,
        observations: typing.Union[MetaOapg.properties.observations, str, schemas.Unset] = schemas.unset,
        location_type: typing.Union[MetaOapg.properties.location_type, str, schemas.Unset] = schemas.unset,
        half_day: typing.Union[MetaOapg.properties.half_day, str, schemas.Unset] = schemas.unset,
        in_location_latitude: typing.Union[MetaOapg.properties.in_location_latitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        in_location_longitude: typing.Union[MetaOapg.properties.in_location_longitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        in_location_accuracy: typing.Union[MetaOapg.properties.in_location_accuracy, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        out_location_latitude: typing.Union[MetaOapg.properties.out_location_latitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        out_location_longitude: typing.Union[MetaOapg.properties.out_location_longitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        out_location_accuracy: typing.Union[MetaOapg.properties.out_location_accuracy, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        workable: typing.Union[MetaOapg.properties.workable, bool, schemas.Unset] = schemas.unset,
        automatic_clock_in: typing.Union[MetaOapg.properties.automatic_clock_in, bool, schemas.Unset] = schemas.unset,
        automatic_clock_out: typing.Union[MetaOapg.properties.automatic_clock_out, bool, schemas.Unset] = schemas.unset,
        time_settings_break_configuration_id: typing.Union[MetaOapg.properties.time_settings_break_configuration_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Attendance':
        return super().__new__(
            cls,
            *args,
            id=id,
            employee_id=employee_id,
            clock_in=clock_in,
            clock_out=clock_out,
            observations=observations,
            location_type=location_type,
            half_day=half_day,
            in_location_latitude=in_location_latitude,
            in_location_longitude=in_location_longitude,
            in_location_accuracy=in_location_accuracy,
            out_location_latitude=out_location_latitude,
            out_location_longitude=out_location_longitude,
            out_location_accuracy=out_location_accuracy,
            workable=workable,
            automatic_clock_in=automatic_clock_in,
            automatic_clock_out=automatic_clock_out,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            _configuration=_configuration,
            **kwargs,
        )
