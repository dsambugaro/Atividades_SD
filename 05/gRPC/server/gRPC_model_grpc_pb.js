// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var gRPC_model_pb = require('./gRPC_model_pb.js');

function serialize_Request(arg) {
  if (!(arg instanceof gRPC_model_pb.Request)) {
    throw new Error('Expected argument of type Request');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_Request(buffer_arg) {
  return gRPC_model_pb.Request.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_Response(arg) {
  if (!(arg instanceof gRPC_model_pb.Response)) {
    throw new Error('Expected argument of type Response');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_Response(buffer_arg) {
  return gRPC_model_pb.Response.deserializeBinary(new Uint8Array(buffer_arg));
}


var GradeService = exports.GradeService = {
  create: {
    path: '/Grade/create',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
  read: {
    path: '/Grade/read',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
  update: {
    path: '/Grade/update',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
  delete: {
    path: '/Grade/delete',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
};

exports.GradeClient = grpc.makeGenericClientConstructor(GradeService);
var AbsencesService = exports.AbsencesService = {
  create: {
    path: '/Absences/create',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
  read: {
    path: '/Absences/read',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
  update: {
    path: '/Absences/update',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
  delete: {
    path: '/Absences/delete',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
};

exports.AbsencesClient = grpc.makeGenericClientConstructor(AbsencesService);
var CourseService = exports.CourseService = {
  gradesAndAbsences: {
    path: '/Course/gradesAndAbsences',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
  students: {
    path: '/Course/students',
    requestStream: false,
    responseStream: false,
    requestType: gRPC_model_pb.Request,
    responseType: gRPC_model_pb.Response,
    requestSerialize: serialize_Request,
    requestDeserialize: deserialize_Request,
    responseSerialize: serialize_Response,
    responseDeserialize: deserialize_Response,
  },
};

exports.CourseClient = grpc.makeGenericClientConstructor(CourseService);
