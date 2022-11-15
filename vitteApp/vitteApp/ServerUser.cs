using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ServiceModel;
using System.Net.Configuration;
using System.Data.SqlClient;

namespace vitteApp
{
    internal class ServerUser
    {
        public string Username { get; set; }

        private string Password { get; set; }

        public OperationContext operationContext { get; set; }

        public ServerUser(string username, string password)
        {
        }
    }

    public class Database
    {
        private System.Data.SqlClient.SqlConnection ConnectDatabase()
        {
            System.Data.SqlClient.SqlConnection connection = new System.Data.SqlClient.SqlConnection();
            connection.ConnectionString = $@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename={Environment.CurrentDirectory}\db\students.mdf;Integrated Security=True;Connect Timeout=30";
            return connection;
        }
        public bool checkUser(string username, string password)
        {
            System.Data.SqlClient.SqlConnection connection = ConnectDatabase();

            using (var cmd = new SqlCommand() { Connection = connection })
            {
                cmd.CommandText = "SELECT username, passwd FROM students WHERE username = @Username;";
                cmd.Parameters.AddWithValue("@Username", username);

                connection.Open();

                var reader = cmd.ExecuteReader();

                if (reader.HasRows)
                {
                    reader.Read();

                    if (reader.GetString(1).ToString() == password)
                    {
                        connection.Close();
                        return true;
                    }
                    else
                    {
                        connection.Close();
                        return false;
                    }
                }
                else
                {
                    connection.Close();
                    return false;

                }
            }
        }
    }
}
