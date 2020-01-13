// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: networking/v1alpha3/sharedconfig.proto

package v1alpha3

import (
	fmt "fmt"
	proto "github.com/gogo/protobuf/proto"
	io "io"
	math "math"
	math_bits "math/bits"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.GoGoProtoPackageIsVersion2 // please upgrade the proto package

type RateLimitDescriptor_RateLimit_Unit int32

const (
	RateLimitDescriptor_RateLimit_UNKNOWN RateLimitDescriptor_RateLimit_Unit = 0
	RateLimitDescriptor_RateLimit_SECOND  RateLimitDescriptor_RateLimit_Unit = 1
	RateLimitDescriptor_RateLimit_MINUTE  RateLimitDescriptor_RateLimit_Unit = 2
	RateLimitDescriptor_RateLimit_HOUR    RateLimitDescriptor_RateLimit_Unit = 3
	RateLimitDescriptor_RateLimit_DAY     RateLimitDescriptor_RateLimit_Unit = 4
)

var RateLimitDescriptor_RateLimit_Unit_name = map[int32]string{
	0: "UNKNOWN",
	1: "SECOND",
	2: "MINUTE",
	3: "HOUR",
	4: "DAY",
}

var RateLimitDescriptor_RateLimit_Unit_value = map[string]int32{
	"UNKNOWN": 0,
	"SECOND":  1,
	"MINUTE":  2,
	"HOUR":    3,
	"DAY":     4,
}

func (x RateLimitDescriptor_RateLimit_Unit) String() string {
	return proto.EnumName(RateLimitDescriptor_RateLimit_Unit_name, int32(x))
}

func (RateLimitDescriptor_RateLimit_Unit) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_1fecce513478fcb2, []int{2, 0, 0}
}

type SharedConfig struct {
	RateLimitConfigs     []*RateLimitConfig `protobuf:"bytes,1,rep,name=rate_limit_configs,json=rateLimitConfigs,proto3" json:"rate_limit_configs,omitempty"`
	XXX_NoUnkeyedLiteral struct{}           `json:"-"`
	XXX_unrecognized     []byte             `json:"-"`
	XXX_sizecache        int32              `json:"-"`
}

func (m *SharedConfig) Reset()         { *m = SharedConfig{} }
func (m *SharedConfig) String() string { return proto.CompactTextString(m) }
func (*SharedConfig) ProtoMessage()    {}
func (*SharedConfig) Descriptor() ([]byte, []int) {
	return fileDescriptor_1fecce513478fcb2, []int{0}
}
func (m *SharedConfig) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *SharedConfig) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_SharedConfig.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *SharedConfig) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SharedConfig.Merge(m, src)
}
func (m *SharedConfig) XXX_Size() int {
	return m.Size()
}
func (m *SharedConfig) XXX_DiscardUnknown() {
	xxx_messageInfo_SharedConfig.DiscardUnknown(m)
}

var xxx_messageInfo_SharedConfig proto.InternalMessageInfo

func (m *SharedConfig) GetRateLimitConfigs() []*RateLimitConfig {
	if m != nil {
		return m.RateLimitConfigs
	}
	return nil
}

type RateLimitConfig struct {
	Domain               string                 `protobuf:"bytes,1,opt,name=domain,proto3" json:"domain,omitempty"`
	Descriptors          []*RateLimitDescriptor `protobuf:"bytes,2,rep,name=descriptors,proto3" json:"descriptors,omitempty"`
	XXX_NoUnkeyedLiteral struct{}               `json:"-"`
	XXX_unrecognized     []byte                 `json:"-"`
	XXX_sizecache        int32                  `json:"-"`
}

func (m *RateLimitConfig) Reset()         { *m = RateLimitConfig{} }
func (m *RateLimitConfig) String() string { return proto.CompactTextString(m) }
func (*RateLimitConfig) ProtoMessage()    {}
func (*RateLimitConfig) Descriptor() ([]byte, []int) {
	return fileDescriptor_1fecce513478fcb2, []int{1}
}
func (m *RateLimitConfig) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *RateLimitConfig) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_RateLimitConfig.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *RateLimitConfig) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RateLimitConfig.Merge(m, src)
}
func (m *RateLimitConfig) XXX_Size() int {
	return m.Size()
}
func (m *RateLimitConfig) XXX_DiscardUnknown() {
	xxx_messageInfo_RateLimitConfig.DiscardUnknown(m)
}

