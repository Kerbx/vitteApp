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

        public string Connect(string username, string passwd)
        {
            Database database = new Database();

            if(database.checkUser(username, passwd))
            {
                ServerUser user = new ServerUser
                {
                    Username = username,
                    operationContext = OperationContext.Current
                };
                users.Add(user);

                return username;
            }
            else
            {
                Console.WriteLine("Invalid username or password.");
                return "";
            }
        }

        public void Disconnect(string username)
        {
            var user = users.FirstOrDefault(i => i.Username == username);

            if(user != null)
            {
                users.Remove(user);
            }
        }

        public void Get(string query)
        {
            throw new NotImplementedException();
        }
    }
}
