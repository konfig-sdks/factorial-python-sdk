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


class ApplicationUpdateDataRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            ats_application_phase_id = schemas.IntSchema
            qualified = schemas.BoolSchema
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            phone = schemas.StrSchema
            email = schemas.StrSchema
            personal_url = schemas.StrSchema
            
            
            class disqualified_reason(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "not_a_fit": "NOT_A_FIT",
                        "self_disqualified": "SELF_DISQUALIFIED",
                        "salary": "SALARY",
                        "other_reason": "OTHER_REASON",
                        "underqualified": "UNDERQUALIFIED",
                        "offer_not_accepted": "OFFER_NOT_ACCEPTED",
                        "other_offer": "OTHER_OFFER",
                        "no_response": "NO_RESPONSE",
                    }
                
                @schemas.classproperty
                def NOT_A_FIT(cls):
                    return cls("not_a_fit")
                
                @schemas.classproperty
                def SELF_DISQUALIFIED(cls):
                    return cls("self_disqualified")
                
                @schemas.classproperty
                def SALARY(cls):
                    return cls("salary")
                
                @schemas.classproperty
                def OTHER_REASON(cls):
                    return cls("other_reason")
                
                @schemas.classproperty
                def UNDERQUALIFIED(cls):
                    return cls("underqualified")
                
                @schemas.classproperty
                def OFFER_NOT_ACCEPTED(cls):
                    return cls("offer_not_accepted")
                
                @schemas.classproperty
                def OTHER_OFFER(cls):
                    return cls("other_offer")
                
                @schemas.classproperty
                def NO_RESPONSE(cls):
                    return cls("no_response")
            cv = schemas.BinarySchema
            photo = schemas.BinarySchema
            __annotations__ = {
                "ats_application_phase_id": ats_application_phase_id,
                "qualified": qualified,
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "email": email,
                "personal_url": personal_url,
                "disqualified_reason": disqualified_reason,
                "cv": cv,
                "photo": photo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ats_application_phase_id"]) -> MetaOapg.properties.ats_application_phase_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qualified"]) -> MetaOapg.properties.qualified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_url"]) -> MetaOapg.properties.personal_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disqualified_reason"]) -> MetaOapg.properties.disqualified_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cv"]) -> MetaOapg.properties.cv: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photo"]) -> MetaOapg.properties.photo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ats_application_phase_id", "qualified", "first_name", "last_name", "phone", "email", "personal_url", "disqualified_reason", "cv", "photo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ats_application_phase_id"]) -> typing.Union[MetaOapg.properties.ats_application_phase_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qualified"]) -> typing.Union[MetaOapg.properties.qualified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_url"]) -> typing.Union[MetaOapg.properties.personal_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disqualified_reason"]) -> typing.Union[MetaOapg.properties.disqualified_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cv"]) -> typing.Union[MetaOapg.properties.cv, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photo"]) -> typing.Union[MetaOapg.properties.photo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ats_application_phase_id", "qualified", "first_name", "last_name", "phone", "email", "personal_url", "disqualified_reason", "cv", "photo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ats_application_phase_id: typing.Union[MetaOapg.properties.ats_application_phase_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        qualified: typing.Union[MetaOapg.properties.qualified, bool, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        personal_url: typing.Union[MetaOapg.properties.personal_url, str, schemas.Unset] = schemas.unset,
        disqualified_reason: typing.Union[MetaOapg.properties.disqualified_reason, str, schemas.Unset] = schemas.unset,
        cv: typing.Union[MetaOapg.properties.cv, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        photo: typing.Union[MetaOapg.properties.photo, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationUpdateDataRequest':
        return super().__new__(
            cls,
            *args,
            ats_application_phase_id=ats_application_phase_id,
            qualified=qualified,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            personal_url=personal_url,
            disqualified_reason=disqualified_reason,
            cv=cv,
            photo=photo,
            _configuration=_configuration,
            **kwargs,
        )
