import typing_extensions

from factorial_python_sdk.apis.tags import TagValues
from factorial_python_sdk.apis.tags.employee_api import EmployeeApi
from factorial_python_sdk.apis.tags.leave_api import LeaveApi
from factorial_python_sdk.apis.tags.shift_api import ShiftApi
from factorial_python_sdk.apis.tags.task_api import TaskApi
from factorial_python_sdk.apis.tags.post_api import PostApi
from factorial_python_sdk.apis.tags.team_api import TeamApi
from factorial_python_sdk.apis.tags.webhook_api import WebhookApi
from factorial_python_sdk.apis.tags.document_api import DocumentApi
from factorial_python_sdk.apis.tags.workplace_api import WorkplaceApi
from factorial_python_sdk.apis.tags.compensation_api import CompensationApi
from factorial_python_sdk.apis.tags.folder_api import FolderApi
from factorial_python_sdk.apis.tags.custom_field_api import CustomFieldApi
from factorial_python_sdk.apis.tags.candidate_api import CandidateApi
from factorial_python_sdk.apis.tags.table_api import TableApi
from factorial_python_sdk.apis.tags.supplement_api import SupplementApi
from factorial_python_sdk.apis.tags.custom_field_value_api import CustomFieldValueApi
from factorial_python_sdk.apis.tags.key_api import KeyApi
from factorial_python_sdk.apis.tags.user_api import UserApi
from factorial_python_sdk.apis.tags.location_api import LocationApi
from factorial_python_sdk.apis.tags.model_break_api import ModelBreakApi
from factorial_python_sdk.apis.tags.attendance_api import AttendanceApi
from factorial_python_sdk.apis.tags.contract_version_api import ContractVersionApi
from factorial_python_sdk.apis.tags.integration_api import IntegrationApi
from factorial_python_sdk.apis.tags.contract_api import ContractApi
from factorial_python_sdk.apis.tags.message_api import MessageApi
from factorial_python_sdk.apis.tags.policy_api import PolicyApi
from factorial_python_sdk.apis.tags.holiday_api import HolidayApi
from factorial_python_sdk.apis.tags.expense_api import ExpenseApi
from factorial_python_sdk.apis.tags.application_api import ApplicationApi
from factorial_python_sdk.apis.tags.taxonomy_api import TaxonomyApi
from factorial_python_sdk.apis.tags.legal_entity_api import LegalEntityApi
from factorial_python_sdk.apis.tags.family_situation_api import FamilySituationApi
from factorial_python_sdk.apis.tags.event_api import EventApi
from factorial_python_sdk.apis.tags.custom_table_api import CustomTableApi
from factorial_python_sdk.apis.tags.integration_code_api import IntegrationCodeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.LEAVE: LeaveApi,
        TagValues.SHIFT: ShiftApi,
        TagValues.TASK: TaskApi,
        TagValues.POST: PostApi,
        TagValues.TEAM: TeamApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.DOCUMENT: DocumentApi,
        TagValues.WORKPLACE: WorkplaceApi,
        TagValues.COMPENSATION: CompensationApi,
        TagValues.FOLDER: FolderApi,
        TagValues.CUSTOM_FIELD: CustomFieldApi,
        TagValues.CANDIDATE: CandidateApi,
        TagValues.TABLE: TableApi,
        TagValues.SUPPLEMENT: SupplementApi,
        TagValues.CUSTOM_FIELD_VALUE: CustomFieldValueApi,
        TagValues.KEY: KeyApi,
        TagValues.USER: UserApi,
        TagValues.LOCATION: LocationApi,
        TagValues.BREAK: ModelBreakApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.CONTRACT_VERSION: ContractVersionApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.POLICY: PolicyApi,
        TagValues.HOLIDAY: HolidayApi,
        TagValues.EXPENSE: ExpenseApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.TAXONOMY: TaxonomyApi,
        TagValues.LEGAL_ENTITY: LegalEntityApi,
        TagValues.FAMILY_SITUATION: FamilySituationApi,
        TagValues.EVENT: EventApi,
        TagValues.CUSTOM_TABLE: CustomTableApi,
        TagValues.INTEGRATION_CODE: IntegrationCodeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.LEAVE: LeaveApi,
        TagValues.SHIFT: ShiftApi,
        TagValues.TASK: TaskApi,
        TagValues.POST: PostApi,
        TagValues.TEAM: TeamApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.DOCUMENT: DocumentApi,
        TagValues.WORKPLACE: WorkplaceApi,
        TagValues.COMPENSATION: CompensationApi,
        TagValues.FOLDER: FolderApi,
        TagValues.CUSTOM_FIELD: CustomFieldApi,
        TagValues.CANDIDATE: CandidateApi,
        TagValues.TABLE: TableApi,
        TagValues.SUPPLEMENT: SupplementApi,
        TagValues.CUSTOM_FIELD_VALUE: CustomFieldValueApi,
        TagValues.KEY: KeyApi,
        TagValues.USER: UserApi,
        TagValues.LOCATION: LocationApi,
        TagValues.BREAK: ModelBreakApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.CONTRACT_VERSION: ContractVersionApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.POLICY: PolicyApi,
        TagValues.HOLIDAY: HolidayApi,
        TagValues.EXPENSE: ExpenseApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.TAXONOMY: TaxonomyApi,
        TagValues.LEGAL_ENTITY: LegalEntityApi,
        TagValues.FAMILY_SITUATION: FamilySituationApi,
        TagValues.EVENT: EventApi,
        TagValues.CUSTOM_TABLE: CustomTableApi,
        TagValues.INTEGRATION_CODE: IntegrationCodeApi,
    }
)
