using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ServiceModel;


namespace vitteApp
{
    internal class ServerUser
    {
        public string Username { get; set; }

        public string Password { get; set; }

        public OperationContext operationContext { get; set; }
    }
}
