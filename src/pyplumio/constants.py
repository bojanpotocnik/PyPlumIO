"""Contains contants."""

VERSION: str = '0.0.2'

FRAME_START: int = 0x68
FRAME_END: int = 0x16
HEADER_SIZE: int = 7
BROADCAST_ADDRESS: int = 0x00
ECONET_ADDRESS: int = 0x56
ECONET_TYPE: int = 0x30
ECONET_VERSION: int = 0x05

MODES: list = (
    'OFF',
    'STARTING',
    'STARTING',
    'HEATING',
    'STANDBY',
    'EXTINGUISHED',
    'STOPPED',
    'SCHEDULED START',
    'ALARM',
    'SEALING'
)

TEMP_NAMES: list = (
    'tempCO',
    'tempFeeder',
    'tempCWU',
    'tempExternalSensor',
    'tempBack',
    'tempFlueGas',
    'tempOpticalSensor',
    'tempUpperBuffer',
    'tempLowerBuffer',
    'tempUpperSolar',
    'tempLowerSolar',
    'tempFireplace',
    'totalGain',
    'tempHydraulicCoupler',
    'tempExchanger',
    'tempAirIn',
    'tempAirOut'
)

EDITABLE_PARAMS: list = (
    'AIRFLOW_POWER_100',
    'AIRFLOW_POWER_50',
    'AIRFLOW_POWER_30',
    'POWER_100',
    'POWER_50',
    'POWER_30',
    'MAX_FAN_BOILER_POWER',
    'MIN_FAN_BOILER_POWER',
    'FUEL_FEEDING_TIME_100',
    'FUEL_FEEDING_TIME_50',
    'FUEL_FEEDING_TIME_30',
    'FUEL_FEEDING_BREAK_100',
    'FUEL_FEEDING_BREAK_50',
    'FUEL_FEEDING_BREAK_30',
    'CYCLE_TIME',
    'H2_HYSTERESIS',
    'H1_HYSTERESIS',
    'BOILER_HYSTERESIS',
    'CONTROL_MODE',
    'MIN_FL_POWER',
    'MAX_FL_POWER',
    'MIN_BOILER_POWER',
    'MAX_BOILER_POWER',
    'MIN_FAN_POWER',
    'MAX_FAN_POWER',
    'T_REDUCTION_AIRFLOW',
    'FAN_POWER_GAIN',
    'FUEL_FLOW_CORRECTION_FL',
    'FUEL_FLOW_CORRECTION',
    'AIRFLOW_CORRECTION_100',
    'FEEDER_CORRECTION_100',
    'AIRFLOW_CORRECTION_50',
    'FEEDER_CORRECTION_50',
    'AIRFLOW_CORRECTION_30',
    'FEEDER_CORRECTION_30',
    'AIRFLOW_POWER_GRATE',
    'HIST_BOILER_GRATE',
    'SUPERVISION_WORK_AIRFLOW',
    'SUPERVISION_WORK_AIRFLOW_BRAKE',
    'CO_TEMP_GRATE',
    'DET_TIME_FUEL_GRATE',
    'AIRFLOW_POWER_KINDLE',
    'SMALL_AIRFLOW_POWER_KINDLE',
    'AIRFLOW_KINDLE_DELAY',
    'SCAVENGE_KINDLE',
    'FEEDER_KINDLE',
    'FEEDER_KINDLE_WEIGHT',
    'KINDLE_TIME',
    'WARMING_UP_TIME',
    'FUMES_TEMP_KINDLE_FINISH',
    'FINISH_KINDLE_THRESHOLD',
    'FUMES_DELTA_KINDLE',
    'DELTA_T_KINDLE',
    'MIN_KINDLE_POWER_TIME',
    'SCAVENGE_AFTER_KINDLE',
    'AIRFLOW_POWER_AFTER_KINDLE',
    'SUPERVISION_TIME',
    'FEED_TIME_SUPERVISION',
    'FEED_TIME_SUPERVISION_WEIGHT',
    'FEED_SUPERVISION_BREAK',
    'SUPERVISON_CYCLE_DURATION',
    'AIRFLOW_POWER_SUPERVISION',
    'FAN_SUPERVISON_BREAK',
    'FAN_WORK_SUPERVISION',
    'INCREASE_FAN_SUPPORT_MODE',
    'MAX_EXTINGUISH_TIME',
    'MIN_EXTINGUISH_TIME',
    'EXTINGUISH_TIME',
    'AIRFLOW_POWER_EXTINGUISH',
    'AIRFLOW_WORK_EXTINGUISH',
    'AIRFLOW_BRAKE_EXTINGUISH',
    'SCAVENGE_START_EXTINGUISH',
    'SCAVENGE_STOP_EXTINGUISH',
    'CLEAN_BEGIN_TIME',
    'EXTINGUISH_CLEAN_TIME',
    'AIRFLOW_POWER_CLEAN',
    'WARMING_UP_BRAKE_TIME',
    'WARMING_UP_CYCLE_TIME',
    'REMIND_TIME',
    'LAMBDA_WORK',
    'LAMBDA_CORRECTION_RANGE',
    'OXYGEN_100',
    'OXYGEN_50',
    'OXYGEN_30',
    'OXYGEN_CORRECTION_FL',
    'FUEL_KG_H',
    'FEEDER_CALIBRATION',
    'FUEL_FACTOR',
    'CALORIFIC_KWH_KG',
    'FUEL_DETECTION_TIME',
    'FUMES_TEMP_FUEL_DETECTION',
    'SCHEDULE_FEEDER_2',
    'FEED2_H1',
    'FEED2_H2',
    'FEED2_H3',
    'FEED2_H4',
    'FEED2_WORK',
    'FEED2_BREAK',
    'CO_TEMP_SET',
    'MIN_SET_CO_TEMP',
    'MAX_SET_CO_TEMP',
    'SWITCH_CO_TEMP',
    'PAUSE_CO_CWU',
    'PAUSE_TERM',
    'WORK_TERM',
    'INCREASE_TEMP_CO',
    'PROGRAM_CONTROL_CO',
    'CO_HEAT_CURVE',
    'PARALLEL_CO_HEAT_CURVE',
    'WEATHER_FACTOR',
    'TERM_BOILER_OPERATION',
    'TERM_BOILER_MODE',
    'DECREASE_SET_CO_TERM',
    'TERM_PUMP_OFF',
    'AL_BOILER_TEMP',
    'MAX_FEED_TEMP',
    'EXTERN_BOILER_TEMP',
    'ALARM_NOTIF',
    'PUMP_HYSTERESIS',
    'CWU_SET_TEMP',
    'MIN_CWU_SET_TEMP',
    'MAX_CWU_SET_TEMP',
    'CWU_WORK_MODE',
    'CWU_HYSTERESIS',
    'CWU_DISINFECTION',
    'AUTO_SUMMER',
    'SUMMER_TEMP_ON',
    'SUMMER_TEMP_OFF',
    'CWU_FEEDING_EXTENSION',
    'CIRCULATION_CONTROL',
    'CIRCULATION_PAUSE_TIME',
    'CIRCULATION_WORK_TIME',
    'CIRCULATION_START_TEMP',
    'BUFFER_CONTROL',
    'BUFFER_MAX_TEMP',
    'MIN_BUFFER_TEMP',
    'BUFFER_HISTERESIS',
    'BUFFER_LOAD_START',
    'BUFFER_LOAD_STOP'
)

MIXERS_PARAMS: list = (
    'MIX_SET_TEMP',
    'MIN_MIX_SET_TEMP',
    'MAX_MIX_SET_TEMP',
    'LOW_MIX_SET_TEMP',
    'CTRL_WEATHER_MIX',
    'MIX_HEAT_CURVE',
    'PARALLEL_OFFSET_HEAT_CURV',
    'WEATHER_TEMP_FACTOR',
    'MIX_OPERATION',
    'MIX_INSENSITIVITY',
    'MIX_THERM_OPERATION',
    'MIX_THERM_MODE',
    'MIX_OFF_THERM_PUMP',
    'MIX_SUMMER_WORK'
)
