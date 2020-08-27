#ifndef FIELD_H
#define FIELD_H

#include "enums.h"
#include "c_defs.h"
#ifndef DEFAULTPACK
#pragma pack(push) //保存对齐状态
#pragma pack(1)
#endif
//药库字符串最多为64位
#define NAME_MAX_LENGTH 64
//一条命令中，每个分类包含的drugIndex最大长度
#define DRUGINDEX_OF_CATEGORY_MAX_LENGTH 80
//一条命令中，区域分类包含的drugIndex最大长度
#define DRUGINDEX_OF_REGION_PACKAGE_MAX_LENGTH 100
//序列号保存最大长度256
#define SN_MAX_LENGTH 256
//压力阀值数组最大长度32
#define OCC_THRESHOLD_MAX_LENGTH 32
//#define BATTERY_THRESHOLD_MAX_LENGTH 10
//用户自定义品牌平城最大长度
#define USERDEFINE_BRANDNAME_MAX_LENGTH 20
//品牌名称最大长度
#define BRAND_NAME_STRING_MAX_LENGTH 20
//报警名称最大长度
#define ALARM_NAME_STRING_MAX_LENGTH 64
//读写Flash数据，最大长度
#define FLASH_DATA_MAX_LENGTH 1024
//反转压力Volumn数组最大长度
#define OCCLUSION_LEVEL_MAX_LENGTH 5
//Log
#define LOG_SUMMARY_MAX_LENGTH 64
#define LOG_DETAIL_MAX_LENGTH 384
//screen capture
#define PIXEL_LENGTH 100
//预选品牌，最大长度
#define PRESELECTION_BRAND_MAX_LENGTH 32
//已校准的自定义品牌，最大长度
#define CALIBRIATED_CUSTOM_BRAND_MAX_LENGTH 8
//报警(优先级+报警ID)，最多
#define ALARM_PARAM_MAX_COUNT 250
//FCT
#define FCT_TESTCASE_NAME_MAX_LENGTH 255
#define FCT_TESTCASE_HINTMESSAGE_MAX_LENGTH 255
#define FCT_TRIGGERED_TESTCASE_DETAIL_INFO_MAX_LENGTH 255
//TAA
#define TAA_SCREENVALUE_STRING_MAX_LENGTH 255
#define TAA_TITLEHINT_STRING_MAX_LENGTH 128
#define TAA_OCCLUSION_STRING_MAX_LENGTH 10
#define TAA_BRAND_STRING_MAX_LENGTH 20
#define TAA_SIZE_STRING_MAX_LENGTH 10
#define TAA_TOTAL_STRING_MAX_LENGTH 10
//drug library
#define REGION_MAX_COUNT 64
#define LANGUAGE_MAX_COUNT 64

//import/Export SPI data
#define EXPORT_PUMPFILE_PACKAGE_MAX_LENGTH 1024
//压力校准点参数
#define PRESSURECALIBRATIONPOINT_COUNT 5
#define PRESSURECALIBRATION_KB_COUNT 4
//品牌和压力传感器下,各阻塞等级的压力阈值数组最大长度10
#define BRAND_SENSOR_OCC_THRESHOLD_MAX_LENGTH 10


typedef struct tagCustomFieldGeneralTAA
{
	T_U8 TAACommand;
	T_U16 data;
}TS_Field_CustomGeneralTAA;

typedef struct tagCustomFieldMultiTime
{
	T_U8 time1Hour;
	T_U8 time1Minute;
	T_U8 time2Hour;
	T_U8 time2Minute;
	T_U8 time3Hour;
	T_U8 time3Minute;
	T_U8 RemainTime1Hour;
	T_U8 RemainTime1Minute;
	T_U8 RemainTime2Hour;
	T_U8 RemainTime2Minute;
	T_U8 RemainTime3Hour;
	T_U8 RemainTime3Minute;
}TS_Field_CustomMultiTime;
typedef struct tagInfusionRateField
{
	float rate;
}TS_Field_InfusionRate;
typedef struct tagInfusionRateUnitField
{
	T_U8 rateUnit;
}TS_Field_InfusionRateUnit;
typedef struct tagInfusionVolUnitField
{
	T_U8 volumeUnit;
}TS_Field_InfusionVolUnit;
typedef struct tagTotalVolumeField
{
	float total;
}TS_Field_TotalVolume;

typedef struct tagVTBIField
{
	float VTBI;
}TS_Field_VTBI;

typedef struct tagCustomFieldKVO
{
	float KVO;
}TS_Field_CustomKVO;

typedef struct tagDateTime
{
	T_U16 year;
	T_U8 month;
	T_U8 day;
	T_U8 hour;
	T_U8 minute;
	T_U8 second;

}TS_Field_DateTime;
typedef struct tagCustomFieldDateTime
{
	T_U16 year;
	T_U8 month;
	T_U8 day;
	T_U8 hour;
	T_U8 minute;
	T_U8 second;

}TS_Field_CustomDateTime;
typedef struct tagCustomFieldDateTimePerMaintenance
{
	T_U16 year;
	T_U8 month;
	T_U8 day;
	T_U8 hour;
	T_U8 minute;
	T_U8 second;

}TS_Field_CustomDateTimePerMaintenance;
typedef struct tagCustomFieldMaintenanceDateTime
{
	TS_Field_CustomDateTimePerMaintenance lastMaintenanceDateTime;
	TS_Field_CustomDateTimePerMaintenance nextMaintenanceDateTime;
}TS_Field_CustomMaintenanceDateTime;
typedef struct tagInfusionTimeField
{
	T_U8 hour;
	T_U8 minute;
}TS_Field_InfusionTime;

