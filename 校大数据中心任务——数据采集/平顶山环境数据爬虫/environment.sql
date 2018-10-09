/*
Navicat MySQL Data Transfer

Source Server         : mysql56
Source Server Version : 50637
Source Host           : localhost:3306
Source Database       : environment

Target Server Type    : MYSQL
Target Server Version : 50637
File Encoding         : 65001

Date: 2017-11-30 14:26:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `pdsenvironment`
-- ----------------------------
DROP TABLE IF EXISTS `pdsenvironment`;
CREATE TABLE `pdsenvironment` (
  `updatatime` char(20) NOT NULL DEFAULT '',
  `AreaName` char(20) NOT NULL DEFAULT '',
  `AQI` char(10) DEFAULT NULL,
  `PollutionGrade` char(20) DEFAULT NULL,
  `PM2_5` char(10) DEFAULT NULL,
  `PM10` char(10) DEFAULT NULL,
  `FirstItem` char(10) DEFAULT NULL,
  PRIMARY KEY (`updatatime`,`AreaName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pdsenvironment
-- ----------------------------
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 10时', '平顶山工学院', '84', '状况：良', '43μg/m³\n', '117μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 10时', '新华旅馆', '90', '状况：良', '52μg/m³\n', '129μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 10时', '规划设计院', '79', '状况：良', '43μg/m³\n', '108μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 10时', '高压开关厂', '91', '状况：良', '50μg/m³\n', '132μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 11时', '平顶山工学院', '80', '状况：良', '36μg/m³\n', '110μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 11时', '新华旅馆', '88', '状况：良', '44μg/m³\n', '125μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 11时', '规划设计院', '86', '状况：良', '43μg/m³\r\n', '122μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 11时', '高压开关厂', '87', '状况：良', '45μg/m³\n', '123μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 12时', '平顶山工学院', '79', '状况：良', '34μg/m³\n', '107μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 12时', '新华旅馆', '92', '状况：良', '43μg/m³\n', '134μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 12时', '规划设计院', '93', '状况：良', '40μg/m³\n', '135μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 12时', '高压开关厂', '86', '状况：良', '44μg/m³\n', '122μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 13时', '平顶山工学院', '62', '状况：良', '31μg/m³\n', '74μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 13时', '新华旅馆', '77', '状况：良', '37μg/m³\n', '103μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 13时', '规划设计院', '82', '状况：良', '38μg/m³\n', '114μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 13时', '高压开关厂', '81', '状况：良', '36μg/m³\n', '112μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 14时', '平顶山工学院', '64', '状况：良', '29μg/m³\n', '78μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 14时', '新华旅馆', '78', '状况：良', '40μg/m³\n', '106μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 14时', '规划设计院', '73', '状况：良', '34μg/m³\n', '95μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 14时', '高压开关厂', '80', '状况：良', '32μg/m³\n', '109μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 15时', '平顶山工学院', '65', '状况：良', '33μg/m³\n', '79μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 15时', '新华旅馆', '78', '状况：良', '42μg/m³\n', '105μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 15时', '规划设计院', '73', '状况：良', '33μg/m³\n', '96μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 15时', '高压开关厂', '72', '状况：良', '27μg/m³\n', '94μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 16时', '平顶山工学院', '63', '状况：良', '33μg/m³\r\n', '75μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 16时', '新华旅馆', '94', '状况：良', '45μg/m³\n', '137μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 16时', '规划设计院', '71', '状况：良', '38μg/m³\n', '91μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 16时', '高压开关厂', '81', '状况：良', '28μg/m³\n', '111μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 17时', '平顶山工学院', '70', '状况：良', '34μg/m³\n', '90μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 17时', '新华旅馆', '71', '状况：良', '43μg/m³\n', '92μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 17时', '规划设计院', '74', '状况：良', '34μg/m³\n', '97μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 17时', '高压开关厂', '74', '状况：良', '32μg/m³\n', '98μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 18时', '平顶山工学院', '75', '状况：良', '35μg/m³\n', '100μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 18时', '新华旅馆', '89', '状况：良', '46μg/m³\n', '127μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 18时', '规划设计院', '77', '状况：良', '34μg/m³\r\n', '104μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 18时', '高压开关厂', '77', '状况：良', '29μg/m³\n', '104μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 19时', '平顶山工学院', '78', '状况：良', '39μg/m³\n', '106μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 19时', '新华旅馆', '78', '状况：良', '42μg/m³\n', '106μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 19时', '规划设计院', '68', '状况：良', '39μg/m³\n', '86μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 19时', '高压开关厂', '68', '状况：良', '28μg/m³\n', '86μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 20时', '平顶山工学院', '77', '状况：良', '44μg/m³\n', '103μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 20时', '新华旅馆', '79', '状况：良', '51μg/m³\n', '107μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 20时', '规划设计院', '76', '状况：良', '38μg/m³\n', '102μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 20时', '高压开关厂', '77', '状况：良', '31μg/m³\n', '103μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 21时', '平顶山工学院', '72', '状况：良', '46μg/m³\n', '94μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 21时', '新华旅馆', '72', '状况：良', '50μg/m³\n', '94μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 21时', '规划设计院', '74', '状况：良', '44μg/m³\n', '97μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 21时', '高压开关厂', '69', '状况：良', '34μg/m³\n', '87μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 22时', '平顶山工学院', '74', '状况：良', '46μg/m³\r\n', '98μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 22时', '新华旅馆', '73', '状况：良', '51μg/m³\n', '95μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 22时', '规划设计院', '70', '状况：良', '41μg/m³\n', '90μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 22时', '高压开关厂', '55', '状况：良', '25μg/m³\n', '60μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 23时', '平顶山工学院', '59', '状况：良', '40μg/m³\n', '67μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 23时', '新华旅馆', '64', '状况：良', '46μg/m³\n', '66μg/m³', 'PM2.5');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 23时', '规划设计院', '55', '状况：良', '38μg/m³\n', '59μg/m³', 'PM2.5');
INSERT INTO `pdsenvironment` VALUES ('2017年11月29日 23时', '高压开关厂', '57', '状况：良', '31μg/m³\n', '63μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 00时', '平顶山工学院', '60', '状况：良', '37μg/m³\n', '69μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 00时', '新华旅馆', '67', '状况：良', '37μg/m³\n', '83μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 00时', '规划设计院', '63', '状况：良', '40μg/m³\n', '76μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 00时', '高压开关厂', '70', '状况：良', '29μg/m³\n', '90μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 01时', '平顶山工学院', '59', '状况：良', '41μg/m³\n', '67μg/m³', 'PM2.5');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 01时', '新华旅馆', '58', '状况：良', '32μg/m³\n', '65μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 01时', '规划设计院', '58', '状况：良', '34μg/m³\n', '65μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 01时', '高压开关厂', '55', '状况：良', '35μg/m³\n', '60μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 02时', '平顶山工学院', '58', '状况：良', '38μg/m³\n', '65μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 02时', '新华旅馆', '59', '状况：良', '29μg/m³\n', '67μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 02时', '规划设计院', '67', '状况：良', '35μg/m³\n', '83μg/m³', 'PM10');
INSERT INTO `pdsenvironment` VALUES ('2017年11月30日 02时', '高压开关厂', '55', '状况：良', '28μg/m³\n', '59μg/m³', 'PM10');
