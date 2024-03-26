# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from factorial_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EMPLOYEE = "Employee"
    LEAVE = "Leave"
    SHIFT = "Shift"
    TASK = "Task"
    POST = "Post"
    TEAM = "Team"
    WEBHOOK = "Webhook"
    DOCUMENT = "Document"
    WORKPLACE = "Workplace"
    COMPENSATION = "Compensation"
    FOLDER = "Folder"
    CUSTOM_FIELD = "CustomField"
    CANDIDATE = "Candidate"
    TABLE = "Table"
    SUPPLEMENT = "Supplement"
    CUSTOM_FIELD_VALUE = "CustomFieldValue"
    KEY = "Key"
    USER = "User"
    LOCATION = "Location"
    BREAK = "Break"
    ATTENDANCE = "Attendance"
    CONTRACT_VERSION = "ContractVersion"
    INTEGRATION = "Integration"
    CONTRACT = "Contract"
    MESSAGE = "Message"
    POLICY = "Policy"
    HOLIDAY = "Holiday"
    EXPENSE = "Expense"
    APPLICATION = "Application"
    TAXONOMY = "Taxonomy"
    LEGAL_ENTITY = "LegalEntity"
    FAMILY_SITUATION = "FamilySituation"
    EVENT = "Event"
    CUSTOM_TABLE = "CustomTable"
    INTEGRATION_CODE = "IntegrationCode"
