// source: gRPC_model.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.Request', null, global);
goog.exportSymbol('proto.Response', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.Request = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.Request, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.Request.displayName = 'proto.Request';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.Response = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.Response.repeatedFields_, null);
};
goog.inherits(proto.Response, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.Response.displayName = 'proto.Response';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.Request.prototype.toObject = function(opt_includeInstance) {
  return proto.Request.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Request} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Request.toObject = function(includeInstance, msg) {
  var f, obj = {
    academicCode: jspb.Message.getFieldWithDefault(msg, 1, 0),
    courseCode: jspb.Message.getFieldWithDefault(msg, 2, ""),
    academicYear: jspb.Message.getFieldWithDefault(msg, 3, 0),
    academicSemester: jspb.Message.getFieldWithDefault(msg, 4, 0),
    absences: jspb.Message.getFieldWithDefault(msg, 5, 0),
    grade: jspb.Message.getFloatingPointFieldWithDefault(msg, 6, 0.0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.Request}
 */
proto.Request.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Request;
  return proto.Request.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Request} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Request}
 */
proto.Request.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setAcademicCode(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setCourseCode(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setAcademicYear(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setAcademicSemester(value);
      break;
    case 5:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setAbsences(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setGrade(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.Request.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Request.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Request} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Request.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAcademicCode();
  if (f !== 0) {
    writer.writeUint32(
      1,
      f
    );
  }
  f = message.getCourseCode();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getAcademicYear();
  if (f !== 0) {
    writer.writeUint32(
      3,
      f
    );
  }
  f = message.getAcademicSemester();
  if (f !== 0) {
    writer.writeUint32(
      4,
      f
    );
  }
  f = message.getAbsences();
  if (f !== 0) {
    writer.writeUint32(
      5,
      f
    );
  }
  f = message.getGrade();
  if (f !== 0.0) {
    writer.writeFloat(
      6,
      f
    );
  }
};


/**
 * optional uint32 academic_code = 1;
 * @return {number}
 */
proto.Request.prototype.getAcademicCode = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {number} value
 * @return {!proto.Request} returns this
 */
proto.Request.prototype.setAcademicCode = function(value) {
  return jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional string course_code = 2;
 * @return {string}
 */
proto.Request.prototype.getCourseCode = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.Request} returns this
 */
proto.Request.prototype.setCourseCode = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional uint32 academic_year = 3;
 * @return {number}
 */
proto.Request.prototype.getAcademicYear = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/**
 * @param {number} value
 * @return {!proto.Request} returns this
 */
proto.Request.prototype.setAcademicYear = function(value) {
  return jspb.Message.setProto3IntField(this, 3, value);
};


/**
 * optional uint32 academic_semester = 4;
 * @return {number}
 */
proto.Request.prototype.getAcademicSemester = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 4, 0));
};


/**
 * @param {number} value
 * @return {!proto.Request} returns this
 */
proto.Request.prototype.setAcademicSemester = function(value) {
  return jspb.Message.setProto3IntField(this, 4, value);
};


/**
 * optional uint32 absences = 5;
 * @return {number}
 */
proto.Request.prototype.getAbsences = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 5, 0));
};


/**
 * @param {number} value
 * @return {!proto.Request} returns this
 */
proto.Request.prototype.setAbsences = function(value) {
  return jspb.Message.setProto3IntField(this, 5, value);
};


/**
 * optional float grade = 6;
 * @return {number}
 */
proto.Request.prototype.getGrade = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 6, 0.0));
};


/**
 * @param {number} value
 * @return {!proto.Request} returns this
 */
