<div align="left">

[![Visit Factorial](./header.png)](https://factorialhr.com)

# Factorial<a id="factorial"></a>

Open Api Specifications available at [https://github.com/factorialco/oas](https://github.com/factorialco/oasLooking)

Guides and support available at [https://help.factorialhr.com/integrations](https://help.factorialhr.com/integrations)

# Authentication<a id="authentication"></a>

The public API provides two methods of authentication, ApiKeys and OAuth2. The following sections provide information regarding each one and their intent.

## OAuth2<a id="oauth2"></a>

> OAuth2 is used to identify individual users, not applications or platforms.

OAuth2 is available for authenticating to the public API and making requests via third parties **on behalf of a user**. All actions are authored on behalf of the user that creates the token. This means the intent is to be used mainly to do submit actions the actual user is performing on an alternative interface.

To generate a token you will require opening an authorization dialog that returns a code, this code can then be exchanged for a token.

### Configuration<a id="configuration"></a>

In order to create an OAuth application, you must be an admin, head over to your [personal repository of OAuth applications](https://api.factorialhr.com/oauth/applications), click on `New application` and follow the creation process.

The Factorial API enforces the same permissions at the user level than the Factorial web application. This means that Factorial API users will only be able to perform the same actions they are allowed to do in the Factorial platform.

Next step will be to generate the Authorization Code you will need in order to generate an OAuth2 Token.

### OAuth2 Code Generation<a id="oauth2-code-generation"></a>

Should be generated via browser by opening the following url. The user should be already logged in to Factorial beforehand.

`https://api.factorialhr.com/oauth/authorize?client_id=&redirect_uri=&response_type=code&scope=`

YOUR_CLIENT_ID: OAuth2 Application Id
REDIRECT_URI: OAuth2 Redirect URL

#### State Parameter<a id="state-parameter"></a>

An optional query parameter called `state` can be added to the code generation url. Any string can be used and will be sent on the callback url.

> Authorization protocols provide a `state` parameter that allows you to restore the previous state of your application. The `state` parameter preserves some state objects set by the client in the Authorization request and makes it available to the client in the response.

### OAuth2 Token Generation<a id="oauth2-token-generation"></a>

Once you have the authorization code, you can request their access token to Factorial.

`curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&code=&grant_type=authorization_code&redirect_uri='`

YOUR_CLIENT_ID: OAuth2 Application Id
YOUR_CLIENT_SECRET: OAuth2 Application Secret
AUTHORIZATION_CODE: OAuth2 CODE
REDIRECT_URI: OAuth2 Redirect URL

> You can generate only one OAuth2 token per Code, that means that if you want to generate a new token for a Code that already have one you should refresh your token.

Every time a new token is generated a refresh token is generated as well, so that you can use it on the OAuth2 Refresh Token, and an expire date is also provided.

### OAuth2 Refresh Token<a id="oauth2-refresh-token"></a>

You can generate a new token under the same Code with a new expire date (you can do it as many times as you need). A refresh token is also returned here so that you can use it on the OAuth2 Refresh Token again.

`curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=&client_secret=&refresh_token=&grant_type=refresh_token'`

YOUR_CLIENT_ID: OAuth2 Application Id
YOUR_CLIENT_SECRET: OAuth2 Application Secret
REFRESH_TOKEN: OAuth2 Refresh Token

### OAuth2 Revoke Token<a id="oauth2-revoke-token"></a>

You can revoke an access/refresh token if you do not want it to be active anylonger. This can happen in cases where you have refreshed your token and would like to revoke the previous token if you haven't used the new token yet, as using the new token automatically revokes the previous one.

`curl -X POST 'https://api.factorialhr.com/oauth/revoke' -d 'client_id=&client_secret=&token='`

YOUR_CLIENT_ID: OAuth2 Application Id
YOUR_CLIENT_SECRET: OAuth2 Application Secret
TOKEN: OAuth2 Access/Refresh Token (whichever you wish to revoke)

### OAuth2 Token Usage<a id="oauth2-token-usage"></a>

The generated token is the credential for performing authenticated requests to Factorial. This token should be included in the Authorization header prefixed with the word Bearer and a separating space.
As an example, if your token is `12345` then the header content should be `Bearer 12345`.

### Maintaining a persistent connection<a id="maintaining-a-persistent-connection"></a>

To maintain a persistent connection, you should not let the token expire. You can avoid this by simply refreshing your token before the expiration date. This will give you another token with a new expiration date, before that token expires you should refresh it again, and so on...
If you want to do this automatically, you should provide something in your code that will help you perform the update every time the token expires. Otherwise, you would have to do the update manually and make sure you refresh your token before the expiration date to maintain the connection.

## ApiKeys<a id="apikeys"></a>

> API keys are used to identify systems, not the individual users that access.

ApiKeys have **TOTAL ACCESS** to everything and never expire. Its the creators responsibility to generate them and store them securely.

### Generation<a id="generation"></a>

In the `Core>Keys` section of this documentation you can access the apis for managing this resource.

### Usage<a id="usage"></a>

ApiKeys are a single string of symbols that must be added as a custom header on the request. The header name must be `x-api-key` and the key must be the value without any prefixes.

### Disclaimer<a id="disclaimer"></a>

ApiKey management require full admin permissions as the resource itself allows for full admin access to the entire platform on behalf of the company and not of a user, therefore any operations are not linked to any user in particular.

# Development<a id="development"></a>

## SDKs<a id="sdks"></a>

Coming soon

## Sandbox<a id="sandbox"></a>

A sandbox/demo environment is available for testing integrations via public API calls. Developers can request provisioning with full access to a demo company where to test code before actually interacting with a production environment.

Contact your account manager or account executive to request this environment and get OAuth2 credentials for generating tokens.

Note: the domain for sandbox is different than that from production. Sandbox base domain is `http://api.demo.factorialhr.com`

## Postman<a id="postman"></a>

Click the \"Run in Postman\" button to open the full list of endpoints on your Postman workspace as a Postman Collection.
Inside the collection lookout for the Collection's Variables, configure your variables accordingly.

### Delegating Token Generation To Postman<a id="delegating-token-generation-to-postman"></a>

Coming soon

# Changelog<a id="changelog"></a>

Coming soon

# How to...<a id="how-to"></a>

## Custom Fields<a id="custom-fields"></a>

Custom fields are useful when you want to add some fields that are not the default ones, to every employee of the company.

For that, you have to create via Factorial App the base custom field in order to have all the employees with it. That option is available in customization, inside the company menu

Once you have that, via API, you can [Create a value for a custom field](https://apidoc.factorialhr.com/#72f3f786-e37d-4e80-ada2-0beedd03b171) to each employee. You should know the custom field id in order to make that, you can check it by [getting a collection of custom fields](https://apidoc.factorialhr.com/#f98dae5a-a8d0-474e-a181-7e9603409b42)


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`factorial.application.create_ats_application`](#factorialapplicationcreate_ats_application)
  * [`factorial.application.update_data`](#factorialapplicationupdate_data)
  * [`factorial.attendance.create_new`](#factorialattendancecreate_new)
  * [`factorial.attendance.get_bulk_v2`](#factorialattendanceget_bulk_v2)
  * [`factorial.attendance.get_company_attendance`](#factorialattendanceget_company_attendance)
  * [`factorial.break.create_break`](#factorialbreakcreate_break)
  * [`factorial.break.end_break`](#factorialbreakend_break)
  * [`factorial.break.start_break`](#factorialbreakstart_break)
  * [`factorial.candidate.create_new_candidate`](#factorialcandidatecreate_new_candidate)
  * [`factorial.candidate.delete_existing_candidate`](#factorialcandidatedelete_existing_candidate)
  * [`factorial.candidate.list_all_candidates`](#factorialcandidatelist_all_candidates)
  * [`factorial.candidate.update_candidate_data`](#factorialcandidateupdate_candidate_data)
  * [`factorial.compensation.create_contract_compensation`](#factorialcompensationcreate_contract_compensation)
  * [`factorial.compensation.delete_compensation`](#factorialcompensationdelete_compensation)
  * [`factorial.compensation.get_by_id`](#factorialcompensationget_by_id)
  * [`factorial.compensation.get_compensations`](#factorialcompensationget_compensations)
  * [`factorial.compensation.update_for_contract`](#factorialcompensationupdate_for_contract)
  * [`factorial.contract.delete_version`](#factorialcontractdelete_version)
  * [`factorial.contract.get_all_reference_contracts`](#factorialcontractget_all_reference_contracts)
  * [`factorial.contract.update_version`](#factorialcontractupdate_version)
  * [`factorial.contract_version.create_new_version`](#factorialcontract_versioncreate_new_version)
  * [`factorial.contract_version.get_all_versions`](#factorialcontract_versionget_all_versions)
  * [`factorial.contract_version.get_bulk_versions`](#factorialcontract_versionget_bulk_versions)
  * [`factorial.custom_field.create_field`](#factorialcustom_fieldcreate_field)
  * [`factorial.custom_field.delete_by_id`](#factorialcustom_fielddelete_by_id)
  * [`factorial.custom_field.get_fields_by_group`](#factorialcustom_fieldget_fields_by_group)
  * [`factorial.custom_field.get_fields_by_slug`](#factorialcustom_fieldget_fields_by_slug)
  * [`factorial.custom_field_value.create_custom_value`](#factorialcustom_field_valuecreate_custom_value)
  * [`factorial.custom_field_value.get_by_slug_name`](#factorialcustom_field_valueget_by_slug_name)
  * [`factorial.custom_field_value.get_instance_value`](#factorialcustom_field_valueget_instance_value)
  * [`factorial.custom_field_value.update_value`](#factorialcustom_field_valueupdate_value)
  * [`factorial.custom_table.get`](#factorialcustom_tableget)
  * [`factorial.document.create_new_document`](#factorialdocumentcreate_new_document)
  * [`factorial.document.delete_by_id`](#factorialdocumentdelete_by_id)
  * [`factorial.document.get_by_id`](#factorialdocumentget_by_id)
  * [`factorial.document.list_given_employee_or_folder`](#factorialdocumentlist_given_employee_or_folder)
  * [`factorial.document.update_by_id`](#factorialdocumentupdate_by_id)
  * [`factorial.employee.assign_to_team`](#factorialemployeeassign_to_team)
  * [`factorial.employee.change_email`](#factorialemployeechange_email)
  * [`factorial.employee.create_custom_table_value`](#factorialemployeecreate_custom_table_value)
  * [`factorial.employee.create_employee`](#factorialemployeecreate_employee)
  * [`factorial.employee.create_new`](#factorialemployeecreate_new)
  * [`factorial.employee.get_all_employees`](#factorialemployeeget_all_employees)
  * [`factorial.employee.get_bulk_v2`](#factorialemployeeget_bulk_v2)
  * [`factorial.employee.get_by_id`](#factorialemployeeget_by_id)
  * [`factorial.employee.get_by_payroll_integration_code`](#factorialemployeeget_by_payroll_integration_code)
  * [`factorial.employee.get_custom_table_values`](#factorialemployeeget_custom_table_values)
  * [`factorial.employee.get_employee_by_id`](#factorialemployeeget_employee_by_id)
  * [`factorial.employee.get_employees`](#factorialemployeeget_employees)
  * [`factorial.employee.list_break_configurations_for_dates`](#factorialemployeelist_break_configurations_for_dates)
  * [`factorial.employee.list_family_situations`](#factorialemployeelist_family_situations)
  * [`factorial.employee.send_invitation_email`](#factorialemployeesend_invitation_email)
  * [`factorial.employee.set_termination_details`](#factorialemployeeset_termination_details)
  * [`factorial.employee.terminate_employee`](#factorialemployeeterminate_employee)
  * [`factorial.employee.unassign_to_team`](#factorialemployeeunassign_to_team)
  * [`factorial.employee.unterminate_employee`](#factorialemployeeunterminate_employee)
  * [`factorial.employee.unterminate_post`](#factorialemployeeunterminate_post)
  * [`factorial.employee.update_by_id`](#factorialemployeeupdate_by_id)
  * [`factorial.employee.update_employee_by_id`](#factorialemployeeupdate_employee_by_id)
  * [`factorial.employee.update_in_team`](#factorialemployeeupdate_in_team)
  * [`factorial.event.get_triggered_events`](#factorialeventget_triggered_events)
  * [`factorial.expense.get_by_id`](#factorialexpenseget_by_id)
  * [`factorial.expense.get_company_expenses`](#factorialexpenseget_company_expenses)
  * [`factorial.family_situation.create_new`](#factorialfamily_situationcreate_new)
  * [`factorial.family_situation.update_family_situation`](#factorialfamily_situationupdate_family_situation)
  * [`factorial.folder.create_new_folder`](#factorialfoldercreate_new_folder)
  * [`factorial.folder.get_by_id`](#factorialfolderget_by_id)
  * [`factorial.folder.get_by_name_and_status`](#factorialfolderget_by_name_and_status)
  * [`factorial.folder.update_folder_by_id`](#factorialfolderupdate_folder_by_id)
  * [`factorial.holiday.get_all_company_holidays`](#factorialholidayget_all_company_holidays)
  * [`factorial.holiday.get_by_id`](#factorialholidayget_by_id)
  * [`factorial.integration.delete_payroll_code`](#factorialintegrationdelete_payroll_code)
  * [`factorial.integration.get_all_codes`](#factorialintegrationget_all_codes)
  * [`factorial.integration.update_payroll_code`](#factorialintegrationupdate_payroll_code)
  * [`factorial.integration_code.create_payroll_integration_code`](#factorialintegration_codecreate_payroll_integration_code)
  * [`factorial.key.create_new`](#factorialkeycreate_new)
  * [`factorial.key.delete_by_id`](#factorialkeydelete_by_id)
  * [`factorial.key.get_collection`](#factorialkeyget_collection)
  * [`factorial.leave.create_new_leave`](#factorialleavecreate_new_leave)
  * [`factorial.leave.create_new_leave_0`](#factorialleavecreate_new_leave_0)
  * [`factorial.leave.delete_by_id`](#factorialleavedelete_by_id)
  * [`factorial.leave.delete_by_id_0`](#factorialleavedelete_by_id_0)
  * [`factorial.leave.get_by_id`](#factorialleaveget_by_id)
  * [`factorial.leave.get_by_id_0`](#factorialleaveget_by_id_0)
  * [`factorial.leave.get_company_leaves`](#factorialleaveget_company_leaves)
  * [`factorial.leave.get_company_leaves_0`](#factorialleaveget_company_leaves_0)
  * [`factorial.leave.get_types`](#factorialleaveget_types)
  * [`factorial.leave.type_create`](#factorialleavetype_create)
  * [`factorial.leave.update_by_id`](#factorialleaveupdate_by_id)
  * [`factorial.leave.update_leave_by_id`](#factorialleaveupdate_leave_by_id)
  * [`factorial.leave.update_type`](#factorialleaveupdate_type)
  * [`factorial.legal_entity.get_by_id`](#factoriallegal_entityget_by_id)
  * [`factorial.legal_entity.list_legal_entities`](#factoriallegal_entitylist_legal_entities)
  * [`factorial.location.get_all_locations`](#factoriallocationget_all_locations)
  * [`factorial.location.get_by_id`](#factoriallocationget_by_id)
  * [`factorial.location.update_shift_location`](#factoriallocationupdate_shift_location)
  * [`factorial.message.create_ats_message`](#factorialmessagecreate_ats_message)
  * [`factorial.message.get_all_messages`](#factorialmessageget_all_messages)
  * [`factorial.policy.get_time_off`](#factorialpolicyget_time_off)
  * [`factorial.policy.get_time_off_policies`](#factorialpolicyget_time_off_policies)
  * [`factorial.post.ats_job_posting`](#factorialpostats_job_posting)
  * [`factorial.post.create_new_post`](#factorialpostcreate_new_post)
  * [`factorial.post.duplicate_job_posting`](#factorialpostduplicate_job_posting)
  * [`factorial.post.get_all_postings`](#factorialpostget_all_postings)
  * [`factorial.post.get_by_id`](#factorialpostget_by_id)
  * [`factorial.post.job_posting_update`](#factorialpostjob_posting_update)
  * [`factorial.post.list_posts`](#factorialpostlist_posts)
  * [`factorial.post.remove_job_posting`](#factorialpostremove_job_posting)
  * [`factorial.post.remove_post`](#factorialpostremove_post)
  * [`factorial.post.update_existing_post`](#factorialpostupdate_existing_post)
  * [`factorial.shift.create_clock_in_shift`](#factorialshiftcreate_clock_in_shift)
  * [`factorial.shift.create_new_shift`](#factorialshiftcreate_new_shift)
  * [`factorial.shift.delete_by_id`](#factorialshiftdelete_by_id)
  * [`factorial.shift.delete_shift_by_id`](#factorialshiftdelete_shift_by_id)
  * [`factorial.shift.get_all_shifts`](#factorialshiftget_all_shifts)
  * [`factorial.shift.get_by_id`](#factorialshiftget_by_id)
  * [`factorial.shift.get_from_company`](#factorialshiftget_from_company)
  * [`factorial.shift.publish_shifts_inside_time_range`](#factorialshiftpublish_shifts_inside_time_range)
  * [`factorial.shift.toggle_shift_status`](#factorialshifttoggle_shift_status)
  * [`factorial.shift.update_clock_out_shift`](#factorialshiftupdate_clock_out_shift)
  * [`factorial.shift.update_notes`](#factorialshiftupdate_notes)
  * [`factorial.shift.update_shift`](#factorialshiftupdate_shift)
  * [`factorial.supplement.create_new_supplement`](#factorialsupplementcreate_new_supplement)
  * [`factorial.supplement.delete_by_id`](#factorialsupplementdelete_by_id)
  * [`factorial.supplement.get_all`](#factorialsupplementget_all)
  * [`factorial.supplement.update_by_id`](#factorialsupplementupdate_by_id)
  * [`factorial.table.create_custom_table`](#factorialtablecreate_custom_table)
  * [`factorial.table.create_field`](#factorialtablecreate_field)
  * [`factorial.table.get_custom_table`](#factorialtableget_custom_table)
  * [`factorial.table.get_fields`](#factorialtableget_fields)
  * [`factorial.task.add_file_to_task`](#factorialtaskadd_file_to_task)
  * [`factorial.task.copy_by_id`](#factorialtaskcopy_by_id)
  * [`factorial.task.create_new_task`](#factorialtaskcreate_new_task)
  * [`factorial.task.delete_by_id`](#factorialtaskdelete_by_id)
  * [`factorial.task.delete_file_in_task`](#factorialtaskdelete_file_in_task)
  * [`factorial.task.get_all_tasks`](#factorialtaskget_all_tasks)
  * [`factorial.task.get_by_id`](#factorialtaskget_by_id)
  * [`factorial.task.get_file`](#factorialtaskget_file)
  * [`factorial.task.get_files`](#factorialtaskget_files)
  * [`factorial.task.resolve_by_id`](#factorialtaskresolve_by_id)
  * [`factorial.task.update_by_id`](#factorialtaskupdate_by_id)
  * [`factorial.taxonomy.get_by_id`](#factorialtaxonomyget_by_id)
  * [`factorial.taxonomy.get_company_taxonomies`](#factorialtaxonomyget_company_taxonomies)
  * [`factorial.team.create_new_team`](#factorialteamcreate_new_team)
  * [`factorial.team.get_all_teams`](#factorialteamget_all_teams)
  * [`factorial.team.get_by_id`](#factorialteamget_by_id)
  * [`factorial.team.remove_team`](#factorialteamremove_team)
  * [`factorial.team.update_team_by_id`](#factorialteamupdate_team_by_id)
  * [`factorial.user.info_get`](#factorialuserinfo_get)
  * [`factorial.user.subscribed_webhooks_list`](#factorialusersubscribed_webhooks_list)
  * [`factorial.user.subscribed_webhooks_list_0`](#factorialusersubscribed_webhooks_list_0)
  * [`factorial.webhook.create_subscription`](#factorialwebhookcreate_subscription)
- [Webhooks Types](#webhooks-types)
  * [`factorial.webhook.delete_webhook`](#factorialwebhookdelete_webhook)
  * [`factorial.webhook.delete_webhook_by_id`](#factorialwebhookdelete_webhook_by_id)
  * [`factorial.webhook.subscription_create`](#factorialwebhooksubscription_create)
- [Webhooks Types](#webhooks-types-1)
  * [`factorial.webhook.update_webhook_by_id`](#factorialwebhookupdate_webhook_by_id)
  * [`factorial.workplace.create_new_workplace`](#factorialworkplacecreate_new_workplace)
  * [`factorial.workplace.get_by_id`](#factorialworkplaceget_by_id)
  * [`factorial.workplace.list_all_workplaces`](#factorialworkplacelist_all_workplaces)
  * [`factorial.workplace.remove_workplace`](#factorialworkplaceremove_workplace)
  * [`factorial.workplace.update_workplace_by_id`](#factorialworkplaceupdate_workplace_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Factorial&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from factorial_python_sdk import Factorial, ApiException

factorial = Factorial(

        apikey = 'YOUR_API_KEY',
)

try:
    # Creates an application
    create_ats_application_response = factorial.application.create_ats_application(
        ats_job_posting_id=1,
        source="indeed",
        medium="LinkedIn",
        ats_candidate_id=2,
        cover_letter="",
        first_name="Bob",
        last_name="Stone",
        phone="1134124214",
        email="bob_stone@factorial.co",
        cv="cv.pdf",
        photo="photo.jpg",
        answers=[{
    "ats_question_id": 1,
    "value": "string_example",
}, , ],
    )
    print(create_ats_application_response)
except ApiException as e:
    print("Exception when calling ApplicationApi.create_ats_application: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from factorial_python_sdk import Factorial, ApiException

factorial = Factorial(

        apikey = 'YOUR_API_KEY',
)

async def main():
    try:
        # Creates an application
        create_ats_application_response = await factorial.application.acreate_ats_application(
            ats_job_posting_id=1,
            source="indeed",
            medium="LinkedIn",
            ats_candidate_id=2,
            cover_letter="",
            first_name="Bob",
            last_name="Stone",
            phone="1134124214",
            email="bob_stone@factorial.co",
            cv="cv.pdf",
            photo="photo.jpg",
            answers=[{
    "ats_question_id": 1,
    "value": "string_example",
}, , ],
        )
        print(create_ats_application_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi.create_ats_application: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from factorial_python_sdk import Factorial, ApiException

factorial = Factorial(

        apikey = 'YOUR_API_KEY',
)

try:
    # Creates an application
    create_ats_application_response = factorial.application.raw.create_ats_application(
        ats_job_posting_id=1,
        source="indeed",
        medium="LinkedIn",
        ats_candidate_id=2,
        cover_letter="",
        first_name="Bob",
        last_name="Stone",
        phone="1134124214",
        email="bob_stone@factorial.co",
        cv="cv.pdf",
        photo="photo.jpg",
        answers=[{
    "ats_question_id": 1,
    "value": "string_example",
}, , ],
    )
    pprint(create_ats_application_response.body)
    pprint(create_ats_application_response.body["id"])
    pprint(create_ats_application_response.body["ats_candidate_id"])
    pprint(create_ats_application_response.body["ats_job_posting_id"])
    pprint(create_ats_application_response.body["ats_application_phase_id"])
    pprint(create_ats_application_response.body["ats_application_phase_name"])
    pprint(create_ats_application_response.body["ats_application_phase_type"])
    pprint(create_ats_application_response.body["ats_job_posting_title"])
    pprint(create_ats_application_response.body["conversation_id"])
    pprint(create_ats_application_response.body["cover_letter"])
    pprint(create_ats_application_response.body["cv"])
    pprint(create_ats_application_response.body["photo"])
    pprint(create_ats_application_response.body["disqualified_reason"])
    pprint(create_ats_application_response.body["email"])
    pprint(create_ats_application_response.body["first_name"])
    pprint(create_ats_application_response.body["full_name"])
    pprint(create_ats_application_response.body["last_name"])
    pprint(create_ats_application_response.body["medium"])
    pprint(create_ats_application_response.body["personal_url"])
    pprint(create_ats_application_response.body["phone"])
    pprint(create_ats_application_response.body["qualified"])
    pprint(create_ats_application_response.body["rating_average"])
    pprint(create_ats_application_response.body["source"])
    pprint(create_ats_application_response.body["talent_pool"])
    pprint(create_ats_application_response.body["created_at"])
    pprint(create_ats_application_response.body["answers"])
    pprint(create_ats_application_response.headers)
    pprint(create_ats_application_response.status)
    pprint(create_ats_application_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ApplicationApi.create_ats_application: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `factorial.application.create_ats_application`<a id="factorialapplicationcreate_ats_application"></a>

This endpoint allows a consumer to create and store Ats Applications in Factorial

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_ats_application_response = factorial.application.create_ats_application(
    ats_job_posting_id=1,
    source="indeed",
    medium="LinkedIn",
    ats_candidate_id=2,
    cover_letter="",
    first_name="Bob",
    last_name="Stone",
    phone="1134124214",
    email="bob_stone@factorial.co",
    cv="cv.pdf",
    photo="photo.jpg",
    answers=[{
    "ats_question_id": 1,
    "value": "string_example",
}, , ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ats_job_posting_id: `int`<a id="ats_job_posting_id-int"></a>

##### source: `str`<a id="source-str"></a>

##### medium: `str`<a id="medium-str"></a>

##### ats_candidate_id: `int`<a id="ats_candidate_id-int"></a>

##### cover_letter: `str`<a id="cover_letter-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### email: `str`<a id="email-str"></a>

##### cv: `IO`<a id="cv-io"></a>

##### photo: `IO`<a id="photo-io"></a>

##### answers: [`ApplicationCreateAtsApplicationRequestAnswers`](./factorial_python_sdk/type/application_create_ats_application_request_answers.py)<a id="answers-applicationcreateatsapplicationrequestanswersfactorial_python_sdktypeapplication_create_ats_application_request_answerspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationCreateAtsApplicationRequest`](./factorial_python_sdk/type/application_create_ats_application_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AtsApplication`](./factorial_python_sdk/pydantic/ats_application.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/applications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.application.update_data`<a id="factorialapplicationupdate_data"></a>

Update ATS Application data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_data_response = factorial.application.update_data(
    id="3",
    ats_application_phase_id=1,
    qualified=True,
    first_name="Bob",
    last_name="Stone",
    phone="1134124214",
    email="bob_stone@factorial.co",
    personal_url="www.linkedin.com/awesome",
    disqualified_reason="not_a_fit",
    cv="cv.pdf",
    photo="photo.jpeg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### ats_application_phase_id: `int`<a id="ats_application_phase_id-int"></a>

##### qualified: `bool`<a id="qualified-bool"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### email: `str`<a id="email-str"></a>

##### personal_url: `str`<a id="personal_url-str"></a>

##### disqualified_reason: `str`<a id="disqualified_reason-str"></a>

##### cv: `IO`<a id="cv-io"></a>

##### photo: `IO`<a id="photo-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationUpdateDataRequest`](./factorial_python_sdk/type/application_update_data_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AtsApplication`](./factorial_python_sdk/pydantic/ats_application.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/applications/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.attendance.create_new`<a id="factorialattendancecreate_new"></a>

Creates Attendance

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = factorial.attendance.create_new(
    employee_id=5,
    clock_in="2019-01-01T12:12:01-02:00",
    clock_out="2019-01-01T14:12:01-02:00",
    observations="First Attendance",
    location_type="office",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### clock_in: `str`<a id="clock_in-str"></a>

##### clock_out: `str`<a id="clock_out-str"></a>

##### observations: `str`<a id="observations-str"></a>

##### location_type: `str`<a id="location_type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AttendanceCreateNewRequest`](./factorial_python_sdk/type/attendance_create_new_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Attendance`](./factorial_python_sdk/pydantic/attendance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time/attendance` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.attendance.get_bulk_v2`<a id="factorialattendanceget_bulk_v2"></a>

This endpoint allows you retrieve bulk attendance V2

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bulk_v2_response = factorial.attendance.get_bulk_v2()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceGetBulkV2Response`](./factorial_python_sdk/pydantic/attendance_get_bulk_v2_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/bulk/attendance` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.attendance.get_company_attendance`<a id="factorialattendanceget_company_attendance"></a>

Get attendance from a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_attendance_response = factorial.attendance.get_company_attendance(
    employee_ids_=[1],
    date_from="2023-01-03",
    date_to="2023-01-04",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids_: List[`int`]<a id="employee_ids_-listint"></a>

Employees id array

##### date_from: `str`<a id="date_from-str"></a>

It should be a valid date following the format YYYY-MM-DD

##### date_to: `str`<a id="date_to-str"></a>

It should be a valid date following the format YYYY-MM-DD

#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceGetCompanyAttendanceResponse`](./factorial_python_sdk/pydantic/attendance_get_company_attendance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time/attendance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.break.create_break`<a id="factorialbreakcreate_break"></a>

Creates a break with the break_start and break_end time

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_break_response = factorial.break.create_break(
    employee_id=5,
    break_start="2022-06-23T12:12:01-02:00",
    break_end="2022-06-23T13:12:01-02:00",
    observations="New observation",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### break_start: `str`<a id="break_start-str"></a>

##### break_end: `str`<a id="break_end-str"></a>

##### observations: `str`<a id="observations-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BreakCreateBreakRequest`](./factorial_python_sdk/type/break_create_break_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Attendance`](./factorial_python_sdk/pydantic/attendance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/breaks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.break.end_break`<a id="factorialbreakend_break"></a>

End a break

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
end_break_response = factorial.break.end_break(
    now="2022-06-23T11:00:00.000+00:00",
    employee_id=3,
    observations="Updated break observation",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### now: `str`<a id="now-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### observations: `str`<a id="observations-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BreakEndBreakRequest`](./factorial_python_sdk/type/break_end_break_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Attendance`](./factorial_python_sdk/pydantic/attendance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/breaks/end` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.break.start_break`<a id="factorialbreakstart_break"></a>

Start a break

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
start_break_response = factorial.break.start_break(
    now="2022-06-23T11:00:00.000+00:00",
    employee_id=3,
    observations="New break observation",
    time_settings_break_configuration_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### now: `str`<a id="now-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### observations: `str`<a id="observations-str"></a>

##### time_settings_break_configuration_id: `Optional[int]`<a id="time_settings_break_configuration_id-optionalint"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BreakStartBreakRequest`](./factorial_python_sdk/type/break_start_break_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Attendance`](./factorial_python_sdk/pydantic/attendance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/breaks/start` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.candidate.create_new_candidate`<a id="factorialcandidatecreate_new_candidate"></a>

Create candidates related to a particular company in an ATS

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_candidate_response = factorial.candidate.create_new_candidate(
    first_name="Bob",
    last_name="Stone",
    email="bob_stone@factorial.co",
    source="indeed",
    medium="LinkedIn",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email: `str`<a id="email-str"></a>

##### source: `str`<a id="source-str"></a>

##### medium: `str`<a id="medium-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CandidateCreateNewCandidateRequest`](./factorial_python_sdk/type/candidate_create_new_candidate_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AtsCandidate`](./factorial_python_sdk/pydantic/ats_candidate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/candidates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.candidate.delete_existing_candidate`<a id="factorialcandidatedelete_existing_candidate"></a>

Deletes an existing candidate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_existing_candidate_response = factorial.candidate.delete_existing_candidate(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`AtsCandidate`](./factorial_python_sdk/pydantic/ats_candidate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/candidates/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.candidate.list_all_candidates`<a id="factorialcandidatelist_all_candidates"></a>

Fetch candidates data from Factorial. When using administrator-level API Credentials, all candidates associated with a company will be returned. When using non-admin level API credentials, only candidates that applied to a job for which the user is a hiring manager will be returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_candidates_response = factorial.candidate.list_all_candidates()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CandidateListAllCandidatesResponse`](./factorial_python_sdk/pydantic/candidate_list_all_candidates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/candidates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.candidate.update_candidate_data`<a id="factorialcandidateupdate_candidate_data"></a>

Update ATS Candidates data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_candidate_data_response = factorial.candidate.update_candidate_data(
    id="3",
    first_name="Bob",
    last_name="Stone",
    email="bob_stone@factorial.co",
    talent_pool=True,
    consent_to_talent_pool=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email: `str`<a id="email-str"></a>

##### talent_pool: `bool`<a id="talent_pool-bool"></a>

##### consent_to_talent_pool: `bool`<a id="consent_to_talent_pool-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CandidateUpdateCandidateDataRequest`](./factorial_python_sdk/type/candidate_update_candidate_data_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AtsCandidate`](./factorial_python_sdk/pydantic/ats_candidate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/candidates/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.compensation.create_contract_compensation`<a id="factorialcompensationcreate_contract_compensation"></a>

Creates a compensation for a contract.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_contract_compensation_response = factorial.compensation.create_contract_compensation(
    contract_version_id=2,
    description="Meal 2",
    contracts_taxonomy_id=2,
    compensation_type="fixed",
    amount=2112,
    unit="money",
    sync_with_supplements=True,
    payroll_policy_id=2,
    recurrence_count=2,
    starts_on="2022-08-02",
    recurrence="monthly",
    first_payment_on="2022-08-02",
    calculation="current_period",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contract_version_id: `int`<a id="contract_version_id-int"></a>

##### description: `str`<a id="description-str"></a>

##### contracts_taxonomy_id: `int`<a id="contracts_taxonomy_id-int"></a>

##### compensation_type: `str`<a id="compensation_type-str"></a>

##### amount: `int`<a id="amount-int"></a>

##### unit: `str`<a id="unit-str"></a>

##### sync_with_supplements: `bool`<a id="sync_with_supplements-bool"></a>

##### payroll_policy_id: `int`<a id="payroll_policy_id-int"></a>

##### recurrence_count: `int`<a id="recurrence_count-int"></a>

##### starts_on: `str`<a id="starts_on-str"></a>

##### recurrence: `str`<a id="recurrence-str"></a>

##### first_payment_on: `str`<a id="first_payment_on-str"></a>

##### calculation: `str`<a id="calculation-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompensationCreateContractCompensationRequest`](./factorial_python_sdk/type/compensation_create_contract_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./factorial_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/compensations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.compensation.delete_compensation`<a id="factorialcompensationdelete_compensation"></a>

Delete a compensation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_compensation_response = factorial.compensation.delete_compensation(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationDeleteCompensationResponse`](./factorial_python_sdk/pydantic/compensation_delete_compensation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/compensations/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.compensation.get_by_id`<a id="factorialcompensationget_by_id"></a>

This endpoint allows you to retrieve a compensation by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.compensation.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./factorial_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/compensations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.compensation.get_compensations`<a id="factorialcompensationget_compensations"></a>

This endpoint allows you to retrieve compensations for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compensations_response = factorial.compensation.get_compensations(
    ids=[1],
    contract_version_ids=[1],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: List[`int`]<a id="ids-listint"></a>

Compensations id array

##### contract_version_ids: List[`int`]<a id="contract_version_ids-listint"></a>

Contract versions id array

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationGetCompensationsResponse`](./factorial_python_sdk/pydantic/compensation_get_compensations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/compensations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.compensation.update_for_contract`<a id="factorialcompensationupdate_for_contract"></a>

Updates a compensation for a contract.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_for_contract_response = factorial.compensation.update_for_contract(
    id=1,
    description="Meal 2",
    contracts_taxonomy_id=2,
    compensation_type="fixed",
    amount=2112,
    unit="money",
    sync_with_supplements=True,
    payroll_policy_id=2,
    recurrence_count=2,
    starts_on="2022-08-02",
    recurrence="monthly",
    first_payment_on="2022-08-02",
    calculation="current_period",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### description: `str`<a id="description-str"></a>

##### contracts_taxonomy_id: `int`<a id="contracts_taxonomy_id-int"></a>

##### compensation_type: `str`<a id="compensation_type-str"></a>

##### amount: `int`<a id="amount-int"></a>

##### unit: `str`<a id="unit-str"></a>

##### sync_with_supplements: `bool`<a id="sync_with_supplements-bool"></a>

##### payroll_policy_id: `int`<a id="payroll_policy_id-int"></a>

##### recurrence_count: `int`<a id="recurrence_count-int"></a>

##### starts_on: `str`<a id="starts_on-str"></a>

##### recurrence: `str`<a id="recurrence-str"></a>

##### first_payment_on: `str`<a id="first_payment_on-str"></a>

##### calculation: `str`<a id="calculation-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompensationUpdateForContractRequest`](./factorial_python_sdk/type/compensation_update_for_contract_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./factorial_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/compensations/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.contract.delete_version`<a id="factorialcontractdelete_version"></a>

Delete contract Version

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_version_response = factorial.contract.delete_version(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`ContractVersion`](./factorial_python_sdk/pydantic/contract_version.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/contract_versions/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.contract.get_all_reference_contracts`<a id="factorialcontractget_all_reference_contracts"></a>

The reference contract is the contract that applies today. If no contract applies today, we will return the nearest upcoming contract. If there are no upcoming contracts, we will provide the most recent past contract.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_reference_contracts_response = factorial.contract.get_all_reference_contracts(
    employee_ids_=[1],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids_: List[`int`]<a id="employee_ids_-listint"></a>

Employees id array

#### 🔄 Return<a id="🔄-return"></a>

[`ContractGetAllReferenceContractsResponse`](./factorial_python_sdk/pydantic/contract_get_all_reference_contracts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/reference_contracts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.contract.update_version`<a id="factorialcontractupdate_version"></a>

Update contract Version

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_version_response = factorial.contract.update_version(
    effective_on="2022-04-22",
    id="3",
    employee_id=5,
    starts_on="2021-04-22",
    ends_on="2023-04-22",
    working_hours_frequency="week",
    working_week_days="friday,tuesday,saturday",
    working_hours=800,
    salary_frequency="yearly",
    salary_amount=5000000,
    job_title="Jr Software Developer",
    es_cotization_group=1,
    es_professional_category_id=2,
    es_education_level_id=4,
    es_contract_type_id=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_on: `str`<a id="effective_on-str"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### employee_id: `int`<a id="employee_id-int"></a>

##### starts_on: `str`<a id="starts_on-str"></a>

##### ends_on: `str`<a id="ends_on-str"></a>

##### working_hours_frequency: `str`<a id="working_hours_frequency-str"></a>

##### working_week_days: `str`<a id="working_week_days-str"></a>

##### working_hours: `int`<a id="working_hours-int"></a>

##### salary_frequency: `str`<a id="salary_frequency-str"></a>

##### salary_amount: `int`<a id="salary_amount-int"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### es_cotization_group: `Optional[int]`<a id="es_cotization_group-optionalint"></a>

the cotization group id for Spain contracts

##### es_professional_category_id: `Optional[int]`<a id="es_professional_category_id-optionalint"></a>

the professional category id for Spain contracts

##### es_education_level_id: `Optional[int]`<a id="es_education_level_id-optionalint"></a>

the education level id for Spain contracts

##### es_contract_type_id: `Optional[int]`<a id="es_contract_type_id-optionalint"></a>

the contract type id for Spain contracts

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractUpdateVersionRequest`](./factorial_python_sdk/type/contract_update_version_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContractVersion`](./factorial_python_sdk/pydantic/contract_version.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/contract_versions/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.contract_version.create_new_version`<a id="factorialcontract_versioncreate_new_version"></a>

Create contract Versions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_version_response = factorial.contract_version.create_new_version(
    effective_on="2022-04-22",
    employee_id=5,
    starts_on="2021-04-22",
    ends_on="2023-04-22",
    working_hours_frequency="week",
    working_week_days="friday,tuesday,saturday",
    working_hours=800,
    salary_frequency="yearly",
    salary_amount=5000000,
    job_title="Jr Software Developer",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_on: `str`<a id="effective_on-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### starts_on: `str`<a id="starts_on-str"></a>

##### ends_on: `str`<a id="ends_on-str"></a>

##### working_hours_frequency: `str`<a id="working_hours_frequency-str"></a>

##### working_week_days: `str`<a id="working_week_days-str"></a>

##### working_hours: `int`<a id="working_hours-int"></a>

##### salary_frequency: `str`<a id="salary_frequency-str"></a>

##### salary_amount: `int`<a id="salary_amount-int"></a>

##### job_title: `str`<a id="job_title-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractVersionCreateNewVersionRequest`](./factorial_python_sdk/type/contract_version_create_new_version_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContractVersion`](./factorial_python_sdk/pydantic/contract_version.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/contract_versions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.contract_version.get_all_versions`<a id="factorialcontract_versionget_all_versions"></a>

Get all contract Versions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_versions_response = factorial.contract_version.get_all_versions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ContractVersionGetAllVersionsResponse`](./factorial_python_sdk/pydantic/contract_version_get_all_versions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/contract_versions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.contract_version.get_bulk_versions`<a id="factorialcontract_versionget_bulk_versions"></a>

This endpoint allows you retrieve bulk contract versions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bulk_versions_response = factorial.contract_version.get_bulk_versions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ContractVersionGetBulkVersionsResponse`](./factorial_python_sdk/pydantic/contract_version_get_bulk_versions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/bulk/contract_version` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field.create_field`<a id="factorialcustom_fieldcreate_field"></a>

This endpoint allows you to create custom fields you must provide these parameters
- label: custom field visible name for example `T shirt size` - slug_name: the resource that you want to save the custom field, for example to save `t-shirt size` field in employee you must use `employees-questions` value - field_type: the kind of field value you want to store: text (input), long text (text area), number (input number) or single choice (select input) - required: You can set if the field is mandatory - visible: You can set the roles can see the field (own, reportees, team leader or everybody) - editable: You can set the roles can edit the field (own, reportees, team leader or everybody) - choice_options: You can provide an array of choices to set the options of a single choice field

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_field_response = factorial.custom_field.create_field(
    label="t shirt",
    slug_name="employees-questions",
    field_type="text",
    required=True,
    editable="text",
    visible="text",
    min_value=1,
    max_value=100,
    choice_options=[
        {
            "label": "red",
            "is_active": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

##### slug_name: `str`<a id="slug_name-str"></a>

##### field_type: `str`<a id="field_type-str"></a>

##### required: `bool`<a id="required-bool"></a>

##### editable: `str`<a id="editable-str"></a>

##### visible: `str`<a id="visible-str"></a>

##### min_value: `int`<a id="min_value-int"></a>

##### max_value: `int`<a id="max_value-int"></a>

##### choice_options: [`CustomFieldCreateFieldRequestChoiceOptions`](./factorial_python_sdk/type/custom_field_create_field_request_choice_options.py)<a id="choice_options-customfieldcreatefieldrequestchoiceoptionsfactorial_python_sdktypecustom_field_create_field_request_choice_optionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldCreateFieldRequest`](./factorial_python_sdk/type/custom_field_create_field_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldV2`](./factorial_python_sdk/pydantic/custom_field_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/custom_fields/fields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field.delete_by_id`<a id="factorialcustom_fielddelete_by_id"></a>

Delete a custom field by its id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = factorial.custom_field.delete_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldDeleteByIdResponse`](./factorial_python_sdk/pydantic/custom_field_delete_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/custom_fields/fields/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field.get_fields_by_group`<a id="factorialcustom_fieldget_fields_by_group"></a>

This endpoint allows you to fetch a collection of custom fields. The fields you receive in the response are governed by the `field_group` you supply in the body of your request.
For now, there are 2 acceptable field groups:

 - `employees-questions` which refers to fields relating to an employee

 - `time-tracking-projects` which refers to fields relating to time tracking data

 - `contract-versions` which refers to fields relating to employee contract versions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_by_group_response = factorial.custom_field.get_fields_by_group(
    field_group="employees-questions",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_group: `str`<a id="field_group-str"></a>

Available options: employees-questions (Employee's fields) time-tracking-projects (Shift's project)' contract-versions (Contract versions)'

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldGetFieldsByGroupResponse`](./factorial_python_sdk/pydantic/custom_field_get_fields_by_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field.get_fields_by_slug`<a id="factorialcustom_fieldget_fields_by_slug"></a>

This endpoint allows you to retrieve custom fields by id, label, slug name, slug name. You receive fields tagged in the response by a slug.
For now, there is one acceptable slug name:

 - `employees-questions` which refers to fields relating to an employee

 You can filter by:

 - id: You can query a field by its id. For example `T-shirt size` identifier is 4. you can search the custom field by the id 4.
 - label: you can query a field by its label for example `T shirt size`
 - slug_name: You can use the available slug `employees-questions` in the `slug_name` field to filter fields that belong to this slug.
 - slug_id: It is the identifier of the slug_name. You can use the id of a slug to query custom fields by its id instead of its name.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_by_slug_response = factorial.custom_field.get_fields_by_slug(
    id=1,
    label="tshirt size",
    slug_id=1,
    slug_name="employees-questions",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### label: `str`<a id="label-str"></a>

##### slug_id: `int`<a id="slug_id-int"></a>

##### slug_name: `str`<a id="slug_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldGetFieldsBySlugResponse`](./factorial_python_sdk/pydantic/custom_field_get_fields_by_slug_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/custom_fields/fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field_value.create_custom_value`<a id="factorialcustom_field_valuecreate_custom_value"></a>

As described, a `Custom Field Value` can be thought of as an answer/response to a `Custom Field` these answers/responses belong to the entity that inputed the values e.g. an employee who answered the t-shirt size question by filling it out in their factorial dashboard.
This endpoint allows you to create values for custom fields. It requires an `instance_id` which refers to the `id` of the entity that owns this `Custom Value` e.g. an Employee for which the `employee_id` will correspond to the `instance_id`. It also requires a `field_id` to reference the `Custom Field` which this value is related to.
You can think of `Custom Fields` and `Custom Values` as questions and answers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_value_response = factorial.custom_field_value.create_custom_value(
    value="somelinktomyportfolio.com",
    field_id=1,
    instance_id=23,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### value: `str`<a id="value-str"></a>

##### field_id: `int`<a id="field_id-int"></a>

##### instance_id: `int`<a id="instance_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldValueCreateCustomValueRequest`](./factorial_python_sdk/type/custom_field_value_create_custom_value_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomValue`](./factorial_python_sdk/pydantic/custom_value.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/custom_fields/values` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field_value.get_by_slug_name`<a id="factorialcustom_field_valueget_by_slug_name"></a>

This endpoint allows you to retrieve custom fields by id, label, slug name, slug name. You receive fields tagged in the response by a slug.
For now, there is one acceptable slug name:

 - `employees-questions` which refers to fields relating to an employee

 You can filter by:

 - id: You can query a field value by its id. For example identity card value `12345678Z` identifier is 4. you can search the custom field by the id 4.
 - value: You can query a field by value. For example an employee have a custom field which is "Computer" and it's value is "PC" you can search it by this value.
 - slug_name: You can use the available slug `employees-questions` in the `slug_name` field to filter custom field values that belong to this slug.
 - slug_id: It is the identifier of the slug_name. You can use the id of a slug to query custom fields values by its slug id instead of its slug name.
 - field_id: You can use the available field id to filter custom field values that belong to this field.
 - employee_ids: You can use the available employee ids to filter custom field values that belong to these employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_slug_name_response = factorial.custom_field_value.get_by_slug_name(
    id=1,
    slug_id=1,
    field_id=1,
    slug_name="employees-questions",
    field_value="red",
    employee_ids_=[1],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### slug_id: `int`<a id="slug_id-int"></a>

##### field_id: `int`<a id="field_id-int"></a>

##### slug_name: `str`<a id="slug_name-str"></a>

##### field_value: `str`<a id="field_value-str"></a>

##### employee_ids_: List[`int`]<a id="employee_ids_-listint"></a>

Employees id array

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldValueGetBySlugNameResponse`](./factorial_python_sdk/pydantic/custom_field_value_get_by_slug_name_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/custom_fields/values` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field_value.get_instance_value`<a id="factorialcustom_field_valueget_instance_value"></a>

Given a custom field, get the value for a specific instance

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instance_value_response = factorial.custom_field_value.get_instance_value(
    field_id=1,
    instance_id=23,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_id: `int`<a id="field_id-int"></a>

##### instance_id: `int`<a id="instance_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CustomValue`](./factorial_python_sdk/pydantic/custom_value.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/custom_fields/values` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_field_value.update_value`<a id="factorialcustom_field_valueupdate_value"></a>

This endpoint allows you to update custom fields values

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_value_response = factorial.custom_field_value.update_value(
    id=1,
    value="l",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

##### value: `str`<a id="value-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldValueUpdateValueRequest`](./factorial_python_sdk/type/custom_field_value_update_value_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldV2`](./factorial_python_sdk/pydantic/custom_field_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/custom_fields/values/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.custom_table.get`<a id="factorialcustom_tableget"></a>

This endpoint allows you to retrieve Custom Tables

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = factorial.custom_table.get(
    topic_name="employee",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_name: `str`<a id="topic_name-str"></a>

Filters by topic_name

#### 🔄 Return<a id="🔄-return"></a>

[`CustomTableGetResponse`](./factorial_python_sdk/pydantic/custom_table_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/custom/tables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.document.create_new_document`<a id="factorialdocumentcreate_new_document"></a>

Create a Document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_document_response = factorial.document.create_new_document(
    filename="payslip.pdf",
    file="payslip.pdf",
    employee_id=1,
    folder_id=1,
    request_esignature=True,
    public=True,
    signees=[
        1
    ],
    is_pending_assignment=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filename: `str`<a id="filename-str"></a>

##### file: `IO`<a id="file-io"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### folder_id: `int`<a id="folder_id-int"></a>

##### request_esignature: `bool`<a id="request_esignature-bool"></a>

##### public: `bool`<a id="public-bool"></a>

##### signees: [`DocumentCreateNewDocumentRequestSignees`](./factorial_python_sdk/type/document_create_new_document_request_signees.py)<a id="signees-documentcreatenewdocumentrequestsigneesfactorial_python_sdktypedocument_create_new_document_request_signeespy"></a>

##### is_pending_assignment: `bool`<a id="is_pending_assignment-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentCreateNewDocumentRequest`](./factorial_python_sdk/type/document_create_new_document_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./factorial_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.document.delete_by_id`<a id="factorialdocumentdelete_by_id"></a>

Delete a Document by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = factorial.document.delete_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./factorial_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/documents/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.document.get_by_id`<a id="factorialdocumentget_by_id"></a>

Get a Document by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.document.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./factorial_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/documents/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.document.list_given_employee_or_folder`<a id="factorialdocumentlist_given_employee_or_folder"></a>

Get a collection of Documents given an employee or a folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_given_employee_or_folder_response = factorial.document.list_given_employee_or_folder(
    employee_id=1,
    folder_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

Retrieves the list of documents by employee id

##### folder_id: `int`<a id="folder_id-int"></a>

Retrieves the list of documents by folder id

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentListGivenEmployeeOrFolderResponse`](./factorial_python_sdk/pydantic/document_list_given_employee_or_folder_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.document.update_by_id`<a id="factorialdocumentupdate_by_id"></a>

Update a Document by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = factorial.document.update_by_id(
    id="1",
    public=True,
    employee_id=1,
    folder_id=1,
    request_esignature=False,
    signees=[
        1
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### public: `bool`<a id="public-bool"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### folder_id: `int`<a id="folder_id-int"></a>

##### request_esignature: `bool`<a id="request_esignature-bool"></a>

##### signees: [`DocumentUpdateByIdRequestSignees`](./factorial_python_sdk/type/document_update_by_id_request_signees.py)<a id="signees-documentupdatebyidrequestsigneesfactorial_python_sdktypedocument_update_by_id_request_signeespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentUpdateByIdRequest`](./factorial_python_sdk/type/document_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./factorial_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/documents/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.assign_to_team`<a id="factorialemployeeassign_to_team"></a>

Assign an employee to a team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_to_team_response = factorial.employee.assign_to_team(
    id="1",
    employee_id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### employee_id: `str`<a id="employee_id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./factorial_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams/{id}/employees/{employee_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.change_email`<a id="factorialemployeechange_email"></a>

Changes the email only if the employee has not been confirmed and it does not exist another employee with the requested email.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_email_response = factorial.employee.change_email(
    email="bob_stone1@factorial.co",
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeChangeEmailRequest`](./factorial_python_sdk/type/employee_change_email_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV2`](./factorial_python_sdk/pydantic/employee_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees/{id}/email` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.create_custom_table_value`<a id="factorialemployeecreate_custom_table_value"></a>

This endpoint is used to create and store custom values on custom fields used in custom tables. See custom values for more information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_table_value_response = factorial.employee.create_custom_table_value(
    id=86,
    emloyee_id=10,
    id=1,
    employee_id=3,
    table_values=[
        {
            "id": 1,
            "value": "This is a custom value for a custom field",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

##### employee_id: `int`<a id="employee_id-int"></a>

(Required)

##### requestBody: [`EmployeeCreateCustomTableValueRequest`](./factorial_python_sdk/type/employee_create_custom_table_value_request.py)<a id="requestbody-employeecreatecustomtablevaluerequestfactorial_python_sdktypeemployee_create_custom_table_value_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CustomResourceValue`](./factorial_python_sdk/pydantic/custom_resource_value.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/custom/tables/{id}/values/{employee_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.create_employee`<a id="factorialemployeecreate_employee"></a>

Create employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employee_response = factorial.employee.create_employee(
    email="bob_stone@factorial.co",
    first_name="Bob",
    last_name="Stone",
    birthday_on="2000-01-08",
    start_date="2022-01-08",
    regular_access_starts_on="2022-01-08",
    manager_id=5,
    role="basic",
    timeoff_manager_id=5,
    terminated_on="2022-01-08",
    termination_reason="behaviour",
    company_identifier="124ABC",
    phone_number="622564089",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### birthday_on: `str`<a id="birthday_on-str"></a>

##### start_date: `str`<a id="start_date-str"></a>

##### regular_access_starts_on: `str`<a id="regular_access_starts_on-str"></a>

##### manager_id: `int`<a id="manager_id-int"></a>

##### role: `str`<a id="role-str"></a>

##### timeoff_manager_id: `int`<a id="timeoff_manager_id-int"></a>

##### terminated_on: `str`<a id="terminated_on-str"></a>

##### termination_reason: `str`<a id="termination_reason-str"></a>

##### company_identifier: `str`<a id="company_identifier-str"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeCreateEmployeeRequest`](./factorial_python_sdk/type/employee_create_employee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./factorial_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.create_new`<a id="factorialemployeecreate_new"></a>

Create employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = factorial.employee.create_new(
    email="bob_stone@factorial.co",
    first_name="Bob",
    last_name="Stone",
    birthday_on="2000-01-08",
    role="basic",
    gender="female",
    identifier="Y7729503E",
    identifier_type="nie",
    nationality="es",
    bank_number="ES09 4595 6109 8115 7760 8354",
    country="es",
    city="Barcelona",
    state="Barcelona",
    postal_code="08007",
    address_line_1="c/ Tallers 123",
    address_line_2="Atic 5",
    swift_bic="1234567890",
    company_id=5,
    manager_id=5,
    location_id=5,
    timeoff_manager_id=5,
    legal_entity_id=765,
    company_identifier="124ABC",
    phone_number="622564089",
    social_security_number="223948780514",
    tax_id="121232323",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### birthday_on: `str`<a id="birthday_on-str"></a>

##### role: `str`<a id="role-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### identifier: `str`<a id="identifier-str"></a>

##### identifier_type: `str`<a id="identifier_type-str"></a>

##### nationality: `str`<a id="nationality-str"></a>

##### bank_number: `str`<a id="bank_number-str"></a>

##### country: `str`<a id="country-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### postal_code: `str`<a id="postal_code-str"></a>

##### address_line_1: `str`<a id="address_line_1-str"></a>

##### address_line_2: `str`<a id="address_line_2-str"></a>

##### swift_bic: `str`<a id="swift_bic-str"></a>

##### company_id: `int`<a id="company_id-int"></a>

##### manager_id: `int`<a id="manager_id-int"></a>

##### location_id: `int`<a id="location_id-int"></a>

##### timeoff_manager_id: `int`<a id="timeoff_manager_id-int"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### company_identifier: `str`<a id="company_identifier-str"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### social_security_number: `str`<a id="social_security_number-str"></a>

##### tax_id: `str`<a id="tax_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeCreateNewRequest`](./factorial_python_sdk/type/employee_create_new_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV2`](./factorial_python_sdk/pydantic/employee_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.get_all_employees`<a id="factorialemployeeget_all_employees"></a>

Only `admins` can see all the employees' information, `regular users` will get a restricted version of the payload as a response based on the permission set by the admin

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_employees_response = factorial.employee.get_all_employees(
    full_text_name="Bob Stone",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### full_text_name: `str`<a id="full_text_name-str"></a>

Retrieves the list of employees by full names

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetAllEmployeesResponse`](./factorial_python_sdk/pydantic/employee_get_all_employees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.get_bulk_v2`<a id="factorialemployeeget_bulk_v2"></a>

This endpoint allows you retrieve bulk employees V2

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bulk_v2_response = factorial.employee.get_bulk_v2()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetBulkV2Response`](./factorial_python_sdk/pydantic/employee_get_bulk_v2_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/bulk/employee` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.get_by_id`<a id="factorialemployeeget_by_id"></a>

Only admins can see all the employees' information, regular users will get a restricted version of the payload as a response based on the permission set by the admin

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.employee.get_by_id(
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV2`](./factorial_python_sdk/pydantic/employee_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.get_by_payroll_integration_code`<a id="factorialemployeeget_by_payroll_integration_code"></a>

This endpoint allows fetching an Employee through a Payroll Integration Code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_payroll_integration_code_response = factorial.employee.get_by_payroll_integration_code(
    id="3",
    integration="a3innuva",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### integration: `str`<a id="integration-str"></a>

Payroll Integration name

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetByPayrollIntegrationCodeResponse`](./factorial_python_sdk/pydantic/employee_get_by_payroll_integration_code_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payroll_integrations/codes/{id}/find_employee` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.get_custom_table_values`<a id="factorialemployeeget_custom_table_values"></a>

This endpoint allows you retrieve Custom Table Values for an employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_table_values_response = factorial.employee.get_custom_table_values(
    id=1,
    employee_id=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

##### employee_id: `int`<a id="employee_id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetCustomTableValuesResponse`](./factorial_python_sdk/pydantic/employee_get_custom_table_values_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/custom/tables/{id}/values/{employee_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.get_employee_by_id`<a id="factorialemployeeget_employee_by_id"></a>

Only admins can see all the employees' information, regular users will get a restricted version of the payload as a response based on the permission set by the admin

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_by_id_response = factorial.employee.get_employee_by_id(
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./factorial_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.get_employees`<a id="factorialemployeeget_employees"></a>

Only `admins` can see all the employees' information, `regular users` will get a restricted version of the payload as a response based on the permission set by the admin

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employees_response = factorial.employee.get_employees()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetEmployeesResponse`](./factorial_python_sdk/pydantic/employee_get_employees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.list_break_configurations_for_dates`<a id="factorialemployeelist_break_configurations_for_dates"></a>

List all the posible break configurations to be used optionally in the break start

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_break_configurations_for_dates_response = factorial.employee.list_break_configurations_for_dates(
    start_at="2023-09-30",
    end_at="2023-09-30",
    employee_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_at: `str`<a id="start_at-str"></a>

##### end_at: `str`<a id="end_at-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeListBreakConfigurationsForDatesResponse`](./factorial_python_sdk/pydantic/employee_list_break_configurations_for_dates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/break_configurations_for_dates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.list_family_situations`<a id="factorialemployeelist_family_situations"></a>

Get all family situations - only FR employees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_family_situations_response = factorial.employee.list_family_situations(
    employee_id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Get all family situations given an employee

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeListFamilySituationsResponse`](./factorial_python_sdk/pydantic/employee_list_family_situations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/family_situation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.send_invitation_email`<a id="factorialemployeesend_invitation_email"></a>

When inviting an employee an email is sent to their email. You can resend the email as long as the employee has not accepted the invitation yet.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_invitation_email_response = factorial.employee.send_invitation_email(
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV2`](./factorial_python_sdk/pydantic/employee_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees/{id}/invite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.set_termination_details`<a id="factorialemployeeset_termination_details"></a>

Set the termination date and other termination related parameters for an employee. The employee will finally terminate on the date provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_termination_details_response = factorial.employee.set_termination_details(
    terminated_on="2023-02-08",
    id="5",
    termination_reason="a termination reason",
    termination_reason_type="company",
    termination_assigned_manager_id=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### terminated_on: `str`<a id="terminated_on-str"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### termination_reason: `str`<a id="termination_reason-str"></a>

##### termination_reason_type: `str`<a id="termination_reason_type-str"></a>

##### termination_assigned_manager_id: `int`<a id="termination_assigned_manager_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeSetTerminationDetailsRequest`](./factorial_python_sdk/type/employee_set_termination_details_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV2`](./factorial_python_sdk/pydantic/employee_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees/{id}/terminate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.terminate_employee`<a id="factorialemployeeterminate_employee"></a>

Terminate employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
terminate_employee_response = factorial.employee.terminate_employee(
    id="5",
    terminated_on="1992-05-02",
    termination_reason="Behaviour",
    termination_assigned_manager_id=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### terminated_on: `str`<a id="terminated_on-str"></a>

##### termination_reason: `str`<a id="termination_reason-str"></a>

##### termination_assigned_manager_id: `int`<a id="termination_assigned_manager_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeTerminateEmployeeRequest`](./factorial_python_sdk/type/employee_terminate_employee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./factorial_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{id}/terminate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.unassign_to_team`<a id="factorialemployeeunassign_to_team"></a>

Unassign employee to team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unassign_to_team_response = factorial.employee.unassign_to_team(
    id="1",
    employee_id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### employee_id: `str`<a id="employee_id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./factorial_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams/{id}/employees/{employee_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.unterminate_employee`<a id="factorialemployeeunterminate_employee"></a>

Unterminate employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unterminate_employee_response = factorial.employee.unterminate_employee(
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./factorial_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{id}/unterminate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.unterminate_post`<a id="factorialemployeeunterminate_post"></a>

Unterminate the employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unterminate_post_response = factorial.employee.unterminate_post(
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV2`](./factorial_python_sdk/pydantic/employee_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees/{id}/unterminate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.update_by_id`<a id="factorialemployeeupdate_by_id"></a>

Update employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = factorial.employee.update_by_id(
    id="5",
    first_name="Bob",
    last_name="Stone",
    manager_id=5,
    role="basic",
    timeoff_manager_id=5,
    company_identifier="124ABC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### manager_id: `int`<a id="manager_id-int"></a>

##### role: `str`<a id="role-str"></a>

##### timeoff_manager_id: `int`<a id="timeoff_manager_id-int"></a>

##### company_identifier: `str`<a id="company_identifier-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeUpdateByIdRequest`](./factorial_python_sdk/type/employee_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./factorial_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.update_employee_by_id`<a id="factorialemployeeupdate_employee_by_id"></a>

Update employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_by_id_response = factorial.employee.update_employee_by_id(
    id="5",
    email="bob_stone@factorial.co",
    first_name="Bob",
    last_name="Stone",
    birthday_on="2000-01-08",
    role="basic",
    gender="female",
    identifier="Y7729503E",
    identifier_type="nie",
    nationality="es",
    bank_number="ES09 4595 6109 8115 7760 8354",
    country="es",
    city="Barcelona",
    state="Barcelona",
    postal_code="08007",
    address_line_1="c/ Tallers 123",
    address_line_2="Atic 5",
    swift_bic="1234567890",
    manager_id=5,
    location_id=5,
    timeoff_manager_id=5,
    phone_number="678901234",
    social_security_number=223948780514,
    legal_entity_id=235,
    company_identifier="124ABC",
    contact_name="John",
    contact_number="678901234",
    tax_id="121232323",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### email: `str`<a id="email-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### birthday_on: `str`<a id="birthday_on-str"></a>

##### role: `str`<a id="role-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### identifier: `str`<a id="identifier-str"></a>

##### identifier_type: `str`<a id="identifier_type-str"></a>

##### nationality: `str`<a id="nationality-str"></a>

##### bank_number: `str`<a id="bank_number-str"></a>

##### country: `str`<a id="country-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### postal_code: `str`<a id="postal_code-str"></a>

##### address_line_1: `str`<a id="address_line_1-str"></a>

##### address_line_2: `str`<a id="address_line_2-str"></a>

##### swift_bic: `str`<a id="swift_bic-str"></a>

##### manager_id: `int`<a id="manager_id-int"></a>

##### location_id: `int`<a id="location_id-int"></a>

##### timeoff_manager_id: `int`<a id="timeoff_manager_id-int"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### social_security_number: `int`<a id="social_security_number-int"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### company_identifier: `str`<a id="company_identifier-str"></a>

##### contact_name: `str`<a id="contact_name-str"></a>

##### contact_number: `str`<a id="contact_number-str"></a>

##### tax_id: `str`<a id="tax_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeUpdateEmployeeByIdRequest`](./factorial_python_sdk/type/employee_update_employee_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV2`](./factorial_python_sdk/pydantic/employee_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/employees/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.employee.update_in_team`<a id="factorialemployeeupdate_in_team"></a>

Update an employee in a team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_in_team_response = factorial.employee.update_in_team(
    id="1",
    employee_id="1",
    lead=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### employee_id: `str`<a id="employee_id-str"></a>

(Required)

##### lead: `bool`<a id="lead-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeUpdateInTeamRequest`](./factorial_python_sdk/type/employee_update_in_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./factorial_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams/{id}/employees/{employee_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.event.get_triggered_events`<a id="factorialeventget_triggered_events"></a>

Get triggered events

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_triggered_events_response = factorial.event.get_triggered_events()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EventGetTriggeredEventsResponse`](./factorial_python_sdk/pydantic/event_get_triggered_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.expense.get_by_id`<a id="factorialexpenseget_by_id"></a>

This endpoint allows you to retrieve an expense by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.expense.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Expense`](./factorial_python_sdk/pydantic/expense.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/finance/expenses/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.expense.get_company_expenses`<a id="factorialexpenseget_company_expenses"></a>

This endpoint allows you to retrieve expenses for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_expenses_response = factorial.expense.get_company_expenses()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseGetCompanyExpensesResponse`](./factorial_python_sdk/pydantic/expense_get_company_expenses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/finance/expenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.family_situation.create_new`<a id="factorialfamily_situationcreate_new"></a>

Create a Family Situation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = factorial.family_situation.create_new(
    employee_id=3,
    civil_status="married",
    number_of_dependants=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### civil_status: `str`<a id="civil_status-str"></a>

##### number_of_dependants: `int`<a id="number_of_dependants-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FamilySituationCreateNewRequest`](./factorial_python_sdk/type/family_situation_create_new_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FamilySituation`](./factorial_python_sdk/pydantic/family_situation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/family_situation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.family_situation.update_family_situation`<a id="factorialfamily_situationupdate_family_situation"></a>

Update a Family Situation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_family_situation_response = factorial.family_situation.update_family_situation(
    id="3",
    employee_id=3,
    civil_status="married",
    number_of_dependants=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### employee_id: `int`<a id="employee_id-int"></a>

##### civil_status: `str`<a id="civil_status-str"></a>

##### number_of_dependants: `int`<a id="number_of_dependants-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FamilySituationUpdateFamilySituationRequest`](./factorial_python_sdk/type/family_situation_update_family_situation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FamilySituation`](./factorial_python_sdk/pydantic/family_situation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/family_situation/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.folder.create_new_folder`<a id="factorialfoldercreate_new_folder"></a>

Create a Folders with a given name and active status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_folder_response = factorial.folder.create_new_folder(
    name="payment",
    active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### active: `bool`<a id="active-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FolderCreateNewFolderRequest`](./factorial_python_sdk/type/folder_create_new_folder_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderCreateNewFolderResponse`](./factorial_python_sdk/pydantic/folder_create_new_folder_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.folder.get_by_id`<a id="factorialfolderget_by_id"></a>

Get a Folder by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.folder.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Folder`](./factorial_python_sdk/pydantic/folder.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/folders/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.folder.get_by_name_and_status`<a id="factorialfolderget_by_name_and_status"></a>

Get Folders by given name and active status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_and_status_response = factorial.folder.get_by_name_and_status(
    name="payment",
    active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Retrieves the list of folder by name

##### active: `bool`<a id="active-bool"></a>

Retrieves the list of employees by active status

#### 🔄 Return<a id="🔄-return"></a>

[`FolderGetByNameAndStatusResponse`](./factorial_python_sdk/pydantic/folder_get_by_name_and_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.folder.update_folder_by_id`<a id="factorialfolderupdate_folder_by_id"></a>

Update a folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_folder_by_id_response = factorial.folder.update_folder_by_id(
    id="1",
    name="payment",
    active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### name: `str`<a id="name-str"></a>

##### active: `bool`<a id="active-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FolderUpdateFolderByIdRequest`](./factorial_python_sdk/type/folder_update_folder_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Folder`](./factorial_python_sdk/pydantic/folder.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/folders/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.holiday.get_all_company_holidays`<a id="factorialholidayget_all_company_holidays"></a>

Get all company holidays

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_company_holidays_response = factorial.holiday.get_all_company_holidays()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HolidayGetAllCompanyHolidaysResponse`](./factorial_python_sdk/pydantic/holiday_get_all_company_holidays_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_holidays` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.holiday.get_by_id`<a id="factorialholidayget_by_id"></a>

Get a company holiday by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.holiday.get_by_id(
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyHoliday`](./factorial_python_sdk/pydantic/company_holiday.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_holidays/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.integration.delete_payroll_code`<a id="factorialintegrationdelete_payroll_code"></a>

Deletes an existing payroll code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_payroll_code_response = factorial.integration.delete_payroll_code(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Code`](./factorial_python_sdk/pydantic/code.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payroll_integrations/codes/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.integration.get_all_codes`<a id="factorialintegrationget_all_codes"></a>

This endpoint allows fetching all available Codes, scoped to the integration name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_codes_response = factorial.integration.get_all_codes(
    integration="a3innuva",
    code="TEST_CODE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### integration: `str`<a id="integration-str"></a>

Payroll Integration name

##### code: `str`<a id="code-str"></a>

Unique identifier to relate Factorial with different payroll softwares

#### 🔄 Return<a id="🔄-return"></a>

[`IntegrationGetAllCodesResponse`](./factorial_python_sdk/pydantic/integration_get_all_codes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payroll_integrations/codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.integration.update_payroll_code`<a id="factorialintegrationupdate_payroll_code"></a>

Update a Payroll Integration Code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_payroll_code_response = factorial.integration.update_payroll_code(
    id="3",
    id=3,
    code="TEST_CODE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### requestBody: [`IntegrationUpdatePayrollCodeRequest`](./factorial_python_sdk/type/integration_update_payroll_code_request.py)<a id="requestbody-integrationupdatepayrollcoderequestfactorial_python_sdktypeintegration_update_payroll_code_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Code`](./factorial_python_sdk/pydantic/code.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payroll_integrations/codes/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.integration_code.create_payroll_integration_code`<a id="factorialintegration_codecreate_payroll_integration_code"></a>

This endpoint allows you create and store Payroll Integrations Codes in Factorial.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payroll_integration_code_response = factorial.integration_code.create_payroll_integration_code(
    code="TEST_CODE",
    codeable_id=12,
    codeable_type="Employee",
    integration="temporary",
    forfait_jours=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

##### codeable_id: `int`<a id="codeable_id-int"></a>

##### codeable_type: `str`<a id="codeable_type-str"></a>

##### integration: `str`<a id="integration-str"></a>

##### forfait_jours: `bool`<a id="forfait_jours-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntegrationCodeCreatePayrollIntegrationCodeRequest`](./factorial_python_sdk/type/integration_code_create_payroll_integration_code_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Code`](./factorial_python_sdk/pydantic/code.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payroll_integrations/codes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.key.create_new`<a id="factorialkeycreate_new"></a>

Create a Key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = factorial.key.create_new(
    name="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KeyCreateNewRequest`](./factorial_python_sdk/type/key_create_new_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApiKeyCreate`](./factorial_python_sdk/pydantic/api_key_create.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.key.delete_by_id`<a id="factorialkeydelete_by_id"></a>

Delete an API Key by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = factorial.key.delete_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`ApiKey`](./factorial_python_sdk/pydantic/api_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/keys/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.key.get_collection`<a id="factorialkeyget_collection"></a>

Get a collection of Keys

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_response = factorial.key.get_collection()
```

#### 🔄 Return<a id="🔄-return"></a>

[`KeyGetCollectionResponse`](./factorial_python_sdk/pydantic/key_get_collection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.create_new_leave`<a id="factorialleavecreate_new_leave"></a>

Creates a Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_leave_response = factorial.leave.create_new_leave(
    start_on="2022-03-03",
    finish_on="2022-03-03",
    employee_id=5,
    description="Medical appointment for 4 hours",
    leave_type_id=1,
    half_day="end_of_day",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_on: `str`<a id="start_on-str"></a>

##### finish_on: `str`<a id="finish_on-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### description: `str`<a id="description-str"></a>

##### leave_type_id: `int`<a id="leave_type_id-int"></a>

##### half_day: `str`<a id="half_day-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveCreateNewLeaveRequest`](./factorial_python_sdk/type/leave_create_new_leave_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Leave`](./factorial_python_sdk/pydantic/leave.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leaves` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.create_new_leave_0`<a id="factorialleavecreate_new_leave_0"></a>

Creates a Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_leave_0_response = factorial.leave.create_new_leave_0(
    start_on="2022-03-03",
    finish_on="2022-03-03",
    employee_id=5,
    description="Medical appointment for 4 hours",
    leave_type_id=1,
    half_day="end_of_day",
    start_time="840",
    hours_amount_in_cents=400,
    medical_leave_type=400,
    effective_on="2022-03-03",
    medical_discharge_reason="medical appointment",
    colegiate_number=3,
    has_previous_relapse=False,
    relapse_leave_id=3,
    relapse_on="2022-03-03",
    accident_on="2022-03-01",
    paternity_birth_on="2022-03-02",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_on: `str`<a id="start_on-str"></a>

##### finish_on: `str`<a id="finish_on-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### description: `str`<a id="description-str"></a>

##### leave_type_id: `int`<a id="leave_type_id-int"></a>

##### half_day: `str`<a id="half_day-str"></a>

##### start_time: `str`<a id="start_time-str"></a>

##### hours_amount_in_cents: `int`<a id="hours_amount_in_cents-int"></a>

##### medical_leave_type: `int`<a id="medical_leave_type-int"></a>

##### effective_on: `str`<a id="effective_on-str"></a>

##### medical_discharge_reason: `str`<a id="medical_discharge_reason-str"></a>

##### colegiate_number: `int`<a id="colegiate_number-int"></a>

##### has_previous_relapse: `bool`<a id="has_previous_relapse-bool"></a>

##### relapse_leave_id: `int`<a id="relapse_leave_id-int"></a>

##### relapse_on: `str`<a id="relapse_on-str"></a>

##### accident_on: `str`<a id="accident_on-str"></a>

##### paternity_birth_on: `str`<a id="paternity_birth_on-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveCreateNewLeaveRequest1`](./factorial_python_sdk/type/leave_create_new_leave_request1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Leave`](./factorial_python_sdk/pydantic/leave.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time/leaves` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.delete_by_id`<a id="factorialleavedelete_by_id"></a>

Delete a Leave by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = factorial.leave.delete_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Leave`](./factorial_python_sdk/pydantic/leave.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leaves/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.delete_by_id_0`<a id="factorialleavedelete_by_id_0"></a>

Delete a Leave by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_0_response = factorial.leave.delete_by_id_0(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveV2`](./factorial_python_sdk/pydantic/leave_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time/leaves/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.get_by_id`<a id="factorialleaveget_by_id"></a>

Get a Leave by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.leave.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Leave`](./factorial_python_sdk/pydantic/leave.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leaves/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.get_by_id_0`<a id="factorialleaveget_by_id_0"></a>

Get a Leave by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_0_response = factorial.leave.get_by_id_0(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveV2`](./factorial_python_sdk/pydantic/leave_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time/leaves/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.get_company_leaves`<a id="factorialleaveget_company_leaves"></a>

Get Leaves from a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_leaves_response = factorial.leave.get_company_leaves(
    employee_ids_=[1],
    leave_type_ids_=[1],
    _from="2023-01-03",
    to="2023-01-04",
    include_leave_type=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids_: List[`int`]<a id="employee_ids_-listint"></a>

Employees id array

##### leave_type_ids_: List[`int`]<a id="leave_type_ids_-listint"></a>

Leave type id array

##### _from: `str`<a id="_from-str"></a>

It should be a valid date following the format YYYY-MM-DD

##### to: `str`<a id="to-str"></a>

It should be a valid date following the format YYYY-MM-DD

##### include_leave_type: `bool`<a id="include_leave_type-bool"></a>

Include leave type name

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveGetCompanyLeavesResponse`](./factorial_python_sdk/pydantic/leave_get_company_leaves_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leaves` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.get_company_leaves_0`<a id="factorialleaveget_company_leaves_0"></a>

Get Leaves from a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_leaves_0_response = factorial.leave.get_company_leaves_0(
    employee_ids_=[1],
    leave_type_ids_=[1],
    _from="2023-01-03",
    to="2023-01-04",
    include_leave_type=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids_: List[`int`]<a id="employee_ids_-listint"></a>

Employees id array

##### leave_type_ids_: List[`int`]<a id="leave_type_ids_-listint"></a>

Leave type id array

##### _from: `str`<a id="_from-str"></a>

It should be a valid date following the format YYYY-MM-DD

##### to: `str`<a id="to-str"></a>

It should be a valid date following the format YYYY-MM-DD

##### include_leave_type: `bool`<a id="include_leave_type-bool"></a>

Include leave type name

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveGetCompanyLeaves200Response`](./factorial_python_sdk/pydantic/leave_get_company_leaves200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time/leaves` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.get_types`<a id="factorialleaveget_types"></a>

Get Leave types from a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_types_response = factorial.leave.get_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveGetTypesResponse`](./factorial_python_sdk/pydantic/leave_get_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leave_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.type_create`<a id="factorialleavetype_create"></a>

Create a Leave Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
type_create_response = factorial.leave.type_create(
    name="holiday",
    color="07A2AD",
    accrues=True,
    active=True,
    approval_required=False,
    attachment=False,
    visibility=True,
    workable=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### color: `str`<a id="color-str"></a>

##### accrues: `bool`<a id="accrues-bool"></a>

##### active: `bool`<a id="active-bool"></a>

##### approval_required: `bool`<a id="approval_required-bool"></a>

##### attachment: `bool`<a id="attachment-bool"></a>

##### visibility: `bool`<a id="visibility-bool"></a>

##### workable: `bool`<a id="workable-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveTypeCreateRequest`](./factorial_python_sdk/type/leave_type_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveType`](./factorial_python_sdk/pydantic/leave_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leave_types` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.update_by_id`<a id="factorialleaveupdate_by_id"></a>

Update a Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = factorial.leave.update_by_id(
    id="1",
    description="Medical appointment for 4 hours",
    employee_id=7,
    finish_on="2022-03-03",
    start_on="2022-03-03",
    start_time="720",
    hour_amount_in_cents=400,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### description: `str`<a id="description-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### finish_on: `str`<a id="finish_on-str"></a>

##### start_on: `str`<a id="start_on-str"></a>

##### start_time: `str`<a id="start_time-str"></a>

##### hour_amount_in_cents: `int`<a id="hour_amount_in_cents-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveUpdateByIdRequest`](./factorial_python_sdk/type/leave_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveV2`](./factorial_python_sdk/pydantic/leave_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time/leaves/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.update_leave_by_id`<a id="factorialleaveupdate_leave_by_id"></a>

Update a Leave

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_leave_by_id_response = factorial.leave.update_leave_by_id(
    id="1",
    description="Medical appointment for 4 hours",
    employee_id=7,
    finish_on=5,
    start_on="basic",
    half_day="end_of_day",
    leave_type_id=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### description: `str`<a id="description-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### finish_on: `int`<a id="finish_on-int"></a>

##### start_on: `str`<a id="start_on-str"></a>

##### half_day: `str`<a id="half_day-str"></a>

##### leave_type_id: `int`<a id="leave_type_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveUpdateLeaveByIdRequest`](./factorial_python_sdk/type/leave_update_leave_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Leave`](./factorial_python_sdk/pydantic/leave.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leaves/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.leave.update_type`<a id="factorialleaveupdate_type"></a>

Update a Leave Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_type_response = factorial.leave.update_type(
    name="Special appointment",
    color="FFFFFF",
    id="5",
    accrues=False,
    active=True,
    approval_required=False,
    attachment=True,
    visibility=True,
    workable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### color: `str`<a id="color-str"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### accrues: `bool`<a id="accrues-bool"></a>

##### active: `bool`<a id="active-bool"></a>

##### approval_required: `bool`<a id="approval_required-bool"></a>

##### attachment: `bool`<a id="attachment-bool"></a>

##### visibility: `bool`<a id="visibility-bool"></a>

##### workable: `bool`<a id="workable-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveUpdateTypeRequest`](./factorial_python_sdk/type/leave_update_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveType`](./factorial_python_sdk/pydantic/leave_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/leave_types/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.legal_entity.get_by_id`<a id="factoriallegal_entityget_by_id"></a>

Get a Legal Entity by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.legal_entity.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`LegalEntity`](./factorial_python_sdk/pydantic/legal_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/legal_entities/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.legal_entity.list_legal_entities`<a id="factoriallegal_entitylist_legal_entities"></a>

Get a collection of Legal Entities

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_legal_entities_response = factorial.legal_entity.list_legal_entities()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LegalEntityListLegalEntitiesResponse`](./factorial_python_sdk/pydantic/legal_entity_list_legal_entities_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/legal_entities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.location.get_all_locations`<a id="factoriallocationget_all_locations"></a>

Get all locations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_locations_response = factorial.location.get_all_locations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LocationGetAllLocationsResponse`](./factorial_python_sdk/pydantic/location_get_all_locations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.location.get_by_id`<a id="factoriallocationget_by_id"></a>

Get a Location by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.location.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Location`](./factorial_python_sdk/pydantic/location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.location.update_shift_location`<a id="factoriallocationupdate_shift_location"></a>

Update shift location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_shift_location_response = factorial.location.update_shift_location(
    id="3",
    location_id=2,
    work_area_id=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### location_id: `int`<a id="location_id-int"></a>

##### work_area_id: `int`<a id="work_area_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationUpdateShiftLocationRequest`](./factorial_python_sdk/type/location_update_shift_location_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShiftManagement`](./factorial_python_sdk/pydantic/shift_management.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts_management/{id}/locations` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.message.create_ats_message`<a id="factorialmessagecreate_ats_message"></a>

This endpoint allows you create and store Ats Messages in Factorial, while using your own user interface to display them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_ats_message_response = factorial.message.create_ats_message(
    job_application_id=1,
    content="Message 1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_application_id: `int`<a id="job_application_id-int"></a>

##### content: `str`<a id="content-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessageCreateAtsMessageRequest`](./factorial_python_sdk/type/message_create_ats_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AtsMessage`](./factorial_python_sdk/pydantic/ats_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.message.get_all_messages`<a id="factorialmessageget_all_messages"></a>

Get all ATS Messages

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_messages_response = factorial.message.get_all_messages(
    conversation_id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`MessageGetAllMessagesResponse`](./factorial_python_sdk/pydantic/message_get_all_messages_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/messages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.policy.get_time_off`<a id="factorialpolicyget_time_off"></a>

This endpoint allows you to retrieve a time off policy for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_response = factorial.policy.get_time_off(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./factorial_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/policies/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.policy.get_time_off_policies`<a id="factorialpolicyget_time_off_policies"></a>

This endpoint allows you to retrieve time off policies for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_policies_response = factorial.policy.get_time_off_policies()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyGetTimeOffPoliciesResponse`](./factorial_python_sdk/pydantic/policy_get_time_off_policies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.ats_job_posting`<a id="factorialpostats_job_posting"></a>

This endpoint allows you create and store Ats Job Postings in Factorial.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ats_job_posting_response = factorial.post.ats_job_posting(
    title="Jr Software Developer",
    status="draft",
    description="Full Stack Developer",
    contract_type="temporary",
    remote=True,
    schedule_type="full_time",
    team_id=1,
    location_id=3,
    salary_format="range",
    salary_from_amount_in_cents=50000,
    salary_to_amount_in_cents=60000,
    cv_requirement="mandatory",
    cover_letter_requirement="mandatory",
    phone_requirement="mandatory",
    photo_requirement="mandatory",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### status: `str`<a id="status-str"></a>

##### description: `str`<a id="description-str"></a>

##### contract_type: `str`<a id="contract_type-str"></a>

##### remote: `bool`<a id="remote-bool"></a>

##### schedule_type: `str`<a id="schedule_type-str"></a>

##### team_id: `int`<a id="team_id-int"></a>

##### location_id: `int`<a id="location_id-int"></a>

##### salary_format: `str`<a id="salary_format-str"></a>

##### salary_from_amount_in_cents: `int`<a id="salary_from_amount_in_cents-int"></a>

##### salary_to_amount_in_cents: `int`<a id="salary_to_amount_in_cents-int"></a>

##### cv_requirement: `str`<a id="cv_requirement-str"></a>

##### cover_letter_requirement: `str`<a id="cover_letter_requirement-str"></a>

##### phone_requirement: `str`<a id="phone_requirement-str"></a>

##### photo_requirement: `str`<a id="photo_requirement-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostAtsJobPostingRequest`](./factorial_python_sdk/type/post_ats_job_posting_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AtsJobPosting`](./factorial_python_sdk/pydantic/ats_job_posting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/job_postings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.create_new_post`<a id="factorialpostcreate_new_post"></a>

Create a Post

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_post_response = factorial.post.create_new_post(
    title="New Post",
    description="description",
    posts_group_id=1,
    type="first_day",
    published_at="2022-09-08T00:00:00.000Z",
    stars_at="2022-09-08T00:00:00.000Z",
    ends_at="2022-09-08T00:00:00.000Z",
    location="Green park",
    target_id=1,
    send_notifications=True,
    image=open('/path/to/file', 'rb'),
    allow_comments_and_reactions=True,
    attachments=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### description: `str`<a id="description-str"></a>

##### posts_group_id: `int`<a id="posts_group_id-int"></a>

##### type: `str`<a id="type-str"></a>

##### published_at: `str`<a id="published_at-str"></a>

##### stars_at: `str`<a id="stars_at-str"></a>

##### ends_at: `str`<a id="ends_at-str"></a>

##### location: `str`<a id="location-str"></a>

##### target_id: `int`<a id="target_id-int"></a>

##### send_notifications: `bool`<a id="send_notifications-bool"></a>

##### image: `IO`<a id="image-io"></a>

##### allow_comments_and_reactions: `bool`<a id="allow_comments_and_reactions-bool"></a>

##### attachments: `IO`<a id="attachments-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostCreateNewPostRequest`](./factorial_python_sdk/type/post_create_new_post_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostCreateNewPostResponse`](./factorial_python_sdk/pydantic/post_create_new_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/posts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.duplicate_job_posting`<a id="factorialpostduplicate_job_posting"></a>

Make a duplicate of a job posting. The only parameter required for this operation is the id of the posting you wish to duplicate.
One thing to note about this operation is that the id of the resulting posting will be different from the original, the title will have Copy appended to it, so if your origin title was Don't buy a the title of the duplicate will be Don't buy a Copy in addition to this, the status of the duplicate will default to draft. All this being said, kindly inspect the duplicate and ensure you get it into your desired state.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_job_posting_response = factorial.post.duplicate_job_posting(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`AtsJobPosting`](./factorial_python_sdk/pydantic/ats_job_posting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/job_postings/{id}/duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.get_all_postings`<a id="factorialpostget_all_postings"></a>

This endpoint allows fetching all available Ats Job Postings, scoped to the user credentials and company of that user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_postings_response = factorial.post.get_all_postings(
    status="3",
    team_id=3,
    location_id="1",
    legal_entity_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Job posting status

##### team_id: `int`<a id="team_id-int"></a>

An id of any teams that the ats company has in Factorial

##### location_id: `str`<a id="location_id-str"></a>

An id of any location associated with the ats company in Factorial

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

An id of any legal entity associated with the company in Factorial

#### 🔄 Return<a id="🔄-return"></a>

[`PostGetAllPostingsResponse`](./factorial_python_sdk/pydantic/post_get_all_postings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/job_postings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.get_by_id`<a id="factorialpostget_by_id"></a>

Get Post

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.post.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Post`](./factorial_python_sdk/pydantic/post.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/posts/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.job_posting_update`<a id="factorialpostjob_posting_update"></a>

Update a Job Posting

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
job_posting_update_response = factorial.post.job_posting_update(
    id="3",
    title="Developer",
    description="Full Stack Developer",
    contract_type="temporary",
    remote=True,
    status="draft",
    schedule_type="full_time",
    team_id=1,
    location_id=3,
    salary_format="range",
    salary_from_amount_in_cents=50000,
    salary_to_amount_in_cents=60000,
    cv_requirement="mandatory",
    cover_letter_requirement="mandatory",
    phone_requirement="mandatory",
    photo_requirement="mandatory",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### title: `str`<a id="title-str"></a>

##### description: `str`<a id="description-str"></a>

##### contract_type: `str`<a id="contract_type-str"></a>

##### remote: `bool`<a id="remote-bool"></a>

##### status: `str`<a id="status-str"></a>

##### schedule_type: `str`<a id="schedule_type-str"></a>

##### team_id: `int`<a id="team_id-int"></a>

##### location_id: `int`<a id="location_id-int"></a>

##### salary_format: `str`<a id="salary_format-str"></a>

##### salary_from_amount_in_cents: `int`<a id="salary_from_amount_in_cents-int"></a>

##### salary_to_amount_in_cents: `int`<a id="salary_to_amount_in_cents-int"></a>

##### cv_requirement: `str`<a id="cv_requirement-str"></a>

##### cover_letter_requirement: `str`<a id="cover_letter_requirement-str"></a>

##### phone_requirement: `str`<a id="phone_requirement-str"></a>

##### photo_requirement: `str`<a id="photo_requirement-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostJobPostingUpdateRequest`](./factorial_python_sdk/type/post_job_posting_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AtsJobPosting`](./factorial_python_sdk/pydantic/ats_job_posting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/job_postings/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.list_posts`<a id="factorialpostlist_posts"></a>

This endpoint allows you to fetch a collection of posts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_posts_response = factorial.post.list_posts()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PostListPostsResponse`](./factorial_python_sdk/pydantic/post_list_posts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/posts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.remove_job_posting`<a id="factorialpostremove_job_posting"></a>

Deletes an existing job posting

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_job_posting_response = factorial.post.remove_job_posting(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`AtsJobPosting`](./factorial_python_sdk/pydantic/ats_job_posting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ats/job_postings/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.remove_post`<a id="factorialpostremove_post"></a>

Delete Post

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_post_response = factorial.post.remove_post(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Post`](./factorial_python_sdk/pydantic/post.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/posts/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.post.update_existing_post`<a id="factorialpostupdate_existing_post"></a>

Create a Post

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_post_response = factorial.post.update_existing_post(
    id=1,
    id="1",
    title="New Post",
    description="description",
    stars_at="2022-09-08T00:00:00.000Z",
    location="Green park",
    send_notifications=True,
    delete_cover_image=True,
    image=open('/path/to/file', 'rb'),
    allow_comments_and_reactions=True,
    attachments=open('/path/to/file', 'rb'),
    deleted_attachments=[
        1
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### requestBody: [`PostUpdateExistingPostRequest`](./factorial_python_sdk/type/post_update_existing_post_request.py)<a id="requestbody-postupdateexistingpostrequestfactorial_python_sdktypepost_update_existing_post_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PostUpdateExistingPostResponse`](./factorial_python_sdk/pydantic/post_update_existing_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/posts/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.create_clock_in_shift`<a id="factorialshiftcreate_clock_in_shift"></a>

Creates a shift (time registry) for the current user with the clock_in time of the request and nil clock_out

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_clock_in_shift_response = factorial.shift.create_clock_in_shift(
    employee_id=5,
    now="2019-01-01T12:12:01-02:00",
    observations="New observation",
    location_type="office",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### now: `str`<a id="now-str"></a>

##### observations: `str`<a id="observations-str"></a>

##### location_type: `str`<a id="location_type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftCreateClockInShiftRequest`](./factorial_python_sdk/type/shift_create_clock_in_shift_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Shift`](./factorial_python_sdk/pydantic/shift.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts/clock_in` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.create_new_shift`<a id="factorialshiftcreate_new_shift"></a>

Create a shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_shift_response = factorial.shift.create_new_shift(
    start_at="2022-06-23T11:00:00.000+00:00",
    end_at="2022-06-23T17:00:00.000+00:00",
    employee_id=3,
    notes="Note 2",
    location_id=1,
    work_area_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_at: `str`<a id="start_at-str"></a>

##### end_at: `str`<a id="end_at-str"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### notes: `str`<a id="notes-str"></a>

##### location_id: `int`<a id="location_id-int"></a>

##### work_area_id: `int`<a id="work_area_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftCreateNewShiftRequest`](./factorial_python_sdk/type/shift_create_new_shift_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShiftManagement`](./factorial_python_sdk/pydantic/shift_management.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts_management` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.delete_by_id`<a id="factorialshiftdelete_by_id"></a>

Delete Shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = factorial.shift.delete_by_id(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftManagement`](./factorial_python_sdk/pydantic/shift_management.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts_management/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.delete_shift_by_id`<a id="factorialshiftdelete_shift_by_id"></a>

Delete Shift (time registry)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_shift_by_id_response = factorial.shift.delete_shift_by_id(
    id="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Shift`](./factorial_python_sdk/pydantic/shift.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.get_all_shifts`<a id="factorialshiftget_all_shifts"></a>

By default, it returns all the shifts for the current week

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_shifts_response = factorial.shift.get_all_shifts(
    employee_id=5,
    employee_ids5_b5_d=[
        1
    ],
    start_at="2023-07-24",
    end_at="2023-07-30",
    only_published=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

Employee ID to find shifts from

##### employee_ids5_b5_d: List[`int`]<a id="employee_ids5_b5_d-listint"></a>

Employee IDs to find shifts from

##### start_at: `str`<a id="start_at-str"></a>

Start date to find shifts from

##### end_at: `str`<a id="end_at-str"></a>

End date to find shifts to

##### only_published: `bool`<a id="only_published-bool"></a>

To return only published shifts

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftGetAllShiftsResponse`](./factorial_python_sdk/pydantic/shift_get_all_shifts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts_management` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.get_by_id`<a id="factorialshiftget_by_id"></a>

Get Shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.shift.get_by_id(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftManagement`](./factorial_python_sdk/pydantic/shift_management.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts_management/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.get_from_company`<a id="factorialshiftget_from_company"></a>

Get shifts (time registries) from a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_from_company_response = factorial.shift.get_from_company(
    year="2022",
    month="11",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### year: `str`<a id="year-str"></a>

It should be valid year in the format `YYYY`

##### month: `str`<a id="month-str"></a>

It should be valid month in the calendar ranging rom `01 to 12`. The month format is `MM`

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftGetFromCompanyResponse`](./factorial_python_sdk/pydantic/shift_get_from_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.publish_shifts_inside_time_range`<a id="factorialshiftpublish_shifts_inside_time_range"></a>

Publish shifts inside time range

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
factorial.shift.publish_shifts_inside_time_range(
    start_at="2022-06-23T11:00:00.000+00:00",
    end_at="2022-06-23T17:00:00.000+00:00",
    employee_ids=[
        1
    ],
    send_notification=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_at: `str`<a id="start_at-str"></a>

##### end_at: `str`<a id="end_at-str"></a>

##### employee_ids: [`ShiftPublishShiftsInsideTimeRangeRequestEmployeeIds`](./factorial_python_sdk/type/shift_publish_shifts_inside_time_range_request_employee_ids.py)<a id="employee_ids-shiftpublishshiftsinsidetimerangerequestemployeeidsfactorial_python_sdktypeshift_publish_shifts_inside_time_range_request_employee_idspy"></a>

##### send_notification: `bool`<a id="send_notification-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftPublishShiftsInsideTimeRangeRequest`](./factorial_python_sdk/type/shift_publish_shifts_inside_time_range_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts_management/publish` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.toggle_shift_status`<a id="factorialshifttoggle_shift_status"></a>

Updates a shift (time registry) for the current user with the time of the request. It will clock out if the user wasn't previously clocked in. Else it will clock in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
toggle_shift_status_response = factorial.shift.toggle_shift_status(
    employee_id=5,
    now="2019-01-01T12:12:01-02:00",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### now: `str`<a id="now-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftToggleShiftStatusRequest`](./factorial_python_sdk/type/shift_toggle_shift_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Shift`](./factorial_python_sdk/pydantic/shift.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts/toggle` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.update_clock_out_shift`<a id="factorialshiftupdate_clock_out_shift"></a>

Updates a shift (time registry) for the current user with the clock_out time of the request. It will fail if the user wasn't previously clocked in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_clock_out_shift_response = factorial.shift.update_clock_out_shift(
    employee_id=5,
    now="2019-01-01T12:12:01-02:00",
    observations="Updated observation",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### now: `str`<a id="now-str"></a>

##### observations: `str`<a id="observations-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftUpdateClockOutShiftRequest`](./factorial_python_sdk/type/shift_update_clock_out_shift_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Shift`](./factorial_python_sdk/pydantic/shift.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts/clock_out` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.update_notes`<a id="factorialshiftupdate_notes"></a>

Update shift notes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_notes_response = factorial.shift.update_notes(
    id="3",
    notes="Note 1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### notes: `str`<a id="notes-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftUpdateNotesRequest`](./factorial_python_sdk/type/shift_update_notes_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShiftManagement`](./factorial_python_sdk/pydantic/shift_management.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts_management/{id}/notes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.shift.update_shift`<a id="factorialshiftupdate_shift"></a>

Updates a shift (time registry).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_shift_response = factorial.shift.update_shift(
    id="5",
    clock_in="2019-01-01T12:12:01-02:00",
    clock_out="2019-01-01T12:12:01-02:00",
    observations="First Shift",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### clock_in: `str`<a id="clock_in-str"></a>

##### clock_out: `str`<a id="clock_out-str"></a>

##### observations: `str`<a id="observations-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftUpdateShiftRequest`](./factorial_python_sdk/type/shift_update_shift_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Shift`](./factorial_python_sdk/pydantic/shift.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time/shifts/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.supplement.create_new_supplement`<a id="factorialsupplementcreate_new_supplement"></a>

Create supplements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_supplement_response = factorial.supplement.create_new_supplement(
    employee_id=5,
    amount_in_cents=23333,
    effective_on="2023-04-22",
    contracts_taxonomy_id=2,
    payroll_policy_period_id=3,
    unit="usd",
    contracts_compensation_id=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

##### amount_in_cents: `int`<a id="amount_in_cents-int"></a>

##### effective_on: `str`<a id="effective_on-str"></a>

##### contracts_taxonomy_id: `int`<a id="contracts_taxonomy_id-int"></a>

##### payroll_policy_period_id: `int`<a id="payroll_policy_period_id-int"></a>

##### unit: `str`<a id="unit-str"></a>

##### contracts_compensation_id: `int`<a id="contracts_compensation_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SupplementCreateNewSupplementRequest`](./factorial_python_sdk/type/supplement_create_new_supplement_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Supplement`](./factorial_python_sdk/pydantic/supplement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/supplements` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.supplement.delete_by_id`<a id="factorialsupplementdelete_by_id"></a>

Delete supplements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = factorial.supplement.delete_by_id(
    id="3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Supplement`](./factorial_python_sdk/pydantic/supplement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/supplements/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.supplement.get_all`<a id="factorialsupplementget_all"></a>

Get all supplements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = factorial.supplement.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SupplementGetAllResponse`](./factorial_python_sdk/pydantic/supplement_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/supplements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.supplement.update_by_id`<a id="factorialsupplementupdate_by_id"></a>

Update supplements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = factorial.supplement.update_by_id(
    id="3",
    employee_id=5,
    amount_in_cents=23333,
    effective_on="2023-04-22",
    contracts_taxonomy_id=2,
    payroll_policy_period_id=3,
    unit="usd",
    contracts_compensation_id=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### employee_id: `int`<a id="employee_id-int"></a>

##### amount_in_cents: `int`<a id="amount_in_cents-int"></a>

##### effective_on: `str`<a id="effective_on-str"></a>

##### contracts_taxonomy_id: `int`<a id="contracts_taxonomy_id-int"></a>

##### payroll_policy_period_id: `int`<a id="payroll_policy_period_id-int"></a>

##### unit: `str`<a id="unit-str"></a>

##### contracts_compensation_id: `int`<a id="contracts_compensation_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SupplementUpdateByIdRequest`](./factorial_python_sdk/type/supplement_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Supplement`](./factorial_python_sdk/pydantic/supplement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/supplements/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.table.create_custom_table`<a id="factorialtablecreate_custom_table"></a>

This endpoint is used to create and store custom table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_table_response = factorial.table.create_custom_table(
    name="Kudos",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TableCreateCustomTableRequest`](./factorial_python_sdk/type/table_create_custom_table_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomResource`](./factorial_python_sdk/pydantic/custom_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/custom/tables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.table.create_field`<a id="factorialtablecreate_field"></a>

This endpoint is used to create and store custom fields on custom tables. See custom fields v2 for more information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_field_response = factorial.table.create_field(
    id=86,
    id=1,
    custom_field={
        "id": 1,
        "label": "employee",
        "identifier": "label-1",
        "position": 90773647,
        "required": False,
        "field_type": "text",
        "min_value": -439653,
        "max_value": 47114499,
        "slug_id": 47114499,
        "slug_name": "text",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Custom Table ID (Required)

##### requestBody: [`TableCreateFieldRequest`](./factorial_python_sdk/type/table_create_field_request.py)<a id="requestbody-tablecreatefieldrequestfactorial_python_sdktypetable_create_field_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldV2`](./factorial_python_sdk/pydantic/custom_field_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/custom/tables/{id}/fields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.table.get_custom_table`<a id="factorialtableget_custom_table"></a>

This endpoint allows you retrieve a Custom Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_table_response = factorial.table.get_custom_table(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`CustomResource`](./factorial_python_sdk/pydantic/custom_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/custom/tables/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.table.get_fields`<a id="factorialtableget_fields"></a>

This endpoint allows you retrieve Custom Table Fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_response = factorial.table.get_fields(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Custom Table ID (Required)

#### 🔄 Return<a id="🔄-return"></a>

[`TableGetFieldsResponse`](./factorial_python_sdk/pydantic/table_get_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/custom/tables/{id}/fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.add_file_to_task`<a id="factorialtaskadd_file_to_task"></a>

Create a File in a Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_file_to_task_response = factorial.task.add_file_to_task(
    id="15",
    file="task_file.pdf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskAddFileToTaskRequest`](./factorial_python_sdk/type/task_add_file_to_task_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./factorial_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{id}/files` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.copy_by_id`<a id="factorialtaskcopy_by_id"></a>

Copy Task by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
copy_by_id_response = factorial.task.copy_by_id(
    id="1",
    name="Upload information task",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskCopyByIdRequest`](./factorial_python_sdk/type/task_copy_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./factorial_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{id}/copy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.create_new_task`<a id="factorialtaskcreate_new_task"></a>

Create a Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_task_response = factorial.task.create_new_task(
    name="Upload information task",
    due_on="2022-05-18",
    content="Update information due date to either following weekday or following friday",
    assignee_ids=[
        1
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### due_on: `str`<a id="due_on-str"></a>

##### content: `str`<a id="content-str"></a>

##### assignee_ids: [`TaskCreateNewTaskRequestAssigneeIds`](./factorial_python_sdk/type/task_create_new_task_request_assignee_ids.py)<a id="assignee_ids-taskcreatenewtaskrequestassigneeidsfactorial_python_sdktypetask_create_new_task_request_assignee_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskCreateNewTaskRequest`](./factorial_python_sdk/type/task_create_new_task_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./factorial_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.delete_by_id`<a id="factorialtaskdelete_by_id"></a>

Delete a Task by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = factorial.task.delete_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./factorial_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.delete_file_in_task`<a id="factorialtaskdelete_file_in_task"></a>

Delete a File in a Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_file_in_task_response = factorial.task.delete_file_in_task(
    task_id="15",
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_id: `str`<a id="task_id-str"></a>

(Required)

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`TaskFile`](./factorial_python_sdk/pydantic/task_file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{task_id}/files/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.get_all_tasks`<a id="factorialtaskget_all_tasks"></a>

Get Tasks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_tasks_response = factorial.task.get_all_tasks(
    assignee_id=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignee_id: `int`<a id="assignee_id-int"></a>

Retrieves the list of tasks by assignee

#### 🔄 Return<a id="🔄-return"></a>

[`TaskGetAllTasksResponse`](./factorial_python_sdk/pydantic/task_get_all_tasks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.get_by_id`<a id="factorialtaskget_by_id"></a>

Get a Task by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.task.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./factorial_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.get_file`<a id="factorialtaskget_file"></a>

Get files from one Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_response = factorial.task.get_file(
    task_id="15",
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_id: `str`<a id="task_id-str"></a>

(Required)

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`TaskFile`](./factorial_python_sdk/pydantic/task_file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{task_id}/files/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.get_files`<a id="factorialtaskget_files"></a>

Get files from a Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_files_response = factorial.task.get_files(
    id="15",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`TaskFile`](./factorial_python_sdk/pydantic/task_file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{id}/files` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.resolve_by_id`<a id="factorialtaskresolve_by_id"></a>

Resolve Task by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resolve_by_id_response = factorial.task.resolve_by_id(
    id="1",
    done=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### done: `bool`<a id="done-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskResolveByIdRequest`](./factorial_python_sdk/type/task_resolve_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./factorial_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{id}/resolve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.task.update_by_id`<a id="factorialtaskupdate_by_id"></a>

Update a Task by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = factorial.task.update_by_id(
    id="1",
    due_on="2022-05-18",
    name="Upload information task",
    content="Update information due date to either following weekday or following friday",
    assignee_ids=[
        1
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### due_on: `str`<a id="due_on-str"></a>

##### name: `str`<a id="name-str"></a>

##### content: `str`<a id="content-str"></a>

##### assignee_ids: [`TaskUpdateByIdRequestAssigneeIds`](./factorial_python_sdk/type/task_update_by_id_request_assignee_ids.py)<a id="assignee_ids-taskupdatebyidrequestassigneeidsfactorial_python_sdktypetask_update_by_id_request_assignee_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskUpdateByIdRequest`](./factorial_python_sdk/type/task_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./factorial_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/tasks/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.taxonomy.get_by_id`<a id="factorialtaxonomyget_by_id"></a>

This endpoint allows you to retrieve a taxonomy by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.taxonomy.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Taxonomy`](./factorial_python_sdk/pydantic/taxonomy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/taxonomies/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.taxonomy.get_company_taxonomies`<a id="factorialtaxonomyget_company_taxonomies"></a>

This endpoint allows you to retrieve taxonomies for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_taxonomies_response = factorial.taxonomy.get_company_taxonomies(
    ids=[1],
    legal_entity_ids=[1],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: List[`int`]<a id="ids-listint"></a>

Taxonomies id array

##### legal_entity_ids: List[`int`]<a id="legal_entity_ids-listint"></a>

Legal Entities id array

#### 🔄 Return<a id="🔄-return"></a>

[`TaxonomyGetCompanyTaxonomiesResponse`](./factorial_python_sdk/pydantic/taxonomy_get_company_taxonomies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/taxonomies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.team.create_new_team`<a id="factorialteamcreate_new_team"></a>

Create a team with a given name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_team_response = factorial.team.create_new_team(
    name="Management",
    description="Team description",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### description: `str`<a id="description-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamCreateNewTeamRequest`](./factorial_python_sdk/type/team_create_new_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./factorial_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.team.get_all_teams`<a id="factorialteamget_all_teams"></a>

Get teams

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_teams_response = factorial.team.get_all_teams()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TeamGetAllTeamsResponse`](./factorial_python_sdk/pydantic/team_get_all_teams_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.team.get_by_id`<a id="factorialteamget_by_id"></a>

Get a team by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.team.get_by_id(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`TeamGetByIdResponse`](./factorial_python_sdk/pydantic/team_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.team.remove_team`<a id="factorialteamremove_team"></a>

Delete a team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_team_response = factorial.team.remove_team(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./factorial_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.team.update_team_by_id`<a id="factorialteamupdate_team_by_id"></a>

Update a team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_team_by_id_response = factorial.team.update_team_by_id(
    id="1",
    description="Team description",
    name="Management",
    avatar="https://api.factorialhr.com/rails/active_storage/representations/redirect/bob.png",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### description: `str`<a id="description-str"></a>

##### name: `str`<a id="name-str"></a>

##### avatar: `str`<a id="avatar-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamUpdateTeamByIdRequest`](./factorial_python_sdk/type/team_update_team_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./factorial_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/teams/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.user.info_get`<a id="factorialuserinfo_get"></a>

After token grant, get information of the token holder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
factorial.user.info_get()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.user.subscribed_webhooks_list`<a id="factorialusersubscribed_webhooks_list"></a>

Get a list of all subscribed webhooks for current user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
subscribed_webhooks_list_response = factorial.user.subscribed_webhooks_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserSubscribedWebhooksListResponse`](./factorial_python_sdk/pydantic/user_subscribed_webhooks_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.user.subscribed_webhooks_list_0`<a id="factorialusersubscribed_webhooks_list_0"></a>

Get a list of all subscribed webhooks for current user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
subscribed_webhooks_list_0_response = factorial.user.subscribed_webhooks_list_0()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserSubscribedWebhooksList200Response`](./factorial_python_sdk/pydantic/user_subscribed_webhooks_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.webhook.create_subscription`<a id="factorialwebhookcreate_subscription"></a>

> Creates a subscription for a determined webhook type. If webhook already exists, it just changes the target_url.

 ## Webhooks Types

| **Type** | **Information** |
| --- | --- |
| employee_invited | When creating a new employee, optionally you can send an invitation to create an account in Factorial. If you send an invitation, this event gets triggered. |
| employee_created | When creating a new employee, after submitting the form, this event gets triggered. |
| employee_updated| When updating personal protected employee information such has birthday, this event gets triggered. |
| employee_terminated | When terminating an employee, after submitting the form, this event gets triggered |
| employee_unterminated | When un terminating an employee, after submitting the form, this event gets triggered |
| attendance_clockin | When the user clocks in and starts the timer, this event is triggered. |
| attendance_clockout | When the user clocks out and stops the timer, this event is triggered |
| attendance_shift_created | When the user creates a shift, this event is triggered |
| attendance_shift_updated | When the user edits a shift, this event is triggered |
| attendance_shift_deleted | When the user deletes a shift, this event is triggered |
| ats_application_created | When a candidate applies for a posting. |
| ats_application_updated | When a candidates application for a posting suffers changes. |
| ats_job_posting_created | When a job posting is created. |
| ats_job_posting_updated | When a job posting is updated. |
| ats_job_posting_deleted | When a job posting is deleted. |
| timeoff_leave_created | When a Timeoff Leave is created. |
| timeoff_leave_destroyed | When a Timeoff Leave is destroyed. |
| timeoff_leave_updated | When a Timeoff Leave suffers any changes. |
| timeoff_leave_approved | When a Timeoff Leave is explicitly approved. |
| timeoff_leave_rejected | When a Timeoff Leave is rejected. |
| shift_management_shift_destroyed | When a single Shift Management Shift is destroyed. |
| shift_management_shift_bulk_destroyed | When Shift Management Shifts are destroyed in bulk. |
| document_created | When a document is created. |
| task_created | When a task is created. |
| contract_version_created | When a contract version is created. |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_subscription_response = factorial.webhook.create_subscription(
    type="employee_created",
    target_url="https://webhook.site/48103127-b1f6-3215-8f18-60fdbc013e3f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### target_url: `str`<a id="target_url-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookCreateSubscriptionRequest`](./factorial_python_sdk/type/webhook_create_subscription_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookCreateSubscriptionResponse`](./factorial_python_sdk/pydantic/webhook_create_subscription_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.webhook.delete_webhook`<a id="factorialwebhookdelete_webhook"></a>

Delete a Webook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_webhook_response = factorial.webhook.delete_webhook(
    id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookV2`](./factorial_python_sdk/pydantic/webhook_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/webhooks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.webhook.delete_webhook_by_id`<a id="factorialwebhookdelete_webhook_by_id"></a>

Delete a Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_webhook_by_id_response = factorial.webhook.delete_webhook_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookDeleteWebhookByIdResponse`](./factorial_python_sdk/pydantic/webhook_delete_webhook_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/core/webhooks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.webhook.subscription_create`<a id="factorialwebhooksubscription_create"></a>

> Creates a subscription for a determined webhook type. If webhook already exists, it just changes the target_url.

 ## Webhooks Types

| **Subscription Type** | **Information** |
| --- | --- |
| Authentication::Events::AccessInvited | When creating a new employee, optionally you can send an invitation to create an account in Factorial. If you send an invitation, this event gets triggered. |
| Employees::Events::EmployeeCreated | When creating a new employee, after submitting the form, this event gets triggered. |
| Employees::Events::EmployeeUpdated| When updating personal protected employee information such has birthday, this event gets triggered. |
| Employees::Events::EmployeeTerminated | When terminating an employee, after submitting the form, this event gets triggered |
| Employees::Events::EmployeeUnterminated | When un terminating an employee, after submitting the form, this event gets triggered |
| Attendance::Events::ClockIn | When the user clocks in and starts the timer, this event is triggered. |
| Attendance::Events::ClockOut | When the user clocks out and stops the timer, this event is triggered |
| Attendance::Events::AttendanceShiftCreated | When the user creates a shift, this event is triggered |
| Attendance::Events::AttendanceShiftUpdated | When the user edits a shift, this event is triggered |
| Attendance::Events::AttendanceShiftDeleted | When the user deletes a shift, this event is triggered |
| Ats::Events::ApplicationCreated | When a candidate applies for a posting. |
| Ats::Events::ApplicationUpdated | When a candidates application for a posting suffers changes. |
| Ats::Events::JobPostingCreated | When a job posting is created. |
| Ats::Events::JobPostingUpdated | When a job posting is updated. |
| Ats::Events::JobPostingDeleted | When a job posting is deleted. |
| Timeoff::Events::LeaveCreated | When a Timeoff Leave is created. |
| Timeoff::Events::LeaveDestroyed | When a Timeoff Leave is destroyed. |
| Timeoff::Events::LeaveUpdated | When a Timeoff Leave suffers any changes. |
| Timeoff::Events::LeaveApproved | When a Timeoff Leave is explicitly approved. |
| Timeoff::Events::LeaveRejected | When a Timeoff Leave is rejected. |
| Documents::Events::Created | When a document is created. |
| Tasks::Events::Created | When a task is created. |
| Contracts::Events::ContractVersionCreated | When a contract version is created. |
| Payroll::Events::SupplementCreated | When a payroll supplement is created. |
| Payroll::Events::SupplementUpdated | When a payroll supplement is updated. |
| Payroll::Events::SupplementDeleted | When a payroll supplement is deleted. |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
subscription_create_response = factorial.webhook.subscription_create(
    subscription_type="Employees::Events::EmployeeCreated",
    target_url="https://webhook.site/48103127-b1f6-3215-8f18-60fdbc013e3f",
    name="creating employee webhook",
    challenge="9288376100399000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_type: `str`<a id="subscription_type-str"></a>

##### target_url: `str`<a id="target_url-str"></a>

##### name: `str`<a id="name-str"></a>

##### challenge: `str`<a id="challenge-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookSubscriptionCreateRequest`](./factorial_python_sdk/type/webhook_subscription_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscriptionCreateResponse`](./factorial_python_sdk/pydantic/webhook_subscription_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.webhook.update_webhook_by_id`<a id="factorialwebhookupdate_webhook_by_id"></a>

Update a Webook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_by_id_response = factorial.webhook.update_webhook_by_id(
    id="1",
    target_url="Employees::Events::EmployeeCreated",
    name="creating employee webhook",
    challenge="9288376100399000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

(Required)

##### target_url: `str`<a id="target_url-str"></a>

##### name: `str`<a id="name-str"></a>

##### challenge: `str`<a id="challenge-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookUpdateWebhookByIdRequest`](./factorial_python_sdk/type/webhook_update_webhook_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookV2`](./factorial_python_sdk/pydantic/webhook_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/webhooks/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.workplace.create_new_workplace`<a id="factorialworkplacecreate_new_workplace"></a>

Creates a workplace for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_workplace_response = factorial.workplace.create_new_workplace(
    name="First Workspace",
    country="es",
    timezone="etc/UTC",
    state="CT",
    city="Barcelona",
    address_line_1="Swatch strasse 3",
    address_line_2="Atiquen terceren",
    postal_code="C1231",
    phone_number="55555555",
    company_id=2,
    legal_entity_id=2,
    main=True,
    latitude=41.39612,
    longitude=2.19123,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### country: `str`<a id="country-str"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### state: `str`<a id="state-str"></a>

##### city: `str`<a id="city-str"></a>

##### address_line_1: `str`<a id="address_line_1-str"></a>

##### address_line_2: `str`<a id="address_line_2-str"></a>

##### postal_code: `str`<a id="postal_code-str"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### company_id: `int`<a id="company_id-int"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### main: `bool`<a id="main-bool"></a>

##### latitude: `Union[int, float]`<a id="latitude-unionint-float"></a>

##### longitude: `Union[int, float]`<a id="longitude-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkplaceCreateNewWorkplaceRequest`](./factorial_python_sdk/type/workplace_create_new_workplace_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Workplace`](./factorial_python_sdk/pydantic/workplace.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/workplaces` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.workplace.get_by_id`<a id="factorialworkplaceget_by_id"></a>

This endpoint allows you to retrieve a workplace by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = factorial.workplace.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Workplace`](./factorial_python_sdk/pydantic/workplace.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/workplaces/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.workplace.list_all_workplaces`<a id="factorialworkplacelist_all_workplaces"></a>

This endpoint allows you to retrieve all workplaces for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_workplaces_response = factorial.workplace.list_all_workplaces(
    ids="1,2",
    employee_ids="1,2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Workplaces id comma separated values

##### employee_ids: `str`<a id="employee_ids-str"></a>

Employees id comma separated values

#### 🔄 Return<a id="🔄-return"></a>

[`WorkplaceListAllWorkplacesResponse`](./factorial_python_sdk/pydantic/workplace_list_all_workplaces_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/workplaces` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.workplace.remove_workplace`<a id="factorialworkplaceremove_workplace"></a>

Delete a workplace

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_workplace_response = factorial.workplace.remove_workplace(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(Required)

#### 🔄 Return<a id="🔄-return"></a>

[`WorkplaceRemoveWorkplaceResponse`](./factorial_python_sdk/pydantic/workplace_remove_workplace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/workplaces/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `factorial.workplace.update_workplace_by_id`<a id="factorialworkplaceupdate_workplace_by_id"></a>

Updates a workplace of a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_workplace_by_id_response = factorial.workplace.update_workplace_by_id(
    id=1,
    name="First Workspace",
    country="es",
    state="CT",
    city="Barcelona",
    address_line_1="Swatch strasse 3",
    address_line_2="Atiquen terceren",
    postal_code="C1231",
    phone_number="55555555",
    payroll_policy_id=2,
    main=True,
    timezone="etc/UTC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### name: `str`<a id="name-str"></a>

##### country: `str`<a id="country-str"></a>

##### state: `str`<a id="state-str"></a>

##### city: `str`<a id="city-str"></a>

##### address_line_1: `str`<a id="address_line_1-str"></a>

##### address_line_2: `str`<a id="address_line_2-str"></a>

##### postal_code: `str`<a id="postal_code-str"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### payroll_policy_id: `int`<a id="payroll_policy_id-int"></a>

##### main: `bool`<a id="main-bool"></a>

##### timezone: `str`<a id="timezone-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkplaceUpdateWorkplaceByIdRequest`](./factorial_python_sdk/type/workplace_update_workplace_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Workplace`](./factorial_python_sdk/pydantic/workplace.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/core/workplaces/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
