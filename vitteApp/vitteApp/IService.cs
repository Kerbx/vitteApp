using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace vitteApp
{
    [ServiceContract(CallbackContract = typeof(IServiceCallback))]
    public interface IService
    {
        [OperationContract]
        string Connect(string username, string passwd);
        [OperationContract]
        void Disconnect(string username);
        [OperationContract(IsOneWay = true)]
        void Get(string query);
    }

    public interface IServiceCallback
    {
        [OperationContract]
        void Post(string answer);
    }
}