typedef struct tagMultiRateAndUnitField
{
	T_U8 index;
	T_U8 unit;
	float rate;
}TS_Field_MultiRateAndUnit;
typedef struct tagUnitAndRateField
{
	T_U8 unit;
	float rate;
}TS_Field_UnitAndRate;
typedef struct tagDoseField
{
	float dose;
}TS_Field_Dose;
typedef struct tagDoseUnitField
{
	T_U8 doseUnit;
}TS_Field_DoseUnit;
typedef struct tagCustomFieldDoseUnit
{
	T_U8 doseUnit;
}TS_Field_CustomDoseUnit;
typedef struct tagWeightField
{
	float weight;
}TS_Field_Weight;
typedef struct tagWeightUnitField
{
	T_U8 weightUnit;
}TS_Field_WeightUnit;

typedef struct tagDrugSolutionField
{
	float drugSolution;
}TS_Field_DrugSolution;
typedef struct tagDrugSolutionUnitField
{
	T_U8 drugSolutionUnit;
}TS_Field_DrugSolutionUnit;

typedef struct tagDrugVolumeField
{
	float volume;
}TS_Field_DrugVolume;

typedef struct tagCustomFieldCategoryCount
{
	T_U8 count;
}TS_Field_CustomCategoryCount;

typedef struct tagCustomFieldDrugLibCount
{
	T_U16 count;
}TS_Field_CustomDrugLibCount;
typedef struct tagCustomFieldCategoryItem
{
	T_U8 categoryIndex;
	T_U8 languageID;
	T_U8 encodeID;
	T_U8 categoryNameLength;
	T_U8 categoryNameBuffer[NAME_MAX_LENGTH];
	T_U8 color_R;
	T_U8 color_G;
	T_U8 color_B;
}TS_Field_CustomCategoryItem;
typedef struct tagCustomFieldDrugItem
{
	T_U16 drugIndex;
	T_U8 flag;
	T_U8 languageID;
	T_U8 encodeID;
	T_U8 drugNameLength;
	T_U8 drugNameBuffer[NAME_MAX_LENGTH];
	T_U8 tipsLength;
	T_U8 tipsBuffer[NAME_MAX_LENGTH];
	float doseLower;
	float doseUpper;
	float concentrationLower;
	float concentrationUpper;
	T_U8 color_R;
	T_U8 color_G;
	T_U8 color_B;
}TS_Field_CustomDrugItem;
typedef struct tagCustomFieldDrugItemWithType
{
	T_U16 drugIndex;
	T_U8 flag;
	T_U8 languageID;
	T_U8 encodeID;
	T_U8 drugNameLength;
	T_U8 drugNameBuffer[NAME_MAX_LENGTH];
	T_U8 tipsLength;
	T_U8 tipsBuffer[NAME_MAX_LENGTH];
	float doseLower;
	float doseUpper;
	float concentrationLower;
	float concentrationUpper;
	T_U8 color_R;
	T_U8 color_G;
	T_U8 color_B;
	T_U8 isTypeIII;
}TS_Field_CustomDrugItemWithType;
typedef struct tagACKield
{
	T_U16 messageID;
	T_U8 errNo;
}TS_Field_ACK;
typedef struct tagSerialNumberField
{
	T_U8 serialNumberLength;
	T_U8 serialNumberBuffer[SN_MAX_LENGTH];
}TS_Field_SerialNumber;
typedef struct tagCustomFieldLanguageCount
{
	T_U8 count;
}TS_Field_CustomLanguageCount;
typedef struct tagCustomFieldCategoryDrugIndexes
{
	T_U8 categoryIndex;
	T_U8 language;
	T_U8 drugIndexLength;
	T_U16 drugIndexBuffer[DRUGINDEX_OF_CATEGORY_MAX_LENGTH];
}TS_Field_CustomCategoryDrugIndexes;
typedef struct tagSendFileCompletedField
{
	T_U8 FileType;
	T_U8 SubID;
	T_U8 Result;
}TS_Field_SendFileCompleted;
typedef struct tagCustomFieldSystemMode
{
	T_U8 Mode;
}TS_Field_CustomSystemMode;

typedef struct tagFirmwareField
{
	T_U8 FirmwareType;
	T_U8 MajorVersion;
	T_U16 MinorVersion;
	T_U16 RevisionVersion;
	T_U32 BuildNumber;
}TS_Field_FirmwareVersion;
typedef struct tagCustomFieldOcculsionPressureThreshold
{
	T_U8 thresholdLength;
	T_U8 thresholdBuffer[OCC_THRESHOLD_MAX_LENGTH];
}TS_Field_CustomOcculsionPressureThreshold;

typedef struct tagBattery_Alarm_Duration_Field
{
	T_U16 lowBatteryDuration;
	T_U16 depleteBatteryDuration;
}TS_Field_Battery_Alarm_Duration;
typedef struct tagVoltageField
{
	float voltage;
}TS_Field_Voltage;
typedef struct tagOcclusionLevelField
{
	T_U8 occlusionLevel;
}TS_Field_Occlusion_Level;
typedef struct tagPumpModeField
{
	T_U8 pumpMode;
}TS_Field_Pump_Mode;
typedef struct tagCustomFieldMaintenancePeriod
{
	T_U8 period;
}TS_Field_CustomMaintenance_Period;

