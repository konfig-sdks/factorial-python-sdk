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


class CustomFieldCreateFieldRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "visible",
            "editable",
            "slug_name",
            "label",
            "field_type",
            "required",
        }
        
        class properties:
            label = schemas.StrSchema
            slug_name = schemas.StrSchema
            
            
            class field_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("text")
                
                @schemas.classproperty
                def LONG_TEXT(cls):
                    return cls("long_text")
                
                @schemas.classproperty
                def NUMBER(cls):
                    return cls("number")
                
                @schemas.classproperty
                def SINGLE_CHOICE(cls):
                    return cls("single_choice")
            required = schemas.BoolSchema
            
            
            class editable(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OWNED(cls):
                    return cls("owned")
                
                @schemas.classproperty
                def REPORTEES(cls):
                    return cls("reportees")
                
                @schemas.classproperty
                def TEAM_LEADER(cls):
                    return cls("team_leader")
                
                @schemas.classproperty
                def EVERYBODY(cls):
                    return cls("everybody")
            
            
            class visible(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OWNED(cls):
                    return cls("owned")
                
                @schemas.classproperty
                def REPORTEES(cls):
                    return cls("reportees")
                
                @schemas.classproperty
                def TEAM_LEADER(cls):
                    return cls("team_leader")
                
                @schemas.classproperty
                def EVERYBODY(cls):
                    return cls("everybody")
            min_value = schemas.IntSchema
            max_value = schemas.IntSchema
        
            @staticmethod
            def choice_options() -> typing.Type['CustomFieldCreateFieldRequestChoiceOptions']:
                return CustomFieldCreateFieldRequestChoiceOptions
            __annotations__ = {
                "label": label,
                "slug_name": slug_name,
                "field_type": field_type,
                "required": required,
                "editable": editable,
                "visible": visible,
                "min_value": min_value,
                "max_value": max_value,
                "choice_options": choice_options,
            }
    
    visible: MetaOapg.properties.visible
    editable: MetaOapg.properties.editable
    slug_name: MetaOapg.properties.slug_name
    label: MetaOapg.properties.label
    field_type: MetaOapg.properties.field_type
    required: MetaOapg.properties.required
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug_name"]) -> MetaOapg.properties.slug_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_type"]) -> MetaOapg.properties.field_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editable"]) -> MetaOapg.properties.editable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visible"]) -> MetaOapg.properties.visible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_value"]) -> MetaOapg.properties.min_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_value"]) -> MetaOapg.properties.max_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["choice_options"]) -> 'CustomFieldCreateFieldRequestChoiceOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["label", "slug_name", "field_type", "required", "editable", "visible", "min_value", "max_value", "choice_options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug_name"]) -> MetaOapg.properties.slug_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_type"]) -> MetaOapg.properties.field_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editable"]) -> MetaOapg.properties.editable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visible"]) -> MetaOapg.properties.visible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_value"]) -> typing.Union[MetaOapg.properties.min_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_value"]) -> typing.Union[MetaOapg.properties.max_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["choice_options"]) -> typing.Union['CustomFieldCreateFieldRequestChoiceOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["label", "slug_name", "field_type", "required", "editable", "visible", "min_value", "max_value", "choice_options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        visible: typing.Union[MetaOapg.properties.visible, str, ],
        editable: typing.Union[MetaOapg.properties.editable, str, ],
        slug_name: typing.Union[MetaOapg.properties.slug_name, str, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        field_type: typing.Union[MetaOapg.properties.field_type, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, ],
        min_value: typing.Union[MetaOapg.properties.min_value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_value: typing.Union[MetaOapg.properties.max_value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        choice_options: typing.Union['CustomFieldCreateFieldRequestChoiceOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldCreateFieldRequest':
        return super().__new__(
            cls,
            *args,
            visible=visible,
            editable=editable,
            slug_name=slug_name,
            label=label,
            field_type=field_type,
            required=required,
            min_value=min_value,
            max_value=max_value,
            choice_options=choice_options,
            _configuration=_configuration,
            **kwargs,
        )

from factorial_python_sdk.model.custom_field_create_field_request_choice_options import CustomFieldCreateFieldRequestChoiceOptions