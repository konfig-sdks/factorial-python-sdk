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


class AtsApplication(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            ats_candidate_id = schemas.IntSchema
            ats_job_posting_id = schemas.IntSchema
            ats_application_phase_id = schemas.IntSchema
            ats_application_phase_name = schemas.StrSchema
            ats_application_phase_type = schemas.StrSchema
            ats_job_posting_title = schemas.StrSchema
            conversation_id = schemas.IntSchema
            cover_letter = schemas.StrSchema
        
            @staticmethod
            def cv() -> typing.Type['AtsApplicationCv']:
                return AtsApplicationCv
            photo = schemas.StrSchema
            disqualified_reason = schemas.StrSchema
            email = schemas.StrSchema
            first_name = schemas.StrSchema
            full_name = schemas.StrSchema
            last_name = schemas.StrSchema
            medium = schemas.StrSchema
            personal_url = schemas.StrSchema
            phone = schemas.StrSchema
            qualified = schemas.BoolSchema
            rating_average = schemas.IntSchema
            source = schemas.StrSchema
            talent_pool = schemas.BoolSchema
            created_at = schemas.StrSchema
            
            
            class answers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AtsAnswer']:
                        return AtsAnswer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AtsAnswer'], typing.List['AtsAnswer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'answers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AtsAnswer':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "ats_candidate_id": ats_candidate_id,
                "ats_job_posting_id": ats_job_posting_id,
                "ats_application_phase_id": ats_application_phase_id,
                "ats_application_phase_name": ats_application_phase_name,
                "ats_application_phase_type": ats_application_phase_type,
                "ats_job_posting_title": ats_job_posting_title,
                "conversation_id": conversation_id,
                "cover_letter": cover_letter,
                "cv": cv,
                "photo": photo,
                "disqualified_reason": disqualified_reason,
                "email": email,
                "first_name": first_name,
                "full_name": full_name,
                "last_name": last_name,
                "medium": medium,
                "personal_url": personal_url,
                "phone": phone,
                "qualified": qualified,
                "rating_average": rating_average,
                "source": source,
                "talent_pool": talent_pool,
                "created_at": created_at,
                "answers": answers,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ats_candidate_id"]) -> MetaOapg.properties.ats_candidate_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ats_job_posting_id"]) -> MetaOapg.properties.ats_job_posting_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ats_application_phase_id"]) -> MetaOapg.properties.ats_application_phase_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ats_application_phase_name"]) -> MetaOapg.properties.ats_application_phase_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ats_application_phase_type"]) -> MetaOapg.properties.ats_application_phase_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ats_job_posting_title"]) -> MetaOapg.properties.ats_job_posting_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation_id"]) -> MetaOapg.properties.conversation_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover_letter"]) -> MetaOapg.properties.cover_letter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cv"]) -> 'AtsApplicationCv': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photo"]) -> MetaOapg.properties.photo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disqualified_reason"]) -> MetaOapg.properties.disqualified_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_name"]) -> MetaOapg.properties.full_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["medium"]) -> MetaOapg.properties.medium: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_url"]) -> MetaOapg.properties.personal_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qualified"]) -> MetaOapg.properties.qualified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_average"]) -> MetaOapg.properties.rating_average: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["talent_pool"]) -> MetaOapg.properties.talent_pool: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answers"]) -> MetaOapg.properties.answers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "ats_candidate_id", "ats_job_posting_id", "ats_application_phase_id", "ats_application_phase_name", "ats_application_phase_type", "ats_job_posting_title", "conversation_id", "cover_letter", "cv", "photo", "disqualified_reason", "email", "first_name", "full_name", "last_name", "medium", "personal_url", "phone", "qualified", "rating_average", "source", "talent_pool", "created_at", "answers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ats_candidate_id"]) -> typing.Union[MetaOapg.properties.ats_candidate_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ats_job_posting_id"]) -> typing.Union[MetaOapg.properties.ats_job_posting_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ats_application_phase_id"]) -> typing.Union[MetaOapg.properties.ats_application_phase_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ats_application_phase_name"]) -> typing.Union[MetaOapg.properties.ats_application_phase_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ats_application_phase_type"]) -> typing.Union[MetaOapg.properties.ats_application_phase_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ats_job_posting_title"]) -> typing.Union[MetaOapg.properties.ats_job_posting_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation_id"]) -> typing.Union[MetaOapg.properties.conversation_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover_letter"]) -> typing.Union[MetaOapg.properties.cover_letter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cv"]) -> typing.Union['AtsApplicationCv', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photo"]) -> typing.Union[MetaOapg.properties.photo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disqualified_reason"]) -> typing.Union[MetaOapg.properties.disqualified_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_name"]) -> typing.Union[MetaOapg.properties.full_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["medium"]) -> typing.Union[MetaOapg.properties.medium, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_url"]) -> typing.Union[MetaOapg.properties.personal_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qualified"]) -> typing.Union[MetaOapg.properties.qualified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_average"]) -> typing.Union[MetaOapg.properties.rating_average, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["talent_pool"]) -> typing.Union[MetaOapg.properties.talent_pool, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answers"]) -> typing.Union[MetaOapg.properties.answers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "ats_candidate_id", "ats_job_posting_id", "ats_application_phase_id", "ats_application_phase_name", "ats_application_phase_type", "ats_job_posting_title", "conversation_id", "cover_letter", "cv", "photo", "disqualified_reason", "email", "first_name", "full_name", "last_name", "medium", "personal_url", "phone", "qualified", "rating_average", "source", "talent_pool", "created_at", "answers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ats_candidate_id: typing.Union[MetaOapg.properties.ats_candidate_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ats_job_posting_id: typing.Union[MetaOapg.properties.ats_job_posting_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ats_application_phase_id: typing.Union[MetaOapg.properties.ats_application_phase_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ats_application_phase_name: typing.Union[MetaOapg.properties.ats_application_phase_name, str, schemas.Unset] = schemas.unset,
        ats_application_phase_type: typing.Union[MetaOapg.properties.ats_application_phase_type, str, schemas.Unset] = schemas.unset,
        ats_job_posting_title: typing.Union[MetaOapg.properties.ats_job_posting_title, str, schemas.Unset] = schemas.unset,
        conversation_id: typing.Union[MetaOapg.properties.conversation_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cover_letter: typing.Union[MetaOapg.properties.cover_letter, str, schemas.Unset] = schemas.unset,
        cv: typing.Union['AtsApplicationCv', schemas.Unset] = schemas.unset,
        photo: typing.Union[MetaOapg.properties.photo, str, schemas.Unset] = schemas.unset,
        disqualified_reason: typing.Union[MetaOapg.properties.disqualified_reason, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        full_name: typing.Union[MetaOapg.properties.full_name, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        medium: typing.Union[MetaOapg.properties.medium, str, schemas.Unset] = schemas.unset,
        personal_url: typing.Union[MetaOapg.properties.personal_url, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        qualified: typing.Union[MetaOapg.properties.qualified, bool, schemas.Unset] = schemas.unset,
        rating_average: typing.Union[MetaOapg.properties.rating_average, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        talent_pool: typing.Union[MetaOapg.properties.talent_pool, bool, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        answers: typing.Union[MetaOapg.properties.answers, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AtsApplication':
        return super().__new__(
            cls,
            *args,
            id=id,
            ats_candidate_id=ats_candidate_id,
            ats_job_posting_id=ats_job_posting_id,
            ats_application_phase_id=ats_application_phase_id,
            ats_application_phase_name=ats_application_phase_name,
            ats_application_phase_type=ats_application_phase_type,
            ats_job_posting_title=ats_job_posting_title,
            conversation_id=conversation_id,
            cover_letter=cover_letter,
            cv=cv,
            photo=photo,
            disqualified_reason=disqualified_reason,
            email=email,
            first_name=first_name,
            full_name=full_name,
            last_name=last_name,
            medium=medium,
            personal_url=personal_url,
            phone=phone,
            qualified=qualified,
            rating_average=rating_average,
            source=source,
            talent_pool=talent_pool,
            created_at=created_at,
            answers=answers,
            _configuration=_configuration,
            **kwargs,
        )

from factorial_python_sdk.model.ats_answer import AtsAnswer
from factorial_python_sdk.model.ats_application_cv import AtsApplicationCv