typedef struct tagBrandField
{
	T_U8 brand;
}TS_Field_Brand;
typedef struct tagCustomFieldBrand
{
	T_U8 brand;
}TS_Field_CustomBrand;
typedef struct tagSizeField
{
	T_U8 size;
}TS_Field_Size;
typedef struct tagCustomFieldSyringeData
{
	T_U8 brand;
	T_U8 size;
	//size
	T_U16 external_diameter_min; //unit: 0.01mm
	T_U16 external_diameter_max; //unit: 0.01mm
	T_U16 capacity_length; //unit: 0.01mm
	T_U16 flange_plunger_length; //unit: 0.01mm
	T_S32 sectional_area; //unit: 0.001ml/mm

	//the reverse distance for release pressure
	//T_S32 distance_s;//for sensitive occlusion level, unit: 0.01mm
	//T_S32 distance_low;//for low occlusion level, unit: 0.01mm
	//T_S32 distance_middle;//for middle occlusion level, unit: 0.01mm
	//T_S32 distance_high;//for high occlusion level, unit: 0.01mm

	//pressure reverse volume;unit:0.001mL
	T_U16 reverse_volume[OCCLUSION_LEVEL_MAX_LENGTH];

	T_S32 is_for_neonate; //is allow to use on neonate
	
	//friction,   P=(m-friction_weight)*g/S*factor_for_P
	T_S32 friction_weight; //unit:g
	//zoom 1000
	T_S32 factor_for_P;

	//(real_speed-ideal_speed)/idead_speed=speed_deviation, 
	// real_speed/(speed_deviation+1)= ideal_speed, 
	//so real_speed need multiply by 1/(speed_deviation+1),
	//set_speed=real_speed*sectional_area, real_speed = set_speed/sectional_area, 
	//real_speed*1/(speed_deviation+1) = set_speed/(sectional_area*(speed_deviation+1))
	//so sectional_area need multiply by (speed_deviation+1)=factor

	//the factor radio of sectional area, zoom 1000, S=sectional_area*factor
	T_S32 factor_of_sectional_area_for_low_speed;

	//the factor radio of sectional area, zoom 1000, S=sectional_area*factor
	T_S32 factor_of_sectional_area_for_high_speed;
}TS_Field__CustomSyringeData;
typedef struct tagCustomFieldPressureSensorValue
{
	T_U32 ADCValue;
	float volValue;
	float mmHgValue;
}TS_Field_CustomPressureSensorValue;
//system setting
typedef struct tagCustomFieldAlarmVolume
{
	T_U8 alarmVolume;
}TS_Field_CustomAlarmVolume;
typedef struct tagCustomFieldBrightness
{
	T_U8 brightness;
}TS_Field_CustomBrightness;

typedef struct tagCustomFieldNightModePeriod
{
	T_U8 beginHour;
	T_U8 beginMinute;
	T_U8 endHour;
	T_U8 endMinute;
}TS_Field_CustomNightModePeriod;

typedef struct tagCustomFieldPumpLanguage
{
	T_U8 pumpLanguage;
	T_U8 pumpRegion;
}TS_Field_CustomPumpLanguage;
typedef struct tagCustomFieldInputsAtMain
{
	T_U16 battery_adc;
	//T_U16 near_empty_adc;
	T_U16 syringe_size_adc;
	T_U16 syringe_size;
	T_U16 pressure_adc;
	T_S16 board_temperature;
	T_U8 is_alarm_active_from_smcu;
	//T_U8 dock_connect_pin1;
	//T_U8 dock_connect_pin2;
	T_U8 is_battery_charge;
	T_U8 is_ac_connect;
	T_U8 is_pressure_install;
	T_U8 is_syringe_size_install;
	//T_U8 is_near_empty_install;
	T_U8 is_halfNut_lock;
	T_U8 is_plunger_lock;
	//T_U8 setting1;
	//T_U8 setting2;
	//T_U8 setting3;
	//T_U8 setting4;
	T_U8 is_wifi_install;
	T_U8 wifi_status;
}TS_Field_CustomInputsAtMain;
typedef struct tagCustomFieldPumpAlarm
{
	T_U8 alarmCount;
	T_U8 alarms[ALARM_PARAM_MAX_COUNT];
}TS_Field_CustomPumpAlarm;
typedef struct tagFieldPowerStatus
{
	T_U8 powerStatus;
}TS_Field_PowerStatus;
typedef struct tagCustomFieldPowerStatus
{
	T_U8 powerStatus;
	T_U8 batteryChargeStatus;
	T_U8 batteryStatus;
}TS_Field_CustomPowerStatus;
typedef struct tagCustomFieldSensorStatus
{
	T_U32 sensorMask;
	T_U32 sensorStatus;
}TS_Field_CustomSensorStatus;
typedef struct tagFieldBatteryStatus
{
	T_U8 batteryChargeStatus;
	T_U8 batteryStatus;
}TS_Field_BatteryStatus;

typedef struct tagCustomFieldInfusionMode
{
	T_U8 infusionMode;
}TS_Field_CustomInfusionMode;
typedef struct tagCustomFieldLogTotalNum
{
	T_U32 logTotalNum;
}TS_Field_CustomLogTotalNum;
typedef struct tagCustomFieldLogItem
{
	T_U32 sequence_num;					// 日志的序列号
	T_U32 timestamp;         			// 日志发生的时间戳
	//T_U8 languageID;
	//T_U8 encodeID;
	//T_U8 mode;   						// 用户模式
	//T_U8 event_type;
	T_U16 summaryLength;
	T_U8 summary[LOG_SUMMARY_MAX_LENGTH];		// 事件类型	
	T_U16 detailLength;
	T_U8 admin_detail[LOG_DETAIL_MAX_LENGTH];	// 事件预览（字符串）
}TS_Field_CustomLogItem;
typedef struct tagCustomFieldBatteryThreshold
{
	T_U8 rateRange;
	T_U16 offThreshold;
	T_U16 depletedThreshold;
	T_U16 lowThreshold;
	T_U16 oneThreshold;
	T_U16 twoThreshold;
}TS_Field_CustomBatteryThreshold;
typedef struct tagFieldMultiRateParasGPA
{
	float rate1;
	T_U8 hour1;
	T_U8 minute1;
	float rate2;
	T_U8 hour2;
	T_U8 minute2;
	float rate3;
	T_U8 hour3;
	T_U8 minute3;
}TS_Field_MultiRateParasGPA;
typedef struct tagCustomFieldCurrentDrug
{
	T_U16 drugIndex;
}TS_Field_CustomCurrentDrug;
typedef struct tagCustomFieldFCTFlag
{
	T_U8 FCTRole;
	T_U8 FCTFlag;
}TS_Field_CustomFCTFlag;
typedef struct tagCustomFieldADCRedress
{
	T_S16 adc_redress_pressure;
	T_S16 adc_redress_size;
	T_S16 adc_redress_battery;
	T_S16 adc_redress_near_empty;
	T_S16 adc_redress_bat_temp1;
	T_S16 adc_redress_bat_temp2;
}TS_Field_CustomADCRedress;
typedef struct tagCustomFieldPressurePValue
{
	T_U16 PValue;
}TS_Field_CustomPressurePValue;

