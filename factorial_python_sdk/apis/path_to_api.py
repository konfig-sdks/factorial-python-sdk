import typing_extensions

from factorial_python_sdk.paths import PathValues
from factorial_python_sdk.apis.paths.v1_employees import V1Employees
from factorial_python_sdk.apis.paths.v1_employees_id import V1EmployeesId
from factorial_python_sdk.apis.paths.v1_employees_id_terminate import V1EmployeesIdTerminate
from factorial_python_sdk.apis.paths.v1_employees_id_unterminate import V1EmployeesIdUnterminate
from factorial_python_sdk.apis.paths.v2_core_employees import V2CoreEmployees
from factorial_python_sdk.apis.paths.v2_core_employees_id import V2CoreEmployeesId
from factorial_python_sdk.apis.paths.v2_core_employees_id_invite import V2CoreEmployeesIdInvite
from factorial_python_sdk.apis.paths.v2_core_employees_id_email import V2CoreEmployeesIdEmail
from factorial_python_sdk.apis.paths.v2_core_employees_id_terminate import V2CoreEmployeesIdTerminate
from factorial_python_sdk.apis.paths.v2_core_employees_id_unterminate import V2CoreEmployeesIdUnterminate
from factorial_python_sdk.apis.paths.v2_core_webhooks import V2CoreWebhooks
from factorial_python_sdk.apis.paths.v2_core_webhooks_id import V2CoreWebhooksId
from factorial_python_sdk.apis.paths.v1_me import V1Me
from factorial_python_sdk.apis.paths.v1_locations import V1Locations
from factorial_python_sdk.apis.paths.v1_locations_id import V1LocationsId
from factorial_python_sdk.apis.paths.v1_company_holidays import V1CompanyHolidays
from factorial_python_sdk.apis.paths.v1_company_holidays_id import V1CompanyHolidaysId
from factorial_python_sdk.apis.paths.v1_core_teams import V1CoreTeams
from factorial_python_sdk.apis.paths.v1_core_teams_id import V1CoreTeamsId
from factorial_python_sdk.apis.paths.v1_core_teams_id_employees_employee_id import V1CoreTeamsIdEmployeesEmployeeId
from factorial_python_sdk.apis.paths.v1_core_folders import V1CoreFolders
from factorial_python_sdk.apis.paths.v1_core_folders_id import V1CoreFoldersId
from factorial_python_sdk.apis.paths.v1_core_documents import V1CoreDocuments
from factorial_python_sdk.apis.paths.v1_core_documents_id import V1CoreDocumentsId
from factorial_python_sdk.apis.paths.v1_core_legal_entities import V1CoreLegalEntities
from factorial_python_sdk.apis.paths.v1_core_legal_entities_id import V1CoreLegalEntitiesId
from factorial_python_sdk.apis.paths.v1_core_keys import V1CoreKeys
from factorial_python_sdk.apis.paths.v1_core_keys_id import V1CoreKeysId
from factorial_python_sdk.apis.paths.v1_core_tasks import V1CoreTasks
from factorial_python_sdk.apis.paths.v1_core_tasks_id import V1CoreTasksId
from factorial_python_sdk.apis.paths.v1_core_tasks_id_resolve import V1CoreTasksIdResolve
from factorial_python_sdk.apis.paths.v1_core_tasks_id_copy import V1CoreTasksIdCopy
from factorial_python_sdk.apis.paths.v1_core_tasks_id_files import V1CoreTasksIdFiles
from factorial_python_sdk.apis.paths.v1_core_tasks_task_id_files_id import V1CoreTasksTaskIdFilesId
from factorial_python_sdk.apis.paths.v1_time_shifts import V1TimeShifts
from factorial_python_sdk.apis.paths.v1_time_shifts_clock_in import V1TimeShiftsClockIn
from factorial_python_sdk.apis.paths.v1_time_shifts_clock_out import V1TimeShiftsClockOut
from factorial_python_sdk.apis.paths.v1_time_shifts_toggle import V1TimeShiftsToggle
from factorial_python_sdk.apis.paths.v1_time_shifts_id import V1TimeShiftsId
from factorial_python_sdk.apis.paths.v2_time_attendance import V2TimeAttendance
from factorial_python_sdk.apis.paths.v1_time_leave_types import V1TimeLeaveTypes
from factorial_python_sdk.apis.paths.v1_time_leave_types_id import V1TimeLeaveTypesId
from factorial_python_sdk.apis.paths.v1_time_leaves import V1TimeLeaves
from factorial_python_sdk.apis.paths.v1_time_leaves_id import V1TimeLeavesId
from factorial_python_sdk.apis.paths.v2_time_leaves import V2TimeLeaves
from factorial_python_sdk.apis.paths.v2_time_leaves_id import V2TimeLeavesId
from factorial_python_sdk.apis.paths.v1_payroll_family_situation import V1PayrollFamilySituation
from factorial_python_sdk.apis.paths.v1_payroll_family_situation_id import V1PayrollFamilySituationId
from factorial_python_sdk.apis.paths.v1_custom_fields import V1CustomFields
from factorial_python_sdk.apis.paths.v1_custom_fields_values import V1CustomFieldsValues
from factorial_python_sdk.apis.paths.v1_posts import V1Posts
from factorial_python_sdk.apis.paths.v1_posts_id import V1PostsId
from factorial_python_sdk.apis.paths.v1_ats_job_postings import V1AtsJobPostings
from factorial_python_sdk.apis.paths.v1_ats_job_postings_id import V1AtsJobPostingsId
from factorial_python_sdk.apis.paths.v1_ats_job_postings_id_duplicate import V1AtsJobPostingsIdDuplicate
from factorial_python_sdk.apis.paths.v1_ats_candidates import V1AtsCandidates
from factorial_python_sdk.apis.paths.v1_ats_candidates_id import V1AtsCandidatesId
from factorial_python_sdk.apis.paths.v1_payroll_contract_versions import V1PayrollContractVersions
from factorial_python_sdk.apis.paths.v1_payroll_contract_versions_id import V1PayrollContractVersionsId
from factorial_python_sdk.apis.paths.v1_payroll_reference_contracts import V1PayrollReferenceContracts
from factorial_python_sdk.apis.paths.v1_payroll_supplements import V1PayrollSupplements
from factorial_python_sdk.apis.paths.v1_payroll_supplements_id import V1PayrollSupplementsId
from factorial_python_sdk.apis.paths.v2_payroll_integrations_codes import V2PayrollIntegrationsCodes
from factorial_python_sdk.apis.paths.v2_payroll_integrations_codes_id import V2PayrollIntegrationsCodesId
from factorial_python_sdk.apis.paths.v2_payroll_integrations_codes_id_find_employee import V2PayrollIntegrationsCodesIdFindEmployee
from factorial_python_sdk.apis.paths.v1_time_shifts_management import V1TimeShiftsManagement
from factorial_python_sdk.apis.paths.v1_time_shifts_management_publish import V1TimeShiftsManagementPublish
from factorial_python_sdk.apis.paths.v1_time_shifts_management_id_locations import V1TimeShiftsManagementIdLocations
from factorial_python_sdk.apis.paths.v1_time_shifts_management_id_notes import V1TimeShiftsManagementIdNotes
from factorial_python_sdk.apis.paths.v1_time_shifts_management_id import V1TimeShiftsManagementId
from factorial_python_sdk.apis.paths.v1_time_breaks_start import V1TimeBreaksStart
from factorial_python_sdk.apis.paths.v1_time_breaks_end import V1TimeBreaksEnd
from factorial_python_sdk.apis.paths.v1_time_breaks import V1TimeBreaks
from factorial_python_sdk.apis.paths.v1_time_break_configurations_for_dates import V1TimeBreakConfigurationsForDates
from factorial_python_sdk.apis.paths.v1_ats_applications import V1AtsApplications
from factorial_python_sdk.apis.paths.v1_ats_applications_id import V1AtsApplicationsId
from factorial_python_sdk.apis.paths.v1_ats_messages import V1AtsMessages
from factorial_python_sdk.apis.paths.v2_core_bulk_employee import V2CoreBulkEmployee
from factorial_python_sdk.apis.paths.v2_core_bulk_attendance import V2CoreBulkAttendance
from factorial_python_sdk.apis.paths.v2_core_bulk_contract_version import V2CoreBulkContractVersion
from factorial_python_sdk.apis.paths.v1_core_custom_tables import V1CoreCustomTables
from factorial_python_sdk.apis.paths.v1_core_custom_tables_id import V1CoreCustomTablesId
from factorial_python_sdk.apis.paths.v1_core_custom_tables_id_fields import V1CoreCustomTablesIdFields
from factorial_python_sdk.apis.paths.v1_core_custom_tables_id_values_employee_id import V1CoreCustomTablesIdValuesEmployeeId
from factorial_python_sdk.apis.paths.v1_core_events import V1CoreEvents
from factorial_python_sdk.apis.paths.v1_core_webhooks import V1CoreWebhooks
from factorial_python_sdk.apis.paths.v1_core_webhooks_id import V1CoreWebhooksId
from factorial_python_sdk.apis.paths.v1_time_policies import V1TimePolicies
from factorial_python_sdk.apis.paths.v1_time_policies_id import V1TimePoliciesId
from factorial_python_sdk.apis.paths.v1_finance_expenses import V1FinanceExpenses
from factorial_python_sdk.apis.paths.v1_finance_expenses_id import V1FinanceExpensesId
from factorial_python_sdk.apis.paths.v1_payroll_compensations import V1PayrollCompensations
from factorial_python_sdk.apis.paths.v1_payroll_compensations_id import V1PayrollCompensationsId
from factorial_python_sdk.apis.paths.v1_payroll_taxonomies import V1PayrollTaxonomies
from factorial_python_sdk.apis.paths.v1_payroll_taxonomies_id import V1PayrollTaxonomiesId
from factorial_python_sdk.apis.paths.v2_core_workplaces import V2CoreWorkplaces
from factorial_python_sdk.apis.paths.v2_core_workplaces_id import V2CoreWorkplacesId
from factorial_python_sdk.apis.paths.v2_custom_fields_fields import V2CustomFieldsFields
from factorial_python_sdk.apis.paths.v2_custom_fields_fields_id import V2CustomFieldsFieldsId
from factorial_python_sdk.apis.paths.v2_custom_fields_values import V2CustomFieldsValues
from factorial_python_sdk.apis.paths.v2_custom_fields_values_id import V2CustomFieldsValuesId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_EMPLOYEES: V1Employees,
        PathValues.V1_EMPLOYEES_ID: V1EmployeesId,
        PathValues.V1_EMPLOYEES_ID_TERMINATE: V1EmployeesIdTerminate,
        PathValues.V1_EMPLOYEES_ID_UNTERMINATE: V1EmployeesIdUnterminate,
        PathValues.V2_CORE_EMPLOYEES: V2CoreEmployees,
        PathValues.V2_CORE_EMPLOYEES_ID: V2CoreEmployeesId,
        PathValues.V2_CORE_EMPLOYEES_ID_INVITE: V2CoreEmployeesIdInvite,
        PathValues.V2_CORE_EMPLOYEES_ID_EMAIL: V2CoreEmployeesIdEmail,
        PathValues.V2_CORE_EMPLOYEES_ID_TERMINATE: V2CoreEmployeesIdTerminate,
        PathValues.V2_CORE_EMPLOYEES_ID_UNTERMINATE: V2CoreEmployeesIdUnterminate,
        PathValues.V2_CORE_WEBHOOKS: V2CoreWebhooks,
        PathValues.V2_CORE_WEBHOOKS_ID: V2CoreWebhooksId,
        PathValues.V1_ME: V1Me,
        PathValues.V1_LOCATIONS: V1Locations,
        PathValues.V1_LOCATIONS_ID: V1LocationsId,
        PathValues.V1_COMPANY_HOLIDAYS: V1CompanyHolidays,
        PathValues.V1_COMPANY_HOLIDAYS_ID: V1CompanyHolidaysId,
        PathValues.V1_CORE_TEAMS: V1CoreTeams,
        PathValues.V1_CORE_TEAMS_ID: V1CoreTeamsId,
        PathValues.V1_CORE_TEAMS_ID_EMPLOYEES_EMPLOYEE_ID: V1CoreTeamsIdEmployeesEmployeeId,
        PathValues.V1_CORE_FOLDERS: V1CoreFolders,
        PathValues.V1_CORE_FOLDERS_ID: V1CoreFoldersId,
        PathValues.V1_CORE_DOCUMENTS: V1CoreDocuments,
        PathValues.V1_CORE_DOCUMENTS_ID: V1CoreDocumentsId,
        PathValues.V1_CORE_LEGAL_ENTITIES: V1CoreLegalEntities,
        PathValues.V1_CORE_LEGAL_ENTITIES_ID: V1CoreLegalEntitiesId,
        PathValues.V1_CORE_KEYS: V1CoreKeys,
        PathValues.V1_CORE_KEYS_ID: V1CoreKeysId,
        PathValues.V1_CORE_TASKS: V1CoreTasks,
        PathValues.V1_CORE_TASKS_ID: V1CoreTasksId,
        PathValues.V1_CORE_TASKS_ID_RESOLVE: V1CoreTasksIdResolve,
        PathValues.V1_CORE_TASKS_ID_COPY: V1CoreTasksIdCopy,
        PathValues.V1_CORE_TASKS_ID_FILES: V1CoreTasksIdFiles,
        PathValues.V1_CORE_TASKS_TASK_ID_FILES_ID: V1CoreTasksTaskIdFilesId,
        PathValues.V1_TIME_SHIFTS: V1TimeShifts,
        PathValues.V1_TIME_SHIFTS_CLOCK_IN: V1TimeShiftsClockIn,
        PathValues.V1_TIME_SHIFTS_CLOCK_OUT: V1TimeShiftsClockOut,
        PathValues.V1_TIME_SHIFTS_TOGGLE: V1TimeShiftsToggle,
        PathValues.V1_TIME_SHIFTS_ID: V1TimeShiftsId,
        PathValues.V2_TIME_ATTENDANCE: V2TimeAttendance,
        PathValues.V1_TIME_LEAVE_TYPES: V1TimeLeaveTypes,
        PathValues.V1_TIME_LEAVE_TYPES_ID: V1TimeLeaveTypesId,
        PathValues.V1_TIME_LEAVES: V1TimeLeaves,
        PathValues.V1_TIME_LEAVES_ID: V1TimeLeavesId,
        PathValues.V2_TIME_LEAVES: V2TimeLeaves,
        PathValues.V2_TIME_LEAVES_ID: V2TimeLeavesId,
        PathValues.V1_PAYROLL_FAMILY_SITUATION: V1PayrollFamilySituation,
        PathValues.V1_PAYROLL_FAMILY_SITUATION_ID: V1PayrollFamilySituationId,
        PathValues.V1_CUSTOM_FIELDS: V1CustomFields,
        PathValues.V1_CUSTOM_FIELDS_VALUES: V1CustomFieldsValues,
        PathValues.V1_POSTS: V1Posts,
        PathValues.V1_POSTS_ID: V1PostsId,
        PathValues.V1_ATS_JOB_POSTINGS: V1AtsJobPostings,
        PathValues.V1_ATS_JOB_POSTINGS_ID: V1AtsJobPostingsId,
        PathValues.V1_ATS_JOB_POSTINGS_ID_DUPLICATE: V1AtsJobPostingsIdDuplicate,
        PathValues.V1_ATS_CANDIDATES: V1AtsCandidates,
        PathValues.V1_ATS_CANDIDATES_ID: V1AtsCandidatesId,
        PathValues.V1_PAYROLL_CONTRACT_VERSIONS: V1PayrollContractVersions,
        PathValues.V1_PAYROLL_CONTRACT_VERSIONS_ID: V1PayrollContractVersionsId,
        PathValues.V1_PAYROLL_REFERENCE_CONTRACTS: V1PayrollReferenceContracts,
        PathValues.V1_PAYROLL_SUPPLEMENTS: V1PayrollSupplements,
        PathValues.V1_PAYROLL_SUPPLEMENTS_ID: V1PayrollSupplementsId,
        PathValues.V2_PAYROLL_INTEGRATIONS_CODES: V2PayrollIntegrationsCodes,
        PathValues.V2_PAYROLL_INTEGRATIONS_CODES_ID: V2PayrollIntegrationsCodesId,
        PathValues.V2_PAYROLL_INTEGRATIONS_CODES_ID_FIND_EMPLOYEE: V2PayrollIntegrationsCodesIdFindEmployee,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT: V1TimeShiftsManagement,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_PUBLISH: V1TimeShiftsManagementPublish,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_ID_LOCATIONS: V1TimeShiftsManagementIdLocations,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_ID_NOTES: V1TimeShiftsManagementIdNotes,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_ID: V1TimeShiftsManagementId,
        PathValues.V1_TIME_BREAKS_START: V1TimeBreaksStart,
        PathValues.V1_TIME_BREAKS_END: V1TimeBreaksEnd,
        PathValues.V1_TIME_BREAKS: V1TimeBreaks,
        PathValues.V1_TIME_BREAK_CONFIGURATIONS_FOR_DATES: V1TimeBreakConfigurationsForDates,
        PathValues.V1_ATS_APPLICATIONS: V1AtsApplications,
        PathValues.V1_ATS_APPLICATIONS_ID: V1AtsApplicationsId,
        PathValues.V1_ATS_MESSAGES: V1AtsMessages,
        PathValues.V2_CORE_BULK_EMPLOYEE: V2CoreBulkEmployee,
        PathValues.V2_CORE_BULK_ATTENDANCE: V2CoreBulkAttendance,
        PathValues.V2_CORE_BULK_CONTRACT_VERSION: V2CoreBulkContractVersion,
        PathValues.V1_CORE_CUSTOM_TABLES: V1CoreCustomTables,
        PathValues.V1_CORE_CUSTOM_TABLES_ID: V1CoreCustomTablesId,
        PathValues.V1_CORE_CUSTOM_TABLES_ID_FIELDS: V1CoreCustomTablesIdFields,
        PathValues.V1_CORE_CUSTOM_TABLES_ID_VALUES_EMPLOYEE_ID: V1CoreCustomTablesIdValuesEmployeeId,
        PathValues.V1_CORE_EVENTS: V1CoreEvents,
        PathValues.V1_CORE_WEBHOOKS: V1CoreWebhooks,
        PathValues.V1_CORE_WEBHOOKS_ID: V1CoreWebhooksId,
        PathValues.V1_TIME_POLICIES: V1TimePolicies,
        PathValues.V1_TIME_POLICIES_ID: V1TimePoliciesId,
        PathValues.V1_FINANCE_EXPENSES: V1FinanceExpenses,
        PathValues.V1_FINANCE_EXPENSES_ID: V1FinanceExpensesId,
        PathValues.V1_PAYROLL_COMPENSATIONS: V1PayrollCompensations,
        PathValues.V1_PAYROLL_COMPENSATIONS_ID: V1PayrollCompensationsId,
        PathValues.V1_PAYROLL_TAXONOMIES: V1PayrollTaxonomies,
        PathValues.V1_PAYROLL_TAXONOMIES_ID: V1PayrollTaxonomiesId,
        PathValues.V2_CORE_WORKPLACES: V2CoreWorkplaces,
        PathValues.V2_CORE_WORKPLACES_ID: V2CoreWorkplacesId,
        PathValues.V2_CUSTOM_FIELDS_FIELDS: V2CustomFieldsFields,
        PathValues.V2_CUSTOM_FIELDS_FIELDS_ID: V2CustomFieldsFieldsId,
        PathValues.V2_CUSTOM_FIELDS_VALUES: V2CustomFieldsValues,
        PathValues.V2_CUSTOM_FIELDS_VALUES_ID: V2CustomFieldsValuesId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_EMPLOYEES: V1Employees,
        PathValues.V1_EMPLOYEES_ID: V1EmployeesId,
        PathValues.V1_EMPLOYEES_ID_TERMINATE: V1EmployeesIdTerminate,
        PathValues.V1_EMPLOYEES_ID_UNTERMINATE: V1EmployeesIdUnterminate,
        PathValues.V2_CORE_EMPLOYEES: V2CoreEmployees,
        PathValues.V2_CORE_EMPLOYEES_ID: V2CoreEmployeesId,
        PathValues.V2_CORE_EMPLOYEES_ID_INVITE: V2CoreEmployeesIdInvite,
        PathValues.V2_CORE_EMPLOYEES_ID_EMAIL: V2CoreEmployeesIdEmail,
        PathValues.V2_CORE_EMPLOYEES_ID_TERMINATE: V2CoreEmployeesIdTerminate,
        PathValues.V2_CORE_EMPLOYEES_ID_UNTERMINATE: V2CoreEmployeesIdUnterminate,
        PathValues.V2_CORE_WEBHOOKS: V2CoreWebhooks,
        PathValues.V2_CORE_WEBHOOKS_ID: V2CoreWebhooksId,
        PathValues.V1_ME: V1Me,
        PathValues.V1_LOCATIONS: V1Locations,
        PathValues.V1_LOCATIONS_ID: V1LocationsId,
        PathValues.V1_COMPANY_HOLIDAYS: V1CompanyHolidays,
        PathValues.V1_COMPANY_HOLIDAYS_ID: V1CompanyHolidaysId,
        PathValues.V1_CORE_TEAMS: V1CoreTeams,
        PathValues.V1_CORE_TEAMS_ID: V1CoreTeamsId,
        PathValues.V1_CORE_TEAMS_ID_EMPLOYEES_EMPLOYEE_ID: V1CoreTeamsIdEmployeesEmployeeId,
        PathValues.V1_CORE_FOLDERS: V1CoreFolders,
        PathValues.V1_CORE_FOLDERS_ID: V1CoreFoldersId,
        PathValues.V1_CORE_DOCUMENTS: V1CoreDocuments,
        PathValues.V1_CORE_DOCUMENTS_ID: V1CoreDocumentsId,
        PathValues.V1_CORE_LEGAL_ENTITIES: V1CoreLegalEntities,
        PathValues.V1_CORE_LEGAL_ENTITIES_ID: V1CoreLegalEntitiesId,
        PathValues.V1_CORE_KEYS: V1CoreKeys,
        PathValues.V1_CORE_KEYS_ID: V1CoreKeysId,
        PathValues.V1_CORE_TASKS: V1CoreTasks,
        PathValues.V1_CORE_TASKS_ID: V1CoreTasksId,
        PathValues.V1_CORE_TASKS_ID_RESOLVE: V1CoreTasksIdResolve,
        PathValues.V1_CORE_TASKS_ID_COPY: V1CoreTasksIdCopy,
        PathValues.V1_CORE_TASKS_ID_FILES: V1CoreTasksIdFiles,
        PathValues.V1_CORE_TASKS_TASK_ID_FILES_ID: V1CoreTasksTaskIdFilesId,
        PathValues.V1_TIME_SHIFTS: V1TimeShifts,
        PathValues.V1_TIME_SHIFTS_CLOCK_IN: V1TimeShiftsClockIn,
        PathValues.V1_TIME_SHIFTS_CLOCK_OUT: V1TimeShiftsClockOut,
        PathValues.V1_TIME_SHIFTS_TOGGLE: V1TimeShiftsToggle,
        PathValues.V1_TIME_SHIFTS_ID: V1TimeShiftsId,
        PathValues.V2_TIME_ATTENDANCE: V2TimeAttendance,
        PathValues.V1_TIME_LEAVE_TYPES: V1TimeLeaveTypes,
        PathValues.V1_TIME_LEAVE_TYPES_ID: V1TimeLeaveTypesId,
        PathValues.V1_TIME_LEAVES: V1TimeLeaves,
        PathValues.V1_TIME_LEAVES_ID: V1TimeLeavesId,
        PathValues.V2_TIME_LEAVES: V2TimeLeaves,
        PathValues.V2_TIME_LEAVES_ID: V2TimeLeavesId,
        PathValues.V1_PAYROLL_FAMILY_SITUATION: V1PayrollFamilySituation,
        PathValues.V1_PAYROLL_FAMILY_SITUATION_ID: V1PayrollFamilySituationId,
        PathValues.V1_CUSTOM_FIELDS: V1CustomFields,
        PathValues.V1_CUSTOM_FIELDS_VALUES: V1CustomFieldsValues,
        PathValues.V1_POSTS: V1Posts,
        PathValues.V1_POSTS_ID: V1PostsId,
        PathValues.V1_ATS_JOB_POSTINGS: V1AtsJobPostings,
        PathValues.V1_ATS_JOB_POSTINGS_ID: V1AtsJobPostingsId,
        PathValues.V1_ATS_JOB_POSTINGS_ID_DUPLICATE: V1AtsJobPostingsIdDuplicate,
        PathValues.V1_ATS_CANDIDATES: V1AtsCandidates,
        PathValues.V1_ATS_CANDIDATES_ID: V1AtsCandidatesId,
        PathValues.V1_PAYROLL_CONTRACT_VERSIONS: V1PayrollContractVersions,
        PathValues.V1_PAYROLL_CONTRACT_VERSIONS_ID: V1PayrollContractVersionsId,
        PathValues.V1_PAYROLL_REFERENCE_CONTRACTS: V1PayrollReferenceContracts,
        PathValues.V1_PAYROLL_SUPPLEMENTS: V1PayrollSupplements,
        PathValues.V1_PAYROLL_SUPPLEMENTS_ID: V1PayrollSupplementsId,
        PathValues.V2_PAYROLL_INTEGRATIONS_CODES: V2PayrollIntegrationsCodes,
        PathValues.V2_PAYROLL_INTEGRATIONS_CODES_ID: V2PayrollIntegrationsCodesId,
        PathValues.V2_PAYROLL_INTEGRATIONS_CODES_ID_FIND_EMPLOYEE: V2PayrollIntegrationsCodesIdFindEmployee,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT: V1TimeShiftsManagement,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_PUBLISH: V1TimeShiftsManagementPublish,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_ID_LOCATIONS: V1TimeShiftsManagementIdLocations,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_ID_NOTES: V1TimeShiftsManagementIdNotes,
        PathValues.V1_TIME_SHIFTS_MANAGEMENT_ID: V1TimeShiftsManagementId,
        PathValues.V1_TIME_BREAKS_START: V1TimeBreaksStart,
        PathValues.V1_TIME_BREAKS_END: V1TimeBreaksEnd,
        PathValues.V1_TIME_BREAKS: V1TimeBreaks,
        PathValues.V1_TIME_BREAK_CONFIGURATIONS_FOR_DATES: V1TimeBreakConfigurationsForDates,
        PathValues.V1_ATS_APPLICATIONS: V1AtsApplications,
        PathValues.V1_ATS_APPLICATIONS_ID: V1AtsApplicationsId,
        PathValues.V1_ATS_MESSAGES: V1AtsMessages,
        PathValues.V2_CORE_BULK_EMPLOYEE: V2CoreBulkEmployee,
        PathValues.V2_CORE_BULK_ATTENDANCE: V2CoreBulkAttendance,
        PathValues.V2_CORE_BULK_CONTRACT_VERSION: V2CoreBulkContractVersion,
        PathValues.V1_CORE_CUSTOM_TABLES: V1CoreCustomTables,
        PathValues.V1_CORE_CUSTOM_TABLES_ID: V1CoreCustomTablesId,
        PathValues.V1_CORE_CUSTOM_TABLES_ID_FIELDS: V1CoreCustomTablesIdFields,
        PathValues.V1_CORE_CUSTOM_TABLES_ID_VALUES_EMPLOYEE_ID: V1CoreCustomTablesIdValuesEmployeeId,
        PathValues.V1_CORE_EVENTS: V1CoreEvents,
        PathValues.V1_CORE_WEBHOOKS: V1CoreWebhooks,
        PathValues.V1_CORE_WEBHOOKS_ID: V1CoreWebhooksId,
        PathValues.V1_TIME_POLICIES: V1TimePolicies,
        PathValues.V1_TIME_POLICIES_ID: V1TimePoliciesId,
        PathValues.V1_FINANCE_EXPENSES: V1FinanceExpenses,
        PathValues.V1_FINANCE_EXPENSES_ID: V1FinanceExpensesId,
        PathValues.V1_PAYROLL_COMPENSATIONS: V1PayrollCompensations,
        PathValues.V1_PAYROLL_COMPENSATIONS_ID: V1PayrollCompensationsId,
        PathValues.V1_PAYROLL_TAXONOMIES: V1PayrollTaxonomies,
        PathValues.V1_PAYROLL_TAXONOMIES_ID: V1PayrollTaxonomiesId,
        PathValues.V2_CORE_WORKPLACES: V2CoreWorkplaces,
        PathValues.V2_CORE_WORKPLACES_ID: V2CoreWorkplacesId,
        PathValues.V2_CUSTOM_FIELDS_FIELDS: V2CustomFieldsFields,
        PathValues.V2_CUSTOM_FIELDS_FIELDS_ID: V2CustomFieldsFieldsId,
        PathValues.V2_CUSTOM_FIELDS_VALUES: V2CustomFieldsValues,
        PathValues.V2_CUSTOM_FIELDS_VALUES_ID: V2CustomFieldsValuesId,
    }
)
