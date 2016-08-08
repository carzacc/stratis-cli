"""
Manager interface.
"""

class Manager(object):
    """
    Manager interface.
    """

    _INTERFACE_NAME = 'org.storage.stratis1.Manager'

    def __init__(self, dbus_object):
        """
        Initializer.

        :param dbus_object: the dbus object
        """
        self._dbus_object = dbus_object

    def CreatePool(self, pool_name, devices, num_devices):
        """
        Create a pool.

        :param str pool_name: the pool name
        :param devices: the component devices
        :type devices: sequence of str
        """
        return self._dbus_object.CreatePool(
           pool_name,
           devices,
           num_devices,
           dbus_interface=self._INTERFACE_NAME,
        )

    def DestroyPool(self, pool_name):
        """
        Destroy a pool.

        :param str pool_name: the name of the pool
        """
        return self._dbus_object.DestroyPool(
           pool_name,
           dbus_interface=self._INTERFACE_NAME
        )

    def ListPools(self):
        """
        List all pools.
        """
        return self._dbus_object.ListPools(dbus_interface=self._INTERFACE_NAME)
