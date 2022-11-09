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

        private string Password { get; set; }

        public OperationContext operationContext { get; set; }

        public ServerUser(string username, string password)
        {
            if (!checkUser(username, password))
            {
                Console.WriteLine("INVALID USERNAME OR PASSWORD. TRY AGAIN.");
                this.Username = null;
                this.Password = null;
                this.operationContext = null;
            }
            else
            {
                this.Username = username;
                this.Password = password;
                this.operationContext = OperationContext.Current;
            }
        }

        private bool checkUser(string username, string password)
        {
            return true;
        }
    }
}
