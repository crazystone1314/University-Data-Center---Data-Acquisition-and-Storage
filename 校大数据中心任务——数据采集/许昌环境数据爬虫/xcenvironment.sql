/*
Navicat MySQL Data Transfer

Source Server         : mysql56
Source Server Version : 50637
Source Host           : localhost:3306
Source Database       : environment

Target Server Type    : MYSQL
Target Server Version : 50637
File Encoding         : 65001

Date: 2017-12-29 16:44:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `xcenvironment`
-- ----------------------------
DROP TABLE IF EXISTS `xcenvironment`;
CREATE TABLE `xcenvironment` (
  `Region` char(10) DEFAULT NULL,
  `Date` char(20) NOT NULL,
  `PM25` char(5) DEFAULT NULL,
  `PM10` char(5) DEFAULT NULL,
  `NO2` char(5) DEFAULT NULL,
  `CO` char(5) DEFAULT NULL,
  `O3` char(5) DEFAULT NULL,
  `SO2` char(5) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xcenvironment
-- ----------------------------
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-10-30', '52', '60', '60', '17', '20', '15');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-10-31', '82', '73', '69', '26', '21', '22');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-1', '85', '85', '80', '36', '10', '50');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-10', '46', '71', '41', '27', '25', '18');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-11', '45', '56', '48', '24', '18', '15');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-12', '69', '64', '60', '31', '12', '25');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-13', '66', '72', '70', '38', '15', '45');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-14', '94', '79', '85', '39', '15', '34');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-15', '144', '106', '90', '46', '14', '59');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-16', '152', '95', '88', '33', '13', '38');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-17', '106', '94', '81', '34', '8', '27');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-18', '37', '52', '40', '13', '23', '11');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-19', '94', '60', '66', '18', '7', '13');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-2', '62', '71', '62', '29', '18', '38');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-20', '119', '76', '66', '30', '3', '15');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-21', '126', '88', '78', '31', '10', '19');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-22', '38', '70', '57', '19', '22', '20');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-23', '61', '68', '70', '24', '14', '17');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-24', '80', '76', '74', '24', '12', '24');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-25', '126', '86', '82', '26', '13', '26');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-26', '152', '96', '86', '34', '14', '29');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-27', '150', '103', '92', '35', '11', '28');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-28', '177', '120', '77', '39', '22', '29');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-29', '64', '78', '56', '26', '11', '22');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-3', '87', '79', '62', '28', '29', '24');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-30', '88', '69', '61', '37', '9', '28');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-4', '52', '62', '56', '21', '27', '21');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-5', '56', '62', '68', '21', '27', '16');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-6', '84', '74', '81', '28', '33', '27');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-7', '106', '95', '101', '42', '20', '49');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-8', '175', '117', '100', '53', '25', '48');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-11-9', '124', '97', '85', '43', '31', '27');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-1', '189', '104', '85', '48', '8', '43');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-10', '33', '73', '30', '17', '28', '24');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-11', '74', '64', '49', '22', '22', '23');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-12', '65', '69', '45', '28', '11', '18');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-13', '94', '76', '65', '33', '5', '22');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-14', '122', '84', '69', '43', '2', '21');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-15', '132', '82', '55', '46', '1', '10');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-16', '17', '51', '33', '23', '24', '10');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-17', '33', '47', '39', '25', '19', '12');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-18', '44', '54', '46', '25', '20', '15');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-19', '48', '59', '54', '29', '14', '17');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-2', '125', '80', '55', '25', '15', '18');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-20', '51', '62', '54', '28', '18', '17');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-21', '72', '68', '64', '30', '18', '14');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-22', '116', '87', '75', '33', '20', '22');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-23', '148', '116', '93', '47', '14', '44');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-24', '23', '61', '34', '23', '29', '18');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-25', '68', '76', '65', '32', '17', '18');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-26', '102', '96', '70', '40', '17', '31');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-27', '179', '144', '105', '56', '8', '49');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-28', '213', '159', '90', '57', '9', '37');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-3', '228', '144', '82', '51', '19', '31');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-4', '239', '148', '79', '60', '19', '29');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-5', '103', '91', '68', '33', '14', '26');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-6', '112', '86', '68', '34', '14', '17');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-7', '120', '86', '76', '37', '11', '51');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-8', '73', '69', '55', '25', '16', '19');
INSERT INTO `xcenvironment` VALUES ('许昌', '2017-12-9', '79', '71', '65', '23', '13', '16');