typedef struct tagCustomFieldSyringePressureValue
{
	T_U8 brand;
	T_U8 size;
	T_U16 pressureLevel0;
	T_U16 pressureLevel1;
	T_U16 pressureLevel2;
	T_U16 pressureLevel3;
	T_U16 pressureLevel4;
}TS_Field_CustomSyringePressureValue;
typedef struct tagCustomFieldPressureFactorABC
{
	T_S32  A;
	T_S32  B;
	T_S32  C;
}TS_Field_CustomPressureFactorABC;
typedef struct tagCustomFieldSizeSensorCalibrationFactorKP
{
	T_S32  K;
	T_S32  P;
}TS_Field_CustomSizeSensorCalibrationFactorKP;

//used in Command_Set_CustomBrand_Cali_Para,Command_Get_Syringe_Cali_Flag
typedef struct tagCustomFieldSyringeCaliFlag
{
	T_U8 brand;
	T_U8 size;
	T_U8 caliFlag;
}TS_Field_CustomSyringeCaliFlag;
typedef struct tagCustomFieldAppImgValidFlag
{
	T_U16 appImgValidFlag;
}TS_Field_CustomAppImgValidFlag;
typedef struct tagCustomFieldUIDeliverySecureConfig
{
	T_U8 change_rate_in_run;
	T_U8 lock_in_run;
	T_U8 saving_last_infusion_programming;
	T_U32 residual_time;
	T_U32 alarm_sound_type;
	T_U32 inf_safety_passcode;
	T_U32 alarm_type_passcode;
	T_U32 brand_pre_choice;
}TS_Field_CustomUIDeliverySecureConfig;
typedef struct tagCustomFieldUIUserDefineSyringeBrandName
{
	T_U8 brand;
	T_U8 brandNameBuffer[USERDEFINE_BRANDNAME_MAX_LENGTH];
}TS_Field_CustomUIUserDefineSyringeBrandName;
typedef struct tagCustomFieldSecuritySettingLockPassword
{
	T_U32 password;
}TS_Field_CustomSecuritySettingLockPassword;
typedef struct tagCustomFieldSecuritySwitches
{
	T_U32 switchesMask;
	T_U32 switchesStatus;
}TS_Field_CustomSecuritySwitches;
typedef struct tagCustomFieldCompleteInfusionAlarmTime
{
	T_U8 alarmTime;
}TS_Field_CustomCompleteInfusionAlarmTime;
typedef struct tagCustomFieldAlarmSoundType
{
	T_U8 alarmSoundType;
}TS_Field_CustomAlarmSoundType;
typedef struct tagCustomCustomFieldBrandCaliPara
{
	T_U8 brand;
	T_U8 size;
	float capacityLength;
	float flangePlungerLength;
	float externalDiameterMin;
	float externalDiameterMax;
	T_U8 calibrationFlag;
}TS_Field_CustomCustomBrandCaliPara;
typedef struct tagCustomFieldFlashAddressData
{
	T_U32 address;
	T_U32 data;
}TS_Field_CustomFlashAddressData;
typedef struct tagCustomFieldSupportedMaxFileSize
{
	T_U8 fileType;
	T_U32 maxFileSize;
}TS_Field_CustomSupportedMaxFileSize;

typedef struct tagCustomFieldPreSelectionBrand
{
	T_U8 brandsCount;
	T_U8 brands[PRESELECTION_BRAND_MAX_LENGTH];
}TS_Field_CustomPreSelectionBrand;
typedef struct tagCustomFieldCalibedCustomBrands
{
	T_U8 customBrandsCount;
	T_U8 customBrands[CALIBRIATED_CUSTOM_BRAND_MAX_LENGTH];
}TS_Field_CustomCalibedCustomBrands;
typedef struct tagCustomFieldAlarmTypePassword
{
	T_U32 password;
}TS_Field_CustomAlarmTypePassword;
typedef struct tagCustomFieldSizeSensorValue
{
	T_U16 ADCValue;
}TS_Field_CustomSizeSensorValue;