var xxx_messageInfo_RateLimitConfig proto.InternalMessageInfo

func (m *RateLimitConfig) GetDomain() string {
	if m != nil {
		return m.Domain
	}
	return ""
}

func (m *RateLimitConfig) GetDescriptors() []*RateLimitDescriptor {
	if m != nil {
		return m.Descriptors
	}
	return nil
}

type RateLimitDescriptor struct {
	// Descriptor key.
	Key string `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
	// Descriptor value.
	Value string `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
	// Rate Limiter Configuration
	RateLimit *RateLimitDescriptor_RateLimit `protobuf:"bytes,3,opt,name=rate_limit,json=rateLimit,proto3" json:"rate_limit,omitempty"`
	// Optional Rate Limit Descriptor
	Descriptors []*RateLimitDescriptor `protobuf:"bytes,4,rep,name=descriptors,proto3" json:"descriptors,omitempty"`
	// rate limiter api name
	Api                  string   `protobuf:"bytes,5,opt,name=api,proto3" json:"api,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RateLimitDescriptor) Reset()         { *m = RateLimitDescriptor{} }
func (m *RateLimitDescriptor) String() string { return proto.CompactTextString(m) }
func (*RateLimitDescriptor) ProtoMessage()    {}
func (*RateLimitDescriptor) Descriptor() ([]byte, []int) {
	return fileDescriptor_1fecce513478fcb2, []int{2}
}
func (m *RateLimitDescriptor) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *RateLimitDescriptor) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_RateLimitDescriptor.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *RateLimitDescriptor) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RateLimitDescriptor.Merge(m, src)
}
func (m *RateLimitDescriptor) XXX_Size() int {
	return m.Size()
}
func (m *RateLimitDescriptor) XXX_DiscardUnknown() {
	xxx_messageInfo_RateLimitDescriptor.DiscardUnknown(m)
}

var xxx_messageInfo_RateLimitDescriptor proto.InternalMessageInfo

func (m *RateLimitDescriptor) GetKey() string {
	if m != nil {
		return m.Key
	}
	return ""
}

func (m *RateLimitDescriptor) GetValue() string {
	if m != nil {
		return m.Value
	}
	return ""
}

func (m *RateLimitDescriptor) GetRateLimit() *RateLimitDescriptor_RateLimit {
	if m != nil {
		return m.RateLimit
	}
	return nil
}

func (m *RateLimitDescriptor) GetDescriptors() []*RateLimitDescriptor {
	if m != nil {
		return m.Descriptors
	}
	return nil
}

func (m *RateLimitDescriptor) GetApi() string {
	if m != nil {
		return m.Api
	}
	return ""
}

type RateLimitDescriptor_RateLimit struct {
	RequestsPerUnit      uint32                             `protobuf:"varint,1,opt,name=requests_per_unit,json=requestsPerUnit,proto3" json:"requests_per_unit,omitempty"`
	Unit                 RateLimitDescriptor_RateLimit_Unit `protobuf:"varint,2,opt,name=unit,proto3,enum=istio.networking.v1alpha3.RateLimitDescriptor_RateLimit_Unit" json:"unit,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                           `json:"-"`
	XXX_unrecognized     []byte                             `json:"-"`
	XXX_sizecache        int32                              `json:"-"`
}

func (m *RateLimitDescriptor_RateLimit) Reset()         { *m = RateLimitDescriptor_RateLimit{} }
func (m *RateLimitDescriptor_RateLimit) String() string { return proto.CompactTextString(m) }
func (*RateLimitDescriptor_RateLimit) ProtoMessage()    {}
func (*RateLimitDescriptor_RateLimit) Descriptor() ([]byte, []int) {
	return fileDescriptor_1fecce513478fcb2, []int{2, 0}
}
func (m *RateLimitDescriptor_RateLimit) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *RateLimitDescriptor_RateLimit) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_RateLimitDescriptor_RateLimit.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *RateLimitDescriptor_RateLimit) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RateLimitDescriptor_RateLimit.Merge(m, src)
}
func (m *RateLimitDescriptor_RateLimit) XXX_Size() int {
	return m.Size()
}
func (m *RateLimitDescriptor_RateLimit) XXX_DiscardUnknown() {
	xxx_messageInfo_RateLimitDescriptor_RateLimit.DiscardUnknown(m)
}

