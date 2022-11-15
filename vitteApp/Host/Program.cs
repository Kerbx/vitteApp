using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ServiceModel;

namespace Host
{
    internal class Program
    {
        static void Main(string[] args)
        {
            using (var host = new ServiceHost(typeof(vitteApp.Service)))
            {
                host.Open();
                Console.WriteLine("ЕСТЬ КУРИТЬ.");
                Console.WriteLine("Нажми че-нить, чтоб выйти.");
                Console.ReadKey();
            }
        }
    }
}