typedef struct tagCustomFieldInfusingParamsInWeightSecondaryMode
{
	T_U8 brand;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U32 drugIndex;
	float secondary_residual_volume_WeightSecondaryMode;
	T_U32 residual_time_WeightSecondaryMode;
	float total_volume_WeightSecondaryMode;
	float secondary_rate_WeightSecondaryMode;
	float secondary_dose_WeightSecondaryModeLVP;
	T_U8  doseUnit_WeightSecondaryModeLVP;
	float secondary_weight_WeighSecondarytModeLVP;
	T_U8  weightUnit_WeightSecondaryModeLVP;
	float secondary_drugMass_WeightSecondaryModeLVP;
	T_U8  drugMass_unit_WeightSecondaryModeLVP;
	float secondary_drug_volume_WeightSecondaryModeLVP;//volume
	float primary_residual_volume_WeightSecondaryMode;
	float primary_rate_WeightSecondaryMode;
	float primary_dose_WeightSecondarModeLVP;
	float primary_weight_WeightSecondarModeLVP;
	float primary_drugMass_WeightSecondarModeLVP;
	float primary_drug_volume_WeightSecondarModeLVP;//volume
	float kvo_rate_WeightSecondaryMode;
}TS_Field_CustomInfusingParamsInWeightSecondaryMode;
typedef struct tagCustomFieldInfusingParamsInBasicSecondaryMode
{
	T_U8 brand;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U32 drugIndex;
	float secondary_residual_volume_BasicSecondaryMode;
	T_U32 residual_time_BasicSecondaryMode;
	float total_volume_BasicSecondaryMode;
	float secondary_rate_BasicSecondaryMode;
	T_U8  secondary_only_rate_set_flag_BasicSecondaryMode;
	T_U32 secondary_infusion_time_BasicSecondaryMode;
	float secondary_vtbi_BasicSecondaryMode;
	float primary_residual_volume_BasicSecondaryMode;
	float primary_rate_BasicSecondaryMode;
	T_U8  primary_rate_unit_BasicSecondaryMode;
	T_U32  primary_drop_size_BasicSecondaryMode;
	T_U32  primary_drop_rate_BasicSecondaryMode;
	T_U8  primary_olny_rate_set_flag_BasicSecondaryMode;
	T_U32 primary_infusion_time_BasicSecondaryMode;
	float primary_vtbi_BasicSecondaryMode;
	float kvo_rate_BasicSecondaryMode;
}TS_Field_CustomInfusingParamsInBasicSecondaryMode;
typedef struct tagCustomFieldInfusingParamsInStepMode
{
	T_U8 brand;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U32 drugIndex;
	float residual_volume_StepMode;
	T_U32 residual_time_StepMode;
	float total_volume_StepMode;
	float rate_StepMode;
	T_U32 residual_step_duration_time_StepMode;
	float plateau_rate_StepMode;
	float VTBI_StepMode;
	float initial_rate_StepMode;
	float step_increment_StepMode;
	T_U32 step_duration_time_StepMode;
	float kvo_rate_StepMode;
}TS_Field_CustomInfusingParamsInStepMode;
typedef struct tagCustomFieldInfusingParamsInTaperMode
{
	T_U8 brand;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U32 drugIndex;
	float residual_volume_TaperMode;
	T_U32 residual_time_TaperMode;
	float total_volume_TaperMode;
	float rate_TaperMode;
	float VTBI_TaperMode;
	T_U32 infusion_time_TaperMode;
	T_U32 taperUp_time_TaperMode;
	T_U32 taperDown_time_TaperMode;
	float kvo_rate_TaperMode;
}TS_Field_CustomInfusingParamsInTaperMode;
typedef struct tagCustomFieldInfusingParamsInMultiRateModeLVP
{
	T_U8 brand;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U32 drugIndex;
	float residual_volume_MultiRateModeLVP;
	float total_volume_MultiRateModeLVP;
	float rate1_MultiRateModeLVP;
	T_U32 residual_infusion_Time1_MultiRateModeLVP;
	float rate2_MultiRateModeLVP;
	T_U32 residual_infusion_Time2_MultiRateModeLVP;
	float rate3_MultiRateModeLVP;
	T_U32 residual_infusion_Time3_MultiRateModeLVP;
	float kvo_rate_MultiRateModeLVP;
}TS_Field_CustomInfusingParamsInMultiRateModeLVP;
typedef struct tagCustomFieldInfusingParamsInWeightModeLVP
{
	T_U8 brand;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U32 drugIndex;
	float residual_volume_WeightModeLVP;
	T_U32 residual_time_WeightModeLVP;
	float total_volume_WeightModeLVP;
	float rate_WeightModeLVP;
	float dose_WeightModeLVP;
	T_U8  doseUnit_WeightModeLVP;
	float weight_WeightModeLVP;
	T_U8  weightUnit_WeightModeLVP;
	float drugMass_WeightModeLVP;
	T_U8  drugMass_unit_WeightModeLVP;
	float drug_volume_WeightModeLVP;//volume
	float kvo_rate_WeightModeLVP;
}TS_Field_CustomInfusingParamsInWeightModeLVP;
typedef struct tagCustomFieldInfusingParamsInBasicMode
{
	T_U8 brand;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U32 drugIndex;
	float residual_volume_BasicMode;
	T_U32 residual_time_BasicMode;
	float total_volume_BasicMode;
	float rate_BasicMode;
	T_U8 rateUnit_BasicMode;
	T_U32 dropSize_BasicMode;
	T_U32 dropRate_BasicMode;
	T_U8  olyn_rate_set_flag_BasicMode;
	T_U32 infusion_time_BasicMode;
	float vtbi_BasicMode;
	float kvo_rate_BasicMode;
}TS_Field_CustomInfusingParamsInBasicMode;
typedef struct tagCustomFieldInfusingParamsInWeightMode
{
	T_U8 brand;
	T_U8 size;
	float currentRate;
	T_U8 remainHour;
	T_U8 remainMinute;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U16 drugIndex;
	float total;
	float remainVolume;
	float bolusRate;
	float bolusVTBI;
	float dose;
	T_U8 doseUnit;
}TS_Field_CustomInfusingParamsInWeightMode;
typedef struct tagCustomFieldInfusingParamsInMultiRateMode
{
	T_U8 brand;
	T_U8 size;
	//float currentRate;
	//T_U8 remainHour;
	//T_U8 remainMinute;
	T_U8 occlusionLevel;
	T_U8 drugLibSwitch;
	T_U16 drugIndex;
	float total;
	float remainVolume;
	float bolusRate;
	float bolusVTBI;
	float rate1;
	T_U8 remainHour1;
	T_U8 remainMinute1;
	float rate2;
	T_U8 remainHour2;
	T_U8 remainMinute2;
	float rate3;
	T_U8 remainHour3;
	T_U8 remainMinute3;
}TS_Field_CustomInfusingParamsInMultiRateMode;
typedef struct tagCustomFieldInfusingParamsOfMode
{
	T_U8 infusionMode;//all modes

	T_U8 brand;//rate/time/weight/multi_rate
	T_U8 size;
	float currentRate;
	T_U8 remainHour;
	T_U8 remainMinute;
	T_U8 occlusionLevel;//rate/time/weight/multi_rate
	T_U8 drugLibSwitch;//rate/time/weight/multi_rate
	T_U16 drugIndex;//rate/time/weight/multi_rate
	float total;
	float remainVolume;
	float bolusRate;
	float bolusVTBI;
	//dose
	float dose;
	T_U8 doseUnit;
	//multi-rate
	float rate1;
	T_U8 remainHour1;
	T_U8 remainMinute1;
	float rate2;
	T_U8 remainHour2;
	T_U8 remainMinute2;
	float rate3;
	T_U8 remainHour3;
	T_U8 remainMinute3;
	//basic mode
	TS_Field_CustomInfusingParamsInBasicMode paras_basicmode;
	//weight mode in LVP
	TS_Field_CustomInfusingParamsInWeightModeLVP paras_weightmodeLVP;
	//multi-rate LVP
	TS_Field_CustomInfusingParamsInMultiRateModeLVP paras_multiratemodeLVP;
	//taper mode
	TS_Field_CustomInfusingParamsInTaperMode paras_tapermodeLVP;
	//step mode
	TS_Field_CustomInfusingParamsInStepMode paras_stepmodeLVP;
	//basic-secondary
	TS_Field_CustomInfusingParamsInBasicSecondaryMode paras_basicSecondaryModeLVP;
	//weight-secondary
	TS_Field_CustomInfusingParamsInWeightSecondaryMode paras_weightSecondaryModeLVP;
}TS_Field_CustomInfusingParamsOfMode;
typedef struct tagCustomFieldInfusionParameterAll
{
	T_U8 infusionMode;
	//速率模式
	float rate_RateMode;
	float VTBI_RateMode;
	//时间模式
	T_U8 hour_TimeMode;
	T_U8 minute_TimeMode;
	float VTBI_TimeMode;
	//体重模式
	float dose_WeightMode;
	T_U8 doseUnit_WeightMode;
	float weight_WeightMode;
	float drug_WeightMode;
	float SOL_WeightMode;//volume
	float VTBI_WeightMode;
	//多速率模式
	float rate1_MultiRateMode;
	T_U8 hour1_MultiRateMode;
	T_U8 minute1_MultiRateMode;
	float rate2_MultiRateMode;
	T_U8 hour2_MultiRateMode;
	T_U8 minute2_MultiRateMode;
	float rate3_MultiRateMode;
	T_U8 hour3_MultiRateMode;
	T_U8 minute3_MultiRateMode;
	//basic mode
	float rate_BasicMode;
	T_U8 rateUnit_BasicMode;
	T_U32 dropSize_BasicMode;
	T_U32 dropRate_BasicMode;
	T_U32 infusion_time_BasicMode;
	float VTBI_BasicMode;
	T_U32 delay_start_time_BasicMode;
	//weight mode in LVP
	float dose_WeightModeLVP;
	T_U8 doseUnit_WeightModeLVP;//only used in GET
	float weight_WeightModeLVP;
	T_U8 weightUnit_WeightModeLVP;//only used in GET
	float drugMass_WeightModeLVP; //drugmass
	T_U8 drugMass_unit_WeightModeLVP;//only used in GET
	float volume_WeightModeLVP;//volume
	float VTBI_WeightModeLVP;
	T_U32 delay_start_time_WeightModeLVP;
	//multi-rate LVP
	float rate1_MultiRateModeLVP;
	T_U32 infusion_Time1_MultiRateModeLVP;
	float rate2_MultiRateModeLVP;
	T_U32 infusion_Time2_MultiRateModeLVP;
	float rate3_MultiRateModeLVP;
	T_U32 infusion_Time3_MultiRateModeLVP;
	//taper mode
	float VTBI_TaperMode;
	T_U32 infusion_time_TaperMode;
	T_U32 taperUp_time_TaperMode;
	T_U32 taperDown_time_TaperMode;

	//step mode
	float plateau_rate_StepMode;
	float VTBI_StepMode;
	float initial_rate_StepMode;
	float step_increment_StepMode;
	T_U32 step_duration_time_StepMode;

	//drug index
	T_U8 drugLib_Switch;
	T_U32 drug_Index;


}TS_Field_CustomInfusionParameterAll;
//while infusing
typedef struct tagCustomFieldInfusingParameterAll
{
	T_U8 infusionMode;
	//速率模式/多速率模式
	float current_rate_RateMode;
	//时间模式
	T_U8 hour_TimeMode;
	T_U8 minute_TimeMode;
	//体重模式
	float dose_WeightMode;
}TS_Field_CustomInfusingParameterAll;
typedef struct tagCustomFieldSizeDiameterRange
{
	T_U16 ExternalDiameterMin0;//5ml
	T_U16 ExternalDiameterMax0;
	T_U16 ExternalDiameterMin1;//10ml
	T_U16 ExternalDiameterMax1;
	T_U16 ExternalDiameterMin2;//20ml
	T_U16 ExternalDiameterMax2;
	T_U16 ExternalDiameterMin3;//30ml
	T_U16 ExternalDiameterMax3;
	T_U16 ExternalDiameterMin4;//50ml
	T_U16 ExternalDiameterMax4;
}TS_Field_CustomSizeDiameterRange;
typedef struct tagCustomFieldIsFCTMode
{
	T_U8 testcaseRole;
	T_U8 isFCTMode;
}TS_Field_CustomIsFCTMode;
typedef struct tagCustomFieldFCTTestcaseCount
{
	T_U8 testcaseRole;
	T_U8 testcaseCount;
}TS_Field_CustomFCTTestcaseCount;
typedef struct tagCustomFieldFCTTestcaseItem
{
	T_U8 testcaseRole;
	T_U8 testcaseIndex;
	T_U8 testcaseNameLength;
	T_U8 testcaseName[FCT_TESTCASE_NAME_MAX_LENGTH];
}TS_Field_CustomFCTTestcaseItem;
typedef struct tagCustomFieldFCTTestcaseHint
{
	T_U8 testcaseRole;
	T_U8 testcaseIndex;
	T_U8 testcaseHintLength;
	T_U8 testcaseHintMessage[FCT_TESTCASE_HINTMESSAGE_MAX_LENGTH];
}TS_Field_CustomFCTTestcaseHint;
typedef struct tagCustomFieldTriggeredFCTTestcaseItem
{
	T_U8 testcaseRole;
	T_U8 testcaseIndex;
	T_U8 testcaseResult;
	T_U8 testcaseTriggeredDetailLength;
	T_U8 testcaseTriggeredDetail[FCT_TRIGGERED_TESTCASE_DETAIL_INFO_MAX_LENGTH];
}TS_Field_CustomTriggeredFCTTestcaseItem;