var xxx_messageInfo_RateLimitDescriptor_RateLimit proto.InternalMessageInfo

func (m *RateLimitDescriptor_RateLimit) GetRequestsPerUnit() uint32 {
	if m != nil {
		return m.RequestsPerUnit
	}
	return 0
}

func (m *RateLimitDescriptor_RateLimit) GetUnit() RateLimitDescriptor_RateLimit_Unit {
	if m != nil {
		return m.Unit
	}
	return RateLimitDescriptor_RateLimit_UNKNOWN
}

func init() {
	proto.RegisterEnum("istio.networking.v1alpha3.RateLimitDescriptor_RateLimit_Unit", RateLimitDescriptor_RateLimit_Unit_name, RateLimitDescriptor_RateLimit_Unit_value)
	proto.RegisterType((*SharedConfig)(nil), "istio.networking.v1alpha3.SharedConfig")
	proto.RegisterType((*RateLimitConfig)(nil), "istio.networking.v1alpha3.RateLimitConfig")
	proto.RegisterType((*RateLimitDescriptor)(nil), "istio.networking.v1alpha3.RateLimitDescriptor")
	proto.RegisterType((*RateLimitDescriptor_RateLimit)(nil), "istio.networking.v1alpha3.RateLimitDescriptor.RateLimit")
}

func init() {
	proto.RegisterFile("networking/v1alpha3/sharedconfig.proto", fileDescriptor_1fecce513478fcb2)
}

