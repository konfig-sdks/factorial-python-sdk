# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from factorial_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_EMPLOYEES = "/v1/employees"
    V1_EMPLOYEES_ID = "/v1/employees/{id}"
    V1_EMPLOYEES_ID_TERMINATE = "/v1/employees/{id}/terminate"
    V1_EMPLOYEES_ID_UNTERMINATE = "/v1/employees/{id}/unterminate"
    V2_CORE_EMPLOYEES = "/v2/core/employees"
    V2_CORE_EMPLOYEES_ID = "/v2/core/employees/{id}"
    V2_CORE_EMPLOYEES_ID_INVITE = "/v2/core/employees/{id}/invite"
    V2_CORE_EMPLOYEES_ID_EMAIL = "/v2/core/employees/{id}/email"
    V2_CORE_EMPLOYEES_ID_TERMINATE = "/v2/core/employees/{id}/terminate"
    V2_CORE_EMPLOYEES_ID_UNTERMINATE = "/v2/core/employees/{id}/unterminate"
    V2_CORE_WEBHOOKS = "/v2/core/webhooks"
    V2_CORE_WEBHOOKS_ID = "/v2/core/webhooks/{id}"
    V1_ME = "/v1/me"
    V1_LOCATIONS = "/v1/locations"
    V1_LOCATIONS_ID = "/v1/locations/{id}"
    V1_COMPANY_HOLIDAYS = "/v1/company_holidays"
    V1_COMPANY_HOLIDAYS_ID = "/v1/company_holidays/{id}"
    V1_CORE_TEAMS = "/v1/core/teams"
    V1_CORE_TEAMS_ID = "/v1/core/teams/{id}"
    V1_CORE_TEAMS_ID_EMPLOYEES_EMPLOYEE_ID = "/v1/core/teams/{id}/employees/{employee_id}"
    V1_CORE_FOLDERS = "/v1/core/folders"
    V1_CORE_FOLDERS_ID = "/v1/core/folders/{id}"
    V1_CORE_DOCUMENTS = "/v1/core/documents"
    V1_CORE_DOCUMENTS_ID = "/v1/core/documents/{id}"
    V1_CORE_LEGAL_ENTITIES = "/v1/core/legal_entities"
    V1_CORE_LEGAL_ENTITIES_ID = "/v1/core/legal_entities/{id}"
    V1_CORE_KEYS = "/v1/core/keys"
    V1_CORE_KEYS_ID = "/v1/core/keys/{id}"
    V1_CORE_TASKS = "/v1/core/tasks"
    V1_CORE_TASKS_ID = "/v1/core/tasks/{id}"
    V1_CORE_TASKS_ID_RESOLVE = "/v1/core/tasks/{id}/resolve"
    V1_CORE_TASKS_ID_COPY = "/v1/core/tasks/{id}/copy"
    V1_CORE_TASKS_ID_FILES = "/v1/core/tasks/{id}/files"
    V1_CORE_TASKS_TASK_ID_FILES_ID = "/v1/core/tasks/{task_id}/files/{id}"
    V1_TIME_SHIFTS = "/v1/time/shifts"
    V1_TIME_SHIFTS_CLOCK_IN = "/v1/time/shifts/clock_in"
    V1_TIME_SHIFTS_CLOCK_OUT = "/v1/time/shifts/clock_out"
    V1_TIME_SHIFTS_TOGGLE = "/v1/time/shifts/toggle"
    V1_TIME_SHIFTS_ID = "/v1/time/shifts/{id}"
    V2_TIME_ATTENDANCE = "/v2/time/attendance"
    V1_TIME_LEAVE_TYPES = "/v1/time/leave_types"
    V1_TIME_LEAVE_TYPES_ID = "/v1/time/leave_types/{id}"
    V1_TIME_LEAVES = "/v1/time/leaves"
    V1_TIME_LEAVES_ID = "/v1/time/leaves/{id}"
    V2_TIME_LEAVES = "/v2/time/leaves"
    V2_TIME_LEAVES_ID = "/v2/time/leaves/{id}"
    V1_PAYROLL_FAMILY_SITUATION = "/v1/payroll/family_situation"
    V1_PAYROLL_FAMILY_SITUATION_ID = "/v1/payroll/family_situation/{id}"
    V1_CUSTOM_FIELDS = "/v1/custom_fields"
    V1_CUSTOM_FIELDS_VALUES = "/v1/custom_fields/values"
    V1_POSTS = "/v1/posts"
    V1_POSTS_ID = "/v1/posts/{id}"
    V1_ATS_JOB_POSTINGS = "/v1/ats/job_postings"
    V1_ATS_JOB_POSTINGS_ID = "/v1/ats/job_postings/{id}"
    V1_ATS_JOB_POSTINGS_ID_DUPLICATE = "/v1/ats/job_postings/{id}/duplicate"
    V1_ATS_CANDIDATES = "/v1/ats/candidates"
    V1_ATS_CANDIDATES_ID = "/v1/ats/candidates/{id}"
    V1_PAYROLL_CONTRACT_VERSIONS = "/v1/payroll/contract_versions"
    V1_PAYROLL_CONTRACT_VERSIONS_ID = "/v1/payroll/contract_versions/{id}"
    V1_PAYROLL_REFERENCE_CONTRACTS = "/v1/payroll/reference_contracts"
    V1_PAYROLL_SUPPLEMENTS = "/v1/payroll/supplements"
    V1_PAYROLL_SUPPLEMENTS_ID = "/v1/payroll/supplements/{id}"
    V2_PAYROLL_INTEGRATIONS_CODES = "/v2/payroll_integrations/codes"
    V2_PAYROLL_INTEGRATIONS_CODES_ID = "/v2/payroll_integrations/codes/{id}"
    V2_PAYROLL_INTEGRATIONS_CODES_ID_FIND_EMPLOYEE = "/v2/payroll_integrations/codes/{id}/find_employee"
    V1_TIME_SHIFTS_MANAGEMENT = "/v1/time/shifts_management"
    V1_TIME_SHIFTS_MANAGEMENT_PUBLISH = "/v1/time/shifts_management/publish"
    V1_TIME_SHIFTS_MANAGEMENT_ID_LOCATIONS = "/v1/time/shifts_management/{id}/locations"
    V1_TIME_SHIFTS_MANAGEMENT_ID_NOTES = "/v1/time/shifts_management/{id}/notes"
    V1_TIME_SHIFTS_MANAGEMENT_ID = "/v1/time/shifts_management/{id}"
    V1_TIME_BREAKS_START = "/v1/time/breaks/start"
    V1_TIME_BREAKS_END = "/v1/time/breaks/end"
    V1_TIME_BREAKS = "/v1/time/breaks"
    V1_TIME_BREAK_CONFIGURATIONS_FOR_DATES = "/v1/time/break_configurations_for_dates"
    V1_ATS_APPLICATIONS = "/v1/ats/applications"
    V1_ATS_APPLICATIONS_ID = "/v1/ats/applications/{id}"
    V1_ATS_MESSAGES = "/v1/ats/messages"
    V2_CORE_BULK_EMPLOYEE = "/v2/core/bulk/employee"
    V2_CORE_BULK_ATTENDANCE = "/v2/core/bulk/attendance"
    V2_CORE_BULK_CONTRACT_VERSION = "/v2/core/bulk/contract_version"
    V1_CORE_CUSTOM_TABLES = "/v1/core/custom/tables"
    V1_CORE_CUSTOM_TABLES_ID = "/v1/core/custom/tables/{id}"
    V1_CORE_CUSTOM_TABLES_ID_FIELDS = "/v1/core/custom/tables/{id}/fields"
    V1_CORE_CUSTOM_TABLES_ID_VALUES_EMPLOYEE_ID = "/v1/core/custom/tables/{id}/values/{employee_id}"
    V1_CORE_EVENTS = "/v1/core/events"
    V1_CORE_WEBHOOKS = "/v1/core/webhooks"
    V1_CORE_WEBHOOKS_ID = "/v1/core/webhooks/{id}"
    V1_TIME_POLICIES = "/v1/time/policies"
    V1_TIME_POLICIES_ID = "/v1/time/policies/{id}"
    V1_FINANCE_EXPENSES = "/v1/finance/expenses"
    V1_FINANCE_EXPENSES_ID = "/v1/finance/expenses/{id}"
    V1_PAYROLL_COMPENSATIONS = "/v1/payroll/compensations"
    V1_PAYROLL_COMPENSATIONS_ID = "/v1/payroll/compensations/{id}"
    V1_PAYROLL_TAXONOMIES = "/v1/payroll/taxonomies"
    V1_PAYROLL_TAXONOMIES_ID = "/v1/payroll/taxonomies/{id}"
    V2_CORE_WORKPLACES = "/v2/core/workplaces"
    V2_CORE_WORKPLACES_ID = "/v2/core/workplaces/{id}"
    V2_CUSTOM_FIELDS_FIELDS = "/v2/custom_fields/fields"
    V2_CUSTOM_FIELDS_FIELDS_ID = "/v2/custom_fields/fields/{id}"
    V2_CUSTOM_FIELDS_VALUES = "/v2/custom_fields/values"
    V2_CUSTOM_FIELDS_VALUES_ID = "/v2/custom_fields/values/{id}"
