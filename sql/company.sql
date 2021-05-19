/*
Navicat MySQL Data Transfer

Source Server         : Mysql
Source Server Version : 80018
Source Host           : localhost:3306
Source Database       : company

Target Server Type    : MYSQL
Target Server Version : 50599
File Encoding         : 65001

Date: 2021-05-17 23:03:28
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for checkstat
-- ----------------------------
DROP TABLE IF EXISTS `checkstat`;
CREATE TABLE `checkstat` (
`CheckID`  int(20) NOT NULL COMMENT '考勤编号' ,
`EmployeeID`  char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '员工编号' ,
`EmployeeName`  varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '员工姓名' ,
`OvertimeDay`  int(6) NOT NULL COMMENT '加班天数' ,
`AbsentDay`  int(6) NOT NULL COMMENT '旷工天数' ,
`LateDay`  int(6) NOT NULL COMMENT '迟到次数' ,
`CheckDate`  datetime NOT NULL COMMENT '考勤日期' ,
PRIMARY KEY (`CheckID`),
FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `EmployeeID` (`EmployeeID`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

;

-- ----------------------------
-- Records of checkstat
-- ----------------------------
BEGIN;
INSERT INTO `checkstat` VALUES ('1', '1', 'zhang', '10', '5', '3', '2020-01-01 00:00:00.000'), ('2', '2', 'chen', '3', '2', '1', '2020-01-01 00:00:00.000'), ('3', '3', 'dai', '5', '4', '2', '2020-01-01 00:00:00.000'), ('4', '4', 'li', '7', '1', '1', '2020-01-01 00:00:00.000');
COMMIT;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
`DepartmentID`  char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '部门编号' ,
`DepartmentName`  char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '部门名称' ,
`DepartmentCount`  int(12) NOT NULL COMMENT '部门人数' ,
PRIMARY KEY (`DepartmentID`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

;

-- ----------------------------
-- Records of department
-- ----------------------------
BEGIN;
INSERT INTO `department` VALUES ('001', '财务部', '30'), ('002', '产品开发部', '40'), ('003', '人力资源部', '50'), ('004', '生产部', '80');
COMMIT;

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
`EmployeeID`  char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '员工编号' ,
`EmployeeName`  varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '姓名' ,
`Sex`  varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '性别' ,
`Age`  int(6) NOT NULL COMMENT '年龄' ,
`DepartmentId`  char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '部门编号' ,
`EmploymentYear`  char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '入职年份' ,
`Telephone`  varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '电话' ,
`IdentityID`  varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '身份证号' ,
`Duty`  varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '职务' ,
PRIMARY KEY (`EmployeeID`),
FOREIGN KEY (`DepartmentId`) REFERENCES `department` (`DepartmentID`) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (`Duty`) REFERENCES `wageconfig` (`Duty`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `DepartmentId` (`DepartmentId`) USING BTREE ,
INDEX `Duty` (`Duty`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

;

-- ----------------------------
-- Records of employee
-- ----------------------------
BEGIN;
INSERT INTO `employee` VALUES ('1', 'zhang', '男', '18', '001', '2020', '123+', '3323+', '财务类'), ('2', 'chen', '女', '20', '001', '2019', '135+', '3333+', '管理类'), ('3', 'dai', '女', '30', '003', '2010', '166+', '1233+', '服务类'), ('4', 'li', '男', '25', '002', '2018', '153+', '6658+', '销售类');
COMMIT;

-- ----------------------------
-- Table structure for wage
-- ----------------------------
DROP TABLE IF EXISTS `wage`;
CREATE TABLE `wage` (
`WageID`  int(20) NOT NULL COMMENT '编号' ,
`EmployeeID`  char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '员工编号' ,
`EmployeeName`  varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '员工姓名' ,
`WageDate`  datetime NOT NULL COMMENT '工资日期' ,
`BaseWage`  int(8) NOT NULL COMMENT '基本工资' ,
`OvertimeWage`  int(8) NOT NULL COMMENT '加班工资' ,
`AbsentWage`  int(8) NOT NULL COMMENT '旷工减薪' ,
`LateWage`  int(8) NOT NULL COMMENT '迟到减薪' ,
`TaxWage`  int(8) NOT NULL COMMENT '税费' ,
`BonusWage`  int(8) NOT NULL COMMENT '奖金' ,
`Totalwage`  int(8) NOT NULL COMMENT '总工资' ,
PRIMARY KEY (`WageID`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

;

-- ----------------------------
-- Records of wage
-- ----------------------------
BEGIN;
INSERT INTO `wage` VALUES ('1', '1', 'zhang', '2021-01-01 00:00:00.000000', '2350', '1300', '550', '210', '245', '1200', '3845'), ('2', '2', 'chen', '2021-01-01 00:00:00.000000', '1800', '360', '200', '70', '150', '1100', '2841'), ('3', '3', 'dai', '2021-01-01 00:00:00.000000', '2950', '850', '520', '140', '371', '1500', '4269'), ('4', '4', 'li', '2021-01-01 00:00:00.000000', '2150', '1050', '120', '70', '302', '1300', '4008');
COMMIT;

-- ----------------------------
-- Table structure for wageconfig
-- ----------------------------
DROP TABLE IF EXISTS `wageconfig`;
CREATE TABLE `wageconfig` (
`Duty`  varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '职务' ,
`BaseWage`  int(8) NOT NULL COMMENT '基本工资' ,
`OvertimeStandard`  int(8) NOT NULL COMMENT '加班标准' ,
`AbsentStandard`  int(8) NOT NULL COMMENT '旷工标准' ,
`TaxRate`  float(8,2) NOT NULL COMMENT '税率' ,
`LateStandard`  int(8) NOT NULL COMMENT '迟到标准' ,
`Bonus`  int(8) NOT NULL COMMENT '奖金' ,
PRIMARY KEY (`Duty`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

;

-- ----------------------------
-- Records of wageconfig
-- ----------------------------
BEGIN;
INSERT INTO `wageconfig` VALUES ('服务类', '2150', '150', '120', '0.07', '70', '1300'), ('管理类', '2950', '170', '130', '0.08', '70', '1500'), ('财务类', '2350', '130', '110', '0.06', '70', '1200'), ('销售类', '1800', '120', '100', '0.05', '70', '1100');
COMMIT;