typedef struct tagCustomFieldTAAScreenValue
{
	T_U8 rowIndex;
	T_U8 columnIndex;
	T_U8 screenID;
	T_U8 screenValueLength;
	T_U8 screenValue[TAA_SCREENVALUE_STRING_MAX_LENGTH];
}TS_Field_CustomTAAScreenValue;
typedef struct tagCustomFieldTAATitleHint
{
	T_U8 titleHintType;
	T_U8 dataLength;
	T_U8 data[TAA_TITLEHINT_STRING_MAX_LENGTH];
}TS_Field_CustomTAATitleHint;
typedef struct tagCustomFieldTAARightAreaScreenValue
{
	T_U8 occusionLevel[TAA_OCCLUSION_STRING_MAX_LENGTH];
	T_U8 brand[TAA_BRAND_STRING_MAX_LENGTH];
	T_U8 size[TAA_SIZE_STRING_MAX_LENGTH];
	T_U8 total[TAA_TOTAL_STRING_MAX_LENGTH];
}TS_Field_CustomTAARightAreaScreenValue;
typedef struct tagCustomFieldTAACursorPosInScreen
{
	T_U8 rowIndex;
	T_U8 columnIndex;
	T_U8 screenID;
}TS_Field_CustomTAACursorPosInScreen;
typedef struct tagCustomFieldExportFileFromPumpStart
{
	T_U8 fileType;
	T_U32 fileSize;
	T_U16 blockCount;
}TS_Field_CustomExportFileFromPumpStart;
typedef struct tagCustomFieldExportFileFromPumpPackage
{
	T_U8 fileType;
	T_U16 sequenceNumber;
	T_U16 filePackageLength;
	T_U8 filePackage[EXPORT_PUMPFILE_PACKAGE_MAX_LENGTH];
}TS_Field_CustomExportFileFromPumpPackage;
typedef struct tagCustomFieldExportFileFromPumpResult
{
	T_U8 fileType;
	T_U8 result;
	T_U32 checkSum;
}TS_Field_CustomExportFileFromPumpResult;
typedef struct tagCustomFieldImportFileToPumpPackage
{
	T_U8 fileType;
	T_U16 sequenceNumber;
}TS_Field_CustomImportFileToPumpPackage;