proto.Request.prototype.setGrade = function(value) {
  return jspb.Message.setProto3FloatField(this, 6, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.Response.repeatedFields_ = [4,5,6,7];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.Response.prototype.toObject = function(opt_includeInstance) {
  return proto.Response.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Response} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Response.toObject = function(includeInstance, msg) {
  var f, obj = {
    status: jspb.Message.getFieldWithDefault(msg, 1, 0),
    errorCode: jspb.Message.getFieldWithDefault(msg, 2, 0),
    errorMessage: jspb.Message.getFieldWithDefault(msg, 3, ""),
    academicCodeList: (f = jspb.Message.getRepeatedField(msg, 4)) == null ? undefined : f,
    academicNameList: (f = jspb.Message.getRepeatedField(msg, 5)) == null ? undefined : f,
    absencesList: (f = jspb.Message.getRepeatedField(msg, 6)) == null ? undefined : f,
    gradeList: (f = jspb.Message.getRepeatedFloatingPointField(msg, 7)) == null ? undefined : f
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.Response}
 */
proto.Response.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Response;
  return proto.Response.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Response} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Response}
 */
proto.Response.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setStatus(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setErrorCode(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setErrorMessage(value);
      break;
    case 4:
      var value = /** @type {!Array<number>} */ (reader.readPackedUint32());
      msg.setAcademicCodeList(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.addAcademicName(value);
      break;
    case 6:
      var value = /** @type {!Array<number>} */ (reader.readPackedUint32());
      msg.setAbsencesList(value);
      break;
    case 7:
      var value = /** @type {!Array<number>} */ (reader.readPackedFloat());
      msg.setGradeList(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.Response.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Response.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Response} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Response.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getStatus();
  if (f !== 0) {
    writer.writeUint32(
      1,
      f
    );
  }
  f = message.getErrorCode();
  if (f !== 0) {
    writer.writeUint32(
      2,
      f
    );
  }
  f = message.getErrorMessage();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getAcademicCodeList();
  if (f.length > 0) {
    writer.writePackedUint32(
      4,
      f
    );
  }
  f = message.getAcademicNameList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      5,
      f
    );
  }
  f = message.getAbsencesList();
  if (f.length > 0) {
    writer.writePackedUint32(
      6,
      f
    );
  }
  f = message.getGradeList();
  if (f.length > 0) {
    writer.writePackedFloat(
      7,
      f
    );
  }
};


/**
 * optional uint32 status = 1;
 * @return {number}
 */
proto.Response.prototype.getStatus = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {number} value
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.setStatus = function(value) {
  return jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional uint32 error_code = 2;
 * @return {number}
 */
proto.Response.prototype.getErrorCode = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {number} value
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.setErrorCode = function(value) {
  return jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional string error_message = 3;
 * @return {string}
 */
proto.Response.prototype.getErrorMessage = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.setErrorMessage = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * repeated uint32 academic_code = 4;
 * @return {!Array<number>}
 */
proto.Response.prototype.getAcademicCodeList = function() {
  return /** @type {!Array<number>} */ (jspb.Message.getRepeatedField(this, 4));
};


/**
 * @param {!Array<number>} value
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.setAcademicCodeList = function(value) {
  return jspb.Message.setField(this, 4, value || []);
};


/**
 * @param {number} value
 * @param {number=} opt_index
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.addAcademicCode = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 4, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.clearAcademicCodeList = function() {
  return this.setAcademicCodeList([]);
};


/**
 * repeated string academic_name = 5;
 * @return {!Array<string>}
 */
proto.Response.prototype.getAcademicNameList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 5));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.setAcademicNameList = function(value) {
  return jspb.Message.setField(this, 5, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.addAcademicName = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 5, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.clearAcademicNameList = function() {
  return this.setAcademicNameList([]);
};


/**
 * repeated uint32 absences = 6;
 * @return {!Array<number>}
 */
proto.Response.prototype.getAbsencesList = function() {
  return /** @type {!Array<number>} */ (jspb.Message.getRepeatedField(this, 6));
};


/**
 * @param {!Array<number>} value
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.setAbsencesList = function(value) {
  return jspb.Message.setField(this, 6, value || []);
};


/**
 * @param {number} value
 * @param {number=} opt_index
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.addAbsences = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 6, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.clearAbsencesList = function() {
  return this.setAbsencesList([]);
};


/**
 * repeated float grade = 7;
 * @return {!Array<number>}
 */
proto.Response.prototype.getGradeList = function() {
  return /** @type {!Array<number>} */ (jspb.Message.getRepeatedFloatingPointField(this, 7));
};


/**
 * @param {!Array<number>} value
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.setGradeList = function(value) {
  return jspb.Message.setField(this, 7, value || []);
};


/**
 * @param {number} value
 * @param {number=} opt_index
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.addGrade = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 7, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.Response} returns this
 */
proto.Response.prototype.clearGradeList = function() {
  return this.setGradeList([]);
};


goog.object.extend(exports, proto);
