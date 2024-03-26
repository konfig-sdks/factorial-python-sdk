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


class EmployeeUpdateEmployeeByIdRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            email = schemas.StrSchema
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            birthday_on = schemas.StrSchema
            
            
            class role(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "basic": "BASIC",
                        "admin": "ADMIN",
                    }
                
                @schemas.classproperty
                def BASIC(cls):
                    return cls("basic")
                
                @schemas.classproperty
                def ADMIN(cls):
                    return cls("admin")
            
            
            class gender(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "male": "MALE",
                        "female": "FEMALE",
                    }
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
            identifier = schemas.StrSchema
            
            
            class identifier_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "dni": "DNI",
                        "nie": "NIE",
                        "passport": "PASSPORT",
                    }
                
                @schemas.classproperty
                def DNI(cls):
                    return cls("dni")
                
                @schemas.classproperty
                def NIE(cls):
                    return cls("nie")
                
                @schemas.classproperty
                def PASSPORT(cls):
                    return cls("passport")
            nationality = schemas.StrSchema
            bank_number = schemas.StrSchema
            country = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            postal_code = schemas.StrSchema
            address_line_1 = schemas.StrSchema
            address_line_2 = schemas.StrSchema
            swift_bic = schemas.StrSchema
            manager_id = schemas.IntSchema
            location_id = schemas.IntSchema
            timeoff_manager_id = schemas.IntSchema
            phone_number = schemas.StrSchema
            social_security_number = schemas.IntSchema
            legal_entity_id = schemas.IntSchema
            company_identifier = schemas.StrSchema
            contact_name = schemas.StrSchema
            contact_number = schemas.StrSchema
            tax_id = schemas.StrSchema
            __annotations__ = {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "birthday_on": birthday_on,
                "role": role,
                "gender": gender,
                "identifier": identifier,
                "identifier_type": identifier_type,
                "nationality": nationality,
                "bank_number": bank_number,
                "country": country,
                "city": city,
                "state": state,
                "postal_code": postal_code,
                "address_line_1": address_line_1,
                "address_line_2": address_line_2,
                "swift_bic": swift_bic,
                "manager_id": manager_id,
                "location_id": location_id,
                "timeoff_manager_id": timeoff_manager_id,
                "phone_number": phone_number,
                "social_security_number": social_security_number,
                "legal_entity_id": legal_entity_id,
                "company_identifier": company_identifier,
                "contact_name": contact_name,
                "contact_number": contact_number,
                "tax_id": tax_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthday_on"]) -> MetaOapg.properties.birthday_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifier_type"]) -> MetaOapg.properties.identifier_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationality"]) -> MetaOapg.properties.nationality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_number"]) -> MetaOapg.properties.bank_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postal_code"]) -> MetaOapg.properties.postal_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_line_1"]) -> MetaOapg.properties.address_line_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_line_2"]) -> MetaOapg.properties.address_line_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["swift_bic"]) -> MetaOapg.properties.swift_bic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manager_id"]) -> MetaOapg.properties.manager_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeoff_manager_id"]) -> MetaOapg.properties.timeoff_manager_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_security_number"]) -> MetaOapg.properties.social_security_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal_entity_id"]) -> MetaOapg.properties.legal_entity_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_identifier"]) -> MetaOapg.properties.company_identifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_name"]) -> MetaOapg.properties.contact_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_number"]) -> MetaOapg.properties.contact_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_id"]) -> MetaOapg.properties.tax_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "first_name", "last_name", "birthday_on", "role", "gender", "identifier", "identifier_type", "nationality", "bank_number", "country", "city", "state", "postal_code", "address_line_1", "address_line_2", "swift_bic", "manager_id", "location_id", "timeoff_manager_id", "phone_number", "social_security_number", "legal_entity_id", "company_identifier", "contact_name", "contact_number", "tax_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthday_on"]) -> typing.Union[MetaOapg.properties.birthday_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifier"]) -> typing.Union[MetaOapg.properties.identifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifier_type"]) -> typing.Union[MetaOapg.properties.identifier_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationality"]) -> typing.Union[MetaOapg.properties.nationality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_number"]) -> typing.Union[MetaOapg.properties.bank_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postal_code"]) -> typing.Union[MetaOapg.properties.postal_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_line_1"]) -> typing.Union[MetaOapg.properties.address_line_1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_line_2"]) -> typing.Union[MetaOapg.properties.address_line_2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["swift_bic"]) -> typing.Union[MetaOapg.properties.swift_bic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manager_id"]) -> typing.Union[MetaOapg.properties.manager_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> typing.Union[MetaOapg.properties.location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeoff_manager_id"]) -> typing.Union[MetaOapg.properties.timeoff_manager_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_security_number"]) -> typing.Union[MetaOapg.properties.social_security_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal_entity_id"]) -> typing.Union[MetaOapg.properties.legal_entity_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_identifier"]) -> typing.Union[MetaOapg.properties.company_identifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_name"]) -> typing.Union[MetaOapg.properties.contact_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_number"]) -> typing.Union[MetaOapg.properties.contact_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_id"]) -> typing.Union[MetaOapg.properties.tax_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "first_name", "last_name", "birthday_on", "role", "gender", "identifier", "identifier_type", "nationality", "bank_number", "country", "city", "state", "postal_code", "address_line_1", "address_line_2", "swift_bic", "manager_id", "location_id", "timeoff_manager_id", "phone_number", "social_security_number", "legal_entity_id", "company_identifier", "contact_name", "contact_number", "tax_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        birthday_on: typing.Union[MetaOapg.properties.birthday_on, str, schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        identifier: typing.Union[MetaOapg.properties.identifier, str, schemas.Unset] = schemas.unset,
        identifier_type: typing.Union[MetaOapg.properties.identifier_type, str, schemas.Unset] = schemas.unset,
        nationality: typing.Union[MetaOapg.properties.nationality, str, schemas.Unset] = schemas.unset,
        bank_number: typing.Union[MetaOapg.properties.bank_number, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        postal_code: typing.Union[MetaOapg.properties.postal_code, str, schemas.Unset] = schemas.unset,
        address_line_1: typing.Union[MetaOapg.properties.address_line_1, str, schemas.Unset] = schemas.unset,
        address_line_2: typing.Union[MetaOapg.properties.address_line_2, str, schemas.Unset] = schemas.unset,
        swift_bic: typing.Union[MetaOapg.properties.swift_bic, str, schemas.Unset] = schemas.unset,
        manager_id: typing.Union[MetaOapg.properties.manager_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        timeoff_manager_id: typing.Union[MetaOapg.properties.timeoff_manager_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, schemas.Unset] = schemas.unset,
        social_security_number: typing.Union[MetaOapg.properties.social_security_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        legal_entity_id: typing.Union[MetaOapg.properties.legal_entity_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        company_identifier: typing.Union[MetaOapg.properties.company_identifier, str, schemas.Unset] = schemas.unset,
        contact_name: typing.Union[MetaOapg.properties.contact_name, str, schemas.Unset] = schemas.unset,
        contact_number: typing.Union[MetaOapg.properties.contact_number, str, schemas.Unset] = schemas.unset,
        tax_id: typing.Union[MetaOapg.properties.tax_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeUpdateEmployeeByIdRequest':
        return super().__new__(
            cls,
            *args,
            email=email,
            first_name=first_name,
            last_name=last_name,
            birthday_on=birthday_on,
            role=role,
            gender=gender,
            identifier=identifier,
            identifier_type=identifier_type,
            nationality=nationality,
            bank_number=bank_number,
            country=country,
            city=city,
            state=state,
            postal_code=postal_code,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            swift_bic=swift_bic,
            manager_id=manager_id,
            location_id=location_id,
            timeoff_manager_id=timeoff_manager_id,
            phone_number=phone_number,
            social_security_number=social_security_number,
            legal_entity_id=legal_entity_id,
            company_identifier=company_identifier,
            contact_name=contact_name,
            contact_number=contact_number,
            tax_id=tax_id,
            _configuration=_configuration,
            **kwargs,
        )