var fileDescriptor_1fecce513478fcb2 = []byte{
	// 408 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x53, 0x4d, 0x8f, 0xd3, 0x30,
	0x10, 0xc5, 0x4d, 0xb6, 0x4b, 0x27, 0xc0, 0x06, 0x83, 0x50, 0xe0, 0x50, 0x45, 0x39, 0xa0, 0x6a,
	0x0f, 0x8e, 0xe8, 0x5e, 0xb8, 0x80, 0x04, 0xdb, 0x95, 0x40, 0x40, 0xba, 0xb8, 0x44, 0x05, 0x2e,
	0x91, 0x69, 0x4d, 0x6b, 0xb5, 0x8d, 0x83, 0xed, 0x16, 0x21, 0x7e, 0x20, 0x88, 0x13, 0x3f, 0x01,
	0xf5, 0x97, 0xa0, 0x38, 0xfd, 0x80, 0xaa, 0x48, 0xc0, 0xde, 0xec, 0x99, 0xf7, 0xde, 0xcc, 0x7b,
	0xd2, 0xc0, 0xdd, 0x9c, 0x9b, 0x8f, 0x52, 0x4d, 0x44, 0x3e, 0x8a, 0x17, 0xf7, 0xd8, 0xb4, 0x18,
	0xb3, 0x93, 0x58, 0x8f, 0x99, 0xe2, 0xc3, 0x81, 0xcc, 0xdf, 0x8b, 0x11, 0x29, 0x94, 0x34, 0x12,
	0xdf, 0x16, 0xda, 0x08, 0x49, 0xb6, 0x68, 0xb2, 0x46, 0x47, 0x63, 0xb8, 0xd2, 0xb3, 0x84, 0x53,
	0x4b, 0xc0, 0xaf, 0x01, 0x2b, 0x66, 0x78, 0x36, 0x15, 0x33, 0x61, 0xb2, 0x4a, 0x45, 0x07, 0x28,
	0x74, 0x5a, 0x5e, 0xfb, 0x98, 0xfc, 0x51, 0x87, 0x50, 0x66, 0xf8, 0xf3, 0x92, 0x53, 0xe9, 0x50,
	0x5f, 0xfd, 0x5e, 0xd0, 0xd1, 0x67, 0x38, 0xda, 0x01, 0xe1, 0x5b, 0x50, 0x1f, 0xca, 0x19, 0x13,
	0x79, 0x80, 0x42, 0xd4, 0x6a, 0xd0, 0xd5, 0x0f, 0x9f, 0x83, 0x37, 0xe4, 0x7a, 0xa0, 0x44, 0x61,
	0xa4, 0xd2, 0x41, 0xcd, 0x4e, 0x27, 0x7f, 0x33, 0xbd, 0xb3, 0xa1, 0xd1, 0x5f, 0x25, 0xa2, 0x2f,
	0x0e, 0xdc, 0xd8, 0x03, 0xc2, 0x3e, 0x38, 0x13, 0xfe, 0x69, 0x35, 0xbe, 0x7c, 0xe2, 0x9b, 0x70,
	0xb0, 0x60, 0xd3, 0x39, 0x0f, 0x6a, 0xb6, 0x56, 0x7d, 0x70, 0x1f, 0x60, 0x1b, 0x4b, 0xe0, 0x84,
	0xa8, 0xe5, 0xb5, 0xef, 0xff, 0xdb, 0x42, 0xdb, 0x1a, 0x6d, 0x6c, 0xc2, 0xd9, 0xb5, 0xea, 0x5e,
	0xd8, 0x6a, 0x69, 0x89, 0x15, 0x22, 0x38, 0xa8, 0x2c, 0xb1, 0x42, 0xdc, 0xf9, 0x86, 0xa0, 0xb1,
	0xa1, 0xe1, 0x63, 0xb8, 0xae, 0xf8, 0x87, 0x39, 0xd7, 0x46, 0x67, 0x05, 0x57, 0xd9, 0x3c, 0x17,
	0xc6, 0x06, 0x70, 0x95, 0x1e, 0xad, 0x1b, 0xe7, 0x5c, 0xa5, 0xb9, 0x30, 0xf8, 0x25, 0xb8, 0xb6,
	0x5d, 0x66, 0x71, 0xad, 0xfd, 0xe0, 0x7f, 0x0d, 0x93, 0x52, 0x8c, 0x5a, 0xa9, 0xe8, 0x21, 0xb8,
	0x56, 0xda, 0x83, 0xc3, 0x34, 0x79, 0x96, 0x74, 0xfb, 0x89, 0x7f, 0x09, 0x03, 0xd4, 0x7b, 0x67,
	0xa7, 0xdd, 0xa4, 0xe3, 0xa3, 0xf2, 0xfd, 0xe2, 0x69, 0x92, 0xbe, 0x3a, 0xf3, 0x6b, 0xf8, 0x32,
	0xb8, 0x4f, 0xba, 0x29, 0xf5, 0x1d, 0x7c, 0x08, 0x4e, 0xe7, 0xd1, 0x1b, 0xdf, 0x7d, 0x4c, 0xbe,
	0x2e, 0x9b, 0xe8, 0xfb, 0xb2, 0x89, 0x7e, 0x2c, 0x9b, 0xe8, 0x6d, 0x58, 0x6d, 0x24, 0x64, 0xcc,
	0x0a, 0x11, 0xef, 0x39, 0x87, 0x77, 0x75, 0x7b, 0x02, 0x27, 0x3f, 0x03, 0x00, 0x00, 0xff, 0xff,
	0xac, 0xaf, 0xaf, 0x8f, 0x2c, 0x03, 0x00, 0x00,
}

func (m *SharedConfig) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *SharedConfig) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *SharedConfig) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if len(m.RateLimitConfigs) > 0 {
		for iNdEx := len(m.RateLimitConfigs) - 1; iNdEx >= 0; iNdEx-- {
			{
				size, err := m.RateLimitConfigs[iNdEx].MarshalToSizedBuffer(dAtA[:i])
				if err != nil {
					return 0, err
				}
				i -= size
				i = encodeVarintSharedconfig(dAtA, i, uint64(size))
			}
			i--
			dAtA[i] = 0xa
		}
	}
	return len(dAtA) - i, nil
}

