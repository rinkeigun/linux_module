;/***********************************************************
;	file : boot.asm
;	2016.06.13 Huiqun.Lin
;	Description : Bootloader
;************************************************************/

[BITS 16]

ORG 0x7C00

;/************************************************************
;
;	BOOT
;
;************************************************************/

JMP BOOT		;BS_jmpBoot
BS_jmpBoot2		DB	0x90
BS_OEMName		DB	"MyOS   "
BPB_BytsPerSec	DW	0x0200		;BytesPerSector
BPB_SecPerClus	DB	0x01		;SectorPerCluster
BPB_RsvdSecCnt	DW	0x0001		;reservedSectors
BPB_NumFATs		DB	0x02		;totalFATs
BPB_RootEntCnt	DW	0x00E0		;MaxRootEntries
BPB_TotSec16	DW	0x0B40		;TotalSectors
BPB_Media		DB	0xF0		;MediaDescriptor
BPB_FATSz16		DW	0x0009		;SectorsPerFAT
BPB_SecPerTrk	DW	0x0012		;SectorsPerTrack
BPB_NumHeads	DW	0x0002		;NumHeads
BPB_HiddSec		DD	0x00000000	;HiddenSector
BPB_TotSec32	DD	0x00000000	;TotalSectors

BPB_DrvNum		DB	0x00		;DriveNum
BS_Reserved1	DB	0x00		;Reserved
BS_BootSig		DB	0x29		;BootSignature
BS_VoIID		DD	0x20160613	;VolumeSerialNumber
BS_VolLab		DB	"MyOS  "	;VolumeLabel
BS_FilSsType	DB	"FAT12  "	;FileSystemType

BOOT:
	CLI
	HLT

TIMES 510 - ( $ - $$ ) DB 0
DW 0xAA55