typedef struct tagCustomFieldImportFileResult
{
	T_U8 fileType;
	T_U8 result;
	T_U32 checkSum;
}TS_Field_CustomImportFileResult;
typedef struct tagCustomFieldSystemStatus
{
	T_U8 systemStatus;
}TS_Field_CustomSystemStatus;
typedef struct tagCustomFieldBrandCount
{
	T_U8 allBrandCount;
	T_U8 presetBrandCount;
	T_U8 customBrandCount;
}TS_Field_CustomBrandCount;
typedef struct tagCustomFieldBrandName
{
	T_U8 brandIndex;
	T_U8 brandLevel;
	T_U8 brandNameLength;
	T_U8 brandNameBuffer[BRAND_NAME_STRING_MAX_LENGTH];
}TS_Field_CustomBrandName;
typedef struct tagCustomFieldAlarmCount
{
	T_U8 count;
}TS_Field_CustomAlarmCount;

typedef struct tagCustomFieldAlarmName
{
	T_U8 alarmIndex;
	T_U8 alarmLevel;
	T_U8 alarmNameLength;
	T_U8 alarmNameBuffer[ALARM_NAME_STRING_MAX_LENGTH];
}TS_Field_CustomAlarmName;

typedef struct tagCustomFieldTubePrecisionCalibrationStatus
{
	T_U8 tubeCalibrationStatus;
}TS_Field_CustomTubePrecisionCalibrationStatus;
typedef struct tagCustomFieldTubePrecisionCalibrationBrandSetResult
{
	T_U8 tubeCalibrationBrandSetResult;
}TS_Field_CustomTubePrecisionCalibrationBrandSetResult;
typedef struct tagCustomFieldTubePrecisionCalibrationPrimingStartResult
{
	T_U8 tubeCalibrationPrimingStartResult;
}TS_Field_CustomTubePrecisionCalibrationPrimingStartResult;
typedef struct tagCustomFieldTubePrecisionCalibrationPrimingStopResult
{
	T_U8 tubeCaliParaPrimingStopResult;
}TS_Field_CustomTubePrecisionCalibrationPrimingStopResult;
typedef struct tagCustomFieldTubePrecisionCalibrationParaSetResult
{
	T_U8 sequenceNumber;
	T_U8 caliParaSetResult;
}TS_Field_CustomTubePrecisionCalibrationParaSetResult;
typedef struct tagCustomFieldTubePrecisionCaliInfusionValueSetResult
{
	T_U8 sequenceNumber;
	T_U8 calibrationValueSetResult;
}TS_Field_CustomTubePrecisionCaliInfusionValueSetResult;
typedef struct tagCustomFieldRegionLanguageList
{
	T_U8 regionCount;
	T_U8 regionBuffer[REGION_MAX_COUNT];
	T_U8 languageCount;
	T_U8 languageBuffer[LANGUAGE_MAX_COUNT];
}TS_Field_CustomRegionLanguageList;
typedef struct tagCustomFieldRegionCategoryCount
{
	T_U8 regionIndex;
	T_U8 categoryCount;
}TS_Field_CustomRegionCategoryCount;
typedef struct tagCustomFieldRegionCategoryItem
{
	T_U8 regionIndex;
	T_U8 categoryIndex;
	T_U8 languageID;
	T_U8 encodeID;
	T_U8 categoryNameLength;
	T_U8 categoryNameBuffer[NAME_MAX_LENGTH];
	T_U8 color_R;
	T_U8 color_G;
	T_U8 color_B;
}TS_Field_CustomRegionCategoryItem;

