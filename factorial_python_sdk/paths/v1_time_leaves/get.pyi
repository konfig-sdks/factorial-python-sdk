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

from factorial_python_sdk.model.leave_get_company_leaves_response import LeaveGetCompanyLeavesResponse as LeaveGetCompanyLeavesResponseSchema

from factorial_python_sdk.type.leave_get_company_leaves_response import LeaveGetCompanyLeavesResponse

from ...api_client import Dictionary
from factorial_python_sdk.pydantic.leave_get_company_leaves_response import LeaveGetCompanyLeavesResponse as LeaveGetCompanyLeavesResponsePydantic

# Query params


class EmployeeIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.IntSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EmployeeIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class LeaveTypeIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.IntSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LeaveTypeIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ModelFromSchema = schemas.StrSchema
ToSchema = schemas.StrSchema
IncludeLeaveTypeSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'employee_ids[]': typing.Union[EmployeeIdsSchema, list, tuple, ],
        'leave_type_ids[]': typing.Union[LeaveTypeIdsSchema, list, tuple, ],
        'from': typing.Union[ModelFromSchema, str, ],
        'to': typing.Union[ToSchema, str, ],
        'include_leave_type': typing.Union[IncludeLeaveTypeSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_employee_ids_ = api_client.QueryParameter(
    name="employee_ids[]",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeIdsSchema,
    explode=True,
)
request_query_leave_type_ids_ = api_client.QueryParameter(
    name="leave_type_ids[]",
    style=api_client.ParameterStyle.FORM,
    schema=LeaveTypeIdsSchema,
    explode=True,
)
request_query__from = api_client.QueryParameter(
    name="from",
    style=api_client.ParameterStyle.FORM,
    schema=ModelFromSchema,
    explode=True,
)
request_query_to = api_client.QueryParameter(
    name="to",
    style=api_client.ParameterStyle.FORM,
    schema=ToSchema,
    explode=True,
)
request_query_include_leave_type = api_client.QueryParameter(
    name="include_leave_type",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeLeaveTypeSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = LeaveGetCompanyLeavesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LeaveGetCompanyLeavesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LeaveGetCompanyLeavesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_company_leaves_mapped_args(
        self,
        employee_ids_: typing.Optional[typing.List[int]] = None,
        leave_type_ids_: typing.Optional[typing.List[int]] = None,
        _from: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        include_leave_type: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if employee_ids_ is not None:
            _query_params["employee_ids[]"] = employee_ids_
        if leave_type_ids_ is not None:
            _query_params["leave_type_ids[]"] = leave_type_ids_
        if _from is not None:
            _query_params["from"] = _from
        if to is not None:
            _query_params["to"] = to
        if include_leave_type is not None:
            _query_params["include_leave_type"] = include_leave_type
        args.query = _query_params
        return args

    async def _aget_company_leaves_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Leaves
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_employee_ids_,
            request_query_leave_type_ids_,
            request_query__from,
            request_query_to,
            request_query_include_leave_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/time/leaves',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_company_leaves_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Leaves
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_employee_ids_,
            request_query_leave_type_ids_,
            request_query__from,
            request_query_to,
            request_query_include_leave_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/time/leaves',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetCompanyLeavesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_company_leaves(
        self,
        employee_ids_: typing.Optional[typing.List[int]] = None,
        leave_type_ids_: typing.Optional[typing.List[int]] = None,
        _from: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        include_leave_type: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_company_leaves_mapped_args(
            employee_ids_=employee_ids_,
            leave_type_ids_=leave_type_ids_,
            _from=_from,
            to=to,
            include_leave_type=include_leave_type,
        )
        return await self._aget_company_leaves_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_company_leaves(
        self,
        employee_ids_: typing.Optional[typing.List[int]] = None,
        leave_type_ids_: typing.Optional[typing.List[int]] = None,
        _from: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        include_leave_type: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_company_leaves_mapped_args(
            employee_ids_=employee_ids_,
            leave_type_ids_=leave_type_ids_,
            _from=_from,
            to=to,
            include_leave_type=include_leave_type,
        )
        return self._get_company_leaves_oapg(
            query_params=args.query,
        )

class GetCompanyLeaves(BaseApi):

    async def aget_company_leaves(
        self,
        employee_ids_: typing.Optional[typing.List[int]] = None,
        leave_type_ids_: typing.Optional[typing.List[int]] = None,
        _from: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        include_leave_type: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> LeaveGetCompanyLeavesResponsePydantic:
        raw_response = await self.raw.aget_company_leaves(
            employee_ids_=employee_ids_,
            leave_type_ids_=leave_type_ids_,
            _from=_from,
            to=to,
            include_leave_type=include_leave_type,
            **kwargs,
        )
        if validate:
            return RootModel[LeaveGetCompanyLeavesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(LeaveGetCompanyLeavesResponsePydantic, raw_response.body)
    
    
    def get_company_leaves(
        self,
        employee_ids_: typing.Optional[typing.List[int]] = None,
        leave_type_ids_: typing.Optional[typing.List[int]] = None,
        _from: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        include_leave_type: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> LeaveGetCompanyLeavesResponsePydantic:
        raw_response = self.raw.get_company_leaves(
            employee_ids_=employee_ids_,
            leave_type_ids_=leave_type_ids_,
            _from=_from,
            to=to,
            include_leave_type=include_leave_type,
        )
        if validate:
            return RootModel[LeaveGetCompanyLeavesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(LeaveGetCompanyLeavesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        employee_ids_: typing.Optional[typing.List[int]] = None,
        leave_type_ids_: typing.Optional[typing.List[int]] = None,
        _from: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        include_leave_type: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_company_leaves_mapped_args(
            employee_ids_=employee_ids_,
            leave_type_ids_=leave_type_ids_,
            _from=_from,
            to=to,
            include_leave_type=include_leave_type,
        )
        return await self._aget_company_leaves_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        employee_ids_: typing.Optional[typing.List[int]] = None,
        leave_type_ids_: typing.Optional[typing.List[int]] = None,
        _from: typing.Optional[str] = None,
        to: typing.Optional[str] = None,
        include_leave_type: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_company_leaves_mapped_args(
            employee_ids_=employee_ids_,
            leave_type_ids_=leave_type_ids_,
            _from=_from,
            to=to,
            include_leave_type=include_leave_type,
        )
        return self._get_company_leaves_oapg(
            query_params=args.query,
        )

