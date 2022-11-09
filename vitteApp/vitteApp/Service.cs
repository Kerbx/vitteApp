using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace vitteApp
{
    [ServiceBehavior(InstanceContextMode = InstanceContextMode.Single)]
    public class Service : IService
    {
        List<ServerUser> users = new List<ServerUser>();

        public void Connect(string username, string passwd)
        {
            ServerUser user = new ServerUser(username, passwd);
        }

        public void Disconnect(int ID)
        {
            throw new NotImplementedException();
        }

        public void Get(string query)
        {
            throw new NotImplementedException();
        }
    }
}