func (m *RateLimitConfig) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *RateLimitConfig) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *RateLimitConfig) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if len(m.Descriptors) > 0 {
		for iNdEx := len(m.Descriptors) - 1; iNdEx >= 0; iNdEx-- {
			{
				size, err := m.Descriptors[iNdEx].MarshalToSizedBuffer(dAtA[:i])
				if err != nil {
					return 0, err
				}
				i -= size
				i = encodeVarintSharedconfig(dAtA, i, uint64(size))
			}
			i--
			dAtA[i] = 0x12
		}
	}
	if len(m.Domain) > 0 {
		i -= len(m.Domain)
		copy(dAtA[i:], m.Domain)
		i = encodeVarintSharedconfig(dAtA, i, uint64(len(m.Domain)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func (m *RateLimitDescriptor) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *RateLimitDescriptor) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *RateLimitDescriptor) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if len(m.Api) > 0 {
		i -= len(m.Api)
		copy(dAtA[i:], m.Api)
		i = encodeVarintSharedconfig(dAtA, i, uint64(len(m.Api)))
		i--
		dAtA[i] = 0x2a
	}
	if len(m.Descriptors) > 0 {
		for iNdEx := len(m.Descriptors) - 1; iNdEx >= 0; iNdEx-- {
			{
				size, err := m.Descriptors[iNdEx].MarshalToSizedBuffer(dAtA[:i])
				if err != nil {
					return 0, err
				}
				i -= size
				i = encodeVarintSharedconfig(dAtA, i, uint64(size))
			}
			i--
			dAtA[i] = 0x22
		}
	}
	if m.RateLimit != nil {
		{
			size, err := m.RateLimit.MarshalToSizedBuffer(dAtA[:i])
			if err != nil {
				return 0, err
			}
			i -= size
			i = encodeVarintSharedconfig(dAtA, i, uint64(size))
		}
		i--
		dAtA[i] = 0x1a
	}
	if len(m.Value) > 0 {
		i -= len(m.Value)
		copy(dAtA[i:], m.Value)
		i = encodeVarintSharedconfig(dAtA, i, uint64(len(m.Value)))
		i--
		dAtA[i] = 0x12
	}
	if len(m.Key) > 0 {
		i -= len(m.Key)
		copy(dAtA[i:], m.Key)
		i = encodeVarintSharedconfig(dAtA, i, uint64(len(m.Key)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func (m *RateLimitDescriptor_RateLimit) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *RateLimitDescriptor_RateLimit) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *RateLimitDescriptor_RateLimit) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if m.Unit != 0 {
		i = encodeVarintSharedconfig(dAtA, i, uint64(m.Unit))
		i--
		dAtA[i] = 0x10
	}
	if m.RequestsPerUnit != 0 {
		i = encodeVarintSharedconfig(dAtA, i, uint64(m.RequestsPerUnit))
		i--
		dAtA[i] = 0x8
	}
	return len(dAtA) - i, nil
}

func encodeVarintSharedconfig(dAtA []byte, offset int, v uint64) int {
	offset -= sovSharedconfig(v)
	base := offset
	for v >= 1<<7 {
		dAtA[offset] = uint8(v&0x7f | 0x80)
		v >>= 7
		offset++
	}
	dAtA[offset] = uint8(v)
	return base
}
func (m *SharedConfig) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	if len(m.RateLimitConfigs) > 0 {
		for _, e := range m.RateLimitConfigs {
			l = e.Size()
			n += 1 + l + sovSharedconfig(uint64(l))
		}
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *RateLimitConfig) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.Domain)
	if l > 0 {
		n += 1 + l + sovSharedconfig(uint64(l))
	}
	if len(m.Descriptors) > 0 {
		for _, e := range m.Descriptors {
			l = e.Size()
			n += 1 + l + sovSharedconfig(uint64(l))
		}
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *RateLimitDescriptor) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.Key)
	if l > 0 {
		n += 1 + l + sovSharedconfig(uint64(l))
	}
	l = len(m.Value)
	if l > 0 {
		n += 1 + l + sovSharedconfig(uint64(l))
	}
	if m.RateLimit != nil {
		l = m.RateLimit.Size()
		n += 1 + l + sovSharedconfig(uint64(l))
	}
	if len(m.Descriptors) > 0 {
		for _, e := range m.Descriptors {
			l = e.Size()
			n += 1 + l + sovSharedconfig(uint64(l))
		}
	}
	l = len(m.Api)
	if l > 0 {
		n += 1 + l + sovSharedconfig(uint64(l))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *RateLimitDescriptor_RateLimit) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	if m.RequestsPerUnit != 0 {
		n += 1 + sovSharedconfig(uint64(m.RequestsPerUnit))
	}
	if m.Unit != 0 {
		n += 1 + sovSharedconfig(uint64(m.Unit))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func sovSharedconfig(x uint64) (n int) {
	return (math_bits.Len64(x|1) + 6) / 7
}
func sozSharedconfig(x uint64) (n int) {
	return sovSharedconfig(uint64((x << 1) ^ uint64((int64(x) >> 63))))
}
func (m *SharedConfig) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowSharedconfig
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: SharedConfig: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: SharedConfig: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field RateLimitConfigs", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.RateLimitConfigs = append(m.RateLimitConfigs, &RateLimitConfig{})
			if err := m.RateLimitConfigs[len(m.RateLimitConfigs)-1].Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipSharedconfig(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *RateLimitConfig) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowSharedconfig
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: RateLimitConfig: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: RateLimitConfig: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Domain", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Domain = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		case 2:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Descriptors", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Descriptors = append(m.Descriptors, &RateLimitDescriptor{})
			if err := m.Descriptors[len(m.Descriptors)-1].Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipSharedconfig(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *RateLimitDescriptor) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowSharedconfig
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: RateLimitDescriptor: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: RateLimitDescriptor: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Key", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Key = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		case 2:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Value", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Value = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		case 3:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field RateLimit", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if m.RateLimit == nil {
				m.RateLimit = &RateLimitDescriptor_RateLimit{}
			}
			if err := m.RateLimit.Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		case 4:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Descriptors", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Descriptors = append(m.Descriptors, &RateLimitDescriptor{})
			if err := m.Descriptors[len(m.Descriptors)-1].Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		case 5:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Api", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthSharedconfig
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Api = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipSharedconfig(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *RateLimitDescriptor_RateLimit) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowSharedconfig
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: RateLimit: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: RateLimit: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 0 {
				return fmt.Errorf("proto: wrong wireType = %d for field RequestsPerUnit", wireType)
			}
			m.RequestsPerUnit = 0
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				m.RequestsPerUnit |= uint32(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
		case 2:
			if wireType != 0 {
				return fmt.Errorf("proto: wrong wireType = %d for field Unit", wireType)
			}
			m.Unit = 0
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				m.Unit |= RateLimitDescriptor_RateLimit_Unit(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
		default:
			iNdEx = preIndex
			skippy, err := skipSharedconfig(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthSharedconfig
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func skipSharedconfig(dAtA []byte) (n int, err error) {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return 0, ErrIntOverflowSharedconfig
			}
			if iNdEx >= l {
				return 0, io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= (uint64(b) & 0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		wireType := int(wire & 0x7)
		switch wireType {
		case 0:
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				iNdEx++
				if dAtA[iNdEx-1] < 0x80 {
					break
				}
			}
			return iNdEx, nil
		case 1:
			iNdEx += 8
			return iNdEx, nil
		case 2:
			var length int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowSharedconfig
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				length |= (int(b) & 0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if length < 0 {
				return 0, ErrInvalidLengthSharedconfig
			}
			iNdEx += length
			if iNdEx < 0 {
				return 0, ErrInvalidLengthSharedconfig
			}
			return iNdEx, nil
		case 3:
			for {
				var innerWire uint64
				var start int = iNdEx
				for shift := uint(0); ; shift += 7 {
					if shift >= 64 {
						return 0, ErrIntOverflowSharedconfig
					}
					if iNdEx >= l {
						return 0, io.ErrUnexpectedEOF
					}
					b := dAtA[iNdEx]
					iNdEx++
					innerWire |= (uint64(b) & 0x7F) << shift
					if b < 0x80 {
						break
					}
				}
				innerWireType := int(innerWire & 0x7)
				if innerWireType == 4 {
					break
				}
				next, err := skipSharedconfig(dAtA[start:])
				if err != nil {
					return 0, err
				}
				iNdEx = start + next
				if iNdEx < 0 {
					return 0, ErrInvalidLengthSharedconfig
				}
			}
			return iNdEx, nil
		case 4:
			return iNdEx, nil
		case 5:
			iNdEx += 4
			return iNdEx, nil
		default:
			return 0, fmt.Errorf("proto: illegal wireType %d", wireType)
		}
	}
	panic("unreachable")
}

var (
	ErrInvalidLengthSharedconfig = fmt.Errorf("proto: negative length found during unmarshaling")
	ErrIntOverflowSharedconfig   = fmt.Errorf("proto: integer overflow")
)