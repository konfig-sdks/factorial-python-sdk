# coding: utf-8

"""
    Factorial API

    Open Api Specifications available at [https://github.com/factorialco/oas](https://github.com/factorialco/oasLooking)  Guides and support available at [https://help.factorialhr.com/integrations](https://help.factorialhr.com/integrations)  # Authentication  The public API provides two methods of authentication, ApiKeys and OAuth2. The following sections provide information regarding each one and their intent.  ## OAuth2  > OAuth2 is used to identify individual users, not applications or platforms.  OAuth2 is available for authenticating to the public API and making requests via third parties **on behalf of a user**. All actions are authored on behalf of the user that creates the token. This means the intent is to be used mainly to do submit actions the actual user is performing on an alternative interface.  To generate a token you will require opening an authorization dialog that returns a code, this code can then be exchanged for a token.  ### Configuration  In order to create an OAuth application, you must be an admin, head over to your [personal repository of OAuth applications](https://api.factorialhr.com/oauth/applications), click on `New application` and follow the creation process.  The Factorial API enforces the same permissions at the user level than the Factorial web application. This means that Factorial API users will only be able to perform the same actions they are allowed to do in the Factorial platform.  Next step will be to generate the Authorization Code you will need in order to generate an OAuth2 Token.  ### OAuth2 Code Generation  Should be generated via browser by opening the following url. The user should be already logged in to Factorial beforehand.  `https://api.factorialhr.com/oauth/authorize?client_id=&redirect_uri=&response_type=code&scope=`  YOUR_CLIENT_ID: OAuth2 Application Id REDIRECT_URI: OAuth2 Redirect URL  #### State Parameter  An optional query parameter called `state` can be added to the code generation url. Any string can be used and will be sent on the callback url.  > Authorization protocols provide a `state` parameter that allows you to restore the previous state of your application. The `state` parameter preserves some state objects set by the client in the Authorization request and makes it available to the client in the response.  ### OAuth2 Token Generation  Once you have the authorization code, you can request their access token to Factorial.  `curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&code=&grant_type=authorization_code&redirect_uri='`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret AUTHORIZATION_CODE: OAuth2 CODE REDIRECT_URI: OAuth2 Redirect URL  > You can generate only one OAuth2 token per Code, that means that if you want to generate a new token for a Code that already have one you should refresh your token.  Every time a new token is generated a refresh token is generated as well, so that you can use it on the OAuth2 Refresh Token, and an expire date is also provided.  ### OAuth2 Refresh Token  You can generate a new token under the same Code with a new expire date (you can do it as many times as you need). A refresh token is also returned here so that you can use it on the OAuth2 Refresh Token again.  `curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&refresh_token=&grant_type=refresh_token'`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret REFRESH_TOKEN: OAuth2 Refresh Token  ### OAuth2 Revoke Token  You can revoke an access/refresh token if you do not want it to be active anylonger. This can happen in cases where you have refreshed your token and would like to revoke the previous token if you haven't used the new token yet, as using the new token automatically revokes the previous one.  `curl -X POST 'https://api.factorialhr.com/oauth/revoke' -d 'client_id=&client_secret=&token='`  YOUR_CLIENT_ID: OAuth2 Application Id YOUR_CLIENT_SECRET: OAuth2 Application Secret TOKEN: OAuth2 Access/Refresh Token (whichever you wish to revoke)  ### OAuth2 Token Usage  The generated token is the credential for performing authenticated requests to Factorial. This token should be included in the Authorization header prefixed with the word Bearer and a separating space. As an example, if your token is `12345` then the header content should be `Bearer 12345`.  ### Maintaining a persistent connection  To maintain a persistent connection, you should not let the token expire. You can avoid this by simply refreshing your token before the expiration date. This will give you another token with a new expiration date, before that token expires you should refresh it again, and so on... If you want to do this automatically, you should provide something in your code that will help you perform the update every time the token expires. Otherwise, you would have to do the update manually and make sure you refresh your token before the expiration date to maintain the connection.  ## ApiKeys  > API keys are used to identify systems, not the individual users that access.  ApiKeys have **TOTAL ACCESS** to everything and never expire. Its the creators responsibility to generate them and store them securely.  ### Generation  In the `Core>Keys` section of this documentation you can access the apis for managing this resource.  ### Usage  ApiKeys are a single string of symbols that must be added as a custom header on the request. The header name must be `x-api-key` and the key must be the value without any prefixes.  ### Disclaimer  ApiKey management require full admin permissions as the resource itself allows for full admin access to the entire platform on behalf of the company and not of a user, therefore any operations are not linked to any user in particular.  # Development  ## SDKs  Coming soon  ## Sandbox  A sandbox/demo environment is available for testing integrations via public API calls. Developers can request provisioning with full access to a demo company where to test code before actually interacting with a production environment.  Contact your account manager or account executive to request this environment and get OAuth2 credentials for generating tokens.  Note: the domain for sandbox is different than that from production. Sandbox base domain is `http://api.demo.factorialhr.com`  ## Postman  Click the \"Run in Postman\" button to open the full list of endpoints on your Postman workspace as a Postman Collection. Inside the collection lookout for the Collection's Variables, configure your variables accordingly.  ### Delegating Token Generation To Postman  Coming soon  # Changelog  Coming soon  # How to...  ## Custom Fields  Custom fields are useful when you want to add some fields that are not the default ones, to every employee of the company.  For that, you have to create via Factorial App the base custom field in order to have all the employees with it. That option is available in customization, inside the company menu  Once you have that, via API, you can [Create a value for a custom field](https://apidoc.factorialhr.com/#72f3f786-e37d-4e80-ada2-0beedd03b171) to each employee. You should know the custom field id in order to make that, you can check it by [getting a collection of custom fields](https://apidoc.factorialhr.com/#f98dae5a-a8d0-474e-a181-7e9603409b42)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""


import typing
from factorial_python_sdk.api_response import ApiResponse, AsyncApiResponse
from factorial_python_sdk.exceptions_base import OpenApiException, ApiTypeError, ApiValueError, render_path

class ClientConfigurationError(OpenApiException):
    def __init__(self, msg):
        super(ClientConfigurationError, self).__init__(msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None):
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiStreamingException(OpenApiException):

    def __init__(self, status=None, reason=None, body=None):
        self.status = status
        self.reason = reason
        self.body = body

    def __str__(self):
        """Custom error messages for exception"""
        return "({0})\n Reason: {1}\n Body: {2}".format(self.status, self.reason, self.body)


class ApiException(OpenApiException):

    def __init__(self, status=None, reason=None, api_response: typing.Optional[typing.Union[ApiResponse, AsyncApiResponse]] = None):
        if api_response:
            self.status = api_response.status
            self.reason = api_response.response.reason
            self.body = api_response.body
            self.headers = api_response.response.headers
            self.round_trip_time = api_response.round_trip_time
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None
            self.round_trip_time = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


class AnyOfValidationError(OpenApiException):
    def __init__(self, error_list: typing.List[typing.Union[ApiTypeError, ApiValueError]]):
        self.error_list = error_list
        sub_msgs: typing.List[str] = []
        for type_error in error_list:
            sub_msgs.append(str(type_error))
        num_validation_errors = len(self.error_list)
        if num_validation_errors == 1:
            super().__init__(sub_msgs[0])
        else:
            # create a string that says how many validation errors there were and
            # prints each sub_msg out using a bulleted list of messages
            msg = "{} validation error{} detected: \n".format(num_validation_errors, "s" if num_validation_errors > 1 else "")
            for i, sub_msg in enumerate(sub_msgs):
                msg += " {}. {}\n".format(i+1, sub_msg)
            super().__init__(msg)


class InvalidHostConfigurationError(ClientConfigurationError):
    def __init__(self, host: str, reason: str):
        self.host = host
        self.reason = reason
        super().__init__('Invalid host: "{}", {}'.format(self.host, self.reason))


class MissingRequiredPropertiesError(ApiTypeError):
    def __init__(self, msg: str):
        super().__init__(msg)


class MissingRequiredParametersError(ApiTypeError):
    def __init__(self, error: TypeError):
        self.error = error
        error_str = str(error)
        self.msg = error_str
        if "__new__()" in error_str:
            # parse error to reformat
            missing_parameters = error_str.split(":")[1].strip()
            number_of_parameters = error_str.split("missing")[1].split("required")[0].strip()
            self.msg = "Missing {} required parameter{}: {}".format(number_of_parameters, "s" if int(number_of_parameters) > 1 else "", missing_parameters)
        super().__init__(self.msg)

class SchemaValidationError(OpenApiException):
    def __init__(self, validation_errors: typing.List[typing.Union[ApiValueError, ApiTypeError]]):
        """ Aggregates schema validation errors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.validation_errors = validation_errors
        self.type_errors: typing.List[ApiTypeError] = []
        self.value_errors: typing.List[ApiValueError] = []
        self.missing_required_properties_errors: typing.List[MissingRequiredPropertiesError] = []
        for error in validation_errors:
            if isinstance(error, ApiTypeError):
                self.type_errors.append(error)
            elif isinstance(error, ApiValueError):
                self.value_errors.append(error)
            elif isinstance(error, MissingRequiredPropertiesError):
                self.missing_required_properties_errors.append(error)
        sub_msgs: typing.List[str] = []
        if len(self.missing_required_properties_errors) > 0:
            for error in self.missing_required_properties_errors:
                sub_msgs.append(str(error))
        if len(self.type_errors) > 0:
            for type_error in self.type_errors:
                if isinstance(type_error, MissingRequiredPropertiesError) or isinstance(type_error, MissingRequiredParametersError):
                    sub_msgs.append(str(type_error))
                else:
                    classes = ", ".join([cls.__name__ for cls in type_error.valid_classes])
                    msg = 'Got {}({}) for required type {} at {}'.format(
                        type(type_error.invalid_value).__name__, type_error.invalid_value, classes, render_path(type_error.path_to_item))
                    sub_msgs.append(msg)
        if len(self.value_errors) > 0:
            for value_error in self.value_errors:
                sub_msgs.append(value_error.full_msg)
        sub_msg = ". ".join(sub_msgs)
        num_validation_errors = len(self.validation_errors)
        self.msg = "{} invalid argument{}. {}".format(num_validation_errors, "s" if num_validation_errors > 1 else "", sub_msg)
        super().__init__(self.msg)
