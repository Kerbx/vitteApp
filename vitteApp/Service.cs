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
        public int Connect()
        {
            throw new NotImplementedException();
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
