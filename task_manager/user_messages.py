from django.utils.translation import gettext as _


SUCCES_MESSAGE_CREATE_USER = _('User was created successfully')
SUCCES_MESSAGE_UPDATE_USER = _('User was updated successfully')
SUCCES_MESSAGE_DELETE_USER = _('User has been successfully deleted')

SUCCES_MESSAGE_CREATE_TASK = _('Task was created successfully')
SUCCES_MESSAGE_UPDATE_TASK = _('Task was updated successfully')
SUCCES_MESSAGE_DELETE_TASK = _('Task has been successfully deleted')

SUCCES_MESSAGE_CREATE_STATUS = _('Status was created successfully')
SUCCES_MESSAGE_UPDATE_STATUS = _('Status was updated successfully')
SUCCES_MESSAGE_DELETE_STATUS = _('Status has been successfully deleted')

SUCCES_MESSAGE_CREATE_LABEL = _('Label was created successfully')
SUCCES_MESSAGE_UPDATE_LABEL = _('Label was updated successfully')
SUCCES_MESSAGE_DELETE_LABEL = _('Label has been successfully deleted')


ERROR_MESSAGE_NOT_CORRECT_PASSWORD = _(
    'Please enter a correct username and password. Note that both'
)
ERROR_MESSAGE_NOT_LOGGED = _(
    'You are not logged in! Please log in'
)
ERROR_MESSAGE_NOT_RIGHTS = _(
    "You don't have the rights to change another user"
)
ERROR_MESSAGE_DELETED_TASK = _(
    'A task can only be deleted by its author'
)
ERROR_MESSAGE_NOT_POSSIBLE_DELETE_USER = _(
    'It is not possible to delete a user because it is being used'
)
ERROR_MESSAGE_NOT_POSSIBLE_DELETE_TASK = _(
    'It is not possible to delete a task because it is being used'
)
ERROR_MESSAGE_NOT_POSSIBLE_DELETE_STATUS = _(
    'It is not possible to delete a status because it is being used'
)
ERROR_MESSAGE_NOT_POSSIBLE_DELETE_LABEL = _(
    'It is not possible to delete a label because it is being used'
)
