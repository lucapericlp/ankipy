"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
"""
import anki.links_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class BackendInit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREFERRED_LANGS_FIELD_NUMBER: builtins.int
    LOCALE_FOLDER_PATH_FIELD_NUMBER: builtins.int
    SERVER_FIELD_NUMBER: builtins.int
    @property
    def preferred_langs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    locale_folder_path: builtins.str
    server: builtins.bool
    def __init__(
        self,
        *,
        preferred_langs: collections.abc.Iterable[builtins.str] | None = ...,
        locale_folder_path: builtins.str = ...,
        server: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locale_folder_path", b"locale_folder_path", "preferred_langs", b"preferred_langs", "server", b"server"]) -> None: ...

global___BackendInit = BackendInit

@typing_extensions.final
class I18nBackendInit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREFERRED_LANGS_FIELD_NUMBER: builtins.int
    LOCALE_FOLDER_PATH_FIELD_NUMBER: builtins.int
    @property
    def preferred_langs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    locale_folder_path: builtins.str
    def __init__(
        self,
        *,
        preferred_langs: collections.abc.Iterable[builtins.str] | None = ...,
        locale_folder_path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locale_folder_path", b"locale_folder_path", "preferred_langs", b"preferred_langs"]) -> None: ...

global___I18nBackendInit = I18nBackendInit

@typing_extensions.final
class BackendError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Kind:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _KindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[BackendError._Kind.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        INVALID_INPUT: BackendError._Kind.ValueType  # 0
        UNDO_EMPTY: BackendError._Kind.ValueType  # 1
        INTERRUPTED: BackendError._Kind.ValueType  # 2
        TEMPLATE_PARSE: BackendError._Kind.ValueType  # 3
        IO_ERROR: BackendError._Kind.ValueType  # 4
        DB_ERROR: BackendError._Kind.ValueType  # 5
        NETWORK_ERROR: BackendError._Kind.ValueType  # 6
        SYNC_AUTH_ERROR: BackendError._Kind.ValueType  # 7
        SYNC_OTHER_ERROR: BackendError._Kind.ValueType  # 8
        JSON_ERROR: BackendError._Kind.ValueType  # 9
        PROTO_ERROR: BackendError._Kind.ValueType  # 10
        NOT_FOUND_ERROR: BackendError._Kind.ValueType  # 11
        EXISTS: BackendError._Kind.ValueType  # 12
        FILTERED_DECK_ERROR: BackendError._Kind.ValueType  # 13
        SEARCH_ERROR: BackendError._Kind.ValueType  # 14
        CUSTOM_STUDY_ERROR: BackendError._Kind.ValueType  # 15
        IMPORT_ERROR: BackendError._Kind.ValueType  # 16
        DELETED: BackendError._Kind.ValueType  # 17
        CARD_TYPE_ERROR: BackendError._Kind.ValueType  # 18
        ANKIDROID_PANIC_ERROR: BackendError._Kind.ValueType  # 19
        OS_ERROR: BackendError._Kind.ValueType  # 20
        """Originated from and usually specific to the OS."""
        SCHEDULER_UPGRADE_REQUIRED: BackendError._Kind.ValueType  # 21

    class Kind(_Kind, metaclass=_KindEnumTypeWrapper): ...
    INVALID_INPUT: BackendError.Kind.ValueType  # 0
    UNDO_EMPTY: BackendError.Kind.ValueType  # 1
    INTERRUPTED: BackendError.Kind.ValueType  # 2
    TEMPLATE_PARSE: BackendError.Kind.ValueType  # 3
    IO_ERROR: BackendError.Kind.ValueType  # 4
    DB_ERROR: BackendError.Kind.ValueType  # 5
    NETWORK_ERROR: BackendError.Kind.ValueType  # 6
    SYNC_AUTH_ERROR: BackendError.Kind.ValueType  # 7
    SYNC_OTHER_ERROR: BackendError.Kind.ValueType  # 8
    JSON_ERROR: BackendError.Kind.ValueType  # 9
    PROTO_ERROR: BackendError.Kind.ValueType  # 10
    NOT_FOUND_ERROR: BackendError.Kind.ValueType  # 11
    EXISTS: BackendError.Kind.ValueType  # 12
    FILTERED_DECK_ERROR: BackendError.Kind.ValueType  # 13
    SEARCH_ERROR: BackendError.Kind.ValueType  # 14
    CUSTOM_STUDY_ERROR: BackendError.Kind.ValueType  # 15
    IMPORT_ERROR: BackendError.Kind.ValueType  # 16
    DELETED: BackendError.Kind.ValueType  # 17
    CARD_TYPE_ERROR: BackendError.Kind.ValueType  # 18
    ANKIDROID_PANIC_ERROR: BackendError.Kind.ValueType  # 19
    OS_ERROR: BackendError.Kind.ValueType  # 20
    """Originated from and usually specific to the OS."""
    SCHEDULER_UPGRADE_REQUIRED: BackendError.Kind.ValueType  # 21

    MESSAGE_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    HELP_PAGE_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    BACKTRACE_FIELD_NUMBER: builtins.int
    message: builtins.str
    """error description, usually localized, suitable for displaying to the user"""
    kind: global___BackendError.Kind.ValueType
    """the error subtype"""
    help_page: anki.links_pb2.HelpPageLinkRequest.HelpPage.ValueType
    """optional page in the manual"""
    context: builtins.str
    """additional information about the context in which the error occurred"""
    backtrace: builtins.str
    """a backtrace of the underlying error; requires RUST_BACKTRACE to be set"""
    def __init__(
        self,
        *,
        message: builtins.str = ...,
        kind: global___BackendError.Kind.ValueType = ...,
        help_page: anki.links_pb2.HelpPageLinkRequest.HelpPage.ValueType | None = ...,
        context: builtins.str = ...,
        backtrace: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_help_page", b"_help_page", "help_page", b"help_page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_help_page", b"_help_page", "backtrace", b"backtrace", "context", b"context", "help_page", b"help_page", "kind", b"kind", "message", b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_help_page", b"_help_page"]) -> typing_extensions.Literal["help_page"] | None: ...

global___BackendError = BackendError