typedef struct tagCustomFieldRegionCategoryDrugIndexes
{
	T_U16 blockSeqNumber;
	T_U8 regionIndex;
	T_U8 categoryIndex;
	T_U8 language;
	T_U16 drugIndexLength;
	T_U16 drugIndexBuffer[DRUGINDEX_OF_REGION_PACKAGE_MAX_LENGTH];
}TS_Field_CustomRegionCategoryDrugIndexes;
typedef struct tagCustomFieldStartRegionCategoryDrugIndexes
{
	T_U8 regionIndex;
	T_U8 categoryIndex;
	T_U8 language;
	T_U16 blockCount;
	T_U16 blockSize;
}TS_Field_CustomStartRegionCategoryDrugIndexes;
typedef struct tagCustomFieldRegionCount
{
	T_U8 regionCount;
}TS_Field_CustomRegionCount;

typedef struct tagCustomFieldRegionName
{
	T_U8 regionIndex;
	T_U8 languageID;
	T_U8 regionNameLength;
	T_U8 regionNameBuffer[NAME_MAX_LENGTH];
}TS_Field_CustomRegionName;

typedef struct tagCustomFieldLanguageName
{
	T_U8 languageID;
	T_U8 languageNameLength;
	T_U8 languageNameBuffer[NAME_MAX_LENGTH];
}TS_Field_CustomLanguageName;

typedef struct tagCustomFieldTubeCalibrationFactor
{
	T_U8 brandIndex;
	float factor;
	T_U8 caliFlag;
}TS_Field_CustomTubeCalibrationFactor;
typedef struct tagPressureCalibrationPointData
{
	int pressure;
	int adc;
}TS_PressureCalibrationPointData;
typedef struct tagPressureCalibrationKBData
{
	float k;
	float b;
}TS_PressureCalibrationKBData;
typedef struct tagCustomFieldCustomPressureCalibrationExportedData
{
	T_U8 brandIndex;
	T_U8 pressureSensorType;
	int P;
	TS_PressureCalibrationPointData points[PRESSURECALIBRATIONPOINT_COUNT];
	TS_PressureCalibrationKBData kbs[PRESSURECALIBRATION_KB_COUNT];
}TS_Field_CustomPressureCalibrationExportedData;

typedef struct tagCustomFieldBrandPressureCalibrationFactorKB
{
	T_U8 brandIndex;
	T_U8 pressureSensorType;
	TS_PressureCalibrationKBData kbs[PRESSURECALIBRATION_KB_COUNT];
	T_U8 caliFlag;
}TS_Field_CustomBrandPressureCalibrationFactorKB;

typedef struct tagCustomFieldNightModeAlarmVolume
{
	T_U8 alarmVolume;
}TS_Field_CustomNightModeAlarmVolume;
typedef struct tagCustomFieldNightModeBrightness
{
	T_U8 brightness;
}TS_Field_CustomNightModeBrightness;
typedef struct tagCustomFieldEachPressureSensorValue
{
	T_U8 pressureSensorType;
	T_U32 ADCValue;
	float volValue;
	float mmHgValue;
}TS_Field_CustomEachPressureSensorValue;
typedef struct tagCustomFieldBrandEachPressurePValue
{
	T_U8 brandIndex;
	T_U8 pressureSensorType;
	T_U32 PValue;
}TS_Field_CustomBrandEachPressurePValue;

typedef struct tagCustomFieldSecondaryInfusionCompleteSetting
{
	T_U8 secondaryInfusionCompleteSetting;
}TS_Field_CustomSecondaryInfusionCompleteSetting;

typedef struct tagCustomFieldDripSensorSpeed
{
	T_U16 speed;
}TS_Field_CustomDripSensorSpeed;
typedef struct tagCustomFieldTubeSize
{
	T_U8 tubeSize;
}TS_Field_CustomTubeSize;
typedef struct tagCustomFieldEachBrandOcclusionLevelThreshold
{
	T_U8 brandIndex;
	T_U8 pressureSensorType;
	T_U8 thresholdBufferLength;
	T_S32 thresholdBuffer[BRAND_SENSOR_OCC_THRESHOLD_MAX_LENGTH];
}TS_Field_CustomEachBrandOcclusionLevelThreshold;

typedef struct tagCustomFieldTubeUninstallThreshold
{
	T_U8 pressureSensorType;
	T_U16 lowerTubeUninstallThreshold;
	T_U16 upperTubeUninstallThreshold;
}TS_Field_CustomTubeUninstallThreshold;

typedef struct tagCustomFieldOcclusionRollbackVolume
{
	T_U8 occlusionRollbackVolumesLength;
	float occlusionRollbackVolumeBuffer[BRAND_SENSOR_OCC_THRESHOLD_MAX_LENGTH];
}TS_Field_CustomOcclusionRollbackVolume;

typedef struct tagCustomFieldDrugMassUnit
{
	T_U8 drugMassUnit;
}TS_Field_CustomDrugMassUnit;

typedef struct tagCustomFieldInfusionNearCompleteCriteria
{
	T_U8 infusionNearCompleteCriteria;
	T_U32 criteriaPara;
}TS_Field_CustomInfusionNearCompleteCriteria;
typedef struct tagCustomFieldAirDetectionOption
{
	T_U8 airDetectionOption;
}TS_Field_CustomAirDetectionOption;
typedef struct tagCustomFieldAirDetectionBubbleSensitivity
{
	T_U8 airDetectionOption;
	T_U8 bubbleSensitivity;
}TS_Field_CustomAirDetectionBubbleSensitivity;
typedef struct tagCustomFieldVerifyPasscodeResult
{
	T_U8 screenType;
	T_U8 verifiedResult;
}TS_Field_CustomVerifyPasscodeResult;
typedef struct tagCustomFieldModifyPasscodeResult
{
	T_U8 screenType;
	T_U8 modifyResult;
}TS_Field_CustomModifyPasscodeResult;
typedef struct tagCustomFieldBasicModeRateUnit
{
	T_U8 rateUnitBasicMode;
}TS_Field_CustomBasicModeRateUnit;
typedef struct tagCustomFieldWeightUnit
{
	T_U8 weightUnit;
}TS_Field_CustomWeightUnit;

#ifndef DEFAULTPACK
#pragma pack(pop)//恢复对齐状态;
#endif
#endif