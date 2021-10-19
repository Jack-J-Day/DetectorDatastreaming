# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class FinishedWriting(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsFinishedWriting(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FinishedWriting()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def FinishedWritingBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x77\x72\x64\x6E", size_prefixed=size_prefixed
        )

    # FinishedWriting
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FinishedWriting
    def ServiceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FinishedWriting
    def JobId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FinishedWriting
    def ErrorEncountered(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
            )
        return False

    # FinishedWriting
    def FileName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FinishedWriting
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FinishedWriting
    def Message(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


def FinishedWritingStart(builder):
    builder.StartObject(6)


def FinishedWritingAddServiceId(builder, serviceId):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(serviceId), 0
    )


def FinishedWritingAddJobId(builder, jobId):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(jobId), 0
    )


def FinishedWritingAddErrorEncountered(builder, errorEncountered):
    builder.PrependBoolSlot(2, errorEncountered, 0)


def FinishedWritingAddFileName(builder, fileName):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(fileName), 0
    )


def FinishedWritingAddMetadata(builder, metadata):
    builder.PrependUOffsetTRelativeSlot(
        4, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0
    )


def FinishedWritingAddMessage(builder, message):
    builder.PrependUOffsetTRelativeSlot(
        5, flatbuffers.number_types.UOffsetTFlags.py_type(message), 0
    )


def FinishedWritingEnd(builder):
    return builder.EndObject()
