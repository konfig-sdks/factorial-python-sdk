# coding: utf-8

"""
    Factorial API

    Open Api Specifications available at [https://github.com/factorialco/oas](https://github.com/factorialco/oasLooking)  Guides and support available at [https://help.factorialhr.com/integrations](https://help.factorialhr.com/integrations)  # Authentication  The public API provides two methods of authentication, ApiKeys and OAuth2. The following sections provide information regarding each one and their intent.  ## OAuth2  > OAuth2 is used to identify individual users, not applications or platforms.  OAuth2 is available for authenticating to the public API and making requests via third parties **on behalf of a user**. All actions are authored on behalf of the user that creates the token. This means the intent is to be used mainly to do submit actions the actual user is performing on an alternative interface.  To generate a token you will require opening an authorization dialog that returns a code, this code can then be exchanged for a token.  ### Configuration  In order to create an OAuth application, you must be an admin, head over to your [personal repository of OAuth applications](https://api.factorialhr.com/oauth/applications), click on `New application` and follow the creation process.  The Factorial API enforces the same permissions at the user level than the Factorial web application. This means that Factorial API users will only be able to perform the same actions they are allowed to do in the Factorial platform.  Next step will be to generate the Authorization Code you will need in order to generate an OAuth2 Token.  ### OAuth2 Code Generation  Should be generated via browser by opening the following url. The user should be already logged in to Factorial beforehand.  `https://api.factorialhr.com/oauth/authorize?client_id=&redirect_uri=&response_type=code&scope=`  YOUR_CLIENT_ID: OAuth2 Application Id REDIRECT_URI: OAuth2 Redirect URL  #### State Parameter  An optional query parameter called `state` can be added to the code generation url. Any string can be used and will be sent on the callback url.  > Authorization protocols provide a `state` parameter that allows you to restore the previous state of your application. The `state` parameter preserves some state objects set by the client in the Authorization request and makes it available to the client in the response.  ### OAuth2 Token Generation  Once you have the authorization code, you can request their access token to Factorial.  `curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&code=&grant_type=authorization_code&redirect_uri='`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret AUTHORIZATION_CODE: OAuth2 CODE REDIRECT_URI: OAuth2 Redirect URL  > You can generate only one OAuth2 token per Code, that means that if you want to generate a new token for a Code that already have one you should refresh your token.  Every time a new token is generated a refresh token is generated as well, so that you can use it on the OAuth2 Refresh Token, and an expire date is also provided.  ### OAuth2 Refresh Token  You can generate a new token under the same Code with a new expire date (you can do it as many times as you need). A refresh token is also returned here so that you can use it on the OAuth2 Refresh Token again.  `curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&refresh_token=&grant_type=refresh_token'`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret REFRESH_TOKEN: OAuth2 Refresh Token  ### OAuth2 Revoke Token  You can revoke an access/refresh token if you do not want it to be active anylonger. This can happen in cases where you have refreshed your token and would like to revoke the previous token if you haven't used the new token yet, as using the new token automatically revokes the previous one.  `curl -X POST 'https://api.factorialhr.com/oauth/revoke' -d 'client_id=&client_secret=&token='`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret TOKEN: OAuth2 Access/Refresh Token (whichever you wish to revoke)  ### OAuth2 Token Usage  The generated token is the credential for performing authenticated requests to Factorial. This token should be included in the Authorization header prefixed with the word Bearer and a separating space. As an example, if your token is `12345` then the header content should be `Bearer 12345`.  ### Maintaining a persistent connection  To maintain a persistent connection, you should not let the token expire. You can avoid this by simply refreshing your token before the expiration date. This will give you another token with a new expiration date, before that token expires you should refresh it again, and so on... If you want to do this automatically, you should provide something in your code that will help you perform the update every time the token expires. Otherwise, you would have to do the update manually and make sure you refresh your token before the expiration date to maintain the connection.  ## ApiKeys  > API keys are used to identify systems, not the individual users that access.  ApiKeys have **TOTAL ACCESS** to everything and never expire. Its the creators responsibility to generate them and store them securely.  ### Generation  In the `Core>Keys` section of this documentation you can access the apis for managing this resource.  ### Usage  ApiKeys are a single string of symbols that must be added as a custom header on the request. The header name must be `x-api-key` and the key must be the value without any prefixes.  ### Disclaimer  ApiKey management require full admin permissions as the resource itself allows for full admin access to the entire platform on behalf of the company and not of a user, therefore any operations are not linked to any user in particular.  # Development  ## SDKs  Coming soon  ## Sandbox  A sandbox/demo environment is available for testing integrations via public API calls. Developers can request provisioning with full access to a demo company where to test code before actually interacting with a production environment.  Contact your account manager or account executive to request this environment and get OAuth2 credentials for generating tokens.  Note: the domain for sandbox is different than that from production. Sandbox base domain is `http://api.demo.factorialhr.com`  ## Postman  Click the \"Run in Postman\" button to open the full list of endpoints on your Postman workspace as a Postman Collection. Inside the collection lookout for the Collection's Variables, configure your variables accordingly.  ### Delegating Token Generation To Postman  Coming soon  # Changelog  Coming soon  # How to...  ## Custom Fields  Custom fields are useful when you want to add some fields that are not the default ones, to every employee of the company.  For that, you have to create via Factorial App the base custom field in order to have all the employees with it. That option is available in customization, inside the company menu  Once you have that, via API, you can [Create a value for a custom field](https://apidoc.factorialhr.com/#72f3f786-e37d-4e80-ada2-0beedd03b171) to each employee. You should know the custom field id in order to make that, you can check it by [getting a collection of custom fields](https://apidoc.factorialhr.com/#f98dae5a-a8d0-474e-a181-7e9603409b42)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from factorial_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from factorial_python_sdk.api_response import AsyncGeneratorResponse
from factorial_python_sdk import api_client, exceptions
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

from factorial_python_sdk.model.leave_create_new_leave_request1 import LeaveCreateNewLeaveRequest1 as LeaveCreateNewLeaveRequest1Schema
from factorial_python_sdk.model.leave import Leave as LeaveSchema

from factorial_python_sdk.type.leave_create_new_leave_request1 import LeaveCreateNewLeaveRequest1
from factorial_python_sdk.type.leave import Leave

from ...api_client import Dictionary
from factorial_python_sdk.pydantic.leave_create_new_leave_request1 import LeaveCreateNewLeaveRequest1 as LeaveCreateNewLeaveRequest1Pydantic
from factorial_python_sdk.pydantic.leave import Leave as LeavePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = LeaveCreateNewLeaveRequest1Schema


request_body_leave_create_new_leave_request1 = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'apikey',
]
SchemaFor201ResponseBodyApplicationJson = LeaveSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Leave


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Leave


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_leave_0_mapped_args(
        self,
        start_on: str,
        finish_on: str,
        employee_id: int,
        description: typing.Optional[str] = None,
        leave_type_id: typing.Optional[int] = None,
        half_day: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        hours_amount_in_cents: typing.Optional[int] = None,
        medical_leave_type: typing.Optional[int] = None,
        effective_on: typing.Optional[str] = None,
        medical_discharge_reason: typing.Optional[str] = None,
        colegiate_number: typing.Optional[int] = None,
        has_previous_relapse: typing.Optional[bool] = None,
        relapse_leave_id: typing.Optional[int] = None,
        relapse_on: typing.Optional[str] = None,
        accident_on: typing.Optional[str] = None,
        paternity_birth_on: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if start_on is not None:
            _body["start_on"] = start_on
        if finish_on is not None:
            _body["finish_on"] = finish_on
        if employee_id is not None:
            _body["employee_id"] = employee_id
        if leave_type_id is not None:
            _body["leave_type_id"] = leave_type_id
        if half_day is not None:
            _body["half_day"] = half_day
        if start_time is not None:
            _body["start_time"] = start_time
        if hours_amount_in_cents is not None:
            _body["hours_amount_in_cents"] = hours_amount_in_cents
        if medical_leave_type is not None:
            _body["medical_leave_type"] = medical_leave_type
        if effective_on is not None:
            _body["effective_on"] = effective_on
        if medical_discharge_reason is not None:
            _body["medical_discharge_reason"] = medical_discharge_reason
        if colegiate_number is not None:
            _body["colegiate_number"] = colegiate_number
        if has_previous_relapse is not None:
            _body["has_previous_relapse"] = has_previous_relapse
        if relapse_leave_id is not None:
            _body["relapse_leave_id"] = relapse_leave_id
        if relapse_on is not None:
            _body["relapse_on"] = relapse_on
        if accident_on is not None:
            _body["accident_on"] = accident_on
        if paternity_birth_on is not None:
            _body["paternity_birth_on"] = paternity_birth_on
        args.body = _body
        return args

    async def _acreate_new_leave_0_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a Leave
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/time/leaves',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_leave_create_new_leave_request1.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_leave_0_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a Leave
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/time/leaves',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_leave_create_new_leave_request1.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewLeave0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_leave_0(
        self,
        start_on: str,
        finish_on: str,
        employee_id: int,
        description: typing.Optional[str] = None,
        leave_type_id: typing.Optional[int] = None,
        half_day: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        hours_amount_in_cents: typing.Optional[int] = None,
        medical_leave_type: typing.Optional[int] = None,
        effective_on: typing.Optional[str] = None,
        medical_discharge_reason: typing.Optional[str] = None,
        colegiate_number: typing.Optional[int] = None,
        has_previous_relapse: typing.Optional[bool] = None,
        relapse_leave_id: typing.Optional[int] = None,
        relapse_on: typing.Optional[str] = None,
        accident_on: typing.Optional[str] = None,
        paternity_birth_on: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_leave_0_mapped_args(
            start_on=start_on,
            finish_on=finish_on,
            employee_id=employee_id,
            description=description,
            leave_type_id=leave_type_id,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            medical_leave_type=medical_leave_type,
            effective_on=effective_on,
            medical_discharge_reason=medical_discharge_reason,
            colegiate_number=colegiate_number,
            has_previous_relapse=has_previous_relapse,
            relapse_leave_id=relapse_leave_id,
            relapse_on=relapse_on,
            accident_on=accident_on,
            paternity_birth_on=paternity_birth_on,
        )
        return await self._acreate_new_leave_0_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_leave_0(
        self,
        start_on: str,
        finish_on: str,
        employee_id: int,
        description: typing.Optional[str] = None,
        leave_type_id: typing.Optional[int] = None,
        half_day: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        hours_amount_in_cents: typing.Optional[int] = None,
        medical_leave_type: typing.Optional[int] = None,
        effective_on: typing.Optional[str] = None,
        medical_discharge_reason: typing.Optional[str] = None,
        colegiate_number: typing.Optional[int] = None,
        has_previous_relapse: typing.Optional[bool] = None,
        relapse_leave_id: typing.Optional[int] = None,
        relapse_on: typing.Optional[str] = None,
        accident_on: typing.Optional[str] = None,
        paternity_birth_on: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_leave_0_mapped_args(
            start_on=start_on,
            finish_on=finish_on,
            employee_id=employee_id,
            description=description,
            leave_type_id=leave_type_id,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            medical_leave_type=medical_leave_type,
            effective_on=effective_on,
            medical_discharge_reason=medical_discharge_reason,
            colegiate_number=colegiate_number,
            has_previous_relapse=has_previous_relapse,
            relapse_leave_id=relapse_leave_id,
            relapse_on=relapse_on,
            accident_on=accident_on,
            paternity_birth_on=paternity_birth_on,
        )
        return self._create_new_leave_0_oapg(
            body=args.body,
        )

class CreateNewLeave0(BaseApi):

    async def acreate_new_leave_0(
        self,
        start_on: str,
        finish_on: str,
        employee_id: int,
        description: typing.Optional[str] = None,
        leave_type_id: typing.Optional[int] = None,
        half_day: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        hours_amount_in_cents: typing.Optional[int] = None,
        medical_leave_type: typing.Optional[int] = None,
        effective_on: typing.Optional[str] = None,
        medical_discharge_reason: typing.Optional[str] = None,
        colegiate_number: typing.Optional[int] = None,
        has_previous_relapse: typing.Optional[bool] = None,
        relapse_leave_id: typing.Optional[int] = None,
        relapse_on: typing.Optional[str] = None,
        accident_on: typing.Optional[str] = None,
        paternity_birth_on: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LeavePydantic:
        raw_response = await self.raw.acreate_new_leave_0(
            start_on=start_on,
            finish_on=finish_on,
            employee_id=employee_id,
            description=description,
            leave_type_id=leave_type_id,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            medical_leave_type=medical_leave_type,
            effective_on=effective_on,
            medical_discharge_reason=medical_discharge_reason,
            colegiate_number=colegiate_number,
            has_previous_relapse=has_previous_relapse,
            relapse_leave_id=relapse_leave_id,
            relapse_on=relapse_on,
            accident_on=accident_on,
            paternity_birth_on=paternity_birth_on,
            **kwargs,
        )
        if validate:
            return LeavePydantic(**raw_response.body)
        return api_client.construct_model_instance(LeavePydantic, raw_response.body)
    
    
    def create_new_leave_0(
        self,
        start_on: str,
        finish_on: str,
        employee_id: int,
        description: typing.Optional[str] = None,
        leave_type_id: typing.Optional[int] = None,
        half_day: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        hours_amount_in_cents: typing.Optional[int] = None,
        medical_leave_type: typing.Optional[int] = None,
        effective_on: typing.Optional[str] = None,
        medical_discharge_reason: typing.Optional[str] = None,
        colegiate_number: typing.Optional[int] = None,
        has_previous_relapse: typing.Optional[bool] = None,
        relapse_leave_id: typing.Optional[int] = None,
        relapse_on: typing.Optional[str] = None,
        accident_on: typing.Optional[str] = None,
        paternity_birth_on: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LeavePydantic:
        raw_response = self.raw.create_new_leave_0(
            start_on=start_on,
            finish_on=finish_on,
            employee_id=employee_id,
            description=description,
            leave_type_id=leave_type_id,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            medical_leave_type=medical_leave_type,
            effective_on=effective_on,
            medical_discharge_reason=medical_discharge_reason,
            colegiate_number=colegiate_number,
            has_previous_relapse=has_previous_relapse,
            relapse_leave_id=relapse_leave_id,
            relapse_on=relapse_on,
            accident_on=accident_on,
            paternity_birth_on=paternity_birth_on,
        )
        if validate:
            return LeavePydantic(**raw_response.body)
        return api_client.construct_model_instance(LeavePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        start_on: str,
        finish_on: str,
        employee_id: int,
        description: typing.Optional[str] = None,
        leave_type_id: typing.Optional[int] = None,
        half_day: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        hours_amount_in_cents: typing.Optional[int] = None,
        medical_leave_type: typing.Optional[int] = None,
        effective_on: typing.Optional[str] = None,
        medical_discharge_reason: typing.Optional[str] = None,
        colegiate_number: typing.Optional[int] = None,
        has_previous_relapse: typing.Optional[bool] = None,
        relapse_leave_id: typing.Optional[int] = None,
        relapse_on: typing.Optional[str] = None,
        accident_on: typing.Optional[str] = None,
        paternity_birth_on: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_leave_0_mapped_args(
            start_on=start_on,
            finish_on=finish_on,
            employee_id=employee_id,
            description=description,
            leave_type_id=leave_type_id,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            medical_leave_type=medical_leave_type,
            effective_on=effective_on,
            medical_discharge_reason=medical_discharge_reason,
            colegiate_number=colegiate_number,
            has_previous_relapse=has_previous_relapse,
            relapse_leave_id=relapse_leave_id,
            relapse_on=relapse_on,
            accident_on=accident_on,
            paternity_birth_on=paternity_birth_on,
        )
        return await self._acreate_new_leave_0_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        start_on: str,
        finish_on: str,
        employee_id: int,
        description: typing.Optional[str] = None,
        leave_type_id: typing.Optional[int] = None,
        half_day: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        hours_amount_in_cents: typing.Optional[int] = None,
        medical_leave_type: typing.Optional[int] = None,
        effective_on: typing.Optional[str] = None,
        medical_discharge_reason: typing.Optional[str] = None,
        colegiate_number: typing.Optional[int] = None,
        has_previous_relapse: typing.Optional[bool] = None,
        relapse_leave_id: typing.Optional[int] = None,
        relapse_on: typing.Optional[str] = None,
        accident_on: typing.Optional[str] = None,
        paternity_birth_on: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_leave_0_mapped_args(
            start_on=start_on,
            finish_on=finish_on,
            employee_id=employee_id,
            description=description,
            leave_type_id=leave_type_id,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            medical_leave_type=medical_leave_type,
            effective_on=effective_on,
            medical_discharge_reason=medical_discharge_reason,
            colegiate_number=colegiate_number,
            has_previous_relapse=has_previous_relapse,
            relapse_leave_id=relapse_leave_id,
            relapse_on=relapse_on,
            accident_on=accident_on,
            paternity_birth_on=paternity_birth_on,
        )
        return self._create_new_leave_0_oapg(
            body=args.body,
        )

