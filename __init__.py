# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SafeRouting
                                 A QGIS plugin
 desciption_to_write
                             -------------------
        begin                : 2016-03-16
        copyright            : (C) 2016 by AIFDR and DMInnovation
        email                : info@inasafe.org
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SafeRouting class from file SafeRouting.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .routing import SafeRouting
    return SafeRouting(iface)
