-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 08, 2020 at 05:24 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cliq`
--

-- --------------------------------------------------------

--
-- Table structure for table `artgallery`
--

CREATE TABLE IF NOT EXISTS `artgallery` (
  `agid` int(11) NOT NULL AUTO_INCREMENT,
  `phid` int(11) NOT NULL,
  `caption` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `amount` varchar(50) NOT NULL,
  PRIMARY KEY (`agid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `artgallery`
--


-- --------------------------------------------------------

--
-- Table structure for table `associationreg`
--

CREATE TABLE IF NOT EXISTS `associationreg` (
  `associd` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `assochead` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`associd`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `associationreg`
--

INSERT INTO `associationreg` (`associd`, `name`, `addr`, `assochead`, `email`, `phno`, `username`, `status`) VALUES
(1, 'PhotoAssoc', 'ggg', 'john', 'photoassoc@gmail.com', '9658745263', 'photoassoc', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `award`
--

CREATE TABLE IF NOT EXISTS `award` (
  `awid` int(11) NOT NULL AUTO_INCREMENT,
  `assocname` varchar(50) NOT NULL,
  `award` varchar(50) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `descrip` varchar(50) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`awid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `award`
--

INSERT INTO `award` (`awid`, `assocname`, `award`, `pname`, `descrip`, `date`) VALUES
(1, 'PhotoAssoc', 'best pic', 'manu', 'award for the best pic of the year', '2020-02-03'),
(2, 'PhotoAssoc', 'Photoic Award', 'ajith', 'for the bst pic', '2020-02-07');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE IF NOT EXISTS `booking` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `phid` int(11) NOT NULL,
  `pkgid` int(11) NOT NULL,
  `bookingdate` varchar(50) NOT NULL,
  `fromdate` varchar(50) NOT NULL,
  `todate` varchar(50) NOT NULL,
  `days` int(11) NOT NULL,
  `location` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `cid` int(11) NOT NULL,
  `tamount` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bid`, `phid`, `pkgid`, `bookingdate`, `fromdate`, `todate`, `days`, `location`, `description`, `cid`, `tamount`, `status`) VALUES
(1, 1, 5, '2019-12-13', '0000-00-00', '0000-00-00', 0, '', '', 3, 13000, 'not approved'),
(9, 1, 2, '2020-01-22', '2020-01-02', '2020-01-05', 3, '', '', 3, 25000, 'paid'),
(16, 1, 4, '2020-02-02', '2020-02-25', '2020-02-26', 1, 'fghj', 'ghj', 3, 15000, 'paid'),
(17, 4, 6, '2020-02-07', '2020-02-12', '2020-02-15', 3, 'aluva', 'baptism of my daughter', 3, 20000, 'paid'),
(18, 5, 7, '2020-02-08', '2020-02-12', '2020-02-14', 2, 'changanacherry', 'GHCH', 3, 25000, 'paid'),
(19, 5, 7, '2020-02-08', '2020-02-12', '2020-02-15', 3, 'dfgh', 'fgh', 3, 25000, 'processing');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE IF NOT EXISTS `complaint` (
  `compid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `cname` varchar(50) NOT NULL,
  `complaintdes` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`compid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`compid`, `cid`, `cname`, `complaintdes`, `date`, `type`) VALUES
(3, 4, '', 'sometimes', '2020-02-08', 'photographer'),
(4, 3, 'manu', 'site slow', '2020-02-08', 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `cusreg`
--

CREATE TABLE IF NOT EXISTS `cusreg` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `cusreg`
--

INSERT INTO `cusreg` (`cid`, `name`, `addr`, `gender`, `district`, `email`, `phno`, `uname`, `password`) VALUES
(3, 'manu', 'nest', 'male', 'Ernakulam', 'manu@gmail.com', '9632568974', 'manu', 'manu');

-- --------------------------------------------------------

--
-- Table structure for table `district`
--

CREATE TABLE IF NOT EXISTS `district` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(50) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `district`
--

INSERT INTO `district` (`did`, `district`) VALUES
(1, 'Kasargod'),
(2, 'Kannur'),
(3, 'Ernakulam'),
(4, 'Kottayam'),
(5, 'Wayand'),
(6, 'Kollam'),
(7, 'Trivandrum');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `feedbackmsg` varchar(100) NOT NULL,
  `date` varchar(15) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `phid` int(11) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `cid`, `feedbackmsg`, `date`, `rating`, `phid`) VALUES
(2, 1, 'Good', '02-08-2019', '', 0),
(3, 3, 'good work', '20-08-2019', '', 0),
(4, 1, 'good', '2020-01-31', '', 0),
(5, 1, 'good', '2020-01-31', '', 0),
(6, 1, 'good', '2020-01-31', '', 0),
(7, 1, 'good', '2020-01-31', '', 0),
(8, 1, 'good', '2020-01-31', '', 0),
(9, 1, 'good', '2020-01-31', '', 0),
(10, 0, 'None', '2020-02-05', '4', 1),
(12, 3, 'good work by', '2020-02-05', '4', 1),
(14, 3, 'dfgh', '2020-02-05', '4', 1),
(15, 3, 'good work', '2020-02-07', '4', 4),
(16, 3, 'good', '2020-02-08', '3', 5);

-- --------------------------------------------------------

--
-- Table structure for table `giftgallery`
--

CREATE TABLE IF NOT EXISTS `giftgallery` (
  `agid` int(11) NOT NULL AUTO_INCREMENT,
  `phid` int(11) NOT NULL,
  `caption` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `amount` varchar(50) NOT NULL,
  PRIMARY KEY (`agid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `giftgallery`
--

INSERT INTO `giftgallery` (`agid`, `phid`, `caption`, `image`, `amount`) VALUES
(1, 4, 'drawings', 'static/MEDIA/Computer-Forensic-630x421_Z2SdiJn.jpg', '200'),
(2, 4, 'for wife', 'static/MEDIA/red-spinach-jpg-250x250.jpg', '200');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `type`, `status`) VALUES
('manu', 'manu', 'customer', 'approved'),
('vinu', 'vinu', 'photographer', 'approved'),
('admin', 'admin', 'admin', 'approved'),
('jcreation', 'jcreation', 'photographer', 'approved'),
('photoassoc', 'photoassoc', 'association', 'approved'),
('ajith', 'ajith', 'photographer', 'approved'),
('prav', '23', 'photographer', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE IF NOT EXISTS `notification` (
  `notid` int(11) NOT NULL AUTO_INCREMENT,
  `assocname` varchar(50) NOT NULL,
  `event` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `descrip` varchar(50) NOT NULL,
  `loc` varchar(50) NOT NULL,
  PRIMARY KEY (`notid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`notid`, `assocname`, `event`, `date`, `descrip`, `loc`) VALUES
(1, 'PhotoAssoc', 'competition', '2020-02-23', 'every ', 'aluva');

-- --------------------------------------------------------

--
-- Table structure for table `packages`
--

CREATE TABLE IF NOT EXISTS `packages` (
  `pkgid` int(11) NOT NULL AUTO_INCREMENT,
  `phid` int(11) NOT NULL,
  `package` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  PRIMARY KEY (`pkgid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `packages`
--

INSERT INTO `packages` (`pkgid`, `phid`, `package`, `amount`) VALUES
(2, 1, 'helicam', '25000'),
(4, 1, 'Pre Wedding', '15000'),
(5, 1, 'Post Wedding', '13000'),
(6, 4, 'baptism', '20000'),
(7, 5, 'Pre Wedding', '25000');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE IF NOT EXISTS `payment` (
  `paymentid` int(11) NOT NULL AUTO_INCREMENT,
  `custid` int(11) NOT NULL,
  `phid` int(11) NOT NULL,
  `amount` varchar(50) NOT NULL,
  PRIMARY KEY (`paymentid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`paymentid`, `custid`, `phid`, `amount`) VALUES
(1, 3, 1, '75000'),
(3, 3, 1, '75000'),
(4, 3, 1, '75000'),
(5, 3, 1, '0'),
(6, 3, 1, '75000'),
(7, 3, 4, '60000'),
(8, 3, 1, '15000'),
(9, 3, 5, '50000');

-- --------------------------------------------------------

--
-- Table structure for table `photographerimage`
--

CREATE TABLE IF NOT EXISTS `photographerimage` (
  `phimid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(100) NOT NULL,
  `image` varchar(4000) NOT NULL,
  `phid` int(11) NOT NULL,
  PRIMARY KEY (`phimid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `photographerimage`
--

INSERT INTO `photographerimage` (`phimid`, `caption`, `image`, `phid`) VALUES
(1, 'wedding', 'static/MEDIA/7840163a82fdf16df256e63fdcbdff21.jpg', 1),
(2, 'baptism', 'static/MEDIA/legal.jpg', 1),
(3, 'wedding', 'static/MEDIA/capture%20u.jpg', 4),
(4, 'wedding', 'static/MEDIA/shadow.jpg', 5);

-- --------------------------------------------------------

--
-- Table structure for table `photographerreg`
--

CREATE TABLE IF NOT EXISTS `photographerreg` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `specialization` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `association1` varchar(50) NOT NULL,
  `association2` varchar(50) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `photographerreg`
--

INSERT INTO `photographerreg` (`pid`, `name`, `addr`, `gender`, `district`, `place`, `specialization`, `email`, `phno`, `image`, `uname`, `password`, `status`, `association1`, `association2`) VALUES
(1, 'vinu', 'ggg', 'male', 'kottayam', 'aluva', '', 'vinu@gmail.com', '9856423125', '', 'vinu', 'vinu', 'approved', '', ''),
(2, 'manu', 'Manu Studios, no:32', 'male', 'Ernakulam', 'aluva', '', 'vinu@gmail.com', '9856423125', '', 'manu', 'manu', '', '', ''),
(3, 'j creations', 'sd', 'male', 'Ernakulam', 'aluva', 'all', 'jcreations@gmail.com', '09987654345', 'static/MEDIA/photogrphr.jpg', 'jcreation', 'jcreation', 'approved', 'PhotoAssoc', 'PhotoAssoc'),
(4, 'ajith', 'nest', 'male', 'Ernakulam', 'vytilla', 'all', 'ajith@gmail.com', '9874553652', 'static/MEDIA/IMG_20171211_085637.jpg', 'ajith', 'ajith', 'approved', 'PhotoAssoc', 'not member'),
(5, 'prav', 'sassa', 'male', 'kottayam', 'changanacherry', 'dfdf', 'prav@gmail.com', '9497203294', 'static/MEDIA/photo%20holic.jpg', 'prav', '23', 'approved', 'PhotoAssoc', 'not member');

-- --------------------------------------------------------

--
-- Table structure for table `photographervideo`
--

CREATE TABLE IF NOT EXISTS `photographervideo` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `phid` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `link` varchar(50) NOT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `photographervideo`
--

INSERT INTO `photographervideo` (`vid`, `phid`, `image`, `link`) VALUES
(1, 1, 'static/MEDIA/7840163a82fdf16df256e63fdcbdff21.jpg', 'zWEE2QZrpoQ'),
(2, 4, 'static/MEDIA/7840163a82fdf16df256e63fdcbdff21_drZQcrF.jpg', 'wedding video'),
(3, 5, 'static/MEDIA/photo%20holic_MqafyEm.jpg', 'wedding video');

-- --------------------------------------------------------

--
-- Table structure for table `place`
--

CREATE TABLE IF NOT EXISTS `place` (
  `placeid` int(11) NOT NULL AUTO_INCREMENT,
  `did` int(11) NOT NULL,
  `location` varchar(30) NOT NULL,
  PRIMARY KEY (`placeid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `place`
--

INSERT INTO `place` (`placeid`, `did`, `location`) VALUES
(8, 3, 'aluva'),
(9, 3, 'vytilla');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE IF NOT EXISTS `rating` (
  `ratingid` int(11) NOT NULL AUTO_INCREMENT,
  `phid` int(11) NOT NULL,
  `cusid` int(11) NOT NULL,
  `rate` varchar(50) NOT NULL,
  PRIMARY KEY (`ratingid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `rating`
--


-- --------------------------------------------------------

--
-- Table structure for table `specification`
--

CREATE TABLE IF NOT EXISTS `specification` (
  `specid` int(11) NOT NULL AUTO_INCREMENT,
  `camera` varchar(50) NOT NULL,
  `cmodel` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `phid` int(11) NOT NULL,
  PRIMARY KEY (`specid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `specification`
--

INSERT INTO `specification` (`specid`, `camera`, `cmodel`, `description`, `image`, `phid`) VALUES
(1, 'nikon', 'nikon0345', 'lens6', 'static/MEDIA/cap%20img_KcEyPoS.jpg', 1),
(2, 'sony', 'sony456', 'with hd lens', 'static/MEDIA/photogrphr_itJia27.jpg', 4),
(3, 'nikon', 'nikon432', 'with 2.4 lens and uu', 'static/MEDIA/photo-1492850298657-e81006f7a54c.jpg', 4),
(4, 'dslr5', 'sony456', 'with 2.4 lens and uu', 'static/MEDIA/gps.jpg', 5);
