
#ifndef EXPORT_H
#define EXPORT_H

#include "pack.h"
#include "unpack.h"
#include "field.h"


DLLEXPORT int WINAPI Test();

DLLEXPORT void WINAPI InitHandlers();
DLLEXPORT void WINAPI EmptyBuffer();

DLLEXPORT T_S32 WINAPI GetCommandTest(T_U16 usCommandID, PVOID pStruct);

DLLEXPORT T_S32 WINAPI GetCommandID(IN T_U8 buffer[], IN T_U16 usLength, OUT T_U16 *pusProcessBufferLength);

DLLEXPORT T_S32 WINAPI GetCommandData(T_U16 usCommandID, PVOID pStruct);

DLLEXPORT T_S32 WINAPI GetKVOCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

DLLEXPORT T_S32 WINAPI GetDateTimeBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

DLLEXPORT T_U16 WINAPI MaxCommandLength();

/***********************************************
* Description:
*   Convert The Command GetCategoryCount Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCategoryCountBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetDrugLibCount Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetDrugLibCountBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetCategoryItem Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ucCategoryIndex:  Category Index,the unique key
*   ucLanguage:		  language of category item
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCategoryItemBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucCategoryIndex, T_U8 ucLanguage, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetDrugItem Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ucDrugIndex:      Drug Index,the unique key of drug
*   ucLanguage:		  language of drug item
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetDrugItemBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 ucDrugIndex, T_U8 ucLanguage, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetDrugItemWithType Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ucDrugIndex:      Drug Index,the unique key of drug
*   ucLanguage:		  language of drug item
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetDrugItemWithTypeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 ucDrugIndex, T_U8 ucLanguage, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command ClearDrugLib Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ClearDrugLibBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command UpdateCategoryItem Data To Bytes
*
* Argument:
*   ucSequenceID:         Sequence ID
*   ucProductID:          Product ID
*   ucCategoryIndex:      Category Index
*   ucLanguage:           0:Chinese;1:English;2:Spanish
*   ucEncode:             0:ASCII;1:UTF-8;2:Unicode(16)
*   ucCategoryNameLength: Category Name Buffer's Length
*   pucCategoryNameBuffer:Category Name Buffer
*	ucColor_R            :color of category name
*	ucColor_G            :color of category name
*	ucColor_B            :color of category name
*	usBufferLength:       pucBuffer's length
*   pucBuffer:		      Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI UpdateCategoryItemBytes( IN T_U8 ucSequenceID, 
												IN T_U8 ucProductID, 
												IN T_U8 ucCategoryIndex, 
												IN T_U8 ucLanguage, 
												IN T_U8 ucEncode, 
												IN T_U8 ucCategoryNameLength, 
												IN T_U8 *pucCategoryNameBuffer,
												IN T_U8 ucColor_R,
												IN T_U8 ucColor_G,
												IN T_U8 ucColor_B,
												IN T_U16 usBufferLength, 
												OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command UpdateDrugItem Data To Bytes
*
* Argument:
*   ucSequenceID:         Sequence ID
*   ucProductID:          Product ID
*   ucDrugIndex:          Drug Index 
*   ucFlag:               Flag:drug's flag, 0x01:Removed;0x02:Selected;0x03:Removed and Selected,the priority is low bit > high bit
*   ucLanguage:           0:Chinese;1:English;2:Spanish
*   ucEncode:             0:ASCII;1:UTF-8;2:Unicode(16)
*   ucDrugNameLength:     Drug Name Buffer's Length
*   pucDrugNameBuffer:    Drug Name Buffer
*	ucTipsLength:         pucTipsBuffer's length
*	pucTipsBuffer:        Tips string buffer
*	fDoseLower:           Dose Lower limitation
*	fDoseUpper:           Dose Upper limitation
*	fConcentrationLower:  Concentration Lower limitation
*	fConcentrationUpper:  Concentration Upper limitation
*	ucColor_R:           color of drug name
*	ucColor_G:           color of drug name
*	ucColor_B:           color of drug name
*	usBufferLength:       pucBuffer's length
*   pucBuffer:		      Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI UpdateDrugItemBytes(IN T_U8 ucSequenceID,
											IN T_U8 ucProductID,
											IN T_U16 ucDrugIndex,
											IN T_U8 ucFlag,
											IN T_U8 ucLanguage,
											IN T_U8 ucEncode,
											IN T_U8 ucDrugNameLength,
											IN T_U8 *pucDrugNameBuffer,
											IN T_U8 ucTipsLength,
											IN T_U8 *pucTipsBuffer,
											IN float fDoseLower,
											IN float fDoseUpper,
											IN float fConcentrationLower,
											IN float fConcentrationUpper,
											IN T_U8 ucColor_R,
											IN T_U8 ucColor_G,
											IN T_U8 ucColor_B,
											IN T_U16 usBufferLength,
											OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command UpdateDrugItemWithType To Bytes
*
* Argument:
*   ucSequenceID:         Sequence ID
*   ucProductID:          Product ID
*   ucDrugIndex:          Drug Index
*   ucFlag:               Flag:drug's flag, 0x01:Removed;0x02:Selected;0x03:Removed and Selected,the priority is low bit > high bit
*   ucLanguage:           0:Chinese;1:English;2:Spanish
*   ucEncode:             0:ASCII;1:UTF-8;2:Unicode(16)
*   ucDrugNameLength:     Drug Name Buffer's Length
*   pucDrugNameBuffer:    Drug Name Buffer
*	ucTipsLength:         pucTipsBuffer's length
*	pucTipsBuffer:        Tips string buffer
*	fDoseLower:           Dose Lower limitation
*	fDoseUpper:           Dose Upper limitation
*	fConcentrationLower:  Concentration Lower limitation
*	fConcentrationUpper:  Concentration Upper limitation
*	ucColor_R:           color of drug name
*	ucColor_G:           color of drug name
*	ucColor_B:           color of drug nameuc
*	IsTypeIII:           whether the drug is type III drug
*	usBufferLength:       pucBuffer's length
*   pucBuffer:		      Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI UpdateDrugItemWithTypeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U16 ucDrugIndex,
	IN T_U8 ucFlag,
	IN T_U8 ucLanguage,
	IN T_U8 ucEncode,
	IN T_U8 ucDrugNameLength,
	IN T_U8 *pucDrugNameBuffer,
	IN T_U8 ucTipsLength,
	IN T_U8 *pucTipsBuffer,
	IN float fDoseLower,
	IN float fDoseUpper,
	IN float fConcentrationLower,
	IN float fConcentrationUpper,
	IN T_U8 ucColor_R,
	IN T_U8 ucColor_G,
	IN T_U8 ucColor_B,
	IN T_U8 ucIsTypeIII,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetLanguageCount Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetLanguageCountBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command UpdateCategoryDrugIndex To Bytes
*
* Argument:
*   ucSequenceID           : Sequence ID
*   ucProductID            : Product ID
*   ucCategoryIndex        : Category Index
*   ucLanguage			   : language of Category
*   ucDrugIndexBufferLength: DrugIndex Buffer's Length
*   pusDrugIndexBuffer	   : Drug Indexes of Category
*	usBufferLength         : pucBuffer's length
*   pucBuffer              : Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI UpdateCategoryDrugIndexCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucLanguage, IN T_U8 ucCategoryIndex, IN T_U8 ucDrugIndexBufferLength, IN T_U16 *pusDrugIndexBuffer, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetCategoryDrugIndex To Bytes
*
* Argument:
*   ucSequenceID   : Sequence ID
*   ucProductID    : Product ID
*   ucCategoryIndex: Category Index
*   ucLanguage	   : language of Category
*	usBufferLength : pucBuffer's length
*   pucBuffer      : Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCategoryDrugIndexCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucCategoryIndex, IN T_U8 ucLanguage, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SendFileStart To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucFileType    :     type of file
*   ucSubID       :		sub id of this type file
*   ucFileSize    :     byte size of file,
*   ucCheckSum    :     check sum
*   ucBlockCount  :     the count of package to send
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SendFileStartCommandBytes(IN T_U8 ucSequenceID,
	IN T_U8 ucProductID,
	IN T_U8 ucFileType,
	IN T_U8 ucSubID,
	IN T_U32 ucFileSize,
	IN T_U32 ucCheckSum,
	IN T_U16 ucBlockCount,
	IN T_U16 usBufferLength,
	OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SendFilePackage Data To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucFileType    :     type of file
*   ucSubID       :		sub id of this type file
*   ucSequenceNumber   :     sequence number of this block
*   ucPackageDataLength:     data length of the block buffer
*   pucPackageDataBuffer:    block buffer
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SendFilePackageCommandBytes(IN T_U8 ucSequenceID,
	IN T_U8 ucProductID,
	IN T_U8 ucFileType,
	IN T_U8 ucSubID,
	IN T_U32 ucSequenceNumber,
	IN T_U16 ucPackageDataLength,
	IN T_U8 *pucPackageDataBuffer,
	IN T_U16 usBufferLength,
	OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SendFileCompleted To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucFileType    :     type of file
*   ucSubID       :		sub id of this type file
*   ucResult      :		result of send file,success,fail or others
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SendFileCompletedCommandBytes(IN T_U8 ucSequenceID,
	IN T_U8 ucProductID,
	IN T_U8 ucFileType,
	IN T_U8 ucSubID,
	IN T_U8 ucResult,
	IN T_U16 usBufferLength,
	OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetFirmwareVersion To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetFirmwareVersionCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetCurrentMode To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCurrentModeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ResetPump To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucPumpMode    :		mode to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ResetPumpCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucPumpMode, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSerialNumber To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSerialNumberCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSerialNumber To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucSerialNumberLength    :		length of SerialNumber buffer
*   pucSerialNumberBuffer    :		SerialNumber buffer
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSerialNumberCommandBytes(IN T_U8 ucSequenceID,
	IN T_U8 ucProductID,
	IN T_U8 ucSerialNumberLength,
	IN T_U8 *pucSerialNumberBuffer,
	IN T_U16 usBufferLength,
	OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command ResetSPIFlashData To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulResetDataType:	data type to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ResetSPIFlashDataCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulResetDataType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetOcculsionPressureThreshold To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetOcculsionPressureThresholdCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetOcculsionPressureThreshold To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucThresholdLength  :length of Threshold buffer
*   pucThresholdBuffer :Threshold buffer
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetOcculsionPressureThresholdCommandBytes(IN T_U8 ucSequenceID,
	IN T_U8 ucProductID,
	IN T_U8 ucThresholdLength,
	IN T_U8 *pucThresholdBuffer,
	IN T_U16 usBufferLength,
	OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringeData_Command To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*   ucSize        :     size
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSyringeDataCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, T_U8 ucBrand, T_U8 ucSize, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSyringeData To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*   ucSize        :     size
*   syringeData   :     struct of syringe data
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSyringeDataCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN TS_Field__CustomSyringeData syringeData, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetInputsAtMain To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetInputsAtMainCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
//FQC
/***********************************************
* Description:
*   Convert The Command GetBatteryAlarmDuration To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBatteryAlarmDurationCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBatteryVoltage To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBatteryVoltageCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetOcclusionLevel To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetOcclusionLevelCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetOcclusionLevel To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucPressureLevel:	pressure level
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetOcclusionLevelCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucPressureLevel, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetInfusionMode To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucInfusionMode:		infusion mode
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetInfusionModeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucInfusionMode, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetDateTime To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usYear        :		Year of Datetime
*   ucMonth       :		Month of Datetime
*   ucDay         :		Day of Datetime
*   ucHour        :		Hour of Datetime
*   ucMinute      :		Minute of Datetime
*   ucSecond      :		Second of Datetime
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetDateTimeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U16 usYear, IN T_U8 ucMonth, IN T_U8 ucDay, 
	IN T_U8 ucHour, IN T_U8 ucMinute, IN T_U8 ucSecond, 
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

//Maintenance
/***********************************************
* Description:
*   Convert The Command GetMaintenanceDateTime To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetMaintenanceDateTimeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetMaintenancePeriod To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetMaintenancePeriodCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetMaintenancePeriod To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucMaintenancePeriod:maintenance period
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetMaintenancePeriodCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucMaintenancePeriod, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetPressureSensorValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetPressureSensorValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetAlarmVolume To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetAlarmVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetAlarmVolume To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucVolume      :		Alarm volume
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetAlarmVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucVolume, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBrightness To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBrightnessCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetBrightness To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrightness  :		Brightness
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetBrightnessCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrightness, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetNightModePeriod To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetNightModePeriodCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetNightModePeriod To Bytes
*
* Argument:
*   ucSequenceID  : Sequence ID
*   ucProductID   : Product ID
*   ucBeginHour   :	Night mode begin hour
*   ucBeginMinute :	Night mode begin minute
*   ucEndHour     :	Night mode end hour
*   ucEndMinute   :	Night mode end minute
*	usBufferLength:	pucBuffer's length
*   pucBuffer     :	Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetNightModePeriodCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBeginHour, IN T_U8 ucBeginMinute, IN T_U8 ucEndHour, IN T_U8 ucEndMinute, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetPumpLanguage To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetPumpLanguageCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetPumpLanguage To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucPumpLanguage:		pump language to be set
*   ucPumpRegion  :     pump language region to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetPumpLanguageCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucPumpLanguage, IN T_U8 ucPumpRegion, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ClearHistoryLog To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ClearHistoryLogCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetPumpAlarm To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetPumpAlarmCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetPowerStatus Data To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetPowerStatusCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSensorStatus To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ulSensorMask:     mask code of sensors
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSensorStatusCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulSensorMask, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetInfusionMode To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetInfusionModeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringeBrand To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSyringeBrandCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSyringeBrand To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand       :		brand to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSyringeBrandCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetDoseUnit To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetDoseUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetDoseUnit To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucDoseUnit    :		dose unit to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetDoseUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucDoseUnit, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetKVO To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   fKVORate      :		KVO rate to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetKVOCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN float fKVORate, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command WriteLog To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulType		  :		log type to be written
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI WriteLogCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetLogTotalNum To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetLogTotalNumCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetLog To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ulLogSqeNumber:   log item's sequence number
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetLogCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulLogSqeNumber, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetLogEx(unprotected log) To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ulLogSqeNumber:   log item's sequence number
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetLogExCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulLogSqeNumber, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBatteryThreshold To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ucRateRange:      rate range of battery threshold 
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBatteryThresholdCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRateRange, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetBatteryThreshold To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRateRange   :		rate range
*   usOffthreshold:		threshold of off rate range
*   usDepletedthreshold:threshold of deplete rate range
*   usLowthreshold:		threshold of low rate range
*   usOnethreshold:		threshold of one block rate range
*   usTwothreshold:		threshold of two block rate range
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetBatteryThresholdCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U8 ucRateRange, 
	IN T_U16 usOffthreshold,
	IN T_U16 usDepletedthreshold,
	IN T_U16 usLowthreshold,
	IN T_U16 usOnethreshold,
	IN T_U16 usTwothreshold,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetCurrentDrug To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCurrentDrugCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetCurrentDrug To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usDrugIndex   :		drug index
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetCurrentDrugCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usDrugIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetInfusionParameter To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetInfusionParameterCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetInfusionParameter for GPA To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   infusionParas :		infusion parameters
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetInfusionParameterCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN TS_Field_CustomInfusionParameterAll infusionParas, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetInfusingParameterOfMode for GPA To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   infusingParas :		infusing parameters to be set while infusing
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetInfusingParameterOfModeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN TS_Field_CustomInfusingParameterAll infusingParas, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetTimeModeRate To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucHour        :		hours to be set
*   ucMinute      :		minutes to be set
*   fVTBI         :		VTBI to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
//DLLEXPORT T_S32 WINAPI SetTimeModeRateCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucHour, IN T_U8 ucMinute, IN float fVTBI, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetWeightModeRate To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   fDose		  :		Dose to be set
*   fWeight       :		Weight to be set
*   fDrugSolution :		DrugSolution to be set
*   fVolume       :		Volume to be set
*   fVTBI         :		VTBI to be set
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
//DLLEXPORT T_S32 WINAPI SetWeightModeRateCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
//	IN float fDose, IN float fWeight, IN float fDrugSolution, IN float fVolume, IN float fVTBI, 
//	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetBolusRate To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   fBolusRate    :		bolus rate
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
//DLLEXPORT T_S32 WINAPI SetBolusRateCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN float fBolusRate, IN float fVTBI, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetPrimingRat To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   fPrimingRate  :		priming rate
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
//DLLEXPORT T_S32 WINAPI SetPrimingRateCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN float fPrimingRate, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ResetTotal To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
//DLLEXPORT T_S32 WINAPI ResetTotalCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetMultiRate4GPA To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
//DLLEXPORT T_S32 WINAPI GetMultiRate4GPACommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetFCTFlag To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ucRole        :	  main or UI
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetFCTFlagCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRole, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetFCTFlag To Bytes
*
* Argument:
*   ucSequenceID  :   Sequence ID
*   ucProductID   :   Product ID
*   ucRole        :	  main or UI
*   ucFCTFlag	  :   FCT flag to be set
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetFCTFlagCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRole, IN T_U8 ucFCTFlag, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetADCRedress To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetADCRedressCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetADCRedress To Bytes
*
* Argument:
*   ucSequenceID  :   Sequence ID
*   ucProductID   :   Product ID
*   ssADC_redress_pressure  :   ADC pressure channel redress data
*   ssADC_redress_size      :   ADC size channel redress data
*   ssADC_redress_battery   :   ADC battery channel redress data
*   ssADC_redress_near_empty:   ADC near empty channel redress data
*   ssADC_redress_bat_temp1 :   ADC temp1 channel redress data
*   ssADC_redress_bat_temp2 :   ADC temp2 channel redress data
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetADCRedressCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_S16 ssADC_redress_pressure, IN T_S16 ssADC_redress_size, IN T_S16 ssADC_redress_battery,
	IN T_S16 ssADC_redress_near_empty, IN T_S16 ssADC_redress_bat_temp1, IN T_S16 ssADC_redress_bat_temp2,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetPressurePValue To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetPressurePValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetFCTFlag To Bytes
*
* Argument:
*   ucSequenceID  :   Sequence ID
*   ucProductID   :   Product ID
*   usPValue	  :   Pressure P value to be set
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetPressurePValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usPValue, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringePressureValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*   ucSize        :     size
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSyringePressureValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U8 ucSize, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSyringePressureValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*   ucSize        :     size
*   usPressureLevel0:   pressure value of level 0
*   usPressureLevel1:   pressure value of level 1
*   usPressureLevel2:   pressure value of level 2
*   usPressureLevel3:   pressure value of level 3
*   usPressureLevel4:   pressure value of level 4
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSyringePressureValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U8 ucBrand, IN T_U8 ucSize,
	IN T_U16 usPressureLevel0, IN T_U16 usPressureLevel1, IN T_U16 usPressureLevel2, 
	IN T_U16 usPressureLevel3, IN T_U16 usPressureLevel4,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetPressureFactorABC To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetPressureFactor_ABCCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSizeSensorCalibrationFactorKP To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSizeSensorCalibrationFactor_KPCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringeCaliFlag To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*   ucSize        :     size
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSyringeCaliFlagCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U8 ucSize, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringeCaliFlag To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*   ucSize        :     size
*   ucCaliFalg    :     Calibratin flag
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSyringeCaliFlagCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U8 ucSize, IN T_U8 ucCaliFalg, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetAppImgValidFlag To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetAppImgValidFlagCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringeCaliFlag To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usAppImgValidFlag:  App image valid flag
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetAppImgValidFlagCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usAppImgValidFlag, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetUIDeliverySecureConfig To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetUIDeliverySecureConfigCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringeCaliFlag To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulResidual_time :
*   ulAlarm_sound_type :
*   ulInf_safety_passcode :
*   ulAlarm_type_passcode :
*   ulBrand_pre_choice :
*   ucChange_rate_in_run :
*   ucLock_in_run :
*   ucSaving_last_infusion_programming :
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetUIDeliverySecureConfigCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U32 ulResidual_time, IN T_U32 ulAlarm_sound_type,
	IN T_U32 ulInf_safety_passcode, IN T_U32 ulAlarm_type_passcode,
	IN T_U32 ulBrand_pre_choice, IN T_U8 ucChange_rate_in_run,
	IN T_U8 ucLock_in_run, IN T_U8 ucSaving_last_infusion_programming,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetUIUserDefineSyringeBrandName To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetUIUserDefineSyringeBrandNameCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetUIUserDefineSyringeBrandName To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand ID
*   ucBrandNameLength:	pucBuffer's length
*	pucBrandNameBuffer:	brand name buffer
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetUIUserDefineSyringeBrandNameCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U8 ucBrand, IN T_U8 ucBrandNameLength, IN T_U8 *pucBrandNameBuffer, 
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSecuritySettingLockPassword To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSecuritySettingLockPasswordCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSecuritySettingLockPassword To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulPassword    :     password
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSecuritySettingLockPasswordCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulPassword, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSecuritySwitch To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulSwitchMask  :     switches
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSecuritySwitchCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulSwitchMask, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSecuritySwitch To Bytes
*
* Argument:
*   ucSequenceID  :		Sequence ID
*   ucProductID   :		Product ID
*   ucSwitchMask  :		switch to be edited
*   ulSwitchStatus:		switch status
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSecuritySwitchCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U32 ulSwitchMask, IN T_U32 ulSwitchStatus,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetCompleteInfusionAlarmTime To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCompleteInfusionAlarmTimeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetCompleteInfusionAlarmTime To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucProductID   :     Product ID
*	ucCompleteInfuAlarmTime:alarm time before completing infusion
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetCompleteInfusionAlarmTimeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucCompleteInfuAlarmTime, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetAlarmSoundType To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetAlarmSoundTypeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetAlarmSound To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucAlarmSoundType:   alarm sound type
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetAlarmSoundTypeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucAlarmSoundType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetCustomBrandCaliPara To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*   ucSize        :     size
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCustomBrandCaliParaCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U8 ucSize, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetCustombrandCalipara To Bytes
*
* Argument:
*   ucSequenceID        :     Sequence ID
*   ucProductID         :     Product ID
*   ucBrand		        :     brand
*   ucSize              :     size
*   fCapacityLength     :     syringe capacity length
*   fFlangePlungerLength:     syringe flange to plunger length
*   fExternalDiameter	:     measured syringe external diameter
*	usBufferLength      :	  pucBuffer's length
*   pucBuffer           :	  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetCustomBrandCaliParaCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U8 ucSize, 
	IN float fCapacityLength, IN float fFlangePlungerLength, IN float fExternalDiameter,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ClearAllCustomBrandCaliPara To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ClearAllCustomBrandCaliParaCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ClearCustomBrandCaliPara To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrand		  :     brand
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ClearCustomBrandCaliParaCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrand, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetFlashAddressData To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulAddress     :     Flash address
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetFlashAddressDataCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U32 ulAddress,IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetFlashAddressData To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulAddress     :     Flash address
*   ulData        :     data in flash
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outsideg
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetFlashAddressDataCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U32 ulAddress, IN T_U32 ulData,IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetSupportedMaxFileSize To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucFileType	  :     File type
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSupportedMaxFileSizeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucFileType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetPreSelectonBrand To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetPreSelectonBrandCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetPreSelectonBrand To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usBrandLength :     count of brand
*   pucBrandData  :     brand array
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetPreselectonBrandCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 usBrandLength, IN T_U8*pucBrandData, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetCaliCustomBrand To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetCaliCustomBrandCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetAlarmTypePassword To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetAlarmTypePasswordCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetAlarmTypePassword To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulPassword	  :     password
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetAlarmTypePasswordCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulPassword, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetSizeSensorValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSizeSensorValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetInfusingParameterOfMode To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetInfusingParameterOfModeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetPressureFactorABC To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   slA	          :     factor A
*   slB	          :     factor B
*   slC	          :     factor C
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetPressureFactorABCCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_S32  slA, IN T_S32  slB, IN T_S32  slC, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSizeSensorCalibrationFactorKP To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   slK	          :     factor K
*   slP	          :     factor P
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSizeSensorCalibrationFactorKPCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_S32  slK, IN T_S32 slP, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetProductID To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetProductIDCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetSyringeSizeCaliRange To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSyringeSizeCaliRangeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetSyringeSizeCaliRange To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   tsSizeDiameterRange:Diameter range for each size
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSyringeSizeCaliRangeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN TS_Field_CustomSizeDiameterRange tsSizeDiameterRange, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command RestoreFactorySetting To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI RestoreFactorySettingCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command RestoreFactorySetting_FactoryMode To Bytes
*
* Argument:
*   ucSequenceID:     Sequence ID
*   ucProductID:      Product ID
*   ucResetType:      settings type to be reset
*	usBufferLength:   pucBuffer's length
*   pucBuffer:		  Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI RestoreFactorySetting_FactoryModeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucResetType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command IsFCTMode To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRole        :		main or UI
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI IsFCTModeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRole, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetFCTTestcaseCount To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRole        :		main or UI
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetTestCaseCountCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRole, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetFCTTestcaseItem To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRole        :		main or UI
*   ucTestcaseIndex:    index of FCT test case
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetTestCaseItemCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRole, IN T_U8 ucTestcaseIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetFCTTestcaseHint To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRole        :		main or UI
*   ucTestcaseIndex:    index of FCT test case
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetTestCaseHintCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRole, IN T_U8 ucTestcaseIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command TriggerFCTTestcaseItem To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRole        :		main or UI
*   ucTestcaseIndex:    index of FCT test case
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TriggerTestCaseItemCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRole, IN T_U8 ucTestcaseIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);


//TAA
/***********************************************
* Description:
*   Convert The Command TAARollbackVolume To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulRollbackVolume:	volume to rollback
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TAARollbackVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulRollbackVolume, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command TAAGetScreenValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRow         :		row index in screen
*   ucColumn      :		Column index in screen
*   ucScreenID    :		screen ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TAAGetScreenValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRow, IN T_U8 ucColumn, IN T_U8 ucScreenID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command TAAGetTitleHint To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucTitleHintType:	title or hint
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TAAGetTitleHintCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucTitleHintType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command TAASetForwardVolume To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ulForwardVolume:	volume to forward
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TAASetForwardVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U32 ulForwardVolume, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command TAAStopMotor To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TAAStopMotorCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command TAAGetRightAreaScreenValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TAAGetRightAreaScreenValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command TAAGetCursorPosInScreen To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI TAAGetCursorPosInScreenCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetMaintenanceDateTime To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usYear        :		Year of Maintenance Datetime
*   ucMonth       :		Month of Maintenance Datetime
*   ucDay         :		Day of Maintenance Datetime
*   ucHour        :		Hour of Maintenance Datetime
*   ucMinute      :		Minute of Maintenance Datetime
*   ucSecond      :		Second of Maintenance Datetime
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetMaintenanceDateTimeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U16 usYear, IN T_U8 ucMonth, IN T_U8 ucDay,
	IN T_U8 ucHour, IN T_U8 ucMinute, IN T_U8 ucSecond,
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

//import/Export SPI data

/***********************************************
* Description:
*   Convert The Command ExportFileFromPumpStart To Bytes
*
* Argument:
*   ucFileType    :     file type to be exported
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ExportFileFromPumpStartCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucFileType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ExportFileFromPumpPackage To Bytes
*
* Argument:
*   ucFileType    :     file type to be exported
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ExportFileFromPumpPackageCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucFileType, IN T_U16 usSequenceNum, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ExportFileFromPumpResult To Bytes
*
* Argument:
*   ucFileType    :     file type to be exported
*   ucSendResult  :     exported result
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ExportFileFromPumpResultCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucFileType, IN T_U8 ucSendResult, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ImportFileToPumpStart To Bytes
*
* Argument:
*   ucFileType    :     file type to be exported
*   ulFileSize    :     file size to be exported
*   usBlockCount  :     count of file packages to be exported
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ImportFileToPumpStartCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucFileType, IN T_U32 ulFileSize, IN T_U16 usBlockCount, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ImportFileToPumpPackage To Bytes
*
* Argument:
*   ucFileType    :     file type to be exported
*   usSequenceNum :     sequence number of file package
*   ulFilePackageLength :  length of pucFilePackageBuffer
*   pucFilePackageBuffer:  data of file package
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ImportFileToPumpPackageCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucFileType, IN T_U16 usSequenceNum, IN T_U16 ulFilePackageLength, IN T_U8 *pucFilePackageBuffer, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ImportFileToPumpResult To Bytes
*
* Argument:
*   ucFileType    :     file type to be exported
*   ucSendResult  :     exported result
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ImportFileToPumpResultCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucFileType, IN T_U8 ucSendResult, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command RemoteStartstopInfusion To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucStartStop   :     start or stop
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI RemoteStartstopInfusionCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucStartStop, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetFirmwareDataVersion To Bytes
*
* Argument:
*   ucDataType    :     data type to get version
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetFirmwareDataVersionCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucDataType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SystemStatus To Bytes
*
* Argument:
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSystemStatusCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBrandCount To Bytes
*
* Argument:
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBrandCountCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBrandName To Bytes
*
* Argument:
*   ucBrandIndex  :     brand index
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBrandNameCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrandIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetAlarmCount To Bytes
*
* Argument:
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
//DLLEXPORT T_S32 WINAPI GetAlarmCountCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetAlarmName To Bytes
*
* Argument:
*   ucAlarmIndex  :     alarm index
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetAlarmNameCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucAlarmIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetTotalVolume To Bytes
*
* Argument:
*   fTotalVolume :     total volume
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetTotalVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN float fTotalVolume, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

//Precision Calibration
/***********************************************
* Description:
*   Convert The Command GetTubePrecisionCalibrationStatus To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetTubePrecisionCalibrationStatusCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetTubePrecisionCalibrationBrand To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand index to be calibrated
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetTubePrecisionCalibrationBrandCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrandIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command StartTubePrecisionCalibrationPriming To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI StartTubePrecisionCalibrationPrimingCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command StopTubePrecisionCalibrationPriming To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI StopTubePrecisionCalibrationPrimingCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetPrecisionCalibrationParameter To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucSequenceNumber :  precision calibration sequence
*   fVTBI         :     VTBI used to calibrate
*   fRate         :     Rate used to calibrate
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetTubePrecisionCalibrationParameterCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucSequenceNumber, IN float fVTBI, IN float fRate, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command SetPrecisionCalibrationValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucSequenceNumber :  precision calibration sequence
*   ucActualVolume  :	actual volume when calbration
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetTubePrecisionCalibrationInfusionValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucSequenceNumber, IN float fActualVolume, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command StopTubePrecisionCalibration To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI StopTubePrecisionCalibrationCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetRegionLanguageList To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetRegionLanguageListCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetRegionCategoryCount To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	ucRegionIndex:		region index
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetRegionCategoryCountCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRegionIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetRegionCategoryItem To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	ucRegionIndex:		region index
*   ucCategoryIndex:    Category Index
*   ucLanguage:         language
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetRegionCategoryItemCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRegionIndex, IN T_U8 ucCategoryIndex, IN T_U8 ucLanguageIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command UpdateRegionCategoryItem To Bytes
*
* Argument:
*   ucSequenceID         : Sequence ID
*   ucProductID          : Product ID
*   ucRegionIndex        : region Index
*   ucCategoryIndex      : Category Index
*   ucLanguage           : language
*   usBlockCount         : block count to be set
*	usBufferLength       : pucBuffer's length
*   pucBuffer            : Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI StartUpdateRegionCategoryDrugindexCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U8 ucRegionIndex, IN T_U8 ucCategoryIndex, IN T_U8 ucLanguage, IN T_U16 usBlockCount,IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command StopTubePrecisionCalibration To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usBlockSeqNum :		Block sequence number
*   ucRegionIndex :		region Index
*   ucCategoryIndex        : Category Index
*   ucLanguage			   : language of Category
*   usDrugIndexBufferLength: DrugIndex Buffer's Length
*   pusDrugIndexBuffer	   : Drug Indexes of Category
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI UpdateRegionCategoryDrugindexCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U16 usBlockSeqNum,IN T_U8 ucRegionIndex, IN T_U8 ucCategoryIndex, IN T_U8 ucLanguage, IN T_U16 usDrugIndexBufferLength, IN T_U16 *pusDrugIndexBuffer, 
	IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetRegionCategoryDrugindex To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usBlockSeqIndex :   package sequence number to be sent
*   ucRegionIndex :     region Index,the unique key
*   ucCategoryIndex:    Category Index,the unique key
*   ucLanguage:		    language of category item
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetRegionCategoryDrugindexCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBlockSeqIndex, IN T_U8 ucRegionIndex, IN T_U8 ucCategoryIndex, IN T_U8 ucLanguage, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command StartGetRegionCategoryDrugindex To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRegionIndex :     region Index,the unique key
*   ucCategoryIndex:    Category Index,the unique key
*   ucLanguage:		    language of category item
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI StartGetRegionCategoryDrugIndexCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucRegionIndex, IN T_U8 ucCategoryIndex, IN T_U8 ucLanguage, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command StartImportDruglib To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI StartImportDruglibCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command EndImportDruglib To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   usImportedDrugCount:imported drug count
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI EndImportDruglibCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usImportedDrugCount, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetRegionCount To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetRegionCountCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetRegionName To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucRegionIndex :     region Index,the unique key
*   ucLanguageIndex:	language of category item
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetRegionNameCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRegionIndex, IN T_U8 ucLanguageIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetLanguageName To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucLanguageIndex:	language of category item
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetLanguageNameCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucLanguageIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetTubePrecisionCalibrationFactor To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetTubePrecisionCalibrationFactorCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrandIndex, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetTubePrecisionCalibrationFactor To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*   fFactor		  :		calibration factor
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetTubePrecisionCalibrationFactorCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrandIndex, IN float fFactor, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ExportPressureCalibrationData To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product 
*   ucBrandIndex  :		brand ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ExportPressureCalibrationDataCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U8 ucBrandIndex, IN T_U8 ucPressureSensorType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBrandPressureCalibrationFactorKB To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBrandPressureCalibrationFactorKBCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U8 ucBrandIndex, IN T_U8 ucPressureSensorType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetBrandPressureCalibrationFactorKB To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*   pKBData       :	K,Bs of pressure calibratin paras
*   usKBDataGroupCount :	length of KBs's buffer
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetBrandPressureCalibrationFactorKBCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucBrandIndex, IN T_U8 ucPressureSensorType, IN TS_PressureCalibrationKBData  *pKBData, IN T_U16 usKBDataGroupCount, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
//LVP Night mode
/***********************************************
* Description:
*   Convert The Command GetNightModeAlarmVolume To Bytesf
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetNightModeAlarmVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetNightModeBrightness To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetNightModeBrightnessCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetNightModeAlarmVolume To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucAlarmVolume :		Alarm volume in night mode
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetNightModeAlarmVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucAlarmVolume, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetNightModeBrightness To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrightness  :		Brightness in night mode
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetNightModeBrightnessCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrightness, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
//LVP calibration
/***********************************************
* Description:
*   Convert The Command GetEachPressureSensorValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetEachPressureSensorValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucPressureSensorType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBrandEachPressurePValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBrandEachPressurePValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrandIndex, IN T_U8 ucPressureSensorType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetBrandEachPressurePValue To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*   slP           :		P for presseure calibratin
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetBrandEachPressurePValueCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucBrandIndex, IN T_U8 ucPressureSensorType, IN T_S32 slP, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetSecondaryInfusionCompleteSetting To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetSecondaryInfusionCompleteSettingCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command SetSecondaryInfusionCompleteSetting To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucSecondaryInfusionCompleteSetting  : settings for SecondaryInfusionComplete
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetSecondaryInfusionCompleteSettingCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucSecondaryInfusionCompleteSetting, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetDripSensorSpeed To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetDripSensorSpeedCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
//Tube size
/***********************************************
* Description:
*   Convert The Command GetTubeSize To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetTubeSizeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetTubeSizeCommandBytes To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucTubeSize    :		tube size(drip/mL)
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetTubeSizeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucTubeSize, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBrandOcclusionLevelThreshold To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBrandOcclusionLevelThresholdCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, 
	IN T_U8 ucBrandIndex, IN T_U8 ucPressureSensorType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

/***********************************************
* Description:
*   Convert The Command GetBrandOcclusionLevelThreshold To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucBrandIndex  :		brand ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*   ucOcclusionLevelThresholdBufferLength:	cocclusion level threshold buffer's length
*   pucOcclusionLevelThresholdBuffer :	threshold buffer for all occlusion levels
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetBrandOcclusionLevelThresholdCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucBrandIndex, IN T_U8 ucPressureSensorType, IN T_U8 ucOcclusionLevelThresholdBufferLength, IN T_S32
	*pOcclusionLevelThresholdBuffer, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

//for LVP Debug
/***********************************************
* Description:
*   Convert The Command GetTubeUninstallThreshold To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetTubeUninstallThresholdCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucPressureSensorType, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetOcclusionRollbackVolume To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetOcclusionRollbackVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetTubeUninstallThreshold To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product ID
*   ucPressureSensorType  :pressure sensor type uso/dso
*   usLowerThreshold  :		tube uninstall threshold low limitation
*   usUpperThreshold  :		tube uninstall threshold high limitation
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetTubeUninstallThresholdCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucPressureSensorType, IN T_U16 usLowerThreshold, IN T_U16 usUpperThreshold, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetOcclusionRollbackVolume To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product 
*   pOcclusionRollbackVolumeBuffer:	cocclusion rollback volume buffer's length
*   pucOcclusionLevelThresholdBuffer :	rollback volume buffer for all occlusion levels
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetOcclusionRollbackVolumeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucOcclusionRollbackVolumeBufferLength, IN float*pOcclusionRollbackVolumeBuffer, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetDrugMassUnit To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetDrugMassUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetInfusionNearCompleteCriteria To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetInfusionNearCompleteCriteriaCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetAirDetectionOption To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetAirDetectionOptionCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBubbleSensitivity To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucAirDetectionOption   :air detection option
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBubbleSensitivityCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucAirDetectionOption, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBubbleSensitivity To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucScreenType  :     screen type
*   ucPasscodeLength:	passcode buffer's length
*   pucPasscodeBuffer :	passcode
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI VerifyPasscodeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucScreenType, IN T_U8 ucPasscodeLength, IN T_U8* pucPasscodeBuffer, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetDrugMassUnit To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucDrugMassUnit:     drug mass unit
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetDrugMassUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucDrugMassUnit, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetInfusionNearCompleteCriteria To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucInfusionNearCompleteCriteria  : infusion near complete criteria(by time/volume)
*   ulCriteria_Parameter:time remaining/volume remaining
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetInfusionNearCompleteCriteriaCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucInfusionNearCompleteCriteria, IN T_U32 ulCriteria_Parameter, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetAirDetectionOption To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucAirDetectionOption: air detection option(single bubble,multiple, both
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetAirDetectionOptionCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucAirDetectionOption, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetBubbleSensitivity To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucAirDetectionOption: air detection option(single bubble,multiple bubble
*   ucBubbleSensitivity:  low/medium/high
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetBubbleSensitivityCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
	IN T_U8 ucAirDetectionOption, IN T_U8 ucBubbleSensitivity, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command ModifyPasscode To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucScreenType  :     screen type
*   ucOldPasscodeLength:	old passcode buffer's length
*   pucOldPasscodeBuffer :	old passcode
*   ucNewPasscodeLength:	new passcode buffer's length
*   pucNewPasscodeBuffer :	new passcode
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI ModifyPasscodeCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID,
		IN T_U8 ucScreenType, IN T_U8 ucOldPasscodeLength, IN T_U8* pucOldPasscodeBuffer, IN T_U8 ucNewPasscodeLength, IN T_U8* pucNewPasscodeBuffer, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetBasicModeRateUnit To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetBasicModeRateUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetBasicModeRateUnit To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucRateUnit	  :     rate unit
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetBasicModeRateUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucRateUnit, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command GetWeightUnit To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI GetWeightUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);
/***********************************************
* Description:
*   Convert The Command SetWeightUnit To Bytes
*
* Argument:
*   ucSequenceID  :     Sequence ID
*   ucProductID   :     Product
*   ucRateUnit	  :     weight unit
*	usBufferLength:		pucBuffer's length
*   pucBuffer     :		Buffer defined outside
*
* Return:bytes length after converted
************************************************/
DLLEXPORT T_S32 WINAPI SetWeightUnitCommandBytes(IN T_U8 ucSequenceID, IN T_U8 ucProductID, IN T_U8 ucWeightUnit, IN T_U16 usBufferLength, OUT T_U8 *pucBuffer);

#endif