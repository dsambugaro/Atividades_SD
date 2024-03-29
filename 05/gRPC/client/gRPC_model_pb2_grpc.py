# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gRPC_model_pb2 as gRPC__model__pb2


class GradeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/Grade/create',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )
        self.read = channel.unary_unary(
                '/Grade/read',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )
        self.update = channel.unary_unary(
                '/Grade/update',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )
        self.delete = channel.unary_unary(
                '/Grade/delete',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )


class GradeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GradeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
            'read': grpc.unary_unary_rpc_method_handler(
                    servicer.read,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Grade', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Grade(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Grade/create',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Grade/read',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Grade/update',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Grade/delete',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AbsencesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/Absences/create',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )
        self.read = channel.unary_unary(
                '/Absences/read',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )
        self.update = channel.unary_unary(
                '/Absences/update',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )
        self.delete = channel.unary_unary(
                '/Absences/delete',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )


class AbsencesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AbsencesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
            'read': grpc.unary_unary_rpc_method_handler(
                    servicer.read,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Absences', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Absences(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Absences/create',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Absences/read',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Absences/update',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Absences/delete',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CourseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.gradesAndAbsences = channel.unary_unary(
                '/Course/gradesAndAbsences',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )
        self.students = channel.unary_unary(
                '/Course/students',
                request_serializer=gRPC__model__pb2.Request.SerializeToString,
                response_deserializer=gRPC__model__pb2.Response.FromString,
                )


class CourseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def gradesAndAbsences(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def students(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CourseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'gradesAndAbsences': grpc.unary_unary_rpc_method_handler(
                    servicer.gradesAndAbsences,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
            'students': grpc.unary_unary_rpc_method_handler(
                    servicer.students,
                    request_deserializer=gRPC__model__pb2.Request.FromString,
                    response_serializer=gRPC__model__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Course', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Course(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def gradesAndAbsences(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Course/gradesAndAbsences',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def students(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Course/students',
            gRPC__model__pb2.Request.SerializeToString,
            gRPC__model__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